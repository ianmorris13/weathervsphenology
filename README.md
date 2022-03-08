# weather vs phenology

## Questions for Chodrow

notes before quesitons... yes I know the CSS is not up to spec. I wanted to make sure, everything works before I added. now on to my questions... <br>
to run locally,  run 
$ export FLASK_ENV=development; flask run
in the terminal while under the main branch in the repository folder. You probably know that I'm just not sure If I had to add that. 

1. Does this show an advanced use of python? I know it is no mahcine learning, but there is quiery funcitons that users can input their desired inputs to output clean visualizations, and there are a few optinos to choose from.

2. If not, what do you recommend I expand on? Obviously my eyes were bigger than my stomach when orginally planning this, but so far I have a project that I am somewhat proud of, even if it is not 

3. Is it ok if I continue this project outside the class? I think that was your intention if I'm correct? That's why you had us make our own github page, and not through servers like the UCLA servers, correct? 

## Abstract

Over time, the impact of drought in the western United States, specifically California, has grown to be more and more worrisome. The ecological effect of a drought, specifically, the effect on plant growth, will be analyzed. We will be utilizing already existing data on plant growth and California drought, to understand the lasting effects of a drought that may occur in the future. We aim to focus on whether precipitation and differing temperature gradients affect the distribution of native plants vs the distribution of non-native plants. The goal is to visualize and project the future of the effect climate change has on California's native plants.

## Planned Deliverables

The aim of this project is to create attractive visualizations and create a machine learning model that can predict to utmost accuracy what the progression of California drought will be and the effect it will have on native and non-native plant growth. 

### Partial Success

We will be plotting drought conditions vs plant growth, which will offer a visual of what the past and current conditions are, as well as any correlation between the two. These visuals will be accessed through a webapp that we will create using heroku.

### Full Success
There will be a constant temperature and precipitation graphing, with the option to choose what region the graph is extracting from. Additionally, there will be options to filter between species, genus, native, non-native, etc. Different categories between all flowers and to compare said categories over the years. Lastly, this webapp will be hosted on herokuapp.com, similar to this website https://eitc-app.herokuapp.com/. 

In addition to the data visualizations, we aim to forecast the future of native species. Many factors will need to be considered, especially since there are many variables that come with ecological models.  Nevertheless, the website will provide current information on the correlation and effect of a drought and plant growth. Lastly, we will provide thorough written analysis on the data, explaining why this is important.

## Resources Required

We am going to use open source data from scientific organizations; which include:

Global Biodiversity Information Facility-
Free and open access to biodiversity data
https://www.gbif.org/

We will quiery data that includes the speacies, the number of observations, and the date and location of the observations using the built in data query.

http://scacis.rcc-acis.org/

We will copy paste data of the mean temperature and precipitation sum of each weather station in California from the built in data query, as there is no easy way to download.

## Tools and Skills Required

Web scrapping, machine learning, database management, complex visualizations, website building, and modeling are required for this project. 

Packages may include; Mesa, plotly, matplotlib, pandas, sqlite3, numpy, scikit-learn, seaborn, and possibly others.

## What You Will Learn

We hope to learn how to create attractive websites and present data in a format that's easily digestible. In addition, we hope to forecast the future of this interaction between weather and Californian plant species using machine learning models, or provide an Agent Based Model with this data.


## Risks

A risk that we may encounter stems from the fact that ecological systems are often challenging to predict due to their multifaceted data. There are many variables that go into the growth of an organism, meaning there are also many variables that can affect plant growth which may skew the predictions. This will become especially apparent with any models or forecasts we may run, whether it be through regression or agent-based modeling.

## Ethics

The effect humans have on the climate and ecological systems is important to many. There are many organizations and activists whom advocate for government officials to reduce the harm we cause. Providing data and information on the further damage that climate change can have may provide more support to make an environmental difference. 

Those who may appeal to further work and analysis in climate change are companies that produce the most environmental harm. If government officials decide to place in more regulations on, for example, the waste companies produce, those companies will be financially hurt.

### Some thoughts that may question the ethics of our project:

- What is the possibility for someone looking at a website gets the wrong idea?
    - Maybe our data somehow strengthens another's thoughts against the concept of climate change? 
- Are our data sources ethical in the first place? 
    - Is our data complete and uniform in coverage? Are any geographic areas or groups of people (or organisms) underrepresented? 
- If we choose to use models, what is the cost of making errors in future forcasting?

## Tentative Timeline

### After two weeks
- As a team we will search online and retrieve data on weather and plant growth in California. Specifically, data on precipitation and temperature at differing stations, as well as, amount of native or non-native plants were observed in differing parts of California.
- Clean the data.
- Input the dataframes into a database.

### After four weeks
- Continue searching for additional data on weather in California, further clean dataframes if necsessary.
- Jovy will set up the website, input/update any additional dataframes into the database, create visualizations.


### After six weeks
- We hope to already have a pretty detailed analysis of our data and it's implications. The website should contain interactive plots and have a nice presentable theme.
