import xml.etree.ElementTree as ET
import gspread

from constants import TOOIE_ID, TOOIE_LSS
from completed_runs import get_complete_runs, get_complete_segments
from incomplete_runs import get_runs



def get_xmltree(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    return tree, root

    
def write_to_googlesheet(sheet_id, worksheet_name, data):
    import time
    gc = gspread.oauth()
    sh = gc.open_by_key(sheet_id)
    wk = sh.worksheet(worksheet_name)
    
    num_col = wk.col_count
    print("Spreadsheet Cols:", num_col)
    print("Data Columns:", len(data[0]))
    if num_col <= (len(data[0]) + 1):
        wk.add_cols(len(data[0]) - num_col + 2)

    for i, row in enumerate(data, start = 1):
        for j, value in enumerate(row, start = 2):
            time.sleep(1)
            wk.update_cell(i,j,value)
    
    return

def write_to_csv():
    pass

    
def write_tooie(complete = True, google = True):
    splits_file = TOOIE_LSS
    sheet_id = TOOIE_ID
    worksheet = 'Runs'
    
    tree, root = get_xmltree(splits_file)
    if complete:
        runs = get_complete_runs(root, True)
        data = get_complete_segments(runs, root)
    else:
        pass
    if google:
        write_to_googlesheet(sheet_id, worksheet, data)
    else:
        pass

write_tooie()

