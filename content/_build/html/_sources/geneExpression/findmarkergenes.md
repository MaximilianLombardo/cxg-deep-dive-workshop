# Find Marker Genes

Genes that are highly enriched in a particular group of cells can be used as markers for that population. Marker genes are commonly used to identify cell types in single-cell RNA-seq data. In Gene Expression, we can use the Find Marker Genes tool to identify genes that are specific to a particular cell type relative to other cell types in its tissue.

## Tutorial

First, let's select the lung tissue in Gene Expression. There is an info button next to each cell type label. Clicking the button opens a sidebar with the top 25 marker genes for that cell type:

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_plasma-cell.png" alt="gene expression" class="bg-primary mb-1" width="1200px">

Cell type marker genes.
:::

The marker genes are ranked by their Marker Score (see _Algorithm_ for more details). In the sidebar, we can click the `Add to Dot Plot` button to add these genes to the heatmap.

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_add-dotplot.png" alt="gene expression" class="bg-primary mb-1" width="1200px">

Add marker genes to dotplot.
:::

To get a better sense of the numbers behind the visualization, hover any of the dots in the plot to what fraction of cells of a particular class express the gene and well as average expression values (scaled and non-scaled).

:::{figure-md} markdown-fig
<img src="images/CELLxGENE_gene_expression/geneExpressionHover1.png" alt="collections" class="bg-primary mb-1" width="900px">

Hover over any of the dots on the chat to get a detailed view of data behind visualization
:::

Clicking the `Copy` button copies a comma-separated list of the marker genes to the clipboard. You might use this bring the list of marker genes from CELLxGENE to other analyis software.

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_copy-button.png" alt="gene expression" class="bg-primary mb-1" width="1200px">

Copy Button.
:::

To minimize the sidebar, click the chevron in the upper-right corner of the sidebar.

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_close-button.png" alt="gene expression" class="bg-primary mb-1" width="1200px">

Close button.
:::

Clicking on the info button next to another cell type will replace the marker gene sidebar with the marker genes for the new cell type.



## Algorithm

For a selected cell type in a tissue,

- Use Welch's t-test to compare the gene expressions in the selected cell type to each other cell type in the tissue.
  - Note: each cell type contains cells labeled as that cell type as well as its descendants in the cell ontology. Consequently, cell types are only compared to other cell types that are not in the same lineage (i.e. comparisons with ancestors and descendants are ignored).
  - Record the effect size for each gene in each comparison.
- For each gene, calculate the 5th percentile of the effect sizes across all comparisons. This is the marker score.
  - Let $T_t$ be the set of cell types $\{c_1,\ldots,c_n\}$ in tissue $t$. The marker score ($S_{c_ig_j}$) for gene $g_j$ in cell type $c_i$ is $S_{c_ig_j}=p_5(\{e_{c_kg_j} : c_k \in T_t, c_k \neq c_i\})$ where $p_5$ is the 5th percentile operator and $e_{c_kg_j}$ is the effect size of the t-test comparing $g_j$ in $c_i$ to $c_k$.
- Sort the genes by their marker score in descending order and return the top 25.

## Welch's t-test

Welch's t-test is a statistical test for comparing the means of two independent samples with unequal sample sizes and variances. For a particular gene,

- Let two groups of cells be $c_1$ and $c_2$. Calculate the following values:
  - $m_1$ and $m_2$ are the average expression of the gene in $c_1$ and $c_2$ respectively.
  - $s_1$ and $s_2$ are the standard deviations of the gene in $c_1$ and $c_2$ respectively.
  - $n_1$ and $n_2$ are the number of cells in $c_1$ and $c_2$ respectively _excluding cells from datasets that did not measure the gene_.
- Calculate the effect size (Cohen's d):
  - $e = \frac{m_1 - m_2}{\sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 1}}}$.
- Calculate the t-statistic $t$:
  - $t = \frac{m_1 - m_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$.
- Approximate degrees of freedom using Satterthwaite formula:
  - $df = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{\left(\frac{s_1^2}{n_1}\right)^2}{n_1 - 1} + \frac{\left(\frac{s_2^2}{n_2}\right)^2}{n_2 - 1}}$.
- Calculate the p-value using the t-distribution ($P(T >t)$).

## Validation

To determine if the genes reported by Find Marker Genes contain biologically relevant information, we can check to see if the marker genes alone are enough to recapiulate the cell type clustering of a few test datasets:

