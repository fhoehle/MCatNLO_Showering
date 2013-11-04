First: 
  convert MCatNLO to LHE format, see MCatNLO2LHE

Second:
  GEN SIM
  cmsDriver.py Configuration/GenProduction/python/TT_7TeV_mcatnlo_cff.py --step GEN,SIM --beamspot Realistic7TeV2011Collision --conditions START42_V14B::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM --filein file: MyTT_MCatNLO_test.lhe --fileout TT_test_MCatNLO_START42_V14B_GEN_SIM.root --python_filename TT_test_MCatNLO_START42_V14B_GEN-SIM_cfg.py --no_exec -n 10

  or with own GenFragments
  
  cmsDriver.py Configuration/MyGenProduction/python/TT_7TeV_mcatnlo_cff.py --step GEN,SIM --beamspot Realistic7TeV2011Collision --conditions START42_V14B::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM --filein file:../MCatNLO2LHE/template/TT_MCatNLO_START42_V14B_LHE2EDM.root --fileout TT_test_MCatNLO_START42_V14B_GEN_SIM.root --python_filename TT_test_MCatNLO_START42_V14B_GEN-SIM_cfg.py --no_exec -n -1
  
  with tauola
  
  cmsDriver.py Configuration/MyGenProduction/python/TT_7TeV_mcatnlo_tauola_cff.py --step GEN,SIM --beamspot Realistic7TeV2011Collision --conditions START42_V14B::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM --filein file:../MCatNLO2LHE/template/TT_MCatNLO_START42_V14B_LHE2EDM.root --fileout TT_test_MCatNLO_START42_V14B_GEN_SIM.root --python_filename TT_test_MCatNLO_START42_V14B_GEN-SIM_cfg.py --no_exec -n -1

  
