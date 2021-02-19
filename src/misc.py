'''
Helper functions and various constants.

'''

from datetime import timedelta

def get_datetime(string):
    hms, ms = string.split('.')
    h,m,s = hms.split(':')
    ms, mcs = ms[:3], ms[3:]
    return timedelta(hours = int(h), minutes = int(m), seconds = int(s), milliseconds=int(ms), microseconds = int(mcs))


def fix_segments(best, segment):
    assert all(x for x in best)
    missing = sorted([i for i,x in enumerate(segment) if x is None])
    temp = set(missing)
    start, end = None, None
    for i in missing:
        if start is None:
            start = i
            end = i
            while end in temp:
                end += 1
        elif end == len(segment):
            break
        elif i < end:
            continue
        elif i == end:
            start, end = None, None
        else:
            # put logic here
            total_best = timedelta()
            for i in range(start, end+1):
                total_best += get_datetime(best[i])
            total_time = get_datetime(segment[end])
            for i in range(start, end+1):
                prop = get_datetime(best[i])/total_best
                segment[i] = str(max(prop * total_time, get_datetime(best[i])))

def fix_run_segments(segments, verbose = True):
    for key in segments.keys():
        if key == 'Best' or key == 'Name':
            continue
        else:
            fix_segments(segments['Best'], segments[key])

# Sheets
BANJO_ID = '1xElYGNc8s9Ruyk1jVWSbf4m2i2jgKOAdg0e18z9tTsw'
MARIO_ID = '1F9y3R6o6nxNU-Ce_UnoW10DrwufonaI4FWgWu3vG9_g'
TOOIE_ID = '1CE7tBxi4xo_V6qxbOrWLu68JsCOMc20XzOHksLdjPxg'

# Livesplit
BANJO_LSS = 'E:/Livesplit/Banjo-Kazooie - 100%.lss'
MARIO_LSS = 'E:/Livesplit/Super Mario 64 - 70 Star.lss'
TOOIE_LSS = 'E:/Livesplit/Banjo-Tooie - No DCWBC.lss'
TEST_LSS = '../lss/Banjo-Tooie - No DCWBC.lss'
