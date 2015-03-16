#Analyzing Basketball Data with Python (and R)

The purpose of this project is to develop a series of tutorials and posts that educate interested readers on how to analyze basketball data (specifically NBA data) using Python and R. The tutorials will build knowledge of advanced NBA analysis, programming and analytical skills for the interested reader. The tutorials will be based on custom built packages for both python and R that will facilitate data collection and NBA specific analysis. A nice general framework for this project can be based on Hadley Wickaham's model of [data science](https://gist.github.com/hadley/820f09ded347c62c2864)

The motivation from this work is derived from [Kirk Goldsberry's talk at the 2015 Sloan Sports Analytics Conference](https://www.youtube.com/watch?v=wLf2hLHlFI8). One of his key points was the idea of analytics as the development and use of *reasoning artifacts*. Ideally, these tutorials will take an approach that identifies the question of interest, discusses the necessary *reasoning artifacts*, walks through the derivation of the artifact, and discusses the answer to the original question. Second, he talked about the importance of not reinventing the wheel, but taking skills from other domains that can help enlighten thought on sports. To this point, have a brief discussion of the historical significance of each chapter might be interesting. Third, he's a visualization expert. It is important to have visualization as a key part of these tutorials as they are what really helps make an analytical story come to life. Finally, he talked about the importance of providing access to data to facilitate the next Bill James and John Hollingers. I think this is where we can add real value with the Python and R packages that ease the extraction of raw data from the NBA website. This is the reason for naming the packages after Goldsberry himself.

As part of the project, it might be nice to approach Goldsberry once we have a significant portion of the project completed to ask for his critique and potential involvement. It would be super-cool if he was willing to author a couple chapters, especially on visualizing data.

I think we are uniquely skilled to tackle this challenge for a few reasons. First, we are self-taught *programmers*. That is, we are not professionally trained and therefore have learned exactly what we need to know to do what we want and not much else. This means that we are probably doing many things wrong, but we also can explain things to someone who comes from our background. Second, we have enough of an analytical background to walk-through most of the analysis that the audience for this book will be able to conduct and understand. I think having experience as teachers allows us to think in terms of the educational value of the explanation to maximize the learning of the reader. Many of the books I've read to learn different things haven't been that well written with enough explanation to make things stick. Third, if Daniel continues to teach Sports Analytics, the class can serve as a test environment for each of the tutorials and a great laboratory to get feedback and adjustment for future editions.

There are quite a few moving parts to this project. Some can be completed in parallel while others need to be completed in serial order.  As long as we keep site on the big picture and make sure we are moving forward, we will be fine. It is as important to get a draft finished as it is to make it phenomenal. Once we get it finished, we can iterate, improve, and expand, until we get it to where we are satisfied. **The most important point to remember is that this will be great if we make it as iterative as possible. **

##Keystone Pieces

###1 Python and R Packages
* `py-Goldsberry` (formerly `NBAStats`)
* `GoldsbeRry`
* Package Documentation

####1.1 `py-Goldsberry` (formerly `NBAStats`)
Since this is already built, it's the best place to start. Also, given Daniel's familiarity with Python, it will make for an easy technical transition to completing this project. 

Before we make any changes, we need to map out exactly where this package will sit in the analytical process and what functionality it needs to contain to work. As of now, it uses `pandas`, but I think it might actually be better to move `pandas` outside of the package and re-write the package to be used in conjunction, not on top of `pandas`. 

At one point, we talked about building in some graphs. I think this makes sense for certain graphs like shot charts. In that case, we may need build the package on top of `matplotlib` for python and `ggplot` in R. I'm just not sure what makes the most sense. I don't necessarily want to write tutorials on how to use `pandas` and the other packages since they already exist, but readers will need to have the basic concepts if they want to conduct the analysis.

Once we have the general structure of the package laid out, then we can start auditing and updating. Since data collection from `stats.nba.com` is the primary contribution of the package, we should start with that aspect of the package. First, we need to take stock of the data that this package is already designed to collect and if anything is broken or needs updated. Second, we need to identify the additional data that has been made available by the NBA and add that functionality into the package. Additionally, I think it would be beneficial to add some built in tables of general data from the NBA that is necessary to run the packages. These include a table of players and their id's, games and game ids', and teams and team ids. We can create a long-term development plan that includes updating these tables at some specified interval and re-publishing the package to include the updates.

####1.2 `GoldsbeRry`

####1.3 Package Documentation
While we are putting together the packages, we need to be diligent in writing up the documentation. **This is a key PARALLEL PROCESS!** I'm not exactly sure how to write documentation, but we can read through some examples. Much of the documentation for Python packages is hosted online where as R documentation is traditionally a PDF. I think we can make both online and be fine, especially since we aren't going to be writing any new mathematical functions, but just functions that ease the collection and input of data.

###2 Tutorials/Chapters
Each Chapter should focus on a single research question and an associated set of technical skills necessary to answer each research question. It would be sweet to add a list of additional questions that can be addressed with the technical skills in the chapter and related articles -- kind of like an *extra practice* section in a text book.

* Research Questions
* Programming Skills
* Extra Practice


While there are many different places where readers can get this information, we cannot shy away from "reinventing the wheel" or plagiarizing a bit. We have read enough tutorials where we can aggregate the good and bad parts into our own that can complete the given task. I'm thinking about things like installing Python and R and getting started with each. We only need to do what is absolutely required to complete our tutorials and we can easily add "additional reading" for those who are interesting in learning more in-depth. 

####2.1 Getting up and running with Python and R
Not sure if this should be the first chapter or an appendix. I envision this as being installing `conda` and an introduction to `IPython` as a development environment for Python. For R it would be installing `R` and `R Studio`. I was thinking about `git` because I think it would be good for our own skills to go through and put together a `how-to`, but I think it might be beyond the scope of a book. It might be something to think about if we want to add as an appendix.

To summarize:
* Installing necessary languages
* Introduction to the programming environment
* Basic calculator skills (adding, subtracting, setting scalar values, etc...)
* Suggestions for getting training on just the language
	* Datacamp
	* Codecademy
	* Written tutorials online
	* Books (learning Python the Hard Way, etc...)

####2.2 Introduction to `py-Goldsberry` (`GoldsbeRry`)
This would be installing and loading the packages as well as a walk through of the key pieces of the package. It would be similar to the documentation, but it wouldn't include any detailed technical aspect that isn't necessary to use the package for the next few chapters. In other words, it would be an overview of what data it can pull and how to pull the data using the packages

To summarize:
* Description of `py-Goldsberry`
* Installing/updating `py-Goldsberry`
* Primary features of `py-Goldsberry`
* Basic usage of `py-Goldsberry`
* Link to technical documentation to learn more about the packages

####2.3 Introduction to Advanced Basketball Analytics
I think we can talk about the major concepts of **Offensive Efficiency** and the importance of the **Possession**. The latter gets into things such as **Pace** and **Time independence**. I'm not sure what the best place to start is. I think the possession is nice because its a way to understand the entire game and helps provide an advanced view of the macro events where as the efficiency statistics start to get at micro-level analysis. The possession does provide the opportunity for micro-level analysis such as comparing what happens within a possession. 

Maybe a nice framework would be to talk about the two levels of analysis -- Macro and Micro and provide an overview of the types of questions  that fit into each category. Also, I'm wondering if we should put a introduction together that summarizes the history and purpose of advanced analytics in basketball. That would be something that would be awesome to have a Kirk Goldsberry or John Hollinger write as a foreword. Not sure if we could ever make those connections, but I think if we have something substantial enough that the network is small enough to at least make a serious ask.

#####2.3.1 The 'Possession'

#####2.3.2 The concept of 'Efficiency'
