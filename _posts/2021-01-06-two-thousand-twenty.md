---
title: "The Stanford Software Survey, 2020"
date: 2021-01-05T10:47:58+10:00
draft: false
layout: post
---

2020 was the first year of the Stanford Software Survey, which started discussion
in early April, was developed in the months following, and went out in the Fall.
In this post, we discuss the full results for 68 participants, which can serve as a baseline for future
surveys, and the start of initiative to prove the necessity for research software
engineers.

# About People

## In which school or unit are you most strongly affiliated?

{% assign affiliation_counts = site.data.stanford-software-survey-2020["In which school or unit are you most strongly affiliated?"].counts %}
{% include graphs/pie.html counts=affiliation_counts divid="chart_affiliation_2020" %}

<p class="team team-summary team-summary-large">Not suprisingly, the largest of our user base comes from the School of Medicine, Humanities and Sciences, and Engineering. This result is likely biased based on distribution of the survey to these groups. It also is commonly assumed that hard sciences are most stongly in need of software engineering, which isn't always the case.</p>

<br>

## Do you consider yourself a research software engineer (RSE)?

{% assign rse_counts = site.data.stanford-software-survey-2020["Do you consider yourself a research software engineer (RSE)?"].counts %}
{% include graphs/pie.html counts=rse_counts divid="chart_2020" %}

<p class="team team-summary team-summary-large">This might look like a surprising result. How could a a quarter of the respondents indicate being a research software engineer if the role is relatively new in the United States? It's not surprising when you consider that many "traditional" academic roles, including
graduate students, lab and university staff, and postdoctoral candidates work on research software. This result is an attestation to the idea that we already have an existing community of research software engineers (RSEs) but they are called something different.</p>

## What is your job title?

{% assign job_counts = site.data.stanford-software-survey-2020["What is your job title?"].counts %}
{% include graphs/pie.html counts=job_counts divid="chart_job_2020" %}

<p class="team team-summary team-summary-large">In this result we see that the survey captured a wide range of roles, with the majority being graduate students, postdocs, or research associates, and fewer with roles like Manager or Professor. Titles have been post-processed to add grouping. We call any entry that is a PhD Student (including MD/PhD) or PhD Candidate a "PhD Student," "RA" or "Research Coordinator" or "Research Assistant" a "Research Assistant," all derivations of a Postdoctoral Fellow are called "Postdoc", and general software, systems, any kind of Manager title is simply called "Manager," data and research scientists are grouped under "Research Scientist," and cloud engineers as "Software or Systems Engineer." In future surveys this response field should be a controlled choices input.</p>

<br>

# Software Used


## Does your lab use or develop any open source software, or services?

{% assign dev_counts = site.data.stanford-software-survey-2020["Does your lab use or develop any open source software, or services?"].counts %}
{% include graphs/pie.html counts=dev_counts divid="chart_dev_2020" %}

<p class="team team-summary team-summary-large">We suspect that respondants from departments that do not explicitly do research (and thus need research software) are the ones that indicate not developing any. Based on experience, we've seen that more functional or large service departments like Human Resources or UIT tend to use commercial solutions over doing custom development, which is a logical choice.</p>

<br>

## Do you use research software?

{% assign usage_counts = site.data.stanford-software-survey-2020["Do you use research software?"].counts %}
{% include graphs/pie.html counts=usage_counts divid="chart_usage_2020" %}

<p class="team team-summary team-summary-large">This result attests to the value of research software engineers, as the large majority of respondants indicate using research software. Indeed, it is an essential part of the ecosystem of the University.</p>

<br>

## How important is research software to your work?

{% assign work_counts = site.data.stanford-software-survey-2020["How important is research software to your work?"].counts %}
{% include graphs/bar.html counts=work_counts divid="work_chart_2020" labels="Not at all Important,Somewhat Important,Neutral,Moderately Important,Vital" %}

<p class="team team-summary team-summary-large">This is a proud result! Software is becoming an increasingly important component to conducting research.</p>

<br>

## Have you developed your own research software?

{% assign develop_counts = site.data.stanford-software-survey-2020["Have you developed your own research software?"].counts %}
{% include graphs/pie.html counts=develop_counts divid="chart_2020_develop" %}

<p class="team team-summary team-summary-large">This question could be considered alarming given that only a quarter of respondents identify as research software engineers, but almost three quarters indicate developing their own research software. The next set of questions about training will shed light on whether they feel equipped to do this.</p>
<br>

# Software Development

# How do you rate your software development expertise?

{% assign expertise_counts = site.data.stanford-software-survey-2020["How do you rate your software development expertise?"].counts %}
{% include graphs/bar.html counts=expertise_counts divid="expertise_chart_2020" labels="Beginner,Competent,Proficient,Advanced,Professional" %}

<p class="team team-summary team-summary-large">This is a reassuring result that most participants at least consider themselves proficient in software development.</p>

## Do you feel that you have received sufficient training for software engineering best practices?

{% assign training_counts = site.data.stanford-software-survey-2020["Do you feel that you have received sufficient training for software engineering best practices?"].counts %}
{% include graphs/pie.html counts=training_counts divid="chart_training_2020" %}

<p class="team team-summary team-summary-large">Indeed, the large majority (three quarters) of participants indicate not having enough training to develop research software, and yet three quarters of them are also doing it. If the reputation of the University and reproducible, and accurate science depends on this software, we could be in trouble. It also should not be assumed that training researchers to be software engineers is the best route. Software engineering could be provided as a service instead, for example, having a central team of Research Software Engineers (RSEs) that work together and closely with labs.</p>

