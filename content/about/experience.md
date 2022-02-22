---
# An instance of the Experience widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: experience

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 40

title: Experience
subtitle:

# Date format for experience
#   Refer to https://wowchemy.com/docs/customization/#date-format
date_format: Jan 2006

# Experiences.
#   Add/remove as many `experience` items below as you like.
#   Required fields are `title`, `company`, and `date_start`.
#   Leave `date_end` empty if it's your current employer.
#   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
experience:
  - title: Graduate Student Researcher
    company: University of California, San Diego
    company_url: ''
    company_logo: org-ucsd
    location: San Diego, California
    date_start: '2018-09-25'
    date_end: ''
    description: |2-
        * Working to create a next generation biologically inspired AI neural network with biophysically meaningful parameters tunable for specific learning task
        * Built a biophysically realistic stochastic 3D reaction-diffusion model for synaptic transmission using MCell software and Python scripts containing 120 molecular states
        * Developed equivalent stochastic Markov chain synapse abstraction in Python with biologically tunable parameters, decreasing runtime by 93% and FLOPs by an order of magnitude for use in artificial neural networks models
        * Optimized parameters to match biological conditions using parameter sweep techniques by running models on supercomputer clusters and analyzed subsequent large-scale datasets
  - title: Graduate Teaching Assistant 
    company: University of California, San Diego
    company_url: ''
    company_logo: org-ucsd
    location: California
    date_start: '2019-01-01'
    date_end: '2020-03-20'
    description: Graduate teaching assistant for BENG 260 graduate level neurodynamics course and two quarters of BENG 1 Introductory Lab course for bioengineering undergraduates.

  - title: REU Intern  
    company: Tufts University 
    company_url: ''
    company_logo: org-tufts
    location: Medford, Massachusetts
    date_start: '2017-05-01'
    date_end: '2017-08-20'
    description: Working in the Tzanakakis lab on creating a Cell Ensemble Model for stem cell behavior utilizing both deterministic and stochastic aspects to predict events in response to intrinsic and extrinsic changes in the system.
        
  - title: Software Quality Assurance Intern
    company: Hologic, Inc.
    company_url: ''
    company_logo: org-hologic
    location: Newark, Delaware
    date_start: '2016-06-01'
    date_end: '2016-12-15'
    description: Created and executed formalized testing for mammography device software and technology; collaborated with the Software Engineering team

design:
  columns: '2'
---
