---
layout: default
title: ILAMB
---

## The International Land Model Benchmarking (ILAMB) Package

The International Land Model Benchmarking (ILAMB) Package was designed
to address the goals of the ILAMB Project, a model--data intercomparison
and integration activity.  The ILAMB project was initiated to improve
the performance of land models and, in parallel, improve the design of
new measurement campaigns to reduce uncertainties associated with key
land surface processes. Building upon past model evaluation studies,
described below, the goals of ILAMB are to:

<ul>
<li> develop internationally accepted benchmarks for land model performance, </li>
<li> promote the use of these benchmarks by the international community for model intercomparison, </li>
<li> strengthen linkages between experimental, remote sensing, and climate modeling communities in the design of new model tests and new measurement programs, and </li>
<li> support the design and development of a new, open source, benchmarking software system for use by the international community. </li>
</ul>

Improving the representation of the carbon cycle and land surface
processes in climate models requires extensive comparison of model results
with observations. This process is difficult and time intensive. Past
data-model intercomparisons have strengthened the representation
of key processes in land models, but often this information has not
been easily accessible for use by other modeling teams or in future
intercomparisons. Specifically, there is a large cost in developing
the infrastructure to make meaningful model--data comparisons, even when
the data are freely and easily available. Further, the development of
sophisticated model diagnostics programs---that can fully exploit
the richness of large Earth System data sets like satellite or
Fluxnet measurements---are outside the scope of any single modeling
center. Thus, an important direction for the field is the development
of a community-based model evaluation system that is open source and
modular, allowing for contributions by many different modeling and
measurement teams.

Multiple past intercomparison efforts provide a foundation a new
international benchmarking activity. The original C4MIP effort provided
the community with an elegant conceptual framework for diagnosing the
causes of model-to-model differences in feedback strength ([Friedlingstein
et al., 2006](https://doi.org/10.1175/JCLI3800.1); [Gregory et al., 2009](https://doi.org/10.1175/2009JCLI2949.1)). The Carbon-Land Model Intercomparison
Project (C-LAMP) also was a first step in this direction ([Hoffman et al.,
2008](https://www.climatemodeling.org/~forrest/pubs/papers/Hoffman_iEMSs-C-LAMP_20080707.pdf); [Randerson et al., 2009](https://doi.org/10.1111/j.1365-2486.2009.01912.x). Nine different classes of observations
were used to evaluate two biogeochemistry models (CASA&prime; and CN)
within the Community Climate System Model. For each class of observations,
the models received a score based on the quality of the fit with the
measurements. Information from different data streams were weighted by the
relative importance of the observational constraint, the uncertainty in
the observations, and the uncertainty in the model.

The [2016 ILAMB Workshop](https://www.ilamb.org/meetings/washington2016/
"2016 ILAMB Workshop") was convened in May 2016 in Washington,
District of Columbia, USA, to engage the international research
community in defining scientific priorities for (1) design of
new metrics, (2) improvement of  model development and workflow
practices, (3) Coupled Model Intercomparison Project (CMIP)
evaluation, and to learn about new observational data sets and
measurement campaigns.  The workshop drew more than 60 on-site
participants, and between 20 and 30 individuals---including
students and postdocs---attended online at any time during the
plenary sessions. Participants were from Australia, Canada, China,
Germany, Japan, Netherlands, Sweden, United Kingdom, and the United
States and represented 10 different major modeling centers. Plenary
presentations focused on model benchmarking, emergent constraints,
evaluation metrics, uncertainty quantification, and field experiment
and measurement networks. The 2016 ILAMB Workshop Report ([Hoffman et al., 2017](https://doi.org/10.2172/1330803)) is available
[here](https://www.ilamb.org/meetings/washington2016/2016_ILAMB_Report_V10_web.pdf
"2016 ILAMB Workshop Report").

<a border="0" align="right" target="_blank" href="https://www.ilamb.org/meetings/washington2016/2016_ILAMB_Report_V10_web.pdf"><img width="193" height="250" src="https://www.ilamb.org/meetings/washington2016/2016_ILAMB_Report_cover_small.jpg"></a>

The ILAMB Package provides a variety of in-depth diagnostics of more
than 24 terrestrial biogeochemical and hydrological model variables on
annual and inter-annual time scales. It compares these variables with
over 60 site-based, regional, and global observational data sets, and
scores model performance based on a combination bias, RMSE, and seasonal
cycle metrics. Relationships between many biogeochemical variables and
physical driver variables are calculated from model results and compared
with observational estimates. ILAMB is useful for detailed exploration
of land biogeochemical and hydrological model responses and provides
an interactive interface designed to enable the user to more rapidly
understand the underlying drivers of those responses. The ILAMB version 2 system
design philosophy and implementation are described by
[Collier et al. (2018)](https://doi.org/10.1029/2018MS001354).

<strong>Quick links</strong>:&nbsp;
<a href="https://github.com/rubisco-sfa/ILAMB">Repository</a>,
<a href="https://www.ilamb.org/doc/install.html">Installation</a>,
<a href="https://www.ilamb.org/doc/tutorial.html">Tutorials</a>,
<a href="https://www.ilamb.org/CMIP5/esmHistorical">CMIP5 Results</a>,
and <a href="https://www.ilamb.org/CLM/">CLM Results</a>
<br>
<b>Contact:</b> Forrest M. Hoffman (forrest@climatemodeling.org)
