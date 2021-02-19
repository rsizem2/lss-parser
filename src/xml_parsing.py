'''
Code for pulling run data from livesplit .lss, using the xmltree library
'''

import xml.etree.ElementTree as ET
from collections import defaultdict


def get_xmltree(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return tree, root


def get_complete_segments(root, verbose = False):
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
    # get all the individual segments
    values = list()
    completed_runs = sorted(completed_runs, key=lambda x: int(x))
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


def get_run_segments(root, verbose = False):
    runs = [x.attrib['id'] for x in root.find('AttemptHistory')]
    if verbose:
        print(runs)
    runs = set(runs)
    segments = root.find('Segments')
    segs = defaultdict(list)

    # all runs that get past the first split
    for i, segment in enumerate(segments, start = 1):
        name = segment.find('Name')
        segs['Name'].append(name.text)
        best = segment.find('BestSegmentTime')
        segs['Best'].append(best[0].text)
        if verbose:
            print(name.text)
            print('Best:', best[0].text)
        history = segment.find('SegmentHistory')
        ids = set(runs)
        for run in history:
            run_id = run.attrib['id']
            if len(run):
                segs[run_id].append(run[0].text)
                print(run_id, run[0].text)
            else:
                segs[run_id].append(None)
                print(run_id, None)
                pass
            if run_id in ids: ids.remove(run_id)
        for run_id in ids:
            segs[run_id].append(None)
            print(run_id, None)
    return segs
