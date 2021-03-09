'''
Functions for demonstation and testing
'''


def write_tooie(complete = False, google = False, test = False):
    from misc import TEST_LSS, TOOIE_ID, TOOIE_LSS
    from helper import fix_run_segments, fix_subsplit_names
    from xml_parsing import get_xmltree, get_run_segments, get_complete_segments
    from output import write_to_csv, write_to_sheets
    splits_file = TOOIE_LSS
    csv_file = '../csv/tooie.csv'
    sheet_id = TOOIE_ID
    worksheet = 'Runs'

    tree, root = get_xmltree(splits_file)
    if complete:
        data = get_complete_segments(root, True)
    else:
        runs = get_run_segments(root, True)
        fix_run_segments(runs)
        keys = set(runs.keys())
        rownames = list()
        rownames.extend(['Name', 'Best'])
        keys.difference_update(rownames)
        rownames.extend(sorted(keys))
        fix_subsplit_names(runs['Name'])
        data = [rownames]
        data.extend(list(zip(*[runs[key] for key in runs.keys()])))
    if google:
        write_to_sheets(sheet_id, worksheet, data)
    else:
        write_to_csv(csv_file, data)

def format_data(runs):
    from pandas import DataFrame as df
    #fix_run_segments(runs)
    keys = set(runs.keys())
    rownames = list()
    rownames.extend(['Name', 'Best'])
    keys.difference_update(rownames)
    rownames.extend([" ".join(["Run",x]) for x in sorted(keys)])
    fix_subsplit_names(runs['Name'])
    data = [rownames]
    data.extend(list(zip(*[runs[key] for key in runs.keys()])))
    return df.from_dict(data)

#write_tooie(False, True, True)