1. [Tabula Sapiens blood data](https://cellxgene.cziscience.com/collections/e5f58829-1a66-40b5-a624-9046778e74f5)
2. [COVID blood data (Arunachalam et al.)](https://cellxgene.cziscience.com/collections/b9fc3d70-5a72-4479-a046-c2cc1ab19efc)
3. [Human Lung Cell Atlas lung data](https://cellxgene.cziscience.com/collections/5d445965-6f1a-4b68-ba3a-b8f765155d3a)

Each test dataset was run through one of three analysis workflows:

1. **Standard analysis**: This is the standard analysis workflow offered by [Scanpy](https://scanpy.readthedocs.io/en/stable/) with cell types clustered using the Leiden algorithm.
2. **Marker gene analysis**: We take the union of the top 5 marker genes per cell type, subsample the data down to the resulting genes, and run the standard analysis workflow on the subsampled data.
3. **Random gene analysis**: We subsample the data down to $N$ random genes and run the standard analysis workflow on the subsampled data, where $N$ is the number of marker genes used in (2).

For each dataset and workflow, we report the adjusted rand index (ARI) and normalized mutual information (NMI) between the Leiden clustering results and the original cell type annotations. We also present the UMAP visualizations to qualitatively illustrate the clustering quality for each workflow.

### Tabula Sapiens blood data

**Standard analysis**

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_blood1_standard_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.35, NMI: 0.69
:::


**Marker gene analysis**

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_blood1_marker_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.31, NMI: 0.68
:::

**Random analysis**

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_blood1_random_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.16, NMI: 0.45
:::

### COVID blood data (Arunachalam et al.)

**Standard analysis**


:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_blood2_standard_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.50, NMI: 0.75
:::

**Marker gene analysis**


:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_blood2_marker_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.56, NMI: 0.75
:::

**Random analysis**

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_blood2_random_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.17, NMI: 0.33
:::

### Human Lung Cell Atlas lung data

**Standard analysis**

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_lung_standard_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.50, NMI: 0.80
:::

**Marker gene analysis**

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_lung_marker_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.50, NMI: 0.79
:::

**Random analysis**

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_lung_random_umap.png" alt="gene expression" class="bg-primary mb-1" width="600px">

ARI: 0.18, NMI: 0.41
:::

### Discussion

Subsampling the data down to the union of the top 5 marker genes per cell type typically yields around 250-350 unique genes. If this set of genes were not enriched in biologically relevant genes, subsetting the data down to such a small number of genes would give very low quality results (as shown in the random gene analysis results). Encouragingly, we do not observe any significant decrease in clustering accuracy when subsetting down to the marker genes in any of the datasets tested.

### Reproducibility notebooks

1. [Tabula Sapiens blood data](/doc-site/clustering_validation_blood1.pdf)
2. [COVID blood data (Arunachalam et al.)](/doc-site/clustering_validation_blood2.pdf)
3. [Human Lung Cell Atlas lung data](/doc-site/clustering_validation_lung.pdf)

## Caveats

- It is important to note that some methodological decisions were made to balance accuracy with efficiency and scalability. For example, we use a t-test to perform differential expression, which is a simple and fast test. However, it may not be as accurate as more sophisticated (and computationally intensive) statistical tests.
- While differential expression is typically performed on raw counts for single-cell RNA sequencing data, we opted to use the <NextLink href="04__Analyze%20Public%20Data/4_2__Gene%20Expression%20Documentation/4_2_3__Gene%20Expression%20Data%20Processing">rankit-normalized</NextLink> values in order to identify marker genes that corroborate the gene expressions shown in the dot plot.
- For the beta, we opted to not report the p-values for each gene. Though we can calculate approximate p-values using the t-statistic and degrees of freedom calculated in _Welch's t-test_, it is difficult to accurately aggregate the p-values for each gene across all comparisons. The most reliable method involves repeatedly permuting the data to generate a null distribution, but this is computationally intensive.
- Currently, marker genes are only calculated for cell types in tissues using only _healthy_ cells. Applying secondary filters to the data (like disease, ethnicity, etc.) does not affect the results. Enabling dynamic calculation of marker genes for arbitrary populations of cells in arbitrary subsets of the data may be a direction for future development.
- Ideal marker genes for a particular cell type are expressed in all of its cells and not expressed anywhere else: they have binary expression patterns. In reality, almost no genes have truly binary expression patterns. Instead, they have genes that are statistically enriched in their cells relative to all other cell types. Additionally, genes may be good markers for a cell type in one context (e.g. a tissue) but not another (e.g. the entire human body).

### Marker genes are not available for blood or small populations of cells

It may be difficult to identify any good markers for some cell types, especially if they have a small number of cells or are compared to many similar cell types. To account for the former scenario, marker genes are not displayed for cell types with fewer than 25 cells. The latter scenario is particularly relevant in the blood as it contains many closely-related cell types. As a result, we have temporarily disabled the find marker genes feature for cell types in blood.