#!/bin/tcsh

foreach sample( \
SMS-TChiHZ_HToGG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)
  setenv LSB_JOB_REPORT_MAIL N 
  set inputfilelist="/afs/cern.ch/work/j/jmao/public/releases/CMSSW_9_2_1/src/RazorAnalyzer/lists/Run2/razorNtuplerV3p8/MCFastsim/${sample}.cern.txt"
  set filesPerJob = 6 
  set nfiles = `cat $inputfilelist | wc | awk '{print $1}' `
  set maxjob=`python -c "print int($nfiles.0/$filesPerJob)-1"`
  echo "Sample " $sample " maxjob = " $maxjob 
  mkdir -p ../submissionHZ
  foreach jobnumber(`seq 0 1 $maxjob`)
    if ( ! -e /afs/cern.ch/user/s/sixie/eos/cms/store/group/phys_susy/razor/SusyEwkHgg/jobs/SusyEwkHgg_${sample}.Job${jobnumber}Of${maxjob}.root ) then
    #if ( ! -e /afs/cern.ch/user/s/sixie/eos/cms/store/group/phys_susy/razor/Run2Analysis/ANALYZERNAME/jobs/ANALYZERNAME_${sample}.Job${jobnumber}Of${maxjob}.root ) then
    echo "job " $jobnumber " out of " $maxjob
    bsub -q 1nh -o /afs/cern.ch/work/j/jmao/public/releases/CMSSW_9_2_1/src/RazorAnalyzer/submissionHZ/SusyEwkHgg_${sample}_${jobnumber}.out -J SusyEwkHgg_${sample}_${jobnumber} /afs/cern.ch/user/j/jmao/work/public/releases/CMSSW_9_2_1/src/RazorAnalyzer/scripts/runRazorJob_CERN_EOS_Dustin.csh SusyEwkHgg $inputfilelist 0 10 $filesPerJob $jobnumber SusyEwkHgg_${sample}.Job${jobnumber}Of${maxjob}.root /store/group/phys_susy/razor/SusyEwkHgg/HZtest/ /afs/cern.ch/user/j/jmao/work/public/releases/CMSSW_9_2_1/src/ Razor2016_MoriondRereco
    sleep 0.1
  end

end

