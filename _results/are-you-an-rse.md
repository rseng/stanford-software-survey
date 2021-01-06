---
title: "Self Identification"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# "Do you consider yourself a research software engineer (RSE)?"

## 2020

{% assign counts = site.data.stanford-software-survey-2020["Do you consider yourself a research software engineer (RSE)?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2020" %}
