from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import os
import pickle
import numpy as np

app = Flask(__name__)

# Adjusted the default port
port = int(os.environ.get('PORT', 10000))

# Sample project data
projects = [
    {'id': 1, 'title': 'Student Placement Prediction', 'description': 'Predict if a student will get placed based on their interview feedback and CGPA.'}
]

# Load the pre-trained model
model_path = './model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
else:
    model = None
    print(f"Model file not found at path: {model_path}")

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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project_list():
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:id>', methods=['GET', 'POST'])
def project_detail(id):
    project = next((proj for proj in projects if proj['id'] == id), None)
    if project is None:
        return "Project not found", 404
    
    if request.method == 'POST':
        # Get form data
        if_ = request.form['if']
        cgpa = request.form['cgpa']

        # Convert form data to float and create a feature array
        features = np.array([[float(if_), float(cgpa)]])

        # Predict using the model
        if model is not None:
            prediction = model.predict(features)
            result = 'Placed' if prediction[0] == 1 else 'Not Placed'
        else:
            result = "Model not available"

        # Render the result
        return render_template('result.html', result=result)

    return render_template('project_detail.html', project=project)

if __name__ == '__main__':
    app.run(port=port)
