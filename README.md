# California Climate and Flowering Phenology - PIC16B Final Project

To deploy this webapp locally, first download github desktop and sign in. Then, clone my repository by adding this link in the URL "https://github.com/ianmorris13/weathervsphenology". Once that is cloned, make sure you have three important python packages: pandas, flask, and plotly. The vesions for each that I have and run fine are flask==2.0.2, pandas==1.3.5, plotly==5.1.0, and my python version is python==3.8.12. You should then open up this repository in a terminal. One easy way to do this is by simply right clicking the repository and clicking open in terminal. Once in the terminal run "$ export FLASK_ENV=development; flask run" and from there the webapp should be open in http://localhost:5000


You can see this app online at https://climatevsphenology.herokuapp.com/. However, for some reason that I could never figure out (though it is probably a very silly reason my end), it will not work for the 'Climate Visualizations' page. Because of that, I do not consider it part of my project, it was just something more that I wish could have happened.
 
## Webapp
 
The main goal of this webapp was to see the effect the changing California climate has on flowering phenology of California plant species. We did not get that far as of yet (03/18/22). Instead we currently have our own aggregated database that the user can query parameters and receive visualizations of this data. Eventually, this will turn out into its intended form. However for now, this will just give a glimpse on how the climate and flowering phenology are changing from 2000-2020 independently of one another.
 
Our webapp has three main pages, Plant Distribution of California, Average Flowering Day of Year, and Climate Visualizations. They are all user interactable and pull from the data sources iNaturalist and SC ACIS. iNaturalist provides an aggregated database of both professional and citizen science species observations. We pulled 11 species and cleaned the databases to fix our functions. More info on that can be seen in our DataCleaning.ipynb on the main repository page. As for our climate data, SC ACIS is a sub-team of NOAA, in which they aggregate differing weather station data to provide a robust database of the weather stations across the US. More info on how we cleaned it is also available in our DataCleaning.ipynb on the main repository page.
 
### Plant Distribution of California
 
This page shows all our observations over a map of California, so the user can visualize the distribution of these species. Each species is color coded and their coordinates and name are revealed with a simple hover. The user can input whether they want to see all species, only native species, or only non-native species. They can also specify the climate division and year range they want to see observations for.
 
### Average Flowering Day of Year
 
This page will show the average flowering day of year of a scatter plot, so the user can see any trends that may occur within or across species. Once again the species are color coded and the user can input whether they want to see all species, only native species, or only non-native species. They can also specify the climate division and year range they want to see observations for. However, one thing to note is they can also choose a linear or local regression trendline if they prefer. This may improve any difficulty reading trends.
 
### Climate Visualizations
 
This page will allow the user to visualize climate trends of average temperature and average monthly precipitation for the different climate divisions. By default, all divisions are shown and the trendline shows linear regression across all averages. The user can choose which climate division they may want to focus on. Additionally, there is a gradient coloring of each plot point showing how the temperature and precipitation may affect each other. Something to note is that it is less often a negative correlation than one may think.
 
## Limitations
 
Like stated before, this project did not go as far as originally intended. While this project does show data in an easy to digest way, someone who is less informed on these subjects may interpret them unprofessionally, and come to a conclusion that is actually the opposite of what I am trying to convey with this project. Additionally, there is empty data for some of these species, so some are overrepresented while others are underrepresented. This is another way someone may be misled by this project, and come to an inaccurate conclusion. I hope to include more data in the future to prevent this. I also hope to have better stats that convey thoughtful analytics in which I can present on top of the current appealing visualizations.

One last limitation is that there are biases within iNaturalist. There is a disproportional amount of observations within high income neighborhoods, so this has skewed the data. For now, I hope to find other databases that aren't as skewed.