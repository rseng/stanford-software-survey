---
title: "Job Title"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# What is your job title?

## 2020

{% assign counts = site.data.stanford-software-survey-2020["What is your job title?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2020" %}

<p class="alert alert-info">Titles have been post-processed to add grouping. We call any entry that is a PhD Student (including MD/PhD) or PhD Candidate a "PhD Student," "RA" or "Research Coordinator" or "Research Assistant" a "Research Assistant," all derivations of a Postdoctoral Fellow are called "Postdoc", and general software, systems, any kind of Manager title is simply called "Manager," data and research scientists are grouped under "Research Scientist," and cloud engineers as "Software or Systems Engineer." In future surveys this response field should be a controlled choices input.
