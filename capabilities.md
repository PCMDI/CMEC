---
layout: default
title: Capabilities
---

## Capabilities Overview

The capabilities currently contributing to CMEC are briefly highlighted below:

******
<!-- CMEC driver -->
<div class="span4 box">
<h3>
CMEC driver
</h3>
<p>
CMEC driver is a command-line program that manages execution of CMEC-compliant evaluation modules.  It has been designed to provide a user with a simple and consistent interface regardless of the evaluation module (or set of modules) employed, and is responsible for organization of the output data produced by these evaluations.
</p>
<br>
<strong>Quick links</strong>:
<a href="https://github.com/cmecmetrics/cmec-driver">Repository</a>, 
<a href="https://github.com/cmecmetrics/cmec-driver#installation">Installation</a>
</div>

******

<!-- PMP -->
<div class="span4 box">
<h3>
<a class="reference internal" href="pmp.html">The PCMDI Metrics Package (PMP)</a>
</h3>
<p>
PMP provides a diverse suite of relatively robust high level summary statistics
across space and time scales, gauging the differences between models and observations.
PMP summaries encapsulate the simulated atmosphere, ocean, ice and land - with
current examples highlighting atmospheric characteristics. PMP is useful for
producing quick, high-level summaries of new simulations and putting them into
the context of all previous generations of AMIP and CMIP.
</p>
<center>
<a border="0" href="pmp.html"><img src="{{site.baseurl}}/assets/images/pmp_cover_side_sm.png"></a>
</center>
<br>
<strong>Metrics include</strong>:
ENSO, Mean Climate, MJO metrics, Extra-tropical modes of variability, Monsoon metrics (Sperber and Wang), Precipitation variability, Sub-daily precipitation
<br>
<strong>Quick links</strong>:
<a href="https://github.com/PCMDI/pcmdi_metrics">Repository</a>, 
<a href="https://pcmdi.github.io/pcmdi_metrics/install.html">Installation</a>, and
<a href="results/physical.html">Results</a>
</div>

******

<!-- ILAMB -->
<a name="ILAMB"></a>
<div class="span4 box">
<h3>
<a class="reference internal" href="ilamb.html">The International Land
Model Benchmarking (ILAMB) Package</a>
</h3>
<p>
ILAMB provides a variety of in-depth diagnostics of more than 24
terrestrial biogeochemical and hydrological model variables on annual
and inter-annual time scales. It compares these variables with over
60 site-based, regional, and global observational data sets, and
scores model performance based on a combination bias, RMSE, and seasonal
cycle metrics. Relationships between many biogeochemical variables
and physical driver variables are calculated from model results and
compared with observational estimates. ILAMB is useful for detailed
exploration of land biogeochemical and hydrological model responses and
provides an interactive interface designed to enable the user to more
rapidly understand the underlying drivers of those responses.
</p>
<center>
<a border="0" href="ilamb.html"><img src="{{site.baseurl}}/assets/images/ilamb_biomass_sm.png"></a>
</center>
<br>
<strong>Metrics include</strong>: Ecosystem and Carbon Cycle, Hydrology Cycle, Radiation and Energy Cycle, Forcings, Relationships
<br>
<strong>Quick links</strong>:&nbsp;
<a href="https://github.com/rubisco-sfa/ILAMB">Repository</a>,
<a href="https://www.ilamb.org/doc/install.html">Installation</a>, and
<a href="https://www.ilamb.org/doc/tutorial.html">Tutorials</a>
</div>

******

<!-- IOMB -->
<a name="IOMB"></a>
<div class="span4 box">
<h3>
<a class="reference internal" href="iomb.html">The International Ocean Model
Benchmarking (IOMB) Package</a>
</h3>
<p>
IOMB provides a variety of in-depth diagnostics of marine biogeochmical
model variables on annual and inter-annual time scales. It compares a
growing number of variables with site-based, transect, regional, and
global observational data sets, and scores model performance based on a
combination of bias, RMSE, and seasonal cycle metrics. IOMB is useful
for detailed exploration of ocean biogeochemical model responses and
provides an interactive interface designed to enable the user to more
rapidly understand the underlying drivers of those responses.
</p>
<center>
<a border="0" href="iomb.html"><img src="{{site.baseurl}}/assets/images/iomb_temperature_sm.png"></a>
</center>
<p>IOMB uses the same code base as ILAMB (described above). The links below
refer to ILAMB instead of IOMB.</p>
<br>
<strong>Metrics include</strong>: Chemical Oceanography, Physical Oceanography, SeaAirFluxes
<br>
<strong>Quick links</strong>:&nbsp;
<a href="https://github.com/rubisco-sfa/ILAMB">Repository</a>,
<a href="https://www.ilamb.org/doc/install.html">Installation</a>, and
<a href="https://www.ilamb.org/doc/tutorial.html">Tutorials</a>
</div>

******

<!-- Community -->
<div class="span4 box">
<h3>
Community contributed packages
</h3>
<a href="https://github.com/nick-klingaman/ASoP">Analysing Scales of Precipitation (ASoP)</a>
<br>The ASoP package offers two workflows: one that characterizes the spectrum of precipitation intensity (ASoP Spectral), and another that measures spatial and temporal coherence of precipitation (ASoP Coherence). It can operate on a variety of temporal and spatial scales for both climate models and observations. <a href="https://gmd.copernicus.org/articles/10/57/2017/">Link to reference.</a>
<br><br>
<a href="https://github.com/zarzycki/cymep">Cyclone Metrics Package (CyMeP)</a>
<br>CyMeP offers a suite of metrics for analyzing tropical cyclone trajectories on global or regional scales. This package includes a "scorecard" presentation for easy metrics comparisons along with maps of spatial quantities like storm genesis and track bias. <a href="https://doi.org/10.1175/JAMC-D-20-0149.1">Link to reference.</a>
<br><br>
<a href="https://github.com/cmecmetrics/Drought_Metrics">Drought Metrics</a>
<br>The Drought Metrics package includes a complete suite of metrics for characterizing regional drought. It also narrows down a subset of the most important metrics that characterize drought in that area. <a href="https://doi.org/10.1175/JHM-D-20-0314.1">Link to reference.</a>
<br><br>
<a href="https://github.com/LBL-EESA/TECA">The Toolkit for Extremes Climate Analysis (TECA)</a>
<br>TECA specializes in extreme event detection for phenomena such as tropical cyclones, extra-tropical cyclones, and atmospheric rivers. <a href="https://doi.org/10.1016/j.procs.2012.04.093">Link to reference.</a>

