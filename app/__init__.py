# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from tracemalloc import start
from flask import Flask, g, render_template, request

import pandas as pd
import os
from plotly import express as px
import plotly.graph_objects as go

flowersCA = pd.read_csv('./data/flowersCA.csv')

def flowersOverCA (startYear = 2000, endYear = 2020, nativeInfo = False, div = False):

    flowers = flowersCA
    
    if div:
        flowers = flowers[flowers['Div'] == div]

    if nativeInfo:
        flowers = flowers[flowers['native'] == nativeInfo]

    flowers = flowers[flowers['year'] >= startYear]
    flowers = flowers[flowers['year'] <= endYear]
    
    fig = px.scatter_mapbox(flowers, lat="latitude", lon="longitude",  color="species", zoom=3, height=600)

    fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=4, mapbox_center_lat = 41,
        margin={"r":0,"t":0,"l":0,"b":0})

    return fig

def avgFloweringByYear(startYear = 2000, endYear = 2020, nativeInfo = False, trendline = None, trendline_scope= False, div = False):
    
    startYear = int(startYear)
    endYear = int(endYear)
    ntv = ''
    
    if div:
        l = ['species', 'year', 'native', 'Div']
        avg_df = flowersCA.groupby(l)["DOY"].mean().reset_index().round(0)
        avg_df = avg_df[avg_df['Div'] == div]
    else:
        l = ['species', 'year', 'native']
        avg_df = flowersCA.groupby(l)["DOY"].mean().reset_index().round(0)

    
    if nativeInfo:
        avg_df = avg_df[avg_df['native'] == nativeInfo]
        if nativeInfo == 'yes':
            ntv = "Native "
        else:
            ntv = 'Non-Native '

    if div:
        if div == 'North':
            div = "Northern "
        elif div == 'Central':
            div = 'Central '
        else:
            div = 'Southern '
        
    avg_df = avg_df[avg_df['year'] >= startYear]
    avg_df = avg_df[avg_df['year'] <= endYear]
    
    title = f"Average Flowering Day of {div}Californian {ntv}species from {startYear}-{endYear}"

    if trendline_scope:
        if trendline != 'ols':
            fig = px.scatter(avg_df,
                            x = "year",
                            y = "DOY",
                            color = 'species',
                            trendline = trendline,
                            title  = title
                            )
        else:
            fig = px.scatter(avg_df,
                            x = "year",
                            y = "DOY",
                            color = 'species',
                            trendline = trendline,
                            #trendline_scope = 'overall',
                            title = title)            
    else:
        fig = px.scatter(avg_df,
                         x = "year",
                         y = "DOY",
                         color = 'species',
                         trendline = trendline,
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
    return render_template('main_better.html')

@app.route('/plantDistribution/', methods=['POST', 'GET'])
def plantDistribution():
    if request.method == 'GET':
        return render_template('plantDistribution.html')
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

        _div = request.form.get('_div')

        flowersOverCA(startYear = start_year, endYear = end_year, nativeInfo = plant_type, div = _div).write_html('./app/templates/distributionPlot.html')

        if plant_type == 'yes':
            plant_type = 'native'
        elif plant_type == 'no':
            plant_type = 'non-native'

        return render_template('plantDistribution.html', plot = True, startYear = start_year, endYear = end_year, nativeInfo = plant_type, div = _div)

@app.route('/avgFlowering/', methods=['POST', 'GET'])
def avgFlowering():
    if request.method == 'GET':
        return render_template('avgFlowering.html')

    else:

        if not request.form.get('start_year'):
            start_year = 2000
        else:
            start_year = int(float(request.form.get('start_year')))

        if not request.form.get('end_year'):
            end_year = 2020
        else:
            end_year = int(float(request.form.get('end_year')))

        plant_type = request.form.get('plant_type')
        _div = request.form.get('_div')
        tline = request.form.get('tline')
        scope = request.form.get('scope')


        avgFloweringByYear(startYear = start_year, endYear = end_year, nativeInfo = plant_type, trendline = tline, trendline_scope= scope, div = _div).write_html('./app/templates/avgDOYplot.html')

        if plant_type == 'yes':
            plant_type = 'native'
        elif plant_type == 'no':
            plant_type = 'non-native'

        return render_template('avgFlowering.html', plot = True, startYear = start_year, endYear = end_year, nativeInfo = plant_type, div = _div)

@app.route('/climate_plots/', methods=['GET'])
def climate_plots():
    return render_template('climate_plots')
