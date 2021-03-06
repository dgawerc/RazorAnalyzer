#! /usr/bin/env python
import glob

razorSignalDirs = {
        "Razor2016_MoriondRereco": "/eos/cms/store/group/phys_susy/razor/Run2Analysis/FullRazorInclusive/2016/V3p15_29Aug2017/SignalFastsim/"
        }

def parsePair(f):
    pair = f.replace('.root','').split('_')[-2:]
    return int(pair[0]), int(pair[1])

def getGChiPairs(signalDir, model):
    pattern = "%s/SMS-%s_*_*.root"%(signalDir, model)
    files = glob.glob(pattern)
    pairs = []
    for f in files:
        pairs.append(parsePair(f))
    return pairs

def gchipairs(model, tag='Razor2016_MoriondRereco'):
    gchilist = []
    
    if 'T1x' in model:
        model = 'T1ttbb'
    signalDir = razorSignalDirs[tag].replace('root://eoscms://','')
    return getGChiPairs(signalDir, model)
