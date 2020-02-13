# PlanetLab Status Report

Updated: 2020-02-13

  * [Nodes in the diku_IN5570 slice](nodes-all.txt): 553
  * [Good nodes in the diku_IN5570 slice](nodes-good.txt): 34

What classifies as a good node:

  * Reachable from Oslo within a 5-second delay
  * Can ping google.com

## Scripts

### [`ping.py`](ping.py)

Given a list of nodes via standard input, finds the good ones among
them (see definition of a good node above).

The script assumes that you have the requirements installed in your
Python environment:

```
$ pip install requirements.txt
```

The script **also** assumes that you have an SSH agent running with
your PlanetLab key added.
