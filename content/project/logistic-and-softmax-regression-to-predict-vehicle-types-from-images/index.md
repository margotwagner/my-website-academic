---
title: Logistic and Softmax Regression to Predict Vehicle Types from Images
summary: Trained logistic and softmax regression models built from scratch to predict vehicle types from 200x300 pixel images from the Comprehensive Cars dataset.
tags:
- Machine Learning
- Classification
- Python
date: 2021-01-18T20:06:45.112Z

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: "The Comprehensive Cars (CompCars) dataset (Yang 2015)."
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

We trained logistic and softmax regression models to predict vehicle types from 200x300 pixel images from the Comprehensive Cars dataset. We achieved 60\% test accuracy classifying Convertible and Minivan vehicle types on the resized dataset. In our second model, we achieved 76.4\% average test accuracy classifying Convertible and Minivan vehicle types on the aligned dataset. In our third model, we achieved 80.0\% average test accuracy classifying Sedan and Pickup vehicle types. Lastly, we achieved 57.96\% average test accuracy classifying all four vehicle types using multiclass softmax regression. We observed that model performance is related to the visual similarity of vehicle types in the prediction task. We also explored the effect of varying the number of principal components, learning rate, and using batch vs. gradient descent throughout our analyses.