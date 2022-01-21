---
title: Multi-Layer Neural Network Classification of Fashion MNIST Dataset
summary: Implemented a multi-layer neural network from scratch to classify images of fashion products using the Zalando's Fashion MNIST Dataset in order to identify strategies that optimize performance. 
tags:
- Deep Learning
- Classification
- Python
date: 2021-02-01T20:06:45.112Z

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: "Examples from Zalando's Fashion MNIST Dataset (Zalando 2017)."
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

We implemented a multi-layer neural network to classify images of fashion products using the Zalando's Fashion MNIST Dataset in order to identify strategies that optimize performance in neural networks. Our baseline model consisted of 2 hidden layers of 50 nodes and tanh activation and a softmax output layer, utilized a learning rate of 1.2e-2, momentum gamma of $0.9$, and no regularization, and was trained using stochastic gradient descent of mini-batch size $128$ over $100$ epochs with early stopping. The baseline achieved a high accuracy of 78.36\%. Several variations were tested, including varying activation functions (sigmoid, ReLU, leakyReLU), number of hidden nodes, and number of hidden layers. The fact that the baseline outperformed other variations suggests parameters in a sweet spot that are not too low or too high for the task at hand result in the best performance overall.