import xml.etree.ElementTree as ET

from constants import TOOIE_ID, TOOIE_LSS, TEST_LSS
from completed_runs import get_complete_runs, get_complete_segments
from incomplete_runs import get_run_segments



def get_xmltree(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return tree, root

def write_to_csv():
    pass


def write_tooie(complete = True):
    splits_file = TEST_LSS

    tree, root = get_xmltree(splits_file)
    if complete:
        runs = get_complete_runs(root, True)
        data = get_complete_segments(runs, root)
    else:
        runs = get_run_segments(root, True)
        segs = zip(*[runs[key] for key in runs.keys()])
        for x in segs:
            print(*x)

write_tooie(False)
