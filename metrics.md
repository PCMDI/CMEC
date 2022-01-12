 --
 layout: default
 title: Metrics
 --
 
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
    <td>Coherence: Temporal intermittency, Spatial intermittency
  Coherence figures: correlations of precipitation in space and time over regional blocks.
Spectral: histogram overlap metric, 1d histograms of precipitation, Maps of actual and fractional contribution to precipitation rate by intensity range, 
</td>
    <td><a href="https://github.com/nick-klingaman/ASoP">ASoP repository</a>a></td>
    <td><a href="https://github.com/nick-klingaman/ASoP/blob/master/ASoP_guide.pdf">User Guide</a></td>
  </tr>
  <tr>
    <td>Cyclone Metrics Package (CyMeP)</td>
    <td> Storm characteristics: tropical cyclone days, storm genesis, storm intensity (minimum sea level pressure, maximum 10-meter wind speed, accumulated cyclone energy,  pressure accumulated cyclone energy), latitude of lifetime-maximum intensity
    <b>Statistics: mean, bias, Pearson product-moment coefficient of linear correlation, Spearman rank correlation, hit rate, false alarm ratio
    <b>Figures: Scorecards, Spatial density maps, taylor diagrams, interannual cycle line plots, seasonal cycle line plots
    </td>
    <td><a href="https://github.com/zarzycki/cymep">CyMeP repository</a></td>
    <td><a href="https://github.com/zarzycki/cymep#cymep-cyclone-metrics-package">CyMeP README</a></td>
  </tr>
  <tr>
    <td>Drought Metrics</td>
    <td>Mean precipitation, mean SPI6, Mean SPI36, Seasonality of  Precipitation, Long term monthly mean, Fractional area coverage of drought, Proportion of dry months, Count of dry months, Drought intensity, Probability of drought initiation, probability of drought termination, overall score</td>
    <td><a href="https://github.com/cmecmetrics/Drought_Metrics">Drought Metrics repository</a></td>
    <td><a href="https://github.com/cmecmetrics/Drought_Metrics#drought_metrics">Drought Metrics README</a></td>
  </tr>
  <tr>
    <td>International Land Model Benchmarking (ILAMB)</td>
    <td>Diagnostics figures: contour maps, time series plots, Taylor Diagrams
    <b>Metrics: An overall score that accounts for spatial and temporal statistics of a model compared with observations for different quantities.
    <b>Metrics categories: Ecosystem and Carbon Cycle, Hydrology Cycle, Radiation and Energy Cycle, Forcings, and Relationships (Gross Primary Productivity, Leaf area index, and Evapotranspiration).
</td>
    <td><a href="https://github.com/rubisco-sfa/ILAMB">ILAMB repository</a></td>
    <td><a href="https://www.ilamb.org/doc/">ILAMB documentation</a></td>
  </tr>
  <tr>
    <td>International Ocean Model Benchmarking (IOMB)</td>
    <td>Diagnostics figures: contour maps, time series plots, Taylor Diagrams
    <b>Metrics: An overall score that accounts for spatial and temporal statistics of a model compared with observations for different quantities.
    <b>Metrics categories: Ecosystems, Nutrients, Carbon, Physical Drivers, and Relationships.
</td>
    <td><a href="https://github.com/rubisco-sfa/ILAMB">IOMB repository</a> (shared with ILAMB)</td>
    <td><a href="https://www.ilamb.org/doc/">IOMB documentation</a> (shared with ILAMB)</td>
  </tr>
  <tr>
    <td>Model Diagnostics Task Force (MDTF) Diagnostics</td>
    <td>PODs: ENSO_MSE, ENSO_RWS, Extratropical Variance, Madden-Julian Oscillation Propogation and Amplitude, Madden-Julian Oscillation Spectra and Phasing, Madden-Julian Oscillation Teleconnections, Coupling between Soil Moisture and Evapotranspiration, Wavenumber-Frequency Spectra, Convective Transition Diagnostics, Mixed Layer Depth, Ocean Sufrace Latent Heat Flux Diagnostic, Diurnal Cycle of Precipitation, Surface Temperature Extremes and Distribution Shape, Tropical Pacific Sea Level Diagnostic</td>
    <td><a href="https://github.com/NOAA-GFDL/MDTF-diagnostics">MDTF Diagnostics repository</a></td>
    <td><a href="https://mdtf-diagnostics.readthedocs.io/en/latest/">MDTF Diagnostics documentation</a></td>
  </tr>
  <tr>
    <td>PCMDI Metrics Package (PMP)</td>
    <td>Mean Climate: bias_xy, cor_xy, mae_xy, mean-obs_xy, mean_xy, rms_devzm, rms_xy, rms_xyt, rms_y, rmsc_xy, std-obs_xy, std-obs_xyt, std_xy, std_xy_devzm, std_xyt
    <b>Monsoon (Wang): correlation, rmsn, threat score
    <b>Monsoon (Sperber): decay index, duration, onset index, slope
    <b>Diurnal Cycle: harmonic 1, 2, and 3: amp_avg_lnd, pha_avg_lnd, amp_avg_ocn, pha_avg_ocn
    <b>Modes of Variability: bias, bias_glo, cor, cor_glo, frac, frac_cbf_regrid, mean, mean_glo, rms, rms_glo, rmsc, rmsc_glo, stdv_pc, std_pc_ratio_to_obs, tcor_cbf_vs_eof_pc
    <b>MJO metrics: east power, west power, East-west power ratio
    <b>ENSO_perf: BiasPrLatRmse, BiasPrLonRmse, BiasSSTLonRmse, BiasTauxLonRmse, EnsoAmpl, EnsoDuration, EnsoSeasonality, EnsoSstDiversity_2, EnsoSSTLonRmse, EnsoSstSkew, EnsoSstTsRmse, SeasonalPrLatRmse, SeasonalPrLonRmse, SeasonalSstLonRmse, SeasonalTauxLonRmse
    <b>ENSO_tel: EnsoAmpl, EnsoPrMapDjfCorr, EnsoPrMapDjfRmse, EnsoPrMapDjfStd, EnsoPrMapJjaCorr, EnsoPrMapJjaRmse, EnsoPrMapJjaStd, EnsoSeasonality, EnsoSstLonRmse, EnsoSstMapDjfCorr, EnsoSstMapDjfRmse, EnsoSstMapDjfStd, EnsoSstMapJjaCorr, EnsoSstMapJjaRmse, EnsoSstMapJjaStd
    <b>ENSO_proc: BiasSstLonRmse, BiasTauxLonRmse, EnsoAmpl, EnsoFbSstTaux, EnsoFbSstThf, EnsoSeasonality, EnsoSstLonRmse, EnsoSstSkew, EnsodSstOce_2
    <b>Precipitation variability: Forced annual, forced semi-annual, unforced interannual, unforced seasonal-annual, unforced sub-seasonal, unforced synoptic
    </td>
    <td><a href="https://github.com/PCMDI/pcmdi_metrics">PCMDI metrics repository</a></td>
    <td><a href="https://pcmdi.github.io/pcmdi_metrics/">PCMDI Metrics documentation</a></td>
  </tr>
</table> 
