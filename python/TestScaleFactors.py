import sys, os, argparse
import ROOT as rt

from macro import macro
from macro.razorAnalysis import Analysis
from macro.razorMacros import makeControlSampleHistsForAnalysis, appendScaleFactors

if __name__ == "__main__":
    rt.gROOT.SetBatch()

    #parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="display detailed output messages",
                                action="store_true")
    parser.add_argument("-d", "--debug", help="display excruciatingly detailed output messages",
                                action="store_true")
    parser.add_argument("--tag", dest="tag", default="Razor2015",
                                help="Analysis tag, e.g. Razor2015")
    args = parser.parse_args()
    debugLevel = args.verbose + 2*args.debug
    tag = args.tag
    if tag not in ["Razor2015","Razor2016"]:
        sys.exit("Error: tag "+tag+" not supported!")

    #initialize
    plotOpts = { 'comment':False }
    regions = {}
    #define all tests
    for name,jets in {"OneJet":(0,1),"DiJet":(2,3),"MultiJet":(4,-1)}.iteritems():
        regions["OneLepton"+name+"ClosureTest"] = Analysis("SingleLepton",tag=tag,
                njetsMin=jets[0], njetsMax=jets[1])
        for nb in range(3):
            regions["OneLepton"+name+"ClosureTest"+str(nb)+"B"] = Analysis("SingleLepton",tag=tag,
                    njetsMin=jets[0], njetsMax=jets[1], nbMin=nb, nbMax=nb)
    #add 3B test for MultiJet 
    regions["OneLeptonMultiJetClosureTest3B"] = Analysis("SingleLepton",tag=tag,
            njetsMin=4, nbMin=3, nbMax=3)

    sfHists = macro.loadScaleFactorHists(
            sfFilename="data/ScaleFactors/RazorMADD2015/RazorScaleFactors_%s.root"%(tag), 
            processNames=regions["OneLeptonOneJetClosureTest"].samples, debugLevel=debugLevel)
    sfVars = ("MR","Rsq")
    sfNJetsFile = rt.TFile.Open(
            "data/ScaleFactors/RazorMADD2015/RazorNJetsScaleFactors_%s.root"%(tag))
    sfHists['NJets'] = sfNJetsFile.Get("NJetsCorrectionScaleFactors")
    auxSFs = {"NJets":("NJets40","1")} 
    outfile = rt.TFile("RazorBTagClosureTests_%s.root"%(tag), "RECREATE")

    for region,analysis in regions.iteritems():
        #make output directory
        outdir = 'Plots/'+tag+'/'+region
        os.system('mkdir -p '+outdir)
        #set up analysis
        (xbins,cols) = analysis.unrollBins
        #perform analysis
        hists = makeControlSampleHistsForAnalysis( analysis, plotOpts=plotOpts, sfHists=sfHists,
                sfVars=sfVars, printdir=outdir, auxSFs=auxSFs, btags=analysis.nbMin,
                debugLevel=debugLevel )
        #compute scale factors
        appendScaleFactors( region+"MR", hists, sfHists, lumiData=analysis.lumi, var="MR",
                debugLevel=debugLevel, signifThreshold=1.0, printdir=outdir )
        appendScaleFactors( region+"Rsq", hists, sfHists, lumiData=analysis.lumi, var="Rsq",
                debugLevel=debugLevel, signifThreshold=1.0, printdir=outdir )
        #export histograms
        macro.exportHists( hists, outFileName='controlHistograms'+region+'.root',
                outDir=outdir, debugLevel=debugLevel )
        #write out scale factors
        print "Writing scale factor histogram",sfHists[region+"MR"].GetName(),"to file"
        outfile.cd()
        sfHists[region+"MR"].Write( sfHists[region+"MR"].GetName() )
        sfHists[region+"Rsq"].Write( sfHists[region+"Rsq"].GetName() )

    outfile.Close()