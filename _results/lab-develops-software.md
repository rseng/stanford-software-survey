---
title: "Lab Software Development"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# "Does your lab use or develop any open source software, or services?"

## 2020

{% assign counts = site.data.stanford-software-survey-2020["Does your lab use or develop any open source software, or services?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2020" %}
