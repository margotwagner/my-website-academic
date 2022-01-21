---
title: Sentence Generation and Classification with Variational Autoencoder and BERT
summary: A conditional variational autoencoder uses a sentence premise and lass label to generate a hypothesis specific to that class type. Then, a BERT model is used to classify the results in order to evaluate the style transfer to generating the sentences. 
authors: margotwagner
tags:
- Deep Learning
- Classification
- Text Generation
- PyTorch
- Python
date: 2021-03-20T20:06:45.112Z

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: "BERT Architecture that was fine-tuned with the premise-hypothesis pairs (Fig from Devlin 2018)."
  filename: featured
  focal_point: Smart
  preview_only: false

links:
- icon: github
  icon_pack: fab
  name: Repo
  url: https://github.com/JinlongHuang/CSE251B_Final_Project
url_code: ""
url_pdf: ""
url_slides: "uploads/sentence-generation-BERT-slides.pdf"
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: "example"

draft: false
featured: false
---

In this paper, we explore logical and style-specific sentence generation. Given a
sentence (premise), the goal is to write a hypothesis that either agrees, contradicts, or says nothing about the premise. In order to achieve this goal we use the Contradictory, My Dear Watson dataset from Kaggle and the Stanford Natural Language Inference (SNLI) dataset. We leverage a conditional variational autoencoder for text generation that can take a premise and class label (entail, contradict, or neutral) to generate a hypothesis specific to that class type. We use the classification results from a BERT model in order to evaluate the style transfer to generating the sentences. While our BERT classifier achieved a loss of 0.291 and accuracy of 89.1% on the ground truth dataset, the classifier achieved a loss of 3.513 and accuracy of 38.7% on our best-performing conditional VAE generated examples, performing only slightly better than random chance. Our results suggest that more work needs to be done to algorithmically generate style-specific sentences following specific logical rules.

