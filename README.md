# VidSummarAI

This is an ongoing project trying to build a video summarization algorithm for the [LDV Vision Competition](http://www.ldv.co/visionsummit/2016/competitions/entrepreneurial-computer-vision-challenges).

The goal is to take an input video and produce a summary of it as a GIF.

### Data Source

Data was provided by [Yahoo's Webscope Program](https://webscope.sandbox.yahoo.com/)

### Structure


    explore/ - Ipython Notebooks to explore the data and play with ideas
    vidsummarai/ - Code for data manipulation, model fitting, etc.

### Usage

Currently we are just exploring the data and devising a plan. In the future
there will be a set of tools under vidsummarai/ that will be controlled
by a CLI, allowing you to create a summary of a video.

__Question__:

Do we want to seperate out training/exploring and creation
into seperate projects? Or can we house all the code in this
repository?