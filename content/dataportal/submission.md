# Summary of CZ CELLxGENE Discover Submission Requirements

CELLxGENE partners with the lattice curation team to facilitate the curation and ingestion of datasets into the corpus. You can reach the lattice Curation team by emailing us at [cellxgene@chanzukerberg.com](mailto:cellxgene@chanzuckerberg) and including information about data submission in the subject line. You will then be responsible for making sure the submitted data object adheres to the requirements defined below.

## Schema

CELLxGENE aims to support the publication, sharing, and exploration of single-cell datasets. It seeks to create references of the phenotypes and composition of cells in human tissues. To achieve this, cellxgene requires harmonization of metadata and features in the CELLxGENE Data Portal. For the full set of requirements, please refer to our [schema](https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/3.0.0/schema.md). Here is a abbreviated version for quick reference (please note that the schema requirements represent the minimum required information, and additional metadata can be included in datasets submitted to the cellxgene Data Portal.):

### Collection Information
- Title
- Description
- Contact: name and email
- Publication/preprint DOI (optional)
- URLs for related data or resources (optional)

### Dataset-level Metadata (uns)
- schema_version: '3.0.0'
- title: title of the individual dataset visualization
- batch_condition (optional): list of obs fields defining "batches"
- default_embedding (optional): obsm key for default embeddings
- For spatial assays, include numpy array of hires image in uns.image

### Data (h5ad Format)
- One h5ad file per visualization
- .X and raw.X:
  - raw counts are required
  - normalized counts are strongly recommended
  - raw counts in raw.X if normalized counts in .X
  - raw counts in .X if no normalized matrix
- Cells Metadata (obs)
  - organism_ontology_term_id: NCBITaxon
  - tissue_ontology_term_id: UBERON
  - For organoids, append " (organoid)" to UBERON term
  - For cell cultures, use CL term appended with " (cell culture)"
  - assay_ontology_term_id: EFO
  - disease_ontology_term_id: MONDO or PATO:0000461 for 'normal'
  - cell_type_ontology_term_id: CL
  - self_reported_ethnicity_ontology_term_id: HANCESTRO if human, 'unknown' if info unavailable, 'na' if non-human
  - development_stage_ontology_term_id: HsapDv if human, MmusDv if mouse, 'unknown' if info unavailable
  - sex_ontology_term_id: PATO:0000384 for male, PATO:0000383 for female, or 'unknown' if unavailable
  - donor_id: free text string
  - suspension_type: 'nucleus', 'cell', or 'na'
- Embeddings (obsm)
  - One or more two-dimensional embeddings, prefixed with 'X_'
  - For spatial assays, include x,y coordinates as 'X_spatial'
- Features (var & raw.var)
  - Index is Ensembl ID (human or mouse IDs only)
  - Preferably unfiltered genes for future data integration efforts

### Data Submission Policy
By submitting the data, the submitter grants CZI permission to display, distribute, and create derivative works of the data for CELLxGENE Discover. Personal identifiers must be removed from the metadata. Publicly published data will be subject to a CC-BY license. Collection details will be made public on CELLxGENE Discover.

### Tips for Reducing h5ad File Size
- Use compression=gzip in write_h5ad function
- Store matrix data as float32 instead of float64
- Convert 64-bit metadata columns to 32-bit
- Convert string columns to categorical if possible
- Remove unnecessary 'layers'
- Ensure X & raw.X are sparse.csr_matrix if >50% values are zeroes
