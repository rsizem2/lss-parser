'''
Code for pulling run data from livesplit .lss, using the xmltree library
'''

import xml.etree.ElementTree as ET

def get_complete_runs(root, verbose = True):
    # gets all complete runs
    runs = root.find('AttemptHistory')
    completed_runs = list()
    for run in runs:
        if len(run) > 0:
            # finished runs have a child
            if verbose:
                print(run.attrib)
                print()
            completed_runs.append(run.attrib['id'])
    completed_runs = set(completed_runs)
    segments = root.find('Segments')

    # gets all completed runs with NO skipped splits
    for segment in segments:
        name = segment.find('Name')
        if verbose: print(name.text)
        history = segment.find('SegmentHistory')
        ids = set()
        for run in history:
            if len(run) > 0:
                ids.add(run.attrib['id'])
        completed_runs &= ids
        if verbose:
            print(completed_runs)
            print()
    return completed_runs

def get_complete_segments(runs, root, verbose = True):
    values = list()
    completed_runs = sorted(runs, key=lambda x: int(x))
    segments = root.find('Segments')
    print(completed_runs)
    names = ['Best Segment']
    names.extend('Run '+ x for x in completed_runs)
    values.append(names)
    for i, segment in enumerate(segments):
        name = segment.find('Name')
        print(name.text)
        segs = list()
        best = segment.find('BestSegmentTime')
        for child in best:
            segs.append(child.text)
            print('Best Segment:', child.text)
        history = segment.find('SegmentHistory')
        for run in history:
            if run.attrib['id'] in completed_runs:
                for child in run:
                    print("Run", str(run.attrib['id'])+":", child.text)
                    segs.append(child.text)
            print()
        values.append(segs)

    for x in values:
        print(x)

    return values
