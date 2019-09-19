# Visual Software Analytics Summer School

## Introduction

In this repository, you can find the presentation and some demos that I've shown to you during my lecture on September 18, 2019.

You can play around with the content by opening this repository with Binder Hub by simply clicking on the following button:

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/feststelltaste/software-analytics/)

If the Jupyter Notebook environment is set up (this will around 2 minutes), please navigate to `demos\20190918_Uni_Leipzig` to find this `README.md` as well as the other content.

You can run the notebooks by clicking on the symbol with the "&raquo;" sign. Some notebooks are also presentations. You can start these by clicking on the symbol with the bar chart.

## Notebooks

### Analyzing Java Dependencies with jdeps (Demo Notebook)
<small><a href="Analyzing%20Java%20Dependencies%20with%20jdeps%20%28Demo%20Notebook%29.ipynb">open notebook</a></small>

This shows my vision on how developers can do very specific software data analysis with mainly standard Data Science tools. Using little helper libraries like [OZAPFDIS](https://github.com/feststelltaste/ozapfdis/) or [AUSI](https://github.com/feststelltaste/ausi/) (both are libs are in a very experimental state), they would be very efficient in getting new insights from their own data because they can quickly load in data from the software world into the Data Science world to benefit from the tools and approaches that exist there.

You can look at the D3.js produced visualizations for the my pet software project "DropOver" here:

* <a href="https://feststelltaste.github.io/software-analytics/courses/20190918_Uni_Leipzig/jdeps_demo_output/dropover_bundling.html">D3 Bundling</a>
* <a href="https://feststelltaste.github.io/software-analytics/courses/20190918_Uni_Leipzig/jdeps_demo_output/dropover_d3forced.html">D3 Forced Layout</a>
* <a href="https://feststelltaste.github.io/software-analytics/courses/20190918_Uni_Leipzig/jdeps_demo_output/dropover_semantic_substrate.html">D3 Semantic Substrate</a>

There is another visualization for the rather big project "OpenClinica":

* <a href="https://feststelltaste.github.io/software-analytics/courses/20190918_Uni_Leipzig/jdeps_demo_output/openclinica_d3forced.html">D3 Forced Layout (Open Clinica)</a>

You can also take a look at the output at your local machine. For this, you need to start a HTTP server e. g. with `python -m http.server` in the `jdeps_demo_output` directory and go to `http://localhost:8000` in your browser to see files.


### Data Science On Software Data (Empty Presentation)
<small><a href="Data%20Science%20On%20Software%20Data%20%28Empty%20Presentation%29.ipynb">open notebook</a></small>

This is the empty version of the presentation below. This is used by me to present the topic to a live audience.


### Data Science On Software Data (Presentation)
<small><a href="Data%20Science%20On%20Software%20Data%20%28Presentation%29.ipynb">open notebook</a></small>

This is the presentation including all the Python code for the integrated hands-on demo.


### Estimating the Knowledge Distribution within a Modular System (Demo Notebook)
<small><a href="Estimating%20the%20Knowledge%20Distribution%20within%20a%20Modular%20System%20%28Demo%20Notebook%29.ipynb">open notebook</a></small>

This is a short notebook that shows you how you can estimate the existing knowledge in a modular system. It mines through a Git log dataset, identifies modules and sums up the commits authors to get an impression which author did the most commits in such a module.


### Identifying Modularization Options based on Code Changes (Demo Presentation)
<small><a href="Identifying%20Modularization%20Options%20based%20on%20Code%20Changes%20%28Demo%20Presentation%29.ipynb">open notebook</a></small>

This notebook shows some advanced analysis techniques. The analysis wants to find you, if the modularization of the software systems fits the change behavior of the development team. It uses simple Machine Learning tools like Multi Dimensional Scaling and Agglomerative Hierarchical Clustering to assess the current modularization as well as creating an alternative modularization based purely on the changes made to the software system.


### Parsing and Analysing vmstat Data the Easy Way (Demo Notebook)
<small><a href="Parsing%20and%20Analysing%20vmstat%20Data%20the%20Easy%20Way%20%28Demo%20Notebook%29.ipynb">open notebook</a></small>

This notebook uses a little helper library called [OZAPFDIS](https://github.com/feststelltaste/ozapfdis/) to import data from the Linux tool `vmstat`. It demonstrates how easy our lives could be if we develop such little helper tools to get software data into the Data Science world.


### `Parsing and Analysing vmstat Data the Hard Way (Demo Notebook)`
<small><a href="Parsing%20and%20Analysing%20vmstat%20Data%20the%20Hard%20Way%20%28Demo%20Notebook%29.ipynb">open notebook</a></small>

This notebook shows the typical effort that has to be made when you want to get a dataset from a software system into the Data Science world. You'll see that there is much data wrangling involved. But thanks to the functionality of pandas, getting somehow structured data into a DataFrame is straightforward.

# Your next Steps

## Try out the Workshop

You can find the contents of the Software Analytics Workshop in the Git repository here: https://github.com/feststelltaste/software-analytics-workshop

## Read more about this topic

You'll find my blog at https://feststelltaste.de . There, I wrote about my learning experience with applying Data Science Tools on Software Data.

There are also my TOP 5 recommendations for getting started with the Data Science tools: https://www.feststelltaste.de/category/top5/

## Give Feedback

I would be happy if you provide some feedback about the content that I've created. Feel free to [contact me](https://www.feststelltaste.de/contact/).