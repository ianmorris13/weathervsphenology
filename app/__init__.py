# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run

from flask import Flask, render_template, request

import pandas as pd
from plotly import express as px

flowersCA = pd.read_csv('./data/flowersCA.csv')
averages  = pd.read_csv('./data/averages.csv')

def flowersOverCA (startYear = 2000, endYear = 2020, nativeInfo = False, div = False):
    
    flowers = flowersCA
    
    if div:
        flowers = flowers[flowers['ClimateDivision'] == div]

    if nativeInfo:
        flowers = flowers[flowers['native'] == nativeInfo]

    flowers = flowers[flowers['year'] >= startYear]
    flowers = flowers[flowers['year'] <= endYear]
    
    fig = px.scatter_mapbox(flowers, lat="latitude", lon="longitude",  color="species", zoom=3, height=600)

    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=4, mapbox_center_lat = 41,
        margin={"r":0,"t":0,"l":0,"b":0})

    return fig

def avgFloweringByYear (startYear = 2000, endYear = 2020, nativeInfo = False, trendline = None, trendline_scope= False, div = False):
    
    startYear = int(startYear)
    endYear = int(endYear)
        
    ntv = ''
    divNum = ''
    
    if div:
        l = ['species', 'year', 'native', 'ClimateDivision']
        avg_df = flowersCA.groupby(l)["DOY"].mean().reset_index().round(0)
        avg_df = avg_df[avg_df['ClimateDivision'] == div]
        divNum = f'0{div}'
    else:
        l = ['species', 'year', 'native']
        avg_df = flowersCA.groupby(l)["DOY"].mean().reset_index().round(0)
        
    if nativeInfo:
        avg_df = avg_df[avg_df['native'] == nativeInfo]
        if nativeInfo == 'yes':
            ntv = "Native "
        else:
            ntv = 'Non-Native '
            
        
    avg_df = avg_df[avg_df['year'] >= startYear]
    avg_df = avg_df[avg_df['year'] <= endYear]
    
    title = f"Average {ntv}Flowering Day of Year in CA{divNum} from {startYear}-{endYear}"
    
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
    
    if climatediv:
        avgDf = averages[averages['ClimateDivision'] == climatediv]
        title = f'Average Temperature of CA0{climatediv} from 2000-2020'
        
    else:
        avgDf = averages
        title = 'Average Temperature of California from 2000-2020'
        
    fig =px.scatter(avgDf,
                    x = "Year",
                    y = "MeanAvgTemperature",
                    trendline = "ols",
                    color = 'AvgMonthlyPrecipitation',
                    title = title)
    return fig

def divScatterPrecip (climatediv = False):
    
    if climatediv:
        avgDf = averages[averages['ClimateDivision'] == climatediv]
        title = f'Average Monthly Precipitation of CA0{climatediv} California from 2000-2020'
        
    else:
        avgDf = averages
        title = 'Average Monthly Precipitation of California from 2000-2020'
        
    fig = px.scatter(avgDf,
                    x = "Year",
                    y = "AvgMonthlyPrecipitation",
                    trendline = "ols",
                    color = 'MeanAvgTemperature',
                    title = title)
    return fig


# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)

# Create main page (fancy)

@app.route('/')

# def main():
#     return render_template("main.html")

# comment out the below to focus on just the fundamentals

# after running
# $ export FLASK_ENV=development; flask run
# site will be available at 
# http://localhost:5000

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
