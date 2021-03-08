from AFBElectronCommon import *
import etc.inputs.tnpSampleDef as tnpSamples
samplesDef = {
    'data'   : tnpSamples.AFB['dataUL2017'].clone(),
    'mcNom'  : tnpSamples.AFB['mgUL2017'].clone(),
    'mcAlt'  : tnpSamples.AFB['amcUL2017'].clone(),
    'tagSel' : tnpSamples.AFB['mgUL2017'].clone(),
}
samplesDef['mcNom'].set_cut(tight_mcTrue)
samplesDef['mcAlt'].set_cut(tight_mcTrue)
samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
samplesDef['tagSel'].set_cut('tag_Ele_pt > 38 && '+tight_mcTrue)
additionalCuts={}

baseOutDir = 'results/AFBElectronTriggerUL2017_v3_3/'
tnpTreeDir = 'tnpEleTrig'
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.1 && el_q*tag_Ele_q < 0 && ( el_pt<20 ? sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 : 1 )'
additionalCutBase = {
    'Ele32_MediumID_QPlus' : 'el_pt > 28 && el_q > 0 && passingCutBasedMedium94XV2 == 1 && PrescaleHLTEle32WPTightGsf == 1',
    'Ele32_MediumID_QMinus' : 'el_pt > 28 && el_q < 0 && passingCutBasedMedium94XV2 == 1 && PrescaleHLTEle32WPTightGsf == 1',
    'Ele32Test_MediumID_QPlus' : 'el_pt > 28 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27_MediumID_QPlus' : 'el_pt > 23 && el_q > 0 && passingCutBasedMedium94XV2 == 1 && PrescaleHLTEle27WPTightGsf == 1',
    'Ele27_MediumID_QMinus' : 'el_pt > 23 && el_q < 0 && passingCutBasedMedium94XV2 == 1 && PrescaleHLTEle27WPTightGsf == 1',
    'Ele27Test_MediumID_QPlus' : 'el_pt > 23 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27Or_MediumID_QPlus' : 'el_pt > 23 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele27Or_MediumID_QMinus' : 'el_pt > 23 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QPlus' : 'el_pt > 19 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele23Leg1_MediumID_QMinus' : 'el_pt > 19 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedMedium94XV2 == 1',
    'Ele12Leg2_MediumID_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedMedium94XV2 == 1',
    'Ele32_TightID_Selective_QPlus' : 'el_pt > 28 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge && PrescaleHLTEle32WPTightGsf == 1',
    'Ele32_TightID_Selective_QMinus' : 'el_pt > 28 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge && PrescaleHLTEle32WPTightGsf == 1',
    'Ele27_TightID_Selective_QPlus' : 'el_pt > 23 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge && PrescaleHLTEle27WPTightGsf == 1',
    'Ele27_TightID_Selective_QMinus' : 'el_pt > 23 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge && PrescaleHLTEle27WPTightGsf == 1',
    'Ele27Or_TightID_Selective_QPlus' : 'el_pt > 23 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele27Or_TightID_Selective_QMinus' : 'el_pt > 23 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QPlus' : 'el_pt > 19 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele23Leg1_TightID_Selective_QMinus' : 'el_pt > 19 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QPlus' : 'el_pt > 10 && el_q > 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
    'Ele12Leg2_TightID_Selective_QMinus' : 'el_pt > 10 && el_q < 0 && passingCutBasedTight94XV2 == 1 && el_3charge',
}
flags = {
    'Ele32_MediumID_QPlus' : '( passHltEle32WPTightGsf == 1 )',
    'Ele32_MediumID_QMinus' : '( passHltEle32WPTightGsf == 1 )',
    'Ele32Test_MediumID_QPlus' : '( passHltEle32WPTightGsf == 1 )',
    'Ele27_MediumID_QPlus' : '( passHltEle27WPTightGsf == 1 )',
    'Ele27_MediumID_QMinus' : '( passHltEle27WPTightGsf == 1 )',
    'Ele27Test_MediumID_QPlus' : '( passHltEle27WPTightGsf == 1 )',
    'Ele27Or_MediumID_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele27Or_MediumID_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele23Leg1_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1 == 1 && el_l1et > L1ThesholdHLTEle23Ele12CaloIdLTrackIdLIsoVL )',
    'Ele23Leg1_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1 == 1 && el_l1et > L1ThesholdHLTEle23Ele12CaloIdLTrackIdLIsoVL )',
    'Ele12Leg2_MediumID_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_MediumID_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele32_TightID_Selective_QPlus' : '( passHltEle32WPTightGsf == 1 )',
    'Ele32_TightID_Selective_QMinus' : '( passHltEle32WPTightGsf == 1 )',
    'Ele27_TightID_Selective_QPlus' : '( passHltEle27WPTightGsf == 1 )',
    'Ele27_TightID_Selective_QMinus' : '( passHltEle27WPTightGsf == 1 )',
    'Ele27Or_TightID_Selective_QPlus' : '( passHltEle27WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele27Or_TightID_Selective_QMinus' : '( passHltEle27WPTightGsf == 1 || passHltEle32WPTightGsf == 1 )',
    'Ele23Leg1_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele23Leg1_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match == 1)',
    'Ele12Leg2_TightID_Selective_QPlus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
    'Ele12Leg2_TightID_Selective_QMinus' : '(passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 == 1)',
}

flagBinningDef={
    'Ele32_MediumID_QPlus' : bin_Ele32,
    'Ele32_MediumID_QMinus' : bin_Ele32,
    'Ele32Test_MediumID_QPlus' : bin_Ele32,
    'Ele27_MediumID_QPlus' : bin_Ele27,
    'Ele27_MediumID_QMinus' : bin_Ele27,
    'Ele27Test_MediumID_QPlus' : bin_Ele27,
    'Ele27Or_MediumID_QPlus' : bin_Ele27,
    'Ele27Or_MediumID_QMinus' : bin_Ele27,
    'Ele23Leg1_MediumID_QPlus' : bin_Ele23,
    'Ele23Leg1_MediumID_QMinus' : bin_Ele23,
    'Ele12Leg2_MediumID_QPlus' : bin_Ele12,
    'Ele12Leg2_MediumID_QMinus' : bin_Ele12,
    'Ele32_TightID_Selective_QPlus' : bin_Ele32,
    'Ele32_TightID_Selective_QMinus' : bin_Ele32,
    'Ele27_TightID_Selective_QPlus' : bin_Ele27,
    'Ele27_TightID_Selective_QMinus' : bin_Ele27,
    'Ele27Or_TightID_Selective_QPlus' : bin_Ele27,
    'Ele27Or_TightID_Selective_QMinus' : bin_Ele27,
    'Ele23Leg1_TightID_Selective_QPlus' : bin_Ele23,
    'Ele23Leg1_TightID_Selective_QMinus' : bin_Ele23,
    'Ele12Leg2_TightID_Selective_QPlus' : bin_Ele12,
    'Ele12Leg2_TightID_Selective_QMinus' : bin_Ele12,
}
