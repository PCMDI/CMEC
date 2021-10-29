---
layout: default
title: CMEC
---

## Coordinated Model Evaluation Capabilities

<div class="row">
    <p class="col-sm-12 col-md-12 col-lg-5">
    Coordinated Model Evaluation Capabilities (CMEC) is an effort to bring together a diverse set of analysis
    packages that have been developed to facilitate the systematic evaluation of Earth System Models (ESMs).
    CMEC includes capabilities that are supported by 
    <a href="https://www.energy.gov/">the U.S. Department of Energy</a>, 
    <a href="https://www.energy.gov/science/ber">Office of Biological and Environmental Research (BER)</a>, and 
    <a href="https://climatemodeling.science.energy.gov/program/regional-global-model-analysis">Regional 
    and Global Model Analysis (RGMA)</a>, along with capabilities contributed
    by community-based experts and international agencies.
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

CMEC is motivated by the need for comprehensive and holistic evaluation of Earth system models and datasets, so as to identify persistent biases and improve data credibility. With widespread and rapid growth in the number of available metrics and diagnostic tools, a lack of standards within the evaluation community have meant that running even a single evaluation tool can require extensive user intervention. Given the significant commonality in how these evaluation tools operate, interoperability is a natural goal achievable through robust and light-weight standards.

The three goals of the CMEC project include: (1) to develop robust and light-weight standards for operation of evaluation packages and their output; (2) to develop accompanying tools for installation of evaluation packages, coordinated execution of evaluation packages, and obtaining data products necessary for operation of these tools; and (3) to build connections across groups, centers, and individual investigators performing model evaluation.

CMEC aims to operate on a variety of Earth system data products including but not limited to: Earth system model data such as contributions to the Coupled Model Intercomparison Project (CMIP), reanalysis data products, and other data products produced by global modeling centers or individual research groups. 

To advance this effort, participation is sought from new and existing ESM evaluation packages. 
Inclusion is not limited to packages for CMIP analysis, and both metrics
and diagnostics packages are welcome.

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
        target="_blank">Documentation</a>
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
