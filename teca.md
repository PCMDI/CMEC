---
layout: default
title: TECA
---

## Toolkit for Extremes Climate Analysis (TECA)

### Overview

TECA is a general purpose tool for detecting discrete events in climate
model output. It leverages a map-reduce framework for efficient
parallelization at large scales (order 10K+ cores). Currently, TECA
contains detection algorithms for tropical cyclones, atmospheric rivers,
and extratropical cyclones; and plans are underway to implement algorithms
for mesoscale convective complexes, African Easterly waves, atmospheric
blocks, and fronts.

### Technical Description

TECA has two main interfaces aimed at two distinct use-cases: use
of ‘canned’ algorithms (TC, AR, ETC, etc.), and development of
user-defined algorithms. The TECA code base is written in modern C++
(i.e., using C++ 2011 standards), and contains a Python API.

The first interface is a command-line interface, with command-line
programs for each implemented detection algorithm. The command-line
interfaces take file paths as input and contains a number of arguments
for customization (e.g., setting of detection thresholds, setting output
files). A typical parallel run on NERSC systems looks like the following:

```bash
 srun -n 29200 teca_tc_detect	--input_regex ${data_dir}/${files_regex} \
				--candidate_file candidates_1990s.bin \
 				--track_file tracks_1990s.bin
```

The second interface leverages the Python API to allow non-C++-proficient
developers to easily prototype parallel performant algorithms using
a widely adopted language in the scientific community. Currently, no
canned algorithms are developed with the Python interface (though a few
collaborators are using this facility), but efforts are currently underway
to implement several different atmospheric river detection algorithms
using the Python interface: both for scientific use and to highlight the
flexibility of the TECA pipeline when integrated into Python. While the
Python API method is clearly more complicated from a user’s point of
view, it offers the option to design custom workflows. The example at
the end shows a simple TC-detector implemented with the Python API.

<strong>Quick links</strong>:&nbsp;
<a href="https://github.com/LBL-EESA/TECA">Repository</a>,
<a href="https://github.com/LBL-EESA/TECA#download-build-and-install">Installation</a>,
<a href="https://cascade-climate.atlassian.net/wiki/spaces/TECA/blog/2017/09/29/119668755/Analyzing+Cyclone+Tracks+with+TECA">Tutorials</a>,
<a href="https://github.com/LBL-EESA/TECA/blob/master/doc/teca_users_guide.pdf">Documentation</a>,
<a href="{{site.baseurl}}/teca_wehner_results.html">CAM Results</a>

<br>
<b>Contact:</b> William D. Collins (wdcollins@lbl.gov)

