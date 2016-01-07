import sys
import argparse
import ROOT as rt

#local imports
from macro import macro
from macro.razorAnalysis import wjetsSingleLeptonCutsMC, wjetsSingleLeptonCutsData, ttjetsSingleLeptonCutsMC, ttjetsSingleLeptonCutsData
from macro.razorWeights import *
from macro.razorMacros import *

LUMI_DATA = 2185 #in /pb
MCLUMI = 1 

SAMPLES_TTJ1L = ["Other", "DYJets", "SingleTop", "WJets", "TTJets"]
SAMPLES_WJ1L = ["Other", "DYJets", "SingleTop", "TTJets", "WJets"]
SAMPLES_TTJ2L = ["Other", "DYJets", "SingleTop", "WJets", "TTJets"]
SAMPLES_DYJ2L = ["Other", "SingleTop", "WJets", "TTJets", "DYJets"]
SAMPLES_VetoLepton = ["Other", "ZInv", "QCD", "DYJets", "SingleTop", "WJets", "TTJets"]
SAMPLES_VetoTau = ["Other", "ZInv", "QCD", "DYJets", "SingleTop", "WJets", "TTJets"]

DIR_1L = "root://eoscms:///eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoRazorControlRegions/OneLeptonFull_1p23_2015Final/RazorSkim/"
PREFIX_1L = "RunTwoRazorControlRegions_OneLeptonFull_SingleLeptonSkim"
FILENAMES_1L = {
            "TTJets"   : DIR_1L+"/"+PREFIX_1L+"_TTJets_1pb_weighted_RazorSkim.root",
            "WJets"    : DIR_1L+"/"+PREFIX_1L+"_WJetsToLNu_HTBinned_1pb_weighted_RazorSkim.root",
            "SingleTop": DIR_1L+"/"+PREFIX_1L+"_SingleTop_1pb_weighted_RazorSkim.root",
            "DYJets"   : DIR_1L+"/"+PREFIX_1L+"_DYJetsToLL_M-5toInf_HTBinned_1pb_weighted_RazorSkim.root",
            "Other"    : DIR_1L+"/"+PREFIX_1L+"_Other_1pb_weighted_RazorSkim.root",
            "Data"     : DIR_1L+"/"+PREFIX_1L+"_SingleLepton_Run2015D_GoodLumiGolden_NoDuplicates_RazorSkim.root"
            }

DIR_2L = "root://eoscms:///eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoRazorControlRegions/DileptonFull_1p23_2015Final/RazorSkim/"
PREFIX_2L = "RunTwoRazorControlRegions_DileptonFull_DileptonSkim"
FILENAMES_2L = {
            "TTJets"   : DIR_2L+"/"+PREFIX_2L+"_TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1pb_weighted_RazorSkim.root",
            "WJets"    : DIR_2L+"/"+PREFIX_2L+"_WJetsToLNu_HTBinned_1pb_weighted_RazorSkim.root",
            "SingleTop": DIR_2L+"/"+PREFIX_2L+"_SingleTop_1pb_weighted_RazorSkim.root",
            "DYJets"   : DIR_2L+"/"+PREFIX_2L+"_DYJetsToLL_M-5toInf_HTBinned_1pb_weighted_RazorSkim.root",
            "Other"    : DIR_2L+"/"+PREFIX_2L+"_VV_1pb_weighted_RazorSkim.root",
            "Data"     : DIR_2L+"/"+PREFIX_2L+"_SingleLepton_Run2015D_GoodLumiGolden_NoDuplicates_RazorSkim.root"
            }


DIR_VetoLepton = "root://eoscms:///eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoRazorControlRegions/VetoLeptonFull_1p23_2015Final/RazorNJets80Skim/"
PREFIX_VetoLepton = "RunTwoRazorControlRegions_VetoLeptonFull"
FILENAMES_VetoLepton = {
            "TTJets"   : DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_TTJets_1pb_weighted_RazorSkim.root",
            "WJets"    : DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_WJetsToLNu_HTBinned_1pb_weighted_RazorSkim.root",
            "SingleTop": DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_SingleTop_1pb_weighted_RazorSkim.root",
            "DYJets"   : DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_DYJetsToLL_M-5toInf_HTBinned_1pb_weighted_RazorSkim.root",
            "QCD"      : DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_QCD_HTBinned_1pb_weighted_RazorSkim.root",
            "ZInv"     : DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_ZJetsToNuNu_HTBinned_1pb_weighted_RazorSkim.root",            
            "Other"    : DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_Other_1pb_weighted_RazorSkim.root",
            "Data"     : DIR_VetoLepton+"/"+PREFIX_VetoLepton+"_HTMHT_Run2015D_GoodLumiGolden_RazorSkim.root"
            }

