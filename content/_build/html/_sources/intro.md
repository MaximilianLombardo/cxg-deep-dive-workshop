# CELLxGENE Suite Deep Dive

**By [the CELLxGENE Team](https://cellxgene.cziscience.com/) 🔬**

Welcome to the CELLxGENE Deep Dive Course! This course will take 3 - 4 hours to complete and will demonstrate how to use the entirety of the CELLxGENE suite to aid in your research and single cell analysis journey. You can expect to learn about the following tools from the CELLxGENE suite:

- [Data Portal](https://cellxgene.cziscience.com/collections) and [Schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/3.0.0/schema.md)
    - An overview of how to use the portal discover datasets + the schema that defines the metadata that can be found in the corpus.
- [Gene Expression](https://cellxgene.cziscience.com/gene-expression)
    - Discover where your genes of interest are expressed across the entire CELLxGENE data corpus. Learn about marker genes in cell types and tissues of interest and discover the relationships between cell types.
- [Explorer](https://cellxgene.cziscience.com/e/53d208b0-2cfd-4366-9866-c3c6114081bc.cxg/) and [Annotate](https://github.com/chanzuckerberg/cellxgene)
    - Participants will learn about the CELLxGENE data explorer. We will cover the hosted version, which allows the visualization and dataset filtering based on gene expression and other relevant metadata in individual datasets. We will also cover the local version of the CELLxGENE Explorer application, where users can create custom annotations on a dataset or use models trained on the CELLxGENE corpus to automatically annotate their datasets (prototype).

:::{note} 
If you encounter any issues, contact us at [cellxgene@chanzuckerberg.com](cellxgene@chanzuckerberg.com) or file an issue on [the CELLxGENE annotate github](https://github.com/chanzuckerberg/cellxgene/issues).
:::
 
## Overview
This course is split into 3 sections consisting of both video and text. In the **[preface](preface/landing.md)**, you’ll learn about how this course came to be and find a list of resources for foundational image analysis concepts that will help you get the most out of these materials. In the **[onboarding section](onboard/landing.md)**, you’ll learn more about what napari is, and be guided through installing napari and plugins on your computer. Finally in the **[workflows section](workflow/landing.md)**, you'll dig into three cell segmentation case studies (nuclei, foci in nuclei, and filaments) that illustrate how to perform a cell segmentation workflow from start to finish within napari, using sample data (or your own), and various napari plugins.

<br>
 
 ::::{grid} 2
:::{grid-item-card}  **Notable lessons**
- [All about virtual environments, Python and napari](https://chanzuckerberg.github.io/napari-segmentation-workshop/onboard/whatisnapari.html) 🐍
  
- [Installing the latest version of napari with minimal coding](https://chanzuckerberg.github.io/napari-segmentation-workshop/onboard/gettingstarted.html#video-walkthrough) 💽  

- [Nuclei segmentation with *Cellpose*](workflow/cellpose.md) ⚙️

- [Foci segmentation with *PartSeg*](workflow/partseg.md) ⚙️
  
- [Filament segmentation with *Allen Cell Segmenter*](workflow/allencell.md) ⚙️
:::
:::{grid-item-card}  **Supporting links**
- [Napari.org](https://napari.org) community and developer site

- The [napari hub](https://napari-hub.org) for the latest plugins

- Official Bravo Cohort plugin collection page   

- Image.sc forum sticky thread on the napari segmentation course  
::::