## How would you rate the university's current level of support for your software-development needs?

{% assign usupport_counts = site.data.stanford-software-survey-2020["How would you rate the university's current level of support for your software-development needs?"].counts %}
{% include graphs/bar.html counts=usupport_counts divid="usupport_chart_2020" labels="Very Poor,Poor,Average,Good,Excellent" %}

## Open Source Software Used

<p class="team team-summary team-summary-large">If you look closely at the chart linked from the button below, you'll see everything reported from programming languages (Python, R, Perl, etc.) to version control software and
platforms (e.g., git, GitHub) to scientific programming libraries (e.g., numpy, scipy, matplotlib),
and databases (sqlite, sqalchemy). You'll even see frontend fraemworks like React, NodeJs, and electron!
 A lot of the results also hint at particular domains of science or study such as natural language processing (NLP) or geography. The interesting question,
then, is how can we create some initiative to better showcase and support these open source
libraries?</p>

<a class="button" href="{{ site.baseurl }}/results/open-source-software-used/">Open Source Software Used</a>

<br>

## Open Source Software Developed 

<p class="team team-summary team-summary-large">The graphic linked below shows only a small sample of the open source software developed by Stanford researchers! Very likely there are still cultural challenges to sharing, meaning that a lab or individual won't share due to fears about being "scooped." If you look closely, you'll see that some labs have their own GitHub organization, and other software is developed under the name of an individual.</p>

<a class="button" href="{{ site.baseurl }}/results/open-source-software-developed/">Open Source Software Developed</a>

<br>

## How confident are you with the following technologies?

### Version Control

{% assign vc_counts = site.data.stanford-software-survey-2020["How confident are you with the following technologies? Version control"].counts %}
{% include graphs/pie.html counts=vc_counts divid="chart_2020_version_control" %}

<p class="team team-summary team-summary-large">This is a fantastic result, because it shows that half of participants are confident with version control. Might this be because GitHub and training around using git (e.g., Software Carpentry) has become fairly common and easy to access? Is it because most students are pushed into learning version control for the benefit of collaboration and research? We might consider git part of a minimal set of required learning for doing any kind of collaborative research that relies heavily on software, and the consequence of that is ample training and researchers that have confidence in using it.</p>

### Continuous Integration

{% assign ci_counts = site.data.stanford-software-survey-2020["How confident are you with the following technologies? Continuous integration"].counts %}
{% include graphs/pie.html counts=ci_counts divid="chart_2020_ci" %}

<p class="team team-summary team-summary-large">Unlike version control, the majority of respondants are not confident with continuous integration. This likely can be seen with having many repositories in version control, but not having automated builds or deployments.</p>


### Unit Testing

{% assign test_counts = site.data.stanford-software-survey-2020["How confident are you with the following technologies? Unit testing"].counts %}
{% include graphs/pie.html counts=test_counts divid="chart_2020_testing" %}

<p class="team team-summary team-summary-large">This result is very comparable to the previous. The majority of respondants are not confident with unit testing, and we can likely see this if we look at research software and notice a complete lack of or minimal amount of testing.</p>

<br>

# Hiring or Recruitment

## Have you or someone in your group ever hired someone specifically to develop software?

{% assign hiring_counts = site.data.stanford-software-survey-2020["Have you or someone in your group ever hired someone specifically to develop software?"].counts %}
{% include graphs/pie.html counts=hiring_counts divid="chart_202_hiring0" %}

<p class="team team-summary team-summary-large">This result attests to the need for research software engineers, as a third of respondants report actually hiring someone. What this result cannot show is the number of participants that could have used hiring someone, but simply could not afford it.</p>

## Have you ever included costs for software development in a funding proposal?

{% assign funding_counts = site.data.stanford-software-survey-2020["Have you ever included costs for software development in a funding proposal?"].counts %}
{% include graphs/pie.html counts=funding_counts divid="chart_2020_funding" %}

<p class="team team-summary team-summary-large">This result shows opportunity, as the section of the pie that intended to write research software did not ask for funding, and this can be helped with more awareness and change in culture.</p>

<br>

## How suitable would the following models be for your software development needs? Hire a full-time software developer

### Hire a full-time software developer

{% assign counts_hire1 = site.data.stanford-software-survey-2020["How suitable would the following models be for your software development needs? Hire a full-time software developer"].counts %}
{% include graphs/pie.html counts=counts_hire1 divid="chart_2020_hire1_developer" %}

<p class="team team-summary team-summary-large">Over half of respondants consider it not suitable to hire a full time software developer. It would be interesting to understand why.</p>


### Recruit a developer from RSE Services

{% assign counts_hire2 = site.data.stanford-software-survey-2020["How suitable would the following models be for your software development needs? Recruit a developer from RSE Services"].counts %}
{% include graphs/pie.html counts=counts_hire2 divid="chart_2020_hire2_developer" %}


<p class="team team-summary team-summary-large">Interestingly, while the majority would not want to hire a full time developer, recruiting a developer from RSE Services seems to be the majority choice, with three quarters of respondants indicating that it would be suitable or perfect. This indeed is a result that reflects on the need for a team of research software engineers. The remaining challenge, however, is figuring out how to make that service cost effective for the researchers that likely don't have ample funding.</p>


We hope that in future surveys we can better advertise and incentivize the Stanford community
to participate, and increase the size of the sample.
