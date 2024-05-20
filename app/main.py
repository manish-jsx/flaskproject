from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

port = int(os.environ.get('PORT', 10000))  # Adjusted the default port

@app.route('/')
def index():
    # Load CSV data
    data = pd.read_csv('data.csv')
    # Convert to HTML table
    data_html = data.to_html(classes='table table-striped', index=False)
    return render_template('index.html', data=data_html)

@app.route('/graph')
def graph():
    # Load CSV data
    data = pd.read_csv('graph.csv')
    
    # Create a plotly figure
    fig = px.bar(data, x='Country', y='Score', title='Sample Data Visualization')
    graph_html = fig.to_html(full_html=False)
    
    return render_template('graph.html', graph=graph_html)

if __name__ == '__main__':
    app.run()
