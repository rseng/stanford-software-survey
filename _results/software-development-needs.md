---
title: "Software Development Needs"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# How suitable would the following models be for your software development needs? Hire a full-time software developer

## 2020

### Hire a full-time software developer

{% assign counts = site.data.stanford-software-survey-2020["How suitable would the following models be for your software development needs? Hire a full-time software developer"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2020_hire_developer" %}

### Recruit a developer from RSE Services

{% assign counts2 = site.data.stanford-software-survey-2020["How suitable would the following models be for your software development needs? Recruit a developer from RSE Services"].counts %}
{% include graphs/pie.html counts=counts2 divid="chart_2020_2" %}
