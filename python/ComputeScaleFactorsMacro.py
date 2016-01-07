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
SAMPLES_WJ1L = ["Other", "ZInv", "QCD", "DYJets", "SingleTop", "TTJets", "WJets"]
SAMPLES_TTJ2L = ["Other", "DYJets", "SingleTop", "WJets", "TTJets"]
SAMPLES_DYJ2L = ["Other", "SingleTop", "WJets", "TTJets", "DYJets"]
SAMPLES_Veto = ["Other", "ZInv", "QCD", "DYJets", "SingleTop", "WJets", "TTJets"]
SAMPLES_WJ1L_INV = ["Other", "ZInv", "QCD", "DYJets", "SingleTop", "TTJets", "WJetsInv"]
SAMPLES_DYJ2L_INV = ["Other", "SingleTop", "WJets", "TTJets", "DYJets"]

DIR_1L = "root://eoscms:///eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoRazorControlRegions/OneLeptonFull_1p23_2015Final/RazorSkim/"
PREFIX_1L = "RunTwoRazorControlRegions_OneLeptonFull_SingleLeptonSkim"
FILENAMES_1L = {
            "TTJets"   : DIR_1L+"/"+PREFIX_1L+"_TTJets_1pb_weighted_RazorSkim.root",
            "WJets"    : DIR_1L+"/"+PREFIX_1L+"_WJetsToLNu_HTBinned_1pb_weighted_RazorSkim.root",
            "SingleTop": DIR_1L+"/"+PREFIX_1L+"_SingleTop_1pb_weighted_RazorSkim.root",
            "DYJets"   : DIR_1L+"/"+PREFIX_1L+"_DYJetsToLL_M-5toInf_HTBinned_1pb_weighted_RazorSkim.root",
            "Other"    : DIR_1L+"/"+PREFIX_1L+"_Other_1pb_weighted_RazorSkim.root",
            "ZInv"     : DIR_1L+"/"+PREFIX_1L+"_ZJetsToNuNu_HTBinned_1pb_weighted_RazorSkim.root",
            "QCD"      : DIR_1L+"/"+PREFIX_1L+"_QCD_HTBinned_1pb_weighted_RazorSkim.root",       
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

DIR_1L_INV = "root://eoscms:///eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoRazorControlRegions/OneLeptonAddToMETFull_1p23_2015Final/RazorNJets80Skim/"
PREFIX_1L_INV = "RunTwoRazorControlRegions_OneLeptonAddToMetFull_SingleLeptonSkim"
FILENAMES_1L_INV = {
            "TTJets"   : DIR_1L_INV+"/"+PREFIX_1L_INV+"_TTJets_1pb_weighted_RazorSkim.root",
            "WJetsInv" : DIR_1L_INV+"/"+PREFIX_1L_INV+"_WJetsToLNu_HTBinned_1pb_weighted_RazorSkim.root",
            "SingleTop": DIR_1L_INV+"/"+PREFIX_1L_INV+"_SingleTop_1pb_weighted_RazorSkim.root",
            "DYJets"   : DIR_1L_INV+"/"+PREFIX_1L_INV+"_DYJetsToLL_M-5toInf_HTBinned_1pb_weighted_RazorSkim.root",
            "Other"    : DIR_1L_INV+"/"+PREFIX_1L_INV+"_Other_1pb_weighted_RazorSkim.root",
            "ZInv"     : DIR_1L_INV+"/"+PREFIX_1L_INV+"_ZJetsToNuNu_HTBinned_1pb_weighted_RazorSkim.root",
            "QCD"      : DIR_1L_INV+"/"+PREFIX_1L_INV+"_QCD_HTBinned_1pb_weighted_RazorSkim.root",
            "Data"     : DIR_1L_INV+"/"+PREFIX_1L_INV+"_SingleLepton_Run2015D_RazorSkim_GoodLumiGolden_NoDuplicates.root"
            }

DIR_2L_INV = "root://eoscms:///eos/cms/store/group/phys_susy/razor/Run2Analysis/RunTwoRazorControlRegions/DileptonFullAddToMET_1p23_2015Final/RazorNJets80Skim/"
PREFIX_2L_INV = "RunTwoRazorControlRegions_DileptonAddToMetFull_DileptonSkim"
FILENAMES_2L_INV = {
            "TTJets"   : DIR_2L_INV+"/"+PREFIX_2L_INV+"_TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_1pb_weighted_RazorSkim.root",
            #"WJets"    : DIR_2L_INV+"/"+PREFIX_2L_INV+"_WJetsToLNu_HTBinned_1pb_weighted_RazorSkim.root",
            "SingleTop": DIR_2L_INV+"/"+PREFIX_2L_INV+"_SingleTop_1pb_weighted_RazorSkim.root",
            "DYJets"   : DIR_2L_INV+"/"+PREFIX_2L_INV+"_DYJetsToLL_M-5toInf_HTBinned_1pb_weighted_RazorSkim.root",
            "Other"    : DIR_2L_INV+"/"+PREFIX_2L_INV+"_Other_1pb_weighted_RazorSkim.root",
            "Data"     : DIR_2L_INV+"/"+PREFIX_2L_INV+"_SingleLepton_Run2015D_GoodLumiGolden_NoDuplicates_RazorSkim.root"
            }


weightOpts = []

config = "config/run2_20151229_ControlRegion.config"
cfg = Config.Config(config)
binsMRLep = cfg.getBinning("WJetControlRegion")[0]
binsRsqLep = cfg.getBinning("WJetControlRegion")[1]
binsNBTags = [0.,1.,2.,3.,4.]
binsNJets80 = [0.,1.,2.,3.,4.]
binsNJets = [0.,1.,2.,3.,4.,5.,6.,7.]
binsLepPt = [20.,25.,30.,35.,40.,45.,50.,70.,100]
ControlRegionBinning = { "MR":binsMRLep, "Rsq":binsRsqLep, "NBJetsMedium":binsNBTags, "NJets80":binsNJets80, "NJets40":binsNJets, "lep1.Pt()":binsLepPt, ("MR","Rsq"):[], ("MR","Rsq","NJets40"):[]}
ZNuNu_1L_ControlRegionBinning = { "MR_NoW":binsMRLep, "Rsq_NoW":binsRsqLep, "NBJetsMedium":binsNBTags, "NJets80":binsNJets80, "NJets40":binsNJets, ("MR_NoW","Rsq_NoW"):[] }

printdir="ControlSamplePlots"

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
    weightHists = {}
    sfHists = {}

    #make output directory
    os.system('mkdir -p '+printdir)

    sfVars = ("MR","Rsq")
    sfVars_NoW = ("MR_NoW", "Rsq_NoW")

    # #DYJets control sample
    # dyjetsDileptonHists = makeControlSampleHists("DYJetsDilepton", 
    #             filenames=FILENAMES_2L, samples=SAMPLES_DYJ2L, 
    #             cutsMC=dyjetsDileptonCutsMC, cutsData=dyjetsDileptonCutsData, 
    #             bins=ControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
    #             weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
    #             printdir=printdir, debugLevel=debugLevel)
    # appendScaleFactors("DYJets", dyjetsDileptonHists, sfHists, lumiData=LUMI_DATA, debugLevel=debugLevel, printdir=printdir)

    #WJets control sample
    wjetsSingleLeptonHists = makeControlSampleHists("WJetsSingleLepton", 
                filenames=FILENAMES_1L, samples=SAMPLES_WJ1L, 
                cutsMC=wjetsSingleLeptonCutsMC, cutsData=wjetsSingleLeptonCutsData, 
                bins=ControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
                printdir=printdir, sfVars=sfVars, debugLevel=debugLevel)
    appendScaleFactors("WJets", wjetsSingleLeptonHists, sfHists, lumiData=LUMI_DATA, debugLevel=debugLevel, var=sfVars, printdir=printdir)
    wjetsSingleLeptonHists = makeControlSampleHists("WJetsSingleLeptonAfterCorrection", 
                filenames=FILENAMES_1L, samples=SAMPLES_WJ1L, 
                cutsMC=wjetsSingleLeptonCutsMC, cutsData=wjetsSingleLeptonCutsData, 
                bins=ControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
                printdir=printdir, sfVars=sfVars, debugLevel=debugLevel)

    #TTJets control sample
    ttjetsSingleLeptonHists = makeControlSampleHists("TTJetsSingleLepton", 
                filenames=FILENAMES_1L, samples=SAMPLES_TTJ1L, 
                cutsMC=ttjetsSingleLeptonCutsMC, cutsData=ttjetsSingleLeptonCutsData, 
                bins=ControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
                printdir=printdir, sfVars=sfVars, debugLevel=debugLevel)
    appendScaleFactors("TTJets", ttjetsSingleLeptonHists, sfHists, lumiData=LUMI_DATA, debugLevel=debugLevel, var=sfVars, printdir=printdir)
    ttjetsSingleLeptonHists = makeControlSampleHists("TTJetsSingleLeptonAfterCorrection", 
                filenames=FILENAMES_1L, samples=SAMPLES_TTJ1L, 
                cutsMC=ttjetsSingleLeptonCutsMC, cutsData=ttjetsSingleLeptonCutsData, 
                bins=ControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists=sfHists, weightOpts=weightOpts, 
                printdir=printdir, sfVars=sfVars, debugLevel=debugLevel)


    #WJets control sample
    wjetsSingleLeptonInvHists = makeControlSampleHists("WJetsSingleLeptonInv", 
                filenames=FILENAMES_1L_INV, samples=SAMPLES_WJ1L_INV, 
                cutsMC=wjetsSingleLeptonInvCutsMC, cutsData=wjetsSingleLeptonInvCutsData, 
                bins=ZNuNu_1L_ControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists={}, weightOpts=weightOpts, 
                printdir=printdir, sfVars=sfVars_NoW, debugLevel=debugLevel)
    appendScaleFactors("WJetsInv", wjetsSingleLeptonInvHists, sfHists, var=sfVars_NoW, lumiData=LUMI_DATA, debugLevel=debugLevel, printdir=printdir)
    wjetsSingleLeptonInvHists = makeControlSampleHists("WJetsSingleLeptonInvAfterCorrection", 
                filenames=FILENAMES_1L_INV, samples=SAMPLES_WJ1L_INV, 
                cutsMC=wjetsSingleLeptonInvCutsMC, cutsData=wjetsSingleLeptonInvCutsData, 
                bins=ZNuNu_1L_ControlRegionBinning, lumiMC=MCLUMI, lumiData=LUMI_DATA, 
                weightHists=weightHists, sfHists={}, weightOpts=weightOpts, 
                printdir=printdir, sfVars=sfVars_NoW, debugLevel=debugLevel)


    #write scale factors
    outfile = rt.TFile("RazorScaleFactors.root", "RECREATE")
    for name in sfHists:
        print "Writing scale factor histogram",sfHists[name].GetName(),"to file"
        sfHists[name].Write()
    outfile.Close()