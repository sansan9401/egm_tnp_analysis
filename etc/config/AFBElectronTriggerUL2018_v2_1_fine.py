from AFBElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples
biningDef = [
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.1, -1.80, -1.566, -1.4442, -1.1, -0.8, -0.4, 0.0, 0.4, 0.8, 1.1, 1.4442, 1.566, 1.80, 2.1, 2.5] },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 15, 20, 23, 25, 27, 29, 31, 33, 35, 40, 45, 70, 100, 500] },
]

samplesDef = {
    'data'   : tnpSamples.AFB['dataUL2018'].clone(),
    'mcNom'  : tnpSamples.AFB['amcUL2018'].clone(),
    'mcAlt'  : tnpSamples.AFB['mgUL2018'].clone(),
    'tagSel' : tnpSamples.AFB['amcUL2018'].clone(),
}
samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
samplesDef['tagSel'].set_cut('tag_Ele_pt > 37')

baseOutDir = 'results/AFBElectronTriggerUL2018_v2_1_fine/'
tnpTreeDir = 'tnpEleTrig'
cutBase   = 'tag_Ele_pt > 34 && abs(tag_sc_eta) < 2.1 && el_q*tag_Ele_q < 0'
additionalCutBase = {
    'Ele32_MediumID_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele32_MediumID_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27Or_MediumID_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27Or_MediumID_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele32_TightID_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele32_TightID_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele27Or_TightID_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele27Or_TightID_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele23Leg1_TightID_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele23Leg1_TightID_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele12Leg2_TightID_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedTight94XV2 == 1',
    'Ele12Leg2_TightID_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedTight94XV2 == 1',
    'Ele32_TightID_Selective_QPlus' : 'el_pt > 30 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele32_TightID_Selective_QMinus' : 'el_pt > 30 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele27Or_TightID_Selective_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele27Or_TightID_Selective_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QPlus' : 'el_pt > 20 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QMinus' : 'el_pt > 20 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
}
flags = {
    'Ele32_MediumID_QPlus' : '(passHltEle32WPTightGsf == 1)',
    'Ele32_MediumID_QMinus' : '(passHltEle32WPTightGsf == 1)',
    'Ele27Or_MediumID_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele27Or_MediumID_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele23Leg1_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele32_TightID_QPlus' : '(passHltEle32WPTightGsf == 1)',
    'Ele32_TightID_QMinus' : '(passHltEle32WPTightGsf == 1)',
    'Ele27Or_TightID_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele27Or_TightID_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele23Leg1_TightID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_TightID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_TightID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_TightID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele32_TightID_Selective_QPlus' : '(passHltEle32WPTightGsf == 1)',
    'Ele32_TightID_Selective_QMinus' : '(passHltEle32WPTightGsf == 1)',
    'Ele27Or_TightID_Selective_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele27Or_TightID_Selective_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle28WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele23Leg1_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
}
