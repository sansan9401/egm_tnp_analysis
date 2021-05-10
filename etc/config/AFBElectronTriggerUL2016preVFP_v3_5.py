from AFBElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples
samplesDef = {
    'data'   : tnpSamples.AFB['dataUL2016preVFP'].clone(),
    'mcNom'  : tnpSamples.AFB['miUL2016preVFP'].clone(),
    'mcAlt'  : tnpSamples.AFB['mgUL2016preVFP'].clone(),
    'tagSel' : tnpSamples.AFB['miUL2016preVFP'].clone(),
}
samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
samplesDef['tagSel'].set_cut('tag_Ele_pt > 35')
additionalCuts={}

baseOutDir = 'results/AFBElectronTriggerUL2016preVFP_v3_5/'
tnpTreeDir = 'tnpEleTrig'
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.4 && el_q*tag_Ele_q < 0'
additionalCutBase = {
    'Ele27_MediumID_QPlus' : 'el_pt > 24 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27_MediumID_QMinus' : 'el_pt > 24 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QPlus' : 'el_pt > 19 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QMinus' : 'el_pt > 19 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27_TightID_Selective_QPlus' : 'el_pt > 23 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele27_TightID_Selective_QMinus' : 'el_pt > 23 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QPlus' : 'el_pt > 19 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QMinus' : 'el_pt > 19 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
}
flags = {
    'Ele27_MediumID_QPlus' : '(passHltEle27WPTightGsf == 1)',
    'Ele27_MediumID_QMinus' : '(passHltEle27WPTightGsf == 1)',
    'Ele23Leg1_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele27_TightID_Selective_QPlus' : '(passHltEle27WPTightGsf == 1)',
    'Ele27_TightID_Selective_QMinus' : '(passHltEle27WPTightGsf == 1)',
    'Ele23Leg1_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
}

flagBinningDef={
    'Ele27_MediumID_QPlus' : bin_Ele27,
    'Ele27_MediumID_QMinus' : bin_Ele27,
    'Ele23Leg1_MediumID_QPlus' : bin_Ele23,
    'Ele23Leg1_MediumID_QMinus' : bin_Ele23,
    'Ele12Leg2_MediumID_QPlus' : bin_Ele12,
    'Ele12Leg2_MediumID_QMinus' : bin_Ele12,
    'Ele27_TightID_Selective_QPlus' : bin_Ele27,
    'Ele27_TightID_Selective_QMinus' : bin_Ele27,
    'Ele23Leg1_TightID_Selective_QPlus' : bin_Ele23,
    'Ele23Leg1_TightID_Selective_QMinus' : bin_Ele23,
    'Ele12Leg2_TightID_Selective_QPlus' : bin_Ele12,
    'Ele12Leg2_TightID_Selective_QMinus' : bin_Ele12,
}
