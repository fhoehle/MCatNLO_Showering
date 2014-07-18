# Auto generated configuration file
# using: 
# Revision: 1.303.2.7 
# Source: /cvs/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: REDIGI --step DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --conditions auto:startup --pileup mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi --datamix NODATAMIXER --eventcontent AODSIM --datatier AODSIM --filein file:TT_test_MCatNLO_START42_V14B_GEN_SIM.root --fileout TT_test_MCatNLO_START42_V14B_AODSIM.root --python_filename TT_test_MCatNLO_START42_V14B_AODSIM_cfg.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:TT_test_MCatNLO_START42_V14B_GEN_SIM.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.303.2.7 $'),
    annotation = cms.untracked.string('REDIGI nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['startup']


process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('TT_test_MCatNLO_'+process.GlobalTag.globaltag.split(':')[0]+'_AODSIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AODSIM')
    )
)

# Additional output definition

# Other statements

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step])

import sys
if not "crab" in sys.argv[0]:
  from FWCore.ParameterSet.VarParsing import VarParsing
  options = VarParsing ('analysis')
  options.register('dumpPythonOnly',
          '',
          VarParsing.multiplicity.singleton, VarParsing.varType.string,
          "dump only python cfg for later use")
  options.parseArguments()
  if options.inputFiles != []:
    process.source.fileNames=options.inputFiles
  if options.outputFile != 'output.root':
    process.AODSIMoutput.fileName = options.outputFile
  if options.dumpPythonOnly != "":
   with open(options.dumpPythonOnly,"w") as cfg:
     cfg.write(process.dumpPython())
   print "python dump done"
   sys.exit(0)
