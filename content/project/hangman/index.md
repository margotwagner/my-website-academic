---
title: Hangman Helper AI 
summary: A helper for the Hangman game that suggests to the user the best letter to guess next with a certain probability given the existing game state meaning which letters have been guessed and where they are located as well as the incorrectly guessed letters. 
tags:
- AI
- Probabilistic Graphical Models
date: 2021-03-20T20:06:45.112Z

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: ""
  filename: featured
  focal_point: Smart
  preview_only: false

links:
- icon: github
  icon_pack: fab
  name: Repo
  url: ""
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

draft: true
featured: false
---

Given the current state of a Hangman game - meaning the location of correctly guessed letters if any and incorrectly guessed letter - the Hangman Helper will suggest to the user the letter they should guess next with a certain probability. The Hangman Helper AI uses a 5-letter word corpus and conditional probability rules to construct this output. The network is constructed as a belief network where there is a 5-letter word (W) and 5 letter random variables (L1 to L5). Bayes Rule is used to predict the letter that is most likely to be among the missing letters.  

