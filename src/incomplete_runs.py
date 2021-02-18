'''
Code for pulling out all runs from livesplit .lss which has been parsed into an xml.etree called 'root'

These pull all runs which have a single complete segment, i.e. weren't reset on the first split.
'''

def get_runs(root, verbose = True):
    runs = [x.attrib['id'] for x in root.find('AttemptHistory')]
    if verbose: 
        print(runs)
    runs = set(runs)
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