README
================

This repository contains various functions for parsing livesplit data.
I’ll do more with this at some point…

## Example

Importing .lss data into a Pandas DataFrame.

``` python
splits_file = "lss/Banjo-Tooie - No DCWBC.lss"
tree, root = get_xmltree(splits_file)
runs = get_run_segments(root)
df = write_to_dataframe(runs)
df.head(n = 10)
```

    ##                     0               1  ...               3               4
    ## 0               Split    Best Segment  ...           Run 1           Run 2
    ## 1            Klungo 1  0:01:59.060000  ...  0:02:14.260000  0:02:27.036000
    ## 2           MT Puzzle  0:02:55.644000  ...  0:02:57.694000  0:03:10.725000
    ## 3      Golden Goliath  0:04:35.600000  ...  0:04:36.084000  0:04:36.492000
    ## 4               Flies  0:03:33.797000  ...  0:03:44.893000  0:03:43.783000
    ## 5           Targitzan  0:03:15.758000  ...  0:03:15.758000  0:03:25.521000
    ## 6          GGM Puzzle  0:01:14.999000  ...  0:01:15.343000  0:01:15.081000
    ## 7           WW Puzzle  0:01:21.430000  ...  0:01:26.654000  0:01:28.912000
    ## 8      Enter WW (GGM)  0:05:35.268000  ...  0:05:35.268000  0:05:36.331000
    ## 9  Cactus of Strength  0:02:40.766000  ...  0:03:05.883000  0:02:40.766000
    ## 
    ## [10 rows x 5 columns]
