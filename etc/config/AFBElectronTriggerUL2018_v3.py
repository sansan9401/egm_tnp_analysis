from AFBElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples
samplesDef = {
    'data'   : tnpSamples.AFB['dataUL2018'].clone(),
    'mcNom'  : tnpSamples.AFB['mgUL2018'].clone(),
    'mcAlt'  : tnpSamples.AFB['amcUL2018'].clone(),
    'tagSel' : tnpSamples.AFB['mgUL2018'].clone(),
}
samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
samplesDef['tagSel'].set_cut('tag_Ele_pt > 38')

baseOutDir = 'results/AFBElectronTriggerUL2018_v3/'
tnpTreeDir = 'tnpEleTrig'
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.4 && el_q*tag_Ele_q < 0'
additionalCutBase = {
    'Ele32_MediumID_QPlus' : 'el_pt > 28 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele32_MediumID_QMinus' : 'el_pt > 28 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele28_MediumID_QPlus' : 'el_pt > 24 && el_q > 0 && passingCutBasedMedium94XV2 == 1 && IsEle28On == 1',
    'Ele28_MediumID_QMinus' : 'el_pt > 24 && el_q < 0 && passingCutBasedMedium94XV2 == 1 && IsEle28On == 1',
    'Ele28Or_MediumID_QPlus' : 'el_pt > 24 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele28Or_MediumID_QMinus' : 'el_pt > 24 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QPlus' : 'el_pt > 19 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QMinus' : 'el_pt > 19 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele32_TightID_Selective_QPlus' : 'el_pt > 28 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele32_TightID_Selective_QMinus' : 'el_pt > 28 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele28_TightID_Selective_QPlus' : 'el_pt > 24 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge && IsEle28On == 1',
    'Ele28_TightID_Selective_QMinus' : 'el_pt > 24 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge && IsEle28On == 1',
    'Ele28Or_TightID_Selective_QPlus' : 'el_pt > 24 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele28Or_TightID_Selective_QMinus' : 'el_pt > 24 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QPlus' : 'el_pt > 19 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QMinus' : 'el_pt > 19 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
}
flags = {
    'Ele32_MediumID_QPlus' : '(passHltEle32WPTightGsf == 1)',
    'Ele32_MediumID_QMinus' : '(passHltEle32WPTightGsf == 1)',
    'Ele28_MediumID_QPlus' : '(passHltEle28WPTightGsf == 1)',
    'Ele28_MediumID_QMinus' : '(passHltEle28WPTightGsf == 1)',
    'Ele28Or_MediumID_QPlus' : '( passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele28Or_MediumID_QMinus' : '( passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele23Leg1_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele32_TightID_Selective_QPlus' : '(passHltEle32WPTightGsf == 1)',
    'Ele32_TightID_Selective_QMinus' : '(passHltEle32WPTightGsf == 1)',
    'Ele28_TightID_Selective_QPlus' : '(passHltEle28WPTightGsf == 1)',
    'Ele28_TightID_Selective_QMinus' : '(passHltEle28WPTightGsf == 1)',
    'Ele28Or_TightID_Selective_QPlus' : '( passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele28Or_TightID_Selective_QMinus' : '( passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele23Leg1_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
}

flagBinningDef={
    'Ele32_MediumID_QPlus' : bin_Ele32,
    'Ele32_MediumID_QMinus' : bin_Ele32,
    'Ele28_MediumID_QPlus' : bin_Ele28,
    'Ele28_MediumID_QMinus' : bin_Ele28,
    'Ele28Or_MediumID_QPlus' : bin_Ele28,
    'Ele28Or_MediumID_QMinus' : bin_Ele28,
    'Ele23Leg1_MediumID_QPlus' : bin_Ele23,
    'Ele23Leg1_MediumID_QMinus' : bin_Ele23,
    'Ele12Leg2_MediumID_QPlus' : bin_Ele12,
    'Ele12Leg2_MediumID_QMinus' : bin_Ele12,
    'Ele32_TightID_Selective_QPlus' : bin_Ele32,
    'Ele32_TightID_Selective_QMinus' : bin_Ele32,
    'Ele28_TightID_Selective_QPlus' : bin_Ele28,
    'Ele28_TightID_Selective_QMinus' : bin_Ele28,
    'Ele28Or_TightID_Selective_QPlus' : bin_Ele28,
    'Ele28Or_TightID_Selective_QMinus' : bin_Ele28,
    'Ele23Leg1_TightID_Selective_QPlus' : bin_Ele23,
    'Ele23Leg1_TightID_Selective_QMinus' : bin_Ele23,
    'Ele12Leg2_TightID_Selective_QPlus' : bin_Ele12,
    'Ele12Leg2_TightID_Selective_QMinus' : bin_Ele12,
}    
