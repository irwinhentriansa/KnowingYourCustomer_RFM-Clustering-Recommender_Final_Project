from flask import Flask, render_template, jsonify, request
import joblib
from sklearn.metrics.pairwise import cosine_similarity
# import pandas as pd
import json

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('Cluster_home.html')

@app.route('/data_visualization')
def data_visualization():
    return render_template('Cluster_datavisualization.html')

@app.route('/dataset')
def dataset():
    return render_template('Cluster_tables.html')

@app.route('/model')
def model():
    return render_template('Cluster_model.html')

if __name__ == '__main__':
    # countmatrix = joblib.load('CVJoblib') 
    # df = pd.read_csv('dfcleaned.csv')
    # dfNFRec = pd.read_csv('dfNFRec.csv')
    app.run(debug=True)