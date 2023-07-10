Discover single cell and spatial data
=======================
**Duration**: 20 minutes

In this module, you'll learn about the [CELLxGENE Discover Portal](https://cellxgene.cziscience.com/collections), the [Census Data Schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/3.0.0/schema.md) , and how to submit your datasets to the Discover Portal. Listed below, are the learning goals for each section of this module:

<div class="row">
  <div class="col-12">
    <div class="card">
      <div class="card-body">
        <!-- Content for the first card -->
        <strong>Discover Portal</strong>: 
        <ul>
            <li>Learn how to search, filter, explore, and download single cell and spatial data.</li>
            <li>Explore the corpus via collection view or dataset view.</li>
            <li>Find publication abstracts, group contact information, etc.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-12">
    <div class="card">
      <div class="card-body">
        <!-- Content for the first card -->
        <strong>Census Schema</strong>: 
        <ul>
            <li>Learn about ontologies.</li>
            <li>Review key metadata fields and associated ontologies.</li>
            <li>Understand data policy and accepted data types.</li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-12">
    <div class="card">
      <div class="card-body">
        <!-- Content for the first card -->
        <strong>Data Submission</strong>: 
        <ul>
            <li>Submission Process Overview</li>
            <li>Uses Cases and Questions.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

## Discover UI Overview

:::{figure-md} markdown-fig
<img src="images/collections/halfscreen.png" alt="collections" class="bg-primary mb-1" width="900px">

CZ CELLxGENE Data Portal: Collections Page
:::
---

### Collections
CZ CELLxGENE Discover is optimized for finding, exploring, and reusing single cell data that adhere to a standard [schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/3.0.0/schema.md) that facilitates intuitive exploration and integration. The Collections Page lists the collections[^collections_note] hosted on CELLxGENE Discover and metadata that define the tissue, assay, disease, organism, and cell count for each collection. You can reach the collections page by navigating to [https://cellxgene.cziscience.com/collections](https://cellxgene.cziscience.com/collections) or by navigating to the left hand side of the page header and making sure that the collections page is selected.



[^collections_note]: i.e. collections of datasets associated with a particular publication or consortia effort


:::{figure-md} markdown-fig
<img src="images/collections/header_left.png" alt="collections" class="bg-primary mb-1" width="300px">

<font size="3" > Select the Collections page to explore datasets by their associated publication or consortia group. </font>
:::



Collections represent groups of datasets, typically associated with either a publication or a particular consortia and are displayed as rows in a table on the center of the Collections Page. In each row, we view collection metadtata which includes the collection title (a.k.a. publication title or consortia dataset title), publication reference, the tissue(s), disease state(s), and organism profiled in the collection.

```{margin} Pro Tip
Hover over disease, tissue, and organism fields to expand the list when multiple categories (i.e. '4 tissues') of any field are present
```

:::{figure-md} markdown-fig
<img src="images/collections/collections_metadata.png" alt="collections" class="bg-primary mb-1" width="900px">

Collection metadata
:::

### Datasets

### Filtering Collections

#### Categorical filters

#### Ontology based filters

### Filtering Datasets

#### Numeric Filters

### Viewing a Collection Page

:::{figure-md} markdown-fig
<img src="images/TSCollection/fullscreen.png" alt="collections" class="bg-primary mb-1" width="900px">

Abstract associated with a Collection.
:::


#### Abstract

:::{figure-md} markdown-fig
<img src="images/TSCollection/abstract.png" alt="collections" class="bg-primary mb-1" width="900px">

Abstract associated with a Collection.
:::

#### Contact Information

:::{figure-md} markdown-fig
<img src="images/TSCollection/contact.png" alt="collections" class="bg-primary mb-1" width="900px">

Relevant publication information (contact, raw data store, consortia links)
:::

#### Dataset Metadata

:::{figure-md} markdown-fig
<img src="images/TSCollection/datasets.png" alt="collections" class="bg-primary mb-1" width="900px">

All datasets associated with a dataset are listed in a table on the Collection Page. Tissue, Disease, Orgnism, Number of Cells are all available metadata. On the right hand side of the dataset table, we have options to download or explore a chosen dataset.
:::

#### Dataset Download Dialog

#### Dataset Explore Button








:::{hint}
this is a hint
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


