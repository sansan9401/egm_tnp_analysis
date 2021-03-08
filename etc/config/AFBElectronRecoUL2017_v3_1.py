from AFBElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples
samplesDef = {
    'data'   : tnpSamples.AFB['dataUL2017_officialAOD'].clone(),
    'mcNom'  : tnpSamples.AFB['mgUL2017_officialAOD'].clone(),
#    'mcAlt'  : tnpSamples.AFB['amcUL2017_officialAOD'].clone(),
#    'tagSel' : tnpSamples.AFB['mgUL2017_officialAOD'].clone(),
}
#samplesDef['mcNom'].set_cut(tight_mcTrue)
#samplesDef['mcAlt'].set_cut(tight_mcTrue)
#samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
#samplesDef['tagSel'].set_cut('tag_Ele_pt > 38 && '+tight_mcTrue)
#samplesDef['tagSel'].set_cut('tag_Ele_pt > 38')

baseOutDir = 'results/AFBElectronRecoUL2017_v3_1/'
tnpTreeDir = 'tnpEleReco'
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.1'
additionalCuts={}
additionalCutBase = {}
flags = {
    'Reco' : '(passingRECO == 1)',
}

bin_Reco=[
    {'var':'sc_eta','type':'float','bins':[-2.5,-1.566,-1.4442,0,1.4442,1.566,2.5]},
    {'var':'sc_pt','type':'float','bins':[10,20,30,40]},
]    
flagBinningDef ={
    'Reco' : bin_Reco,
}
