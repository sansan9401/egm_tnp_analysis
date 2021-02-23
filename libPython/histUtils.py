import math
import ROOT
from array import array

##################
# Helper functions
##################

# Check if a string can be a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def removeNegativeBins(h):
    for i in xrange(h.GetNbinsX()):
        if (h.GetBinContent(i) < 0):
            h.SetBinContent(i, 0)

##################################
# To Fill Tag and Probe histograms
##################################

def makePassFailHistograms( sample, flag, bindef, var ):
    ###############################
    # Read in Tag and Probe Ntuples
    ###############################

    tree = ROOT.TChain(sample.tree)
    if len(sample.path)<1:
        print 'No input files...'
        print 'Create an empty file'
        emptyfile = ROOT.TFile(sample.histFile,'recreate')
        emptyfile.Close()
        return

    for p in sample.path:
        print ' adding rootfile: ', p
        tree.Add(p)

    if not sample.puTree is None:
        print ' - Adding weight tree: %s from file %s ' % (sample.weight.split('.')[0], sample.puTree)
        tree.AddFriend(sample.weight.split('.')[0],sample.puTree)

    #################################
    # Prepare hists, cuts and outfile
    #################################

    outfile = ROOT.TFile(sample.histFile,'recreate')    
    formulas_list=ROOT.TList()
    nbins = len(bindef['bins'])
    bin_formulas=[]
    cutBinList = []
    hPass=[]
    hFail=[]
    for ib in range(len(bindef['bins'])):
        hPass+=[ROOT.TH1D('%s_Pass' % bindef['bins'][ib]['name'],bindef['bins'][ib]['title'],var['nbins'],var['min'],var['max'])]
        hFail+=[ROOT.TH1D('%s_Fail' % bindef['bins'][ib]['name'],bindef['bins'][ib]['title'],var['nbins'],var['min'],var['max'])]
        hPass[ib].Sumw2()
        hFail[ib].Sumw2()

        cuts = bindef['bins'][ib]['cut']
        if sample.mcTruth :
            cuts = '%s && mcTrue==1' % cuts
        if not sample.cut is None :
            cuts = '%s && %s' % (cuts,sample.cut)

        if not sample.weight is None:
            cutBin = '( %s ) * %s ' % (cuts, sample.weight)
            if sample.maxWeight < 999:
                cutBin = '( %s ) * (%s < %f ? %s : 1.0 )' % (cuts, sample.weight,sample.maxWeight,sample.weight)
        else:
            cutBin = '%s' % cuts
        cutBinList.append(cutBin)
        bin_formulas+=[ROOT.TTreeFormula('%s_Selection' % bindef['bins'][ib]['name'], cutBin, tree)]
        formulas_list.Add(bin_formulas[ib])

    flag_formula = ROOT.TTreeFormula('Flag_Selection', flag, tree)
    formulas_list.Add(flag_formula)
    tree.SetNotify(formulas_list)

    ######################################
    # Deactivate branches and set adresses
    ######################################

    # Find out with variables are used to activate the corresponding branches
    replace_patterns = ['&', '|', '-', 'cos(', 'sqrt(', 'fabs(', 'abs(', '(', ')', '>', '<', '=', '!', '*', '/', '?', ':']
    branches = " ".join(cutBinList) + " "+sample.massName+" " + flag
    for p in replace_patterns:
        branches = branches.replace(p, ' ')

    branches = set([x for x in branches.split(" ") if x != '' and not is_number(x)])

    # Activate only branches which matter for the tag selection
    tree.SetBranchStatus("*", 0)

    for br in branches:
        tree.SetBranchStatus(br, 1)

    # Set adress of pair mass
    pair_mass_type=tree.GetLeaf(sample.massName).GetTypeName()
    if pair_mass_type=="float" or pair_mass_type=="Float_t":
        pair_mass=array("f",[0.])
        tree.SetBranchAddress(sample.massName,pair_mass)
    elif pair_mass_type=="double" or pair_mass_type=="Double_t":
        pair_mass=array("d",[0.])
        tree.SetBranchAddress(sample.massName,pair_mass)
    else:
        print("Unknown pair_mass type")
        exit(1)
        
    ################
    # Loop over Tree
    ################
    
    nevts = tree.GetEntries()
    startevent = 0
    stepsize = nevts
    if 'jobIndex' in var and 'njob' in var:
       stepsize = nevts/var['njob']+1
       startevent = stepsize*var['jobIndex']
       
    frac_of_nevts = stepsize/20

    print("Starting event loop to fill histograms..")
    print("Run loop from "+str(startevent)+"/"+str(nevts)+" to "+str(startevent+stepsize-1)+"/"+str(nevts))

    for index in range(startevent,startevent+stepsize):
        if index >= nevts: break
        if (index-startevent) % frac_of_nevts == 0:
            print index-startevent,"/",stepsize

        tree.GetEntry(index)

        for bnidx in range(nbins):
            weight = bin_formulas[bnidx].EvalInstance(0)
            if weight:
                if math.isnan(weight):
                    print 'nan weight!!! move to next event'
                    break
                if flag_formula.EvalInstance(0):
                    hPass[bnidx].Fill(pair_mass[0], weight)
                else:
                    hFail[bnidx].Fill(pair_mass[0], weight)
                break

    #####################
    # Deal with the Hists
    #####################
    epass = array('d',[-1.])
    efail = array('d',[-1.])
    for ib in range(len(bindef['bins'])):
        #removeNegativeBins(hPass[ib])
        #removeNegativeBins(hFail[ib])
        print "ib:",ib
        hPass[ib].Write(hPass[ib].GetName())
        hFail[ib].Write(hFail[ib].GetName())

        bin1 = 1
        bin2 = hPass[ib].GetXaxis().GetNbins()
        passI = hPass[ib].IntegralAndError(bin1,bin2,epass)
        failI = hFail[ib].IntegralAndError(bin1,bin2,efail)
        eff   = 0
        e_eff = 0
        if passI > 0 :
            itot  = (passI+failI)
            eff   = passI / (passI+failI)
            e_eff = math.sqrt(passI*passI*efail[0]*efail[0] + failI*failI*epass[0]*epass[0]) / (itot*itot)
        #print cuts
        #print '    ==> pass: %.1f +/- %.1f ; fail : %.1f +/- %.1f : eff: %1.3f +/- %1.3f' % (passI,epass,failI,efail,eff,e_eff)

    ##########
    # Clean up
    ##########

    outfile.Close()
    tree.Delete()
