---
layout: default
title: CMEC
---

## Coordinated Model Evaluation Capabilities

<div class="row">
    <p class="col-sm-12 col-md-12 col-lg-5">
    Coordinated Model Evaluation Capabilities (CMEC) is an effort to bring together a diverse set of analysis
    packages that have been developed to facilitate the systematic evaluation of Earth System Models (ESMs).
    Currently, CMEC includes three capabilities that are supported by 
    <a href="https://www.energy.gov/">the U.S. Department of Energy</a>, 
    <a href="https://www.energy.gov/science/ber">Office of Biological and Environmental Research (BER)</a>, 
    <a href="https://climatemodeling.science.energy.gov/program/regional-global-model-analysis">Regional 
    and Global Climate Modeling Program (RGCM)</a>. As
    CMEC advances, additional analysis packages will be included from community-based expert teams as well
    a efforts directly supported by DOE and other US and international agencies.
    </p>
    <div id="infographic-container" class="col-sm-12 col-md-12 col-lg-7">
    <img src="{{site.baseurl}}/assets/images/171120_CMECInfoGraphic_500x503px_72dpi.png">
    <div id="infographic-pmp"
        class="infographic-clickable text-center"
        role="button"
        data-toggle="popover"
        data-trigger="hover"
        data-target="#pmp-popover-content"
        title="PCMDI Metrics Package">Physical<br>Model<br>Summaries<br>(PMP)
    </div>
    <div id="infographic-teca"
        class="infographic-clickable text-center"
        role="button"
        data-toggle="popover"
        data-trigger="hover"
        data-target="#teca-popover-content"
        title="The Toolkit for Extremes Climate Analysis">Weather<br>Extremes<br>(TECA)
    </div>
    <div id="infographic-ilamb"
        class="infographic-clickable text-center"
        role="button"
        data-toggle="popover"
        data-trigger="hover"
        data-target="#ilamb-popover-content"
        title="The International Land Model Benchmarking Package">Land<br>Biogeochemistry<br>(ILAMB)
    </div>
    <div id="infographic-iomb"
        class="infographic-clickable text-center"
        role="button"
        data-toggle="popover"
        data-trigger="hover"
        data-target="#iomb-popover-content"
        title="The International Ocean Model Benchmarking Package">Ocean<br>Biogeochemistry<br>(IOMB)
    </div>
    </div>
</div>

A primary motivation for CMEC is to analyze model simulations that are contributed to the
<a href="https://www.wcrp-climate.org/wgcm-cmip">Coupled Model Intercomparison Project (CMIP)</a>. Virtually every institution worldwide involved in significant development of ESMs contributes simulations to CMIP.
<a href="https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6">The 6th and latest phase</a> (<a href="https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6">CMIP6</a>;
<a href="https://dx.doi.org/10.1002/2014EO090001">Meehl et al., 2014</a>;
<a href="https://dx.doi.org/10.5194/gmd-9-1937-2016">Eyring et al., 2016</a>) includes a partial but fundamental
shift away from distinct CMIP phases with the advent of an ongoing core of benchmarking experiments known as the
CMIP DECK (Diagnosis, Evaluation, Characterization of Klima – Klima being the German word for climate). The DECK
includes a short list of experimental configurations that are routinely performed by ESM developers during their
model development process. The DECK and “Historical” simulations provide a basis from which ESMs can be compared
with available observations.

To date, many ad hoc analysis packages have been developed to target selected aspects of ESM simulations. With
the growing scope of CMIP and expectations for efficient “quick look” results, there is a clear need for the
community of CMIP analysts to work together. CMEC is establishing a framework for the developers of these
capabilities to collaborate and to deliver a unified set of results.

