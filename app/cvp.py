# first in terminal, make sure you are in the correct folder of the whole repository
# then make you have all necesary packages (anything under from/ import)
# Then, in terminal run $ export FLASK_ENV=development; flask run
# site will then be available at 
# http://localhost:5000

from flask import Flask, render_template, request
import pandas as pd
from plotly import express as px

flowersCA = pd.read_csv('./data/flowersCA.csv')
averages  = pd.read_csv('./data/averages.csv')

def flowersOverCA (startYear = 2000, endYear = 2020, nativeInfo = False, div = False):
    '''
    Will give a vizualization of all observations over years for species 
    of specified parameters based on user input.
    
    @param startYear: the first year wanted in the visualization
    @param endYear: the last year wanted in the visualization
    @param nativeInfo: whether the species are non native, native, or all. default is all
    @param div: which climate division to look at. default is all
    @return fig: the figure of the visualization itself, ready for any other modification
    '''

    #make copy of dataframe as to not modify original
    flowers = flowersCA
    
    if div:
        #if climate division specified, only get those from there
        flowers = flowers[flowers['ClimateDivision'] == div]

    if nativeInfo:
        #if type of flower specified, only get those of that type
        flowers = flowers[flowers['native'] == nativeInfo]

    #make sure all observations are within the specified dates
    flowers = flowers[flowers['year'] >= startYear]
    flowers = flowers[flowers['year'] <= endYear]
    
    #plot  
    fig = px.scatter_mapbox(flowers, lat="latitude", lon="longitude",  color="species", zoom=3, height=600)
    
    #make easier to see and center on california
    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=4, mapbox_center_lat = 41,
        margin={"r":0,"t":0,"l":0,"b":0})

    return fig

def avgFloweringByYear (startYear = 2000, endYear = 2020, nativeInfo = False, trendline = None, trendline_scope= False, div = False):
    '''
    Will give a vizualization of the average flowering day of years for species 
    of specified parameters based on user input.
    
    @param startYear: the first year wanted in the visualization
    @param endYear: the last year wanted in the visualization
    @param nativeInfo: whether the species are non native, native, or all. default is all
    @param trendline: the type of trendline for each data point. default is none
    @param trendline_scope: whether or not the trendline should be based off individual species or all. default is individual
    @param div: which climate division to look at. default is all
    '''

    #make all numbers ints for comparisons   
    startYear = int(startYear)
    endYear = int(endYear)
    
    #empty strings to be filled based on conditionals      
    ntv = ''
    divNum = ''
    
    if div:
        #if div is specified, take data from dataframe including climatedivision
        l = ['species', 'year', 'native', 'ClimateDivision']
        #find average flowering day of year
        avg_df = flowersCA.groupby(l)["DOY"].mean().reset_index().round(0)
        #make sure its in specified climate division
        avg_df = avg_df[avg_df['ClimateDivision'] == div]
        #add division to title
        divNum = f'0{div}'
    else:
        #else take average flowering day regardless of climate division
        l = ['species', 'year', 'native']
        avg_df = flowersCA.groupby(l)["DOY"].mean().reset_index().round(0)
        
    if nativeInfo:
        #if native or non native specified, only take data of that type
        avg_df = avg_df[avg_df['native'] == nativeInfo]
        #ajust title accordingly
        if nativeInfo == 'yes':
            ntv = "Native "
        else:
            ntv = 'Non-Native '
            
    #make sure observation are of the specified years
    avg_df = avg_df[avg_df['year'] >= startYear]
    avg_df = avg_df[avg_df['year'] <= endYear]

    #update title    
    title = f"Average {ntv}Flowering Day of Year in CA{divNum} from {startYear}-{endYear}"

    #plot   
    if trendline_scope:
        fig =px.scatter(avg_df,
                        x = "year",
                        y = "DOY",
                        color = 'species',
                        trendline = trendline,
                        trendline_scope = trendline_scope,
                        title = title)
    else:
        fig =px.scatter(avg_df,
                        x = "year",
                        y = "DOY",
                        color = 'species',
                        trendline = trendline,
                        title = title)
    return fig

def divScatterTemp (climatediv = False):
    '''
    Returns a figure of the average temperature in California from 2000-2020 
    based on the users climate division preference
    
    @param climatediv: the climate division the user prefers to see, the default is all climate divisions in the state
    @return fig: a figure of said climate division's mean temperature over the years
    '''

    #if climate division specified only take data from that division    
    if climatediv:
        avgDf = averages[averages['ClimateDivision'] == climatediv]
        title = f'Average Temperature of CA0{climatediv} from 2000-2020'
        
    else:
        avgDf = averages
        title = 'Average Temperature of California from 2000-2020'

    #plot
    fig =px.scatter(avgDf,
                    x = "Year",
                    y = "MeanAvgTemperature",
                    trendline = "ols",
                    color = 'AvgMonthlyPrecipitation',
                    title = title)
    return fig

