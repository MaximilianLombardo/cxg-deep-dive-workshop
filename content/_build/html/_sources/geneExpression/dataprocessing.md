# Gene Expression Data Processing

:::{figure-md} data-processing
<img src="images/DiscoverDocs/doc-site/4-2_figure5.png" alt="gene expression" class="bg-primary mb-1" width="1200px">

Overview of processing steps from raw read counts to gene expression averages per cell type.
:::

## Removal of Duplicate Cells

Some data on CELLxGENE Discover is duplicated due to independent submissions, for example meta-analysis vs original data. All data submitted on Discover is curated to indicate whether any cell is the primary data. Only cells demarcated as primary data are included in the processing steps below.

## Removal of Low Coverage Cells

Any cell that has less than 500 genes expressed is excluded, this filters out about 8% of all data and does not eliminate any cell type in its entirety. This filter enables more consistent quantile vectors used for the normalization step.

## Removal of Cells Based on Sequencing Assay

Only cells from sequencing assays that measure gene expression and don't require gene-length normalization are included.

**Cells from the following assays are included**:

<table>
  <tr>
    <th>Assay</th>
    <th>EFO ontology term ID</th>
  </tr>
  <tr>
    <td>sci-RNA-seq</td>
    <td>EFO:0010550</td>
  </tr>
  <tr>
    <td>10x 3' v1</td>
    <td>EFO:0009901</td>
  </tr>
  <tr>
    <td>10x 5' v1</td>
    <td>EFO:0011025</td>
  </tr>
  <tr>
    <td>10x 3' v2</td>
    <td>EFO:0009899</td>
  </tr>
  <tr>
    <td>10x 5' v2</td>
    <td>EFO:0009900</td>
  </tr>
  <tr>
    <td>10x 3' v3</td>
    <td>EFO:0009922</td>
  </tr>
  <tr>
    <td>10x 3' transcription profiling</td>
    <td>EFO:0030003</td>
  </tr>
  <tr>
    <td>10x 5' transcription profiling</td>
    <td>EFO:0030004</td>
  </tr>
  <tr>
    <td>10x technology</td>
    <td>EFO:0008995</td>
  </tr>
  <tr>
    <td>Seq-Well</td>
    <td>EFO:0008919</td>
  </tr>
  <tr>
    <td>Drop-seq</td>
    <td>EFO:0008722</td>
  </tr>
  <tr>
    <td>CEL-seq2</td>
    <td>EFO:0010010</td>
  </tr>
</table>

## Gene-length Pre-normalization

**WARNING** - The following process has not been implemented as the feature **currently only includes data that does not require gene-length normalization.**

In platforms that sequence full RNA molecules, such as Smart-seq, gene counts are directly correlated with gene length. To account for this, gene counts from these technologies are divided by the corresponding gene length prior to normalization.

For each gene in our reference files, length was calculated by creating non-overlapping meta-exons across all isoforms of a gene, and then adding up their length in base-pairs.

## Data Normalization

Read counts are normalized using a modification of the rankit method which is a variation of quantile normalization used for gene expression data (Bolstad BM et al., Evans C et al., The GTEx Consortium.).

For a given cell in a count matrix, the read counts across genes are transformed to quantiles, then those quantiles are mapped to the corresponding values of a normal distribution with mean = 3 and variance = 1 ({numref}`rankit-2`). Normalized matrices from multiple datasets of the same tissue are concatenated along the gene axis.

:::{figure-md} rankit
<img src="images/DiscoverDocs/doc-site/4-2_figure6.png" alt="gene expression" class="bg-primary mb-1" width="1200px">

Not normalized.
:::

:::{figure-md} rankit-2
<img src="images/DiscoverDocs/doc-site/4-2_figure7.png" alt="gene expression" class="bg-primary mb-1" width="1200px">

Normalized.
:::



This method accounts for sequencing depth by scaling gene expression to the approximate range of 0 to 6. A high gene-cell value ( > 5 ) indicates that the gene is amongst genes that are the highest expressed in that cell, and similarly a low value ( < 1 ) indicates that the gene is amongst the lowest expressed genes in that cell.

Rankit normalization compresses highly expressed genes to the right tail of the standard normal distribution (see below), thus providing ideal values for using a color representation of gene expression and avoiding saturation that would otherwise be present.

## Considerations

Given that the normalization is a form of quantile normalization that uses a constant target distribution, there are a few important considerations while working with these values:

- These values transform the biological/technical variance of gene expression to a constant variance from a normal distribution.
- It has been proven that quantile normalization reduces technical variance and to a lesser extent biological variance (Abrams ZB et al.).
- Individual gene expression values can produce spurious differential gene expression analysis (Zhao Y et al.).
- This normalization is not designed to specifically account for batch effects, however the use of a constant target distribution mitigates batch effects when calculating average gene expression. This mitigation is stronger as the number of datasets per tissue increases.

## Removal of Noisy Ultra-low Expression Values

After applying normalization, any gene/cell combination that had counts less or equal than 2 are set to missing data. This allows for removal of noise due to ultra-lowly expressed genes and provides a cleaner visualization.

## Summarization of Data in Dot Plot

For each gene/cell type combination the following values are represented in the dot plot, either visually or in text upon hover.

- Gene expression (dot color) – the average rankit-normalized gene expression among genes that have non-zero values.
- Scaled gene expression (dot color) – scaled mean expression to the range [0,1]. Scaling is done by assigning the minimum value in the current view to 0 and the max is assigned to 1.
- Expressing cells (dot size) – percentage of cells of the cell type expressing the gene, in parentheses is shown the absolute number of cells expressing the gene. These numbers are calculated after the following filters have been applied: "Removal of low coverage cells" and "Removal of noisy low expression values".

## Expression and cell count rollup across descendants in the cell ontology

The cell ontology is a hierarchical tree structure that represents the relationship between cell types. For example, the cell type "B cell" is a descendant of the cell type "lymphocyte". For a particular cell type, The cell ontology is used to sum up the expression values and cell counts of cells labeled as that cell type as well as those labeled as its descendants. In the aforementioned example, the average expression of "lymphocyte" would include "B cells" and all its other descendants.

This rollup operation accounts for the fact that different datasets may have labeled their cells with different levels of granularity. It provides a more robust measure of the average expression of low-granularity cell type terms, such as "secretory cell" or "lymphocyte".

# References

1. Abrams ZB et al. A protocol to evaluate RNA sequencing normalization methods. BMC Bioinformatics. 2019. [PubMed](https://pubmed.ncbi.nlm.nih.gov/31861985/).
1. Bolstad BM et al. A comparison of normalization methods for high density oligonucleotide array data based on variance and bias. Bioinformatics. 2002. [PubMed](https://pubmed.ncbi.nlm.nih.gov/12538238/).
1. Evans C et al. Selecting between-sample RNA-Seq normalization methods from the perspective of their assumptions Ciaran. Briefings in Bioinformatics. 2018. [PubMed](https://pubmed.ncbi.nlm.nih.gov/28334202/).
1. The GTEx Consortium. The GTEx Consortium atlas of genetic regulatory effects across human tissues. Science. 2020. [PubMed](https://pubmed.ncbi.nlm.nih.gov/32913098/).
1. Zhao Y et al. How to do quantile normalization correctly for gene expression data analyses. Scientific Reports. 2020. [PubMed](https://pubmed.ncbi.nlm.nih.gov/32968196/).