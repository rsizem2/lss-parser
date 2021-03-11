"""
Various helper functions.
"""

from datetime import timedelta

def get_datetime(string):
    hms, ms = string.split('.')
    h,m,s = hms.split(':')
    ms, mcs = ms[:3], ms[3:]
    return timedelta(hours = int(h), minutes = int(m), seconds = int(s), milliseconds=int(ms), microseconds = int(mcs))


def impute_segments(best, segment):
    assert all(x for x in best)
    missing = set([i for i,x in enumerate(segment) if x is None])
    start, end = None, None
    while missing:
        temp = sorted(missing)
        start = temp[0]
        end = start+1
        while end in missing:
            end += 1
        # put logic here
        if end >= len(segment): 
            break
        total_best = timedelta()
        for i in range(start, end+1):
            total_best += get_datetime(best[i])
            if i in missing: missing.remove(i)
        total_time = get_datetime(segment[end])
        for i in range(start, end+1):
            prop = get_datetime(best[i])/total_best
            segment[i] = str(max(prop * total_time, get_datetime(best[i])))
    return

def fix_missing(segment):
    for i, seg in enumerate(segment):     
        if seg is None:
            segment[i] = ''
 
def fix_subsplit_names(names):
    for i, name in enumerate(names):
        if '}' in name:
            temp = name.split('}')[-1]
            names[i] = temp.strip()
        elif '-' in name:
            names[i] = name.strip(' -')
        

def fix_run_segments(segments, verbose = True):
    for key in segments.keys():
        if key == 'Best' or key == 'Name':
            continue
        else:
            impute_segments(segments['Best'], segments[key])
            fix_missing(segments[key])