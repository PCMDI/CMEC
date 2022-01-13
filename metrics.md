---
layout: default
title: Metrics
---
 
## Metrics Table
 
This table describes the metrics available in CMEC packages
 
<table>
  <tr>
    <th>Package</th>
    <th>Metrics</th>
    <th>Source</th>
    <th>Documentation</th>
  </tr>
  <tr>
    <td>Analyzing Scales of Precipitation (ASoP)</td>
    <td><b>Coherence</b>: Temporal intermittency metrics, spatial intermittency metrics, plots of correlations of precipitation in space and time over regional blocks.
    <br><b>Spectral</b>: Histogram overlap metric, plots of 1d histograms of precipitation, maps of actual and fractional contribution to precipitation rate by intensity range</td>
    <td><a href="https://github.com/nick-klingaman/ASoP">Github repository</a></td>
    <td><a href="https://github.com/nick-klingaman/ASoP/blob/master/ASoP_guide.pdf">User Guide</a></td>
  </tr>
  <tr>
    <td>Cyclone Metrics Package (CyMeP)</td>
    <td><b>Storm characteristics</b>: tropical cyclone days, storm genesis, storm intensity (minimum sea level pressure, maximum 10-meter wind speed, accumulated cyclone energy,  pressure accumulated cyclone energy), latitude of lifetime-maximum intensity
    <br><b>Statistics</b>: mean, bias, Pearson product-moment coefficient of linear correlation, Spearman rank correlation, hit rate, false alarm ratio
    <br><b>Figures</b>: Scorecards, Spatial density maps, taylor diagrams, interannual cycle line plots, seasonal cycle line plots</td>
    <td><a href="https://github.com/zarzycki/cymep">Github repository</a></td>
    <td><a href="https://github.com/zarzycki/cymep#cymep-cyclone-metrics-package">CyMeP README</a></td>
  </tr>
  <tr>
    <td>Drought Metrics</td>
    <td>Mean precipitation, mean SPI6, Mean SPI36, Seasonality of  Precipitation, Long term monthly mean, Fractional area coverage of drought, Proportion of dry months, Count of dry months, Drought intensity, Probability of drought initiation, probability of drought termination, overall score</td>
    <td><a href="https://github.com/cmecmetrics/Drought_Metrics">Github repository</a></td>
    <td><a href="https://github.com/cmecmetrics/Drought_Metrics#drought_metrics">Drought Metrics README</a></td>
  </tr>
  <tr>
    <td>International Land Model Benchmarking (ILAMB)</td>
    <td><b>Diagnostics figures</b>: contour maps, time series plots, Taylor Diagrams
    <br><b>Metrics</b>: An overall score that accounts for spatial and temporal statistics of a model compared with observations for different quantities.
    <br>Metrics categories include Ecosystem and Carbon Cycle, Hydrology Cycle, Radiation and Energy Cycle, Forcings, and Relationships (Gross Primary Productivity, Leaf area index, and Evapotranspiration).</td>
    <td><a href="https://github.com/rubisco-sfa/ILAMB">Github repository</a></td>
    <td><a href="https://www.ilamb.org/doc/">Documentation website</a></td>
  </tr>
  <tr>
    <td>International Ocean Model Benchmarking (IOMB)</td>
    <td><b>Diagnostics figures</b>: contour maps, time series plots, Taylor Diagrams
    <br><b>Metrics</b>: An overall score that accounts for spatial and temporal statistics of a model compared with observations for different quantities.
    <br>Metrics categories include Ecosystems, Nutrients, Carbon, Physical Drivers, and Relationships.</td>
    <td><a href="https://github.com/rubisco-sfa/ILAMB">Github repository</a> (shared with ILAMB)</td>
    <td><a href="https://www.ilamb.org/doc/">Documentation website</a> (shared with ILAMB)</td>
  </tr>
  <tr>
    <td>Model Diagnostics Task Force (MDTF) Diagnostics</td>
    <td><b>Process Oriented Diagnostics (PODs)</b>: ENSO_MSE, ENSO_RWS, Extratropical Variance, Madden-Julian Oscillation Propogation and Amplitude, Madden-Julian Oscillation Spectra and Phasing, Madden-Julian Oscillation Teleconnections, Coupling between Soil Moisture and Evapotranspiration, Wavenumber-Frequency Spectra, Convective Transition Diagnostics, Mixed Layer Depth, Ocean Sufrace Latent Heat Flux Diagnostic, Diurnal Cycle of Precipitation, Surface Temperature Extremes and Distribution Shape, Tropical Pacific Sea Level Diagnostic</td>
    <td><a href="https://github.com/NOAA-GFDL/MDTF-diagnostics">Github repository</a></td>
    <td><a href="https://mdtf-diagnostics.readthedocs.io/en/latest/">Documentation website</a></td>
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