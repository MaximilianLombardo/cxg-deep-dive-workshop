# CELLxGENE Suite Deep Dive

**By the [CELLxGENE Team](https://cellxgene.cziscience.com/) 🔬**

Welcome to the CELLxGENE Deep Dive Course! The [CELLxGENE team](https://cellxgene.cziscience.com/) at the [Chanzuckerberg Initiative (CZI)](https://chanzuckerberg.com/science/) builds and maintains open source tools that help scientists at all levels of familiarity with single cell analysis Find, Explore, Download, and Analyze single cell data. The material in this course is relevant for scientists from all biological disciplines that currently utilize or wish to utilize single cell transcriptomic data in their research. Much of what is covered in this course also applies to single cell non-transcriptomic data (i.e. spatial, epigenetic, etc....) This course will take 3 - 4 hours to complete and will demonstrate how to use the entirety of the CELLxGENE suite to aid in your research and single cell analysis journey.

:::{note} 
If you encounter any issues, contact us at [cellxgene@chanzuckerberg.com](cellxgene@chanzuckerberg.com) or file an issue on [the CELLxGENE annotate github](https://github.com/chanzuckerberg/cellxgene/issues).
:::
 
## Pre-requisites and Introductory Materials

To follow this course, one should have a basic understanding of what single cell data is. Although many of our tools do not require previous exposure to single cell data to get started, it is often helpful to have a basic understanding of single cell data generation and analysis to be able to perform more advanced data queries or derive more nuanced interpretations of outputs from visual tools. If you don't have any previous exposure to single cell, then we suggest the following introductory resources:

- [The Single Cell Course by the Cellular Genetics Informatics team at the Sanger Institute](https://www.singlecellcourse.org/introduction-to-single-cell-rna-seq.html)
- [Introduction to Single-Cell RNA-seq](https://hbctraining.github.io/scRNA-seq_online/lessons/01_intro_to_scRNA-seq.html)




## Course Overview

Broadly speaking the core of the CELLxGENE platform is a standardized data corpus which is composed of author submitted, publicly available datasets. The CELLxGENE team has built tools to allow users to find and download data form the corpus (Data Portal and Cell Census API) or to visualize corpus data in a hosted or local environment (Gene Expression, Hosted Explorer, Annotate). These tools are organized into CZ CELLxGENE Discover (which is comprised of the data portal, API, and hosted visualization tools) and CZ CELLxGENE Annotate (comprised of the desktop explorer). All of these tools are covered by different modules within this course. Here is a list of the tools just mentioned and the intended use cases for each tool that you will learn about in this course:

- [Data Portal](https://cellxgene.cziscience.com/collections) and [Schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/3.0.0/schema.md)
    - An overview of how to use the portal discover datasets + the schema that defines the metadata that can be found in the corpus.
- [Gene Expression](https://cellxgene.cziscience.com/gene-expression)
    - Discover where your genes of interest are expressed across the entire CELLxGENE data corpus. Learn about marker genes in cell types and tissues of interest and discover the relationships between cell types.
- [Explorer](https://cellxgene.cziscience.com/e/53d208b0-2cfd-4366-9866-c3c6114081bc.cxg/) and [Annotate](https://github.com/chanzuckerberg/cellxgene)
    - Visualize and filter cells based on gene expression and other relevant metadata (i.e. donor, tissue of origin, disease annotation, etc. ...) in individual datasets. In the CELLxGENE Annotate (the local version of the Explorer Application) , users can create custom annotations on a dataset or use models trained on the CELLxGENE corpus to automatically annotate their datasets (prototype).
- [Cell Census API](https://chanzuckerberg.github.io/cellxgene-census/)
    - An overview of CELLxGENE Cell Census and API. Participants will learn about the CELLxGENE data corpus and schema. We will then build upon this background to talk about the CZI Cell Census and accompanying API for programmatic access to the CELLxGENE data corpus.

<br>
 
 ::::{grid} 2
:::{grid-item-card}  **Notable lessons**
- [CELLxGENE data portal](www.google.com) TODO make real link 🐍
  
- [Gene Expression](www.google.com)  TODO make real link 💽  

- [Explorer](www.google.com) TODO make real link ⚙️

- [Cell Census API](www.google.com) TODO make real link ⚙️
  
:::
:::{grid-item-card}  **Quick Links**
- [CZ CELLxGENE](https://cellxgene.cziscience.com/): discover the CELLxGENE suite

::::
