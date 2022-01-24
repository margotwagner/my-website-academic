---
title: California Traffic Records Collision Severity Preidction
summary: Using the California Statewide Integrated Traffic Records System dataset from 2001-2020, we look at various features and models to classify between collision severity. 
tags:
- Machine Learning
- Classification
- Python
date: 2020-11-20T20:06:45.112Z

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
url_slides: ""
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

Here we analyze the California Statewide Integrated Traffic Records System
dataset from January 1, 2001 to mid-October 2020 and use it to predict
collision severity. This prediction task was chosen as it is useful to inform
which safety measures to take to reduce collision fatalities. From the dataset,
we selected a variety of features to classify between collision severity ranging
from property damage only to injury to fatal. We compared Logistic
Regression, Decision Tree and Naive Bayes models of classification. The best
performance was achieved using the Logistic Regression with the inclusion
of victim data to get a balanced accuracy of 66.25%. The most important
features of the ones evaluated were whether the collision was a hit and run
misdemeanor, whether towing was required, and whether is was a rear-end
collision.

