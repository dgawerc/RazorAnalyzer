#!/bin/tcsh

foreach sample( \
#GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8 \
#GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8 \
#GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8 \
#QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8 \
#QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8 \
#QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8 \
#GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8 \
#VBFHToGG_M125_13TeV_amcatnlo_pythia8 \
#VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
#ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_v2 \
#bbHToGG_M-125_4FS_yb2_13TeV_amcatnlo \
#bbHToGG_M-125_4FS_ybyt_13TeV_amcatnlo \
#DiPhotonJetsBox_M40_80-Sherpa \
#DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8 \
#DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa \
#TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8 \
#TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
#WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph \
#WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8 \
#TTGG_0Jets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8 \
#WGGJets_TuneCUETP8M1_13TeV_madgraphMLM_pythia8 \
#WGG_5f_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
#ZGGToLLGG_5f_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
)
  setenv LSB_JOB_REPORT_MAIL N 
  set inputfilelist="/afs/cern.ch/work/j/jmao/public/releases/CMSSW_9_2_1/src/RazorAnalyzer/lists/Run2/razorNtuplerV3p8/MC_Summer16/${sample}.cern.txt"
  set filesPerJob = 8 
  set nfiles = `cat $inputfilelist | wc | awk '{print $1}' `
  set maxjob=`python -c "print int($nfiles.0/$filesPerJob)-1"`
  echo "Sample " $sample " maxjob = " $maxjob 
  mkdir -p ../submissionbkg
  foreach jobnumber(`seq 0 1 $maxjob`)
    if ( ! -e /afs/cern.ch/user/s/sixie/eos/cms/store/group/phys_susy/razor/SusyEwkHgg/jobs/SusyEwkHgg_${sample}.Job${jobnumber}Of${maxjob}.root ) then
    #if ( ! -e /afs/cern.ch/user/s/sixie/eos/cms/store/group/phys_susy/razor/Run2Analysis/ANALYZERNAME/jobs/ANALYZERNAME_${sample}.Job${jobnumber}Of${maxjob}.root ) then
    echo "job " $jobnumber " out of " $maxjob
    bsub -q 1nh -o /afs/cern.ch/work/j/jmao/public/releases/CMSSW_9_2_1/src/RazorAnalyzer/submissionHZ/SusyEwkHgg_${sample}_${jobnumber}.out -J SusyEwkHgg_${sample}_${jobnumber} /afs/cern.ch/user/j/jmao/work/public/releases/CMSSW_9_2_1/src/RazorAnalyzer/scripts/runRazorJob_CERN_EOS_Dustin.csh SusyEwkHgg $inputfilelist 0 0 $filesPerJob $jobnumber SusyEwkHgg_${sample}.Job${jobnumber}Of${maxjob}.root /store/group/phys_susy/razor/SusyEwkHgg/${sample}_jobs/ /afs/cern.ch/user/j/jmao/work/public/releases/CMSSW_9_2_1/src/ Razor2016_MoriondRereco
    sleep 0.1
  end

end

