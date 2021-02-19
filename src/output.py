'''
Functions for writing .lss data to .csv or google sheets.
'''
def write_to_sheets(sheet_id, worksheet_name, data):
    import time
    import gspread
    gc = gspread.oauth()
    sh = gc.open_by_key(sheet_id)
    wk = sh.worksheet(worksheet_name)

    num_col = wk.col_count
    print("Spreadsheet Cols:", num_col)
    print("Data Columns:", len(data[0]))
    if num_col <= (len(data[0]) + 1):
        wk.add_cols(len(data[0]) - num_col + 2)

    for i, row in enumerate(data, start = 1):
        for j, value in enumerate(row, start = 1):
            time.sleep(1)
            wk.update_cell(i,j,value)
    return

def write_to_csv(filename, data):
    with open(filename, 'w') as temp:
        for x in data:
            line = ','.join(x)+'\n'
            temp.write(line)
            #print(*x)