DIR_VetoTau = "root://eoscms:///eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoRazorControlRegions/VetoTauFull_1p23_2015Final/"
PREFIX_VetoTau = "RunTwoRazorControlRegions_VetoTauFull_RazorSkim"
FILENAMES_VetoTau = {
            "TTJets"   : DIR_VetoTau+"/"+PREFIX_VetoTau+"_TTJets_1pb_weighted.root",
            "WJets"    : DIR_VetoTau+"/"+PREFIX_VetoTau+"_WJetsToLNu_HTBinned_1pb_weighted.root",
            "SingleTop": DIR_VetoTau+"/"+PREFIX_VetoTau+"_SingleTop_1pb_weighted_RazorSkim.root",
            "DYJets"   : DIR_VetoTau+"/"+PREFIX_VetoTau+"_DYJetsToLL_M-5toInf_HTBinned_1pb_weighted.root",
            "QCD"      : DIR_VetoTau+"/"+PREFIX_VetoTau+"_QCD_HTBinned_1pb_weighted.root",
            "ZInv"     : DIR_VetoTau+"/"+PREFIX_VetoTau+"_ZJetsToNuNu_HTBinned_1pb_weighted.root",            
            "Other"    : DIR_VetoTau+"/"+PREFIX_VetoTau+"_Other_1pb_weighted.root",
            "Data"     : DIR_VetoTau+"/"+PREFIX_VetoTau+"_HTMHT_Run2015D_GoodLumiGolden.root"
            }




weightOpts = []

config = "config/run2_20151229_ControlRegion.config"
cfg = Config.Config(config)
VetoLeptonBinsMRLep = cfg.getBinning("VetoLeptonControlRegion")[0]
VetoLeptonBinsRsqLep = cfg.getBinning("VetoLeptonControlRegion")[1]
VetoLeptonControlRegionBinning = { "MR":VetoLeptonBinsMRLep, "Rsq":VetoLeptonBinsRsqLep }
TTJetsDileptonBinsMRLep = cfg.getBinning("TTJetsDileptonControlRegion")[0]
TTJetsDileptonBinsRsqLep = cfg.getBinning("TTJetsDileptonControlRegion")[1]
TTJetsDileptonBinsNBTags = cfg.getBinning("TTJetsDileptonControlRegion")[2]
TTJetsDileptonBinsNJets80 = cfg.getBinning("TTJetsDileptonControlRegion")[3]
TTJetsDileptonBinsNJets = cfg.getBinning("TTJetsDileptonControlRegion")[4]
TTJetsDileptonBinsLep2Pt = cfg.getBinning("TTJetsDileptonControlRegion")[5]
TTJetsDileptonBinsLep2Eta = cfg.getBinning("TTJetsDileptonControlRegion")[6]
TTJetsDileptonControlRegionBinning = { "MR":TTJetsDileptonBinsMRLep, "Rsq":TTJetsDileptonBinsRsqLep, "NBJetsMedium":TTJetsDileptonBinsNBTags, "NJets80":TTJetsDileptonBinsNJets80, "NJets40":TTJetsDileptonBinsNJets }

printdir="CrossCheckRegionPlots"

if __name__ == "__main__":
    rt.gROOT.SetBatch()

    #parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="display detailed output messages",
                                action="store_true")
    parser.add_argument("-d", "--debug", help="display excruciatingly detailed output messages",
                                action="store_true")
    args = parser.parse_args()
    debugLevel = args.verbose + 2*args.debug

    #initialize
    #weightHists = loadWeightHists(weightfilenames_DEFAULT, weighthistnames_DEFAULT, debugLevel)
    weightHists = {}
    sfHists = {}

    #make output directory
    os.system('mkdir -p '+printdir)

    sfHists = loadScaleFactorHists(sfFilename="/afs/cern.ch/work/s/sixie/public/releases/run2/CMSSW_7_4_2/src/RazorAnalyzer/data/ScaleFactors/RazorScaleFactors.root", processNames=SAMPLES_VetoLepton, debugLevel=debugLevel)


    #TTJets dilepton control sample
    ttjetsDileptonHists = makeControlSampleHists("TTJetsDilepton", 
                filenames=FILENAMES_2L, samples=SAMPLES_TTJ2L, 
                cutsMC=ttjetsDileptonCutsMC, cutsData=ttjetsDileptonCutsData, 
                bins=TTJetsDileptonControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
                printdir=printdir, debugLevel=debugLevel)


    #Veto Lepton cross-check region
    vetoLeptonHists = makeControlSampleHists("VetoLeptonControlRegion", 
                filenames=FILENAMES_VetoLepton, samples=SAMPLES_VetoLepton, 
                cutsMC=vetoLeptonControlRegionCutsMC, cutsData=vetoLeptonControlRegionCutsData, 
                bins=VetoLeptonControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
                printdir=printdir, debugLevel=debugLevel)
   
    # #Veto Tau cross-check region
    # vetoTauHists = makeControlSampleHists("VetoTauControlRegion", 
    #              filenames=FILENAMES_VetoTau, samples=SAMPLES_VetoTau, 
    #              cutsMC=vetoTauControlRegionCutsMC, cutsData=vetoTauControlRegionCutsData, 
    #              bins=VetoTauControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
    #              weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
    #              printdir=printdir, debugLevel=debugLevel)
   


  