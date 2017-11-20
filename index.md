---
layout: default
title: CMEC
---

## CMEC

<div class="row">
    <p class="col-sm-12 col-lg-5">
    Coordinated Model Evaluation Capabilities (CMEC) is an effort to bring together a diverse set of analysis
    packages that have been developed to facilitate the systematic evaluation of Earth System Models (ESMs).
    Currently, CMEC includes three capabilities that are supported by the U.S. Department of Energy, Office
    of Biological and Environmental Research (BER), Regional and Global Climate Modeling Program (RGCM). As
    CMEC advances, additional analysis packages will be included from community-based expert teams as well
    a efforts directly supported by DOE and other US and international agencies.
    </p>
    <div id="infographic-container" class="col-sm-12 col-lg-7">
    <img src="{{site.baseurl}}/assets/images/infographic.png">
    <div id="infographic-pmp"
        class="infographic-clickable text-center"
        role="button"
        data-toggle="popover"
        data-target="#pmp-popover-content"
        title="PCMDI Metrics Package">Physical<br>Model<br>Summaries<br>(PMP)</div>
    <a id="infographic-teca" class="infographic-clickable text-center">Weather<br>Extremes<br>(TECA)</a>
    <a id="infographic-ilamb" class="infographic-clickable text-center">Land<br>Biogeochemistry<br>(ILAMB)</a>
    <a id="infographic-iomb" class="infographic-clickable text-center">Ocean<br>Biogeochemistry<br>(IOMB)</a>
    </div>
</div>

A primary motivation for CMEC is to analyze model simulations that are contributed to the
<a href="https://www.wcrp-climate.org/wgcm-cmip">Coupled Model Intercomparison Project (CMIP)</a>. Virtually all
the institutions worldwide involved in significant development of ESMs contribute simulations to CMIP.
<a href="https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6">The 6th and latest phase</a> (CMIP6;
<a href="https://dx.doi.org/10.1002/2014EO090001">Meehl et al., 2014</a>;
<a href="https://dx.doi.org/10.5194/gmd-9-1937-2016">Eyring et al., 2016</a>) includes a partial but fundamental
shift away from distinct CMIP phases with the advent of an ongoing core of benchmarking experiments known as the
CMIP DECK (Diagnosis, Evaluation, Characterization of Klima – Klima being the German word for climate). The DECK
includes a short list of experimental configurations that are routinely performed by ESM developers during their
model development process. The DECK and “Historical” simulations provide a basis from which ESMs can be compared
with available observations.

To date, many ad hoc analysis packages have been developed to target selected aspects of ESM simulations. With
the growing scope of CMIP and expectations for efficient “quick look” results, there is a clear need for the
community of CMIP analysts to work together. CMEC is establishing a framework for the developers of these capabilities
to collaborate and to deliver a unified set of results.

<div class="popover-content">
    <div id="pmp-popover-content">
        <a href="#">The PCMDI Metrics Package (PMP)</a>
        <p>
        PMP provides diagnostic summaries of physical atmospheric model variables on seasonal, annual, and
        inter-annual time scales. It compares these variables with global satellite remote sensing and
        reanalysis data sets, and scores model performance based on RMSE or other metrics. PMP is useful
        for producing quick, high-level diagnostic summaries of physical atmosphere model performance.
        </p>
        <img src="{{site.baseurl}}/assets/images/pmp_cover_side_sm.png" class="full-width">
        <p>
        <span class="bold">Quick links</span>: <a href="https://github.com/PCMDI/pcmdi_metrics">Repository</a>
        and <a href="https://github.com/PCMDI/pcmdi_metrics/wiki/Install">Installation</a>
        </p>
    </div>
</div>

<script>
    $(document).ready(function(){
        $('[data-toggle="popover"]').popover({
            html: true,
            placement: function(context, source){
                if(window.innerWidth >= 635){
                    return "right";
                }
                else{
                    return "bottom";
                }
            },
            content: function(){
                var targetId = $(this).attr('data-target');
                return $(targetId).html();
            }
        })
    });
</script>