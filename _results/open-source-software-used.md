---
title: "Open Source Software Used"
date: 2021-01-04T12:33:46+10:00
featured: true
weight: 1
layout: d3
---

# List the top open source libraries that you use?

## 2020

<p class="team team-summary team-summary-large">If you look closely, you'll see everything
reported from programming languages (Python, R, Perl, etc.) to version control software and
platforms (e.g., git, GitHub) to scientific programming libraries (e.g., numpy, scipy, matplotlib),
and databases (sqlite, sqalchemy). You'll even see frontend fraemworks like React, NodeJs, and electron!
 A lot of the results also hint at particular domains of science or study such as natural language processing (NLP) or geography. The interesting question,
then, is how can we create some initiative to better showcase and support these open source
libraries? Click on any box to be taken to a page for the software.</p>

{% assign data = site.data.software.software-2020.software.open-source-libraries-used %}
{% include graphs/tree.html data=data divid="chart_2020" %}

