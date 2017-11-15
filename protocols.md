---
layout: default
title: Protocols
---

# Protocols

Conventions for input data
------

The CMEC capabilities can work with a variety of data, but established data conventions provide a design target for the software developers to maximize potential and flexibility. <a href="https://pcmdi.llnl.gov/CMIP6/Guide/modelers.html#5-model-output-requirements"> The CMIP data conventions </a> rely on <a href="http://cfconventions.org/"> the Climate-Forecast or CF conventions </a> as a basis for defining metadata and data structures, and thus CMEC capabilities are well equipped to handle CMIP model output. Data conventions for observational data are now being used to provide the CMIP community with observations that are closely aligned with the CMIP6 data conventions via the <a href="https://www.earthsystemcog.org/projects/obs4mips"> obs4MIPs project</a>. The emphasis of obs4MIPs to date has been on gridded data products, however there are plans  to eventually expand the project to include in-situ and other classes of data. Obs4MIPs is having an important impact with many data providers committing to contribute to an expanding archive, however, to date there are many useful products that do not yet adhere to the CMIP6/obs4MIPs data conventions. As a result, the handling of diverse observational datasets is a challenge for the CMEC and other model evaluation capabilities. The CMIP6/obs4MIPs data conventions provide a foundation to build upon to ensure that systematic model evaluation with observations can be as efficient as possible.

Conventions for interoperability
------

Model evaluation capabilities are designed for a variety of purposes and rely on an assortment of analysis tools. As these packages were independently developed, the instructions for use can vary substantially from one package to another. There are however distinct advantages to having some level of coordination between the various packages so that they can, if desired, be operated in a common framework. For example, a modeling group may want to use several CMEC capabilities in their development/analysis workflow, and having some commonality in how they function can greatly facilitate integration. Much as the grass roots development of the CF conventions formed a basis for the CMIP data standards, efforts are underway to establish a set of common syntax that can be used for operating each CMEC capability at a high level without disrupting how they may function independently.


Common strategies for software documentation and accessibility
------

All CMEC capabilities are open source.  They are maintained on and are freely available from online repositories such as GitHub and Bitbucket.   Currently, there is little commonality in how such codes are documented.   As a first step, some coordination across capabilities can be encouraged by establishing a set of “best practices”, which will be developed and maintained by the teams participating in CMEC.   Recent technological advancements facilitate the sharing of software packages and environments across different platforms (e.g., via Anaconda and PIP) and are expected to be a key component of the coordinated CMEC effort. 

A more ambitious goal of CMEC is to advance the model evaluation science towards ensuring reproducibility.   This considerably complicates the demands placed on software developers, but it will be essential as the diversity and scope of the repeat-use capabilities expands.   While some packages already are keeping track of code development changes (via version control, regression testing, etc.), complete provenance will require all workflow components to be documented, with not just version control of all analysis codes but also versioning of all model and observational datasets.   It will likely take the analysis community many years to advance this (much as it did the CF conventions), but if successful, it will be a fundamental and revolutionary advancement to model evaluation.
