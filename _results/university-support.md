---
title: "University Support"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# How would you rate the university's current level of support for your software-development needs?

## 2020

{% assign counts = site.data.stanford-software-survey-2020["How would you rate the university's current level of support for your software-development needs?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_2020" labels="Very Poor,Poor,Average,Good,Excellent" %}

