---
title: "Confidence in Skill"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# How confident are you with the following technologies?

## 2020

### Version Control

{% assign counts = site.data.stanford-software-survey-2020["How confident are you with the following technologies? Version control"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2020_version_control" %}

### Continuous Integration

{% assign ci_counts = site.data.stanford-software-survey-2020["How confident are you with the following technologies? Continuous integration"].counts %}
{% include graphs/pie.html counts=ci_counts divid="chart_2020_ci" %}

### Unit Testing

{% assign test_counts = site.data.stanford-software-survey-2020["How confident are you with the following technologies? Unit testing"].counts %}
{% include graphs/pie.html counts=test_counts divid="chart_2020_testing" %}
