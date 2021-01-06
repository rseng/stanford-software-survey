---
title: "University Affiliation"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# In which school or unit are you most strongly affiliated?

## 2020

{% assign counts = site.data.stanford-software-survey-2020["In which school or unit are you most strongly affiliated?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2020" %}
