
# Flask Data Visualization App

This is a simple Flask web application that reads data from a CSV file and displays it in a table format on the homepage. Additionally, it provides a bar graph visualization of the data on a separate page using Plotly.

## Screenshots

<div style="text-align: center;">
    <img src="/screenshots/data_graph.png" alt="Graph" width="300"/>  
    <img src="/screenshots/data_table.png" alt="Table" width="300"/>
</div>

## Project Structure

```
myproject/
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── graph.html
│   │   └── index.html
│   └── wsgi.py
├── data.csv
├── graph.csv
├── requirements.txt
├── screenshots/
│   ├── data_graph.png
│   └── data_table.png
└── static/
    └── css/
        └── styles.css
```

## Requirements

- Python 3.7+
- Flask
- pandas
- plotly

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/myproject.git
    cd myproject
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    flask run
    ```

2. **Open your web browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

## Application Features

### Homepage

- Displays the CSV data in a table format.
- Provides a link to view the data visualization.

### Graph Page

- Displays a bar graph visualization of the data using Plotly.

## Data Files

The application reads data from `data.csv` and `graph.csv`. Make sure your CSV files are structured correctly. Here's an example structure for `graph.csv`:

```csv
Country,Score
USA,85
Canada,90
UK,78
Australia,88
India,92
Germany,75
Japan,80
China,95
France,82
Brazil,87
```

## Templates

- `base.html`: The base template that includes the navbar, hero section, and footer.
- `index.html`: Inherits from `base.html` and displays the data table.
- `graph.html`: Inherits from `base.html` and displays the data graph.

## Static Files

- `styles.css`: Custom styles for the application.

## Deployment on Render

To deploy this application on Render, follow these steps:

1. **Create a `requirements.txt` file:**
    ```bash
    pip freeze > requirements.txt
    ```

2. **Create a `render.yaml` file** in the root of your project:
    ```yaml
    services:
    - type: web
        name: my-flask-app
        env: python
        region: oregon
        plan: free
        buildCommand: pip install -r requirements.txt
        startCommand: gunicorn app.wsgi:app


    ```

3. **Push your code to a GitHub repository.**

4. **Create a new Web Service on Render:**
    - Go to [Render](https://render.com/).
    - Click on the "New" button and select "Web Service".
    - Connect your GitHub repository.
    - Use the settings from your `render.yaml` file.

5. **Deploy the service.**

6. **Access your deployed application.**





### Updated Code Files

#### `app/main.py`

```python
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
```

#### `app/wsgi.py`

```python
from app.main import app

if __name__ == "__main__":
    app.run()
```

#### `app/__init__.py`

```python
# This file is intentionally left blank.
```
