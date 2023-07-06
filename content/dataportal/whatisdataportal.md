CELLxGENE Discover Data Portal
=======================
## Learning Objectives

This is a brief introduction to the CELLxGENE Discover Data Portal and corpus. In this lesson, you'll learn about the [CELLxGENE Data Portal](https://cellxgene.cziscience.com/collections), the [schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/3.0.0/schema.md) that every dataset in the portal adheres to, and how to submit your datasets to the CELLxGENE team.

1.  [Data portal Overview](#data-portal-overview)
2.  [Corpus Schema](#corpus-schema)
3.  [Dataset submission](#dataset-submission)

- **Time to learn**: 20 minutes

:::{note}
Please check [documentation](https://cellxgene.cziscience.com/docs/01__CellxGene) for more information.
:::

![Picture of art installation of networked cables](images/napari-viewer.gif)

---

## Data Portal Overview

Napari is a **free**, **open-source**, **community-developed** application with a **graphical user interface**[^mynote1]. It was developed for viewing, annotating, and analysing large and multi-dimensional imaging datasets. This means that napari’s arsenal of tools will continue to develop in tandem with the needs of its users and as new technologies and methodologies become available. These tools are made available as napari **plugins**,[^mynote2] which are installable extensions that add capabilities to napari, like the ability to open a new image type or do segmentation tasks. 

[^mynote1]: A graphical user interface is any interface you can interact with in a separate window, equipped with clickable buttons, built-in tools, and other visual mechanisms.

[^mynote2]: Plugins are installable add-ons for the napari viewer which enhance its image analysis capabilities. They are discoverable in the napari viewer or on [napari hub](https://www.napari-hub.org). 

Napari aims to minimize (and eventually eliminate) the amount of coding knowledge needed to use it, making it friendly for researchers in life-science based fields. However as napari is still being developed and evolving as a platform, the current version (as of June 2022) requires some user understanding of the basics of: **conda**, **Python**, and **virtual environments**. These concepts will be explained in subsequent sections, where you will be guided through installing napari. Core developers are building a stable app version of napari that can be installed like other desktop apps without using code. 

:::{hint}
Although the [napari bundled app](https://napari.org/stable/tutorials/fundamentals/installation.html#install-as-a-bundled-app) already exists, it is still in development and not entirely stable. We recommend [installing napari as a Python package](https://napari.org/stable/tutorials/fundamentals/installation.html#prerequisites-for-installing-napari-as-a-python-package) if you intend to perform cell segmentation. This note will be updated as napari evolves.
:::

## Corpus Schema

Large datasets produced by modern imaging technologies (such as time lapse imaging, confocal microscopy, super-resolution microscopy, or light sheet microscopy) can be challenging for legacy tech to handle and analyze. Sophisticated methods are needed for analysing this data and often these methods utilize programming languages such as Python. Python is an open-source language with many capabilities for image analysis provided by its numerous open-source packages (also called libraries). However, without coding experience, researchers have limited options for utilizing the image processing power of Python. Graphical user interfaces (GUIs), like napari's, are a way to utilize Python-based analysis methods without writing any code.

:::{hint}
Napari’s utility is certainly not limited to handling large datasets. Since napari is based on Python, many useful packages can be made available for a range of simple or complex data processing and analysis tasks.
:::

Napari is built on the Python coding language, intending to bridge the gap between the inherently visual nature of image analysis and the computational power available through Python and its packages. This includes, for example, being able to leverage the speed of GPU-based computing and machine learning for large and complex processes, such as content-aware denoising, handling light-sheet microscope data, or even challenging segmentation cases! 

## Dataset Submission

Since napari is in the alpha stage of development, there are some functions that are not yet stable or available in the GUI. napari can be used in conjuction with other analysis platforms via these plugins for no-code workflows. For example, napari is interoperable with [FIJI](https://imagej.net/software/fiji/) through plugins for using napari with FIJI. Search for FIJI in napari under the top bar menu options: **plugins**>**Install/Uninstall Plugins** and enter "FIJI" as a search term.

## Supporting materials

### Napari documentation

- [Napari.org 'Quick Start'](https://napari.org/tutorials/fundamentals/quick_start.html)

### Community pages for napari

- [CZI napari landing page](https://chanzuckerberg.com/napari-a-multi-dimensional-image-viewer-for-python/)
- [Image.SC forum for napari](https://forum.image.sc/tag/napari)

### Introduction from a napari core developer

<br><center><iframe width="560" height="315" src="https://www.youtube.com/embed/VXdFOcBCto4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center> <br>

