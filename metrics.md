---
layout: default
title: Metrics
---
 
## Model Evaluation Packages
 
This table describes the metrics and diagnostics available in CMEC packages
 
<table>
  <tr>
    <th>Package</th>
    <th>Contents</th>
    <th>Source</th>
    <th>Documentation</th>
  </tr>
  <tr>
    <td>Analyzing Scales of Precipitation (ASoP)</td>
    <td><b>Coherence</b>: Temporal intermittency metrics, spatial intermittency metrics, plots of correlations of precipitation in space and time over regional blocks.
    <br><b>Spectral</b>: Histogram overlap metric, file (for each dataset) containing 100-bin distribution of counts over the time period for each gridpoint, plots of 1d histograms of precipitation, maps of actual and fractional contribution to precipitation rate by intensity range</td>
    <td><a href="https://github.com/nick-klingaman/ASoP">Github repository</a></td>
    <td><a href="https://github.com/nick-klingaman/ASoP/blob/master/ASoP_guide.pdf">User Guide</a></td>
  </tr>
  <tr>
    <td>Cyclone Metrics Package (CyMeP)</td>
    <td><b>Statistics</b>: mean, bias, Pearson correlation, Spearman correlation, hit rate, false alarm ratio
    <br>Statistics measure the following storm characteristics: tropical cyclone days, storm genesis, storm intensity (minimum sea level pressure, maximum 10-meter wind speed, accumulated cyclone energy,  pressure accumulated cyclone energy), latitude of lifetime-maximum intensity
    <br><b>Figures</b>: Scorecards, cyclone trajectories, spatial density maps, Taylor diagrams, interannual cycle line plots, seasonal cycle line plots</td>
    <td><a href="https://github.com/zarzycki/cymep">Github repository</a></td>
    <td><a href="https://github.com/zarzycki/cymep#cymep-cyclone-metrics-package">CyMeP README</a></td>
  </tr>
  <tr>
    <td>Drought Metrics</td>
    <td><b>Metrics</b>: Mean precipitation, mean SPI6, mean SPI36, seasonality of  precipitation, long term monthly mean, fractional area coverage of drought, proportion of dry months, count of dry months, drought intensity, probability of drought initiation, probability of drought termination, total score
    <br><b>Figures</b>: Taylor diagram, heatmap of total scores</td>
    <td><a href="https://github.com/cmecmetrics/Drought_Metrics">Github repository</a></td>
    <td><a href="https://github.com/cmecmetrics/Drought_Metrics#drought_metrics">Drought Metrics README</a></td>
  </tr>
  <tr>
    <td>International Land Model Benchmarking (ILAMB)</td>
    <td><b>Metrics</b>: A set of scores for spatial and temporal statistics of a model compared with observations for different quantities. Scores include overall score, bias score, RMSE score, and others.
    <br>Metrics categories include Ecosystem and Carbon Cycle, Hydrology Cycle, Radiation and Energy Cycle, Forcings, and Relationships (Gross Primary Productivity, Leaf area index, and Evapotranspiration).
    <br><b>Figures</b>: contour maps, time series plots, Taylor diagrams</td>
    <td><a href="https://github.com/rubisco-sfa/ILAMB">Github repository</a></td>
    <td><a href="https://www.ilamb.org/doc/">Documentation website</a></td>
  </tr>
  <tr>
    <td>International Ocean Model Benchmarking (IOMB)</td>
    <td><b>Metrics</b>: A set of scores that account for spatial and temporal statistics of a model compared with observations for different quantities. Scores include overall score, bias score, RMSE score, and others.
    <br>Metrics categories include Ecosystems, Nutrients, Carbon, Physical Drivers, and Relationships.
    <br><b>Figures</b>: contour maps, time series plots, Taylor diagrams</td>
    <td><a href="https://github.com/rubisco-sfa/ILAMB">Github repository</a> (shared with ILAMB)</td>
    <td><a href="https://www.ilamb.org/doc/">Documentation website</a> (shared with ILAMB)</td>
  </tr>
  <tr>
    <td>Model Diagnostics Task Force (MDTF) Diagnostics</td>
    <td><b>Process Oriented Diagnostics (PODs)</b>: ENSO_MSE, ENSO_RWS, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/EOF_500hPa.html">Extratropical Variance</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/MJO_prop_amp.html">Madden-Julian Oscillation Propogation and Amplitude</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/MJO_suite.html">Madden-Julian Oscillation Spectra and Phasing</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/MJO_teleconnection.html">Madden-Julian Oscillation Teleconnections</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/SM_ET_coupling.html">Coupling between Soil Moisture and Evapotranspiration</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/Wheeler_Kiladis.html">Wavenumber-Frequency Spectra</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/convective_transition_diag.html">Convective Transition Diagnostics</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/mixed_layer_depth.html">Mixed Layer Depth</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/ocn_surf_flux_diag.html">Ocean Sufrace Latent Heat Flux Diagnostic</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/precip_diurnal_cycle.html">Diurnal Cycle of Precipitation</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/temp_extremes_distshape.html">Surface Temperature Extremes and Distribution Shape</a>, <a href="https://mdtf-diagnostics.readthedocs.io/en/latest/sphinx_pods/tropical_pacific_sea_level.html">Tropical Pacific Sea Level Diagnostic</a></td>
    <td><a href="https://github.com/NOAA-GFDL/MDTF-diagnostics">Github repository</a></td>
    <td><a href="https://mdtf-diagnostics.readthedocs.io/en/latest/">Documentation website</a><br><a href="https://www.gfdl.noaa.gov/mdtf-diagnostics/">Project Website</a></td>
  </tr>
  <tr>
    <td>PCMDI Metrics Package (PMP)</td>
    <td><b>Mean Climate</b>: Statistics that characterize atmospheric variables and compare models with observations, including bias, mean, correlation, root mean square error, and standard deviation.
    <br><b>Monsoon (Wang)</b>: Correlation, rmsn, threat score for defined regions (North America, South America, North Africa, South Africa, Asia, Australia, and "all" monsoon domains).
    <br><b>Monsoon (Sperber)</b>: Decay index, duration, onset index, slope for defined regions (All-India, Northern Australia, Sahel, Gulf of Guinea, North America, South America).
    <br><b>Diurnal Cycle</b>: Daily mean precipitation, standard deviation of mean diurnal cycle, standard deviation of hourly means, standard deviation of daily means, Fourier harmonics (amplitude and phase) 
    <br><b>Modes of Variability</b>: Statistics for the Northern Annular Mode, Northern Atlantic Oscillation, Sourthern Annular Mode, Pacific North American Pattern, Pacific Decadal Oscillation. 
    <br><b>Madden-Julian Oscillation metrics</b>: East power, West power, East-west power ratio
    <br><b>El Niño–Southern Oscillation (ENSO) performance</b>: Cold tongue bias, trade wind bias, dry equator bias, double intertropical convergence zone bias, seasonalities of biases, ENSO amplitude, ENSO life cycle, ENSO asymmetry, ENSO diversity
    <br><b>El Niño–Southern Oscillation teleconnections</b>: ENSO amplitude, ENSO pattern, ENSO seasonality, DJF precipitation teleconnection, DJF surface temperature teleconnection, JJA precipitation teleconnection, JJA surface temperature teleconnection
    <br><b>El Niño–Southern Oscillation processes</b>: Cold tongue bias, trade winds bias, ENSO pattern, ENSO amplitude, ENSO seasonality, ENSO asymmetry, ocean-atmosphere Bjerknes feedback (atmosphere branch, ocean-atmosphere branch, and ocean branch), balance of Bjerknes feedback and heat fluxes on sea surface temperature anomalies
    <br><b>Precipitation variability</b>: Forced annual, forced semi-annual, unforced interannual, unforced seasonal-annual, unforced sub-seasonal, unforced synoptic</td>
    <td><a href="https://github.com/PCMDI/pcmdi_metrics">Github repository</a></td>
    <td><a href="https://pcmdi.github.io/pcmdi_metrics/">Documentation website</a></td>
</tr>
</table> 