<div class="popover-content">
    <div id="pmp-popover-content">
        <a href="{{site.baseurl}}/pmp.html">The PCMDI Metrics Package (PMP)</a>
        <p>
        PMP provides diagnostic summaries of physical atmospheric model variables on seasonal, annual, and
        inter-annual time scales. It compares these variables with global satellite remote sensing and
        reanalysis data sets, and scores model performance based on RMSE or other metrics. PMP is useful
        for producing quick, high-level diagnostic summaries of physical atmosphere model performance.
        </p>
        <img src="{{site.baseurl}}/assets/images/pmp_cover_side_sm.png" class="full-width">
        <p>
        <span class="bold">Quick links</span>: <a href="https://github.com/PCMDI/pcmdi_metrics"
        target="_blank">Repository</a>, <a href="https://github.com/PCMDI/pcmdi_metrics/wiki/Install"
        target="_blank">Installation</a>, and <a href="results/physical.html" target="_blank">Results</a>
        </p>
    </div>
    <div id="teca-popover-content">
        <a href="{{site.baseurl}}/teca.html">The Toolkit for Extremes Climate Analysis (TECA)</a>
        <p>
	TECA is a high-performance, general purpose tool for detecting discrete
	weather events, such as tropical cyclones, in climate model output.  Its core
	is a map-reduce framework, implemented in C++, that utilizes MPI and OpenMP
	parallelism.  It features Python bindings for the core architecture, which
	allows rapid prototyping new detectors while taking advantage of the
	high-performance parallelism of the C++ core.
        </p>
        <img src="{{site.baseurl}}/assets/images/teca_cam5_globe_400x400.png" class="full-width">
        <p>
        <span class="bold">Quick links</span>:
        <a href="https://github.com/LBL-EESA/TECA" target="_blank">Repository</a>,
        <a href="https://github.com/LBL-EESA/TECA_superbuild" target="_blank">Installation</a>, and
        <a href="https://github.com/LBL-EESA/TECA/blob/master/doc/teca_users_guide.pdf"
        target="_blank">documentation</a>
        </p>
    </div>
    <div id="ilamb-popover-content">
        <a href="{{site.baseurl}}/ilamb.html">The International Land Model Benchmarking (ILAMB) Package</a>
        <p>
        ILAMB provides a variety of in-depth diagnostics of more than 24 terrestrial biogeochemical
        and hydrological model variables on annual and inter-annual time scales. It compares these
        variables with over 60 site-based, regional, and global observational data sets, and scores
        model performance based on a combination bias, RMSE, and seasonal cycle metrics. Relationships
        between many biogeochemical variables and physical driver variables are calculated from model
        results and compared with observational estimates. ILAMB is useful for detailed exploration of
        land biogeochemical and hydrological model responses and provides an interactive interface
        designed to enable the user to more rapidly understand the underlying drivers of those responses.
        </p>
        <img src="{{site.baseurl}}/assets/images/ilamb_biomass_sm.png" class="full-width">
        <p>
        <span class="bold">Quick links</span>: <a href="https://bitbucket.org/ncollier/ilamb"
        target="_blank">Repository</a> and <a href="https://www.ilamb.org/doc/install.html"
        target="_blank">Installation</a>
        </p>
    </div>
    <div id="iomb-popover-content">
        <a href="{{site.baseurl}}/iomb.html">The International Ocean Model Benchmarking (IOMB) Package</a>
        <p>
        IOMB provides a variety of in-depth diagnostics of marine biogeochmical model variables on
        annual and inter-annual time scales. It compares a growing number of variables with site-based,
        transect, regional, and global observational data sets, and scores model performance based on
        a combination of bias, RMSE, and seasonal cycle metrics. IOMB is useful for detailed exploration
        of ocean biogeochemical model responses and provides an interactive interface designed to enable
        the user to more rapidly understand the underlying drivers of those responses.
        </p>
        <img src="{{site.baseurl}}/assets/images/iomb_temperature_sm.png" class="full-width">
        <p>
        <span class="bold">Quick links</span>: <a href="https://bitbucket.org/ncollier/ilamb"
        target="_blank">Repository</a> and <a href="https://www.ilamb.org/doc/install.html"
        target="_blank">Installation</a>
        </p>
    </div>
</div>

<script>
    $(document).ready(function(){
        $('[data-toggle="popover"]').each(function(){
            var self = $(this);
            self.popover({
                html: true,
                container: self,
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
        })
    });
</script>