def divScatterPrecip (climatediv = False):
    '''
    Returns a figure of the average monthly precipitation in Californian weather stations from 2000-2020 
    based on the users climate division preference
    
    @param climatediv: the climate division the user prefers to see, the default is all climate divisions in the state
    @return fig: a figure of said climate division's mean monthly precipitation over the years
    '''

    #if climate division specified only take data from that division
    if climatediv:
        avgDf = averages[averages['ClimateDivision'] == climatediv]
        title = f'Average Monthly Precipitation of CA0{climatediv} California from 2000-2020'
        
    else:
        avgDf = averages
        title = 'Average Monthly Precipitation of California from 2000-2020'
    
    #plot
    fig = px.scatter(avgDf,
                    x = "Year",
                    y = "AvgMonthlyPrecipitation",
                    trendline = "ols",
                    color = 'MeanAvgTemperature',
                    title = title)
    return fig

app = Flask(__name__)

@app.route('/')

def main():
    return render_template('about.html')

@app.route('/plantDistribution/', methods=['POST', 'GET'])
def plantDistribution():
    if request.method == 'GET':
        flowersOverCA().write_html('./app/templates/distributionPlot.html')
        start_year = 2000
        end_year = 2000
        return render_template('plantDistribution.html', startYear = start_year, endYear = end_year)
    else:
        plant_type = request.form.get('plant_type')

        if not request.form.get('start_year'):
            start_year = 2000
        else:
            start_year = int(float(request.form.get('start_year')))

        if not request.form.get('end_year'):
            end_year = 2020
        else:
            end_year = int(float(request.form.get('end_year')))

        if not request.form.get('_div'):
            _div =  request.form.get('_div')
        else:
            _div =  int(float(request.form.get('_div')))


        flowersOverCA(startYear = start_year, endYear = end_year, nativeInfo = plant_type, div = _div).write_html('./app/templates/distributionPlot.html')

        if plant_type == 'yes':
            plant_type = 'native'
        elif plant_type == 'no':
            plant_type = 'non-native'         

        return render_template('plantDistribution.html', startYear = start_year, endYear = end_year, nativeInfo = plant_type, div = _div)

@app.route('/avgFlowering/', methods=['POST', 'GET'])
def avgFlowering():
    if request.method == 'GET':
        avgFloweringByYear().write_html('./app/templates/avgDOYplot.html')
        start_year = 2000
        end_year = 2020

        return render_template('avgFlowering.html', startYear = start_year, endYear = end_year)

    else:

        plant_type = request.form.get('plant_type')
        tline = request.form.get('tline')
        scope = request.form.get('scope')

        if not request.form.get('start_year'):
            start_year = 2000
        else:
            start_year = int(float(request.form.get('start_year')))

        if not request.form.get('end_year'):
            end_year = 2020
        else:
            end_year = int(float(request.form.get('end_year')))

        if not request.form.get('_div'):
            _div =  request.form.get('_div')
        else:
            _div =  int(float(request.form.get('_div')))

        avgFloweringByYear(startYear = start_year, endYear = end_year, nativeInfo = plant_type, trendline = tline, trendline_scope= scope, div = _div).write_html('./app/templates/avgDOYplot.html')

        if plant_type == 'yes':
            plant_type = 'native'
        elif plant_type == 'no':
            plant_type = 'non-native'

        return render_template('avgFlowering.html', startYear = start_year, endYear = end_year, nativeInfo = plant_type, div = _div)

@app.route('/climate_plots/', methods=['POST','GET'])
def climate_plots():
    if request.method == 'GET':
        divScatterTemp().write_html('./app/templates/avgTempPlot.html')
        divScatterPrecip().write_html('./app/templates/avgRainPlot.html')
        return render_template('climate_plots')
    else:
        if not request.form.get('_div'):
            _div =  request.form.get('_div')
        else:
            _div =  int(float(request.form.get('_div')))

        divScatterTemp(_div).write_html('./app/templates/avgTempPlot.html')
        divScatterPrecip(_div).write_html('./app/templates/avgRainPlot.html')    
    return render_template('climate_plots')

@app.route('/species/', methods=['GET'])
def species():
    return render_template('species')    

if __name__ == "__main__":
    app.run(debug==True)