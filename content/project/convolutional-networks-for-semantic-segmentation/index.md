---
title: Convolutional Networks for Semantic Segmentation
summary: Built various deep CNN architectures and trained them to predict the segmentation masks of the images in the India Driving Dataset as a semantic segmentation task.
tags:
- Deep Learning
- Convolutional Neural Networks
- Computer Vision
- PyTorch
- Python
date: 2021-02-16T20:06:45.112Z

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: "High-level architecture for baseline encoder-decorder CNN model."
  filename: featured
  focal_point: Smart
  preview_only: false

links:
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""
#https://github.com/Keshav919/CSE251B_PA3

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: "example"

draft: false
featured: false
---

In this paper, our goal is to apply an encoder-decoder network for the problem of semantic segmentation on the India Driving Dataset. Semantic segmentation belongs to the field of persistent problems in computer vision that requires high accuracy and efficiency, with applications in autonomous driving, robotics, and e-commerce. Our baseline model achieved a pixel accuracy of {\bf 0.699} and an Intersection over Union (IoU) of {\bf 0.159}. We worked to improve the results from a fully convolutional encoder-decoder network using various techniques including augmenting the dataset and addressing class imbalance, with the combination of techniques resulting in an accuracy of {\bf 0.691} and IoU of {\bf 0.144}. We further experimented to optimize the model by utilizing different architectures including changes to the activation function and number of layers, transfer learning, and U-Net implementation. Our best model, using transfer learning, sees a test accuracy of {\bf 0.723}, and a test IoU of {\bf 0.149}.