---
title: Revealing Location-Specific Variation and Drug Transport Specificity in the Allen Brain Atlas
summary: Analyzed 7k gene RNA-seq dataset for a single clinically healthy patientfrom Allen Brain Atlas using ICA, PCA, clustering, and classification to predict brain regions (98.7% accuracy for 3 regions, 67.1% accuracy for 10 regions) to see if variations in gene expression can be used to predict between regions at different resolutions and if that data can be used to determine localization of drug behavior based on chemical similarity to metabolites transported by transporters genetically expressed.  
tags:
- Machine Learning
- Classification
- Computational Neuroscience
- Python
- Bioinformatics
date: 2019-03-22T20:06:45.112Z

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: ""
  filename: featured
  focal_point: Smart
  preview_only: false

links:
url_code: ""
url_pdf: ""
url_slides: "uploads/allen-brain-atlas-analysis.pdf"
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: "example"

draft: false
featured: true
---

This project analyzes single subject RNA-Seq data from the Allen Brain Atlas for clinically healthy patient. Here we look to see if there are significant variations in gene expression data between regions at different resolutions and if that data can be used to determine localization of drug behavior based on chemical similarity to metabolites transported by transporters genetically expressed. We find that this dataset can be used to train and test models to predict brain region information at lower structure-level resolutions, but more information would be needed to reach substructure or molecular resolutions. This can highlight important gene features associated with various regions of the brain, giving insight to their functions. Additionally, gene expression can be mapped from genes to transporters to metabolites to drugs, but more information on metabolites would be required. The cerebellum uptakes drugs with the highest activity compared to the cortex and brainstem. 

