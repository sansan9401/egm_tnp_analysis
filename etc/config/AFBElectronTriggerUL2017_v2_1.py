from AFBElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples
samplesDef = {
    'data'   : tnpSamples.AFB['dataUL2017'].clone(),
    'mcNom'  : tnpSamples.AFB['mgUL2017'].clone(),
    'mcAlt'  : tnpSamples.AFB['amcUL2017'].clone(),
    'tagSel' : tnpSamples.AFB['mgUL2017'].clone(),
}
samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
samplesDef['tagSel'].set_cut('tag_Ele_pt > 37')

baseOutDir = 'results/AFBElectronTriggerUL2017_v2_1/'
tnpTreeDir = 'tnpEleTrig'
cutBase   = 'tag_Ele_pt > 34 && abs(tag_sc_eta) < 2.1 && el_q*tag_Ele_q < 0'
additionalCutBase = {
    'Ele35_MediumID_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele35_MediumID_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele32_MediumID_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele32_MediumID_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27Or_MediumID_QPlus' : 'el_pt > 25 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27Or_MediumID_QMinus' : 'el_pt > 25 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele35_TightID_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele35_TightID_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele32_TightID_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele32_TightID_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele27Or_TightID_QPlus' : 'el_pt > 25 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele27Or_TightID_QMinus' : 'el_pt > 25 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele23Leg1_TightID_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele23Leg1_TightID_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele12Leg2_TightID_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele12Leg2_TightID_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele35_TightID_Selective_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele35_TightID_Selective_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele32_TightID_Selective_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele32_TightID_Selective_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele27Or_TightID_Selective_QPlus' : 'el_pt > 25 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele27Or_TightID_Selective_QMinus' : 'el_pt > 25 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
}
flags = {
    'Ele27Or_MediumID_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle32DoubleEGWPTightGsf == 1 )',
    'Ele27Or_MediumID_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle32DoubleEGWPTightGsf == 1 )',
    'Ele32_MediumID_QPlus' : '(passHltEle32DoubleEGWPTightGsf == 1)',
    'Ele32_MediumID_QMinus' : '(passHltEle32DoubleEGWPTightGsf == 1)',
    'Ele23Leg1_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele27Or_TightID_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle32DoubleEGWPTightGsf == 1 )',
    'Ele27Or_TightID_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle32DoubleEGWPTightGsf == 1 )',
    'Ele32_TightID_QPlus' : '(passHltEle32DoubleEGWPTightGsf == 1)',
    'Ele32_TightID_QMinus' : '(passHltEle32DoubleEGWPTightGsf == 1)',
    'Ele23Leg1_TightID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_TightID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_TightID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_TightID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele27Or_TightID_Selective_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle32DoubleEGWPTightGsf == 1 )',
    'Ele27Or_TightID_Selective_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle32DoubleEGWPTightGsf == 1 )',
    'Ele32_TightID_Selective_QPlus' : '(passHltEle32DoubleEGWPTightGsf == 1)',
    'Ele32_TightID_Selective_QMinus' : '(passHltEle32DoubleEGWPTightGsf == 1)',
    'Ele23Leg1_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
}
