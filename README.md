README
================

The scripts in this repository can be used to parse livesplit data for
easier analysis.

## Example

Importing .lss data into a Pandas DataFrame object

``` python
splits_file = "lss/Banjo-Tooie - No DCWBC.lss"

tree, root = get_xmltree(splits_file)
runs = get_run_segments(root)
format_data(runs).head(n = 10)
```

    ##                     0                 1  ...                 3                 4
    ## 0                Name              Best  ...             Run 1             Run 2
    ## 1            Klungo 1  00:01:59.0600000  ...  00:02:14.2600000  00:02:27.0360000
    ## 2           MT Puzzle  00:02:55.6440000  ...  00:02:57.6940000  00:03:10.7250000
    ## 3      Golden Goliath  00:04:35.6000000  ...  00:04:36.0840000  00:04:36.4920000
    ## 4               Flies  00:03:33.7970000  ...  00:03:44.8930000  00:03:43.7830000
    ## 5           Targitzan  00:03:15.7580000  ...  00:03:15.7580000  00:03:25.5210000
    ## 6          GGM Puzzle  00:01:14.9990000  ...  00:01:15.3430000  00:01:15.0810000
    ## 7           WW Puzzle  00:01:21.4300000  ...  00:01:26.6540000  00:01:28.9120000
    ## 8      Enter WW (GGM)  00:05:35.2680000  ...  00:05:35.2680000  00:05:36.3310000
    ## 9  Cactus of Strength  00:02:40.7660000  ...  00:03:05.8830000  00:02:40.7660000
    ## 
    ## [10 rows x 5 columns]
