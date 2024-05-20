

# Flask Data Visualization App

This is a simple Flask web application that reads data from a CSV file and displays it in a table format on the homepage. Additionally, it provides a bar graph visualization of the data on a separate page using Plotly.

# Screenshots
<div style="text-align: center;">
<img src="/screenshots/data_graph.png" alt="Graph" width="300"/>  <img src="/screenshots/data_table.png" alt="Table" width="300"/>
</div>




## Project Structure

```
myproject/
├── app.py
├── graph.data.csv
├── templates/
│   ├── base.html
│   ├── index.html
│   └── graph.html
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
    pip install Flask pandas plotly
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

## Data File

The application reads data from `graph.data.csv`. Make sure your CSV file is structured correctly. Here's an example structure for `graph.data.csv`:

```csv
Name,Age,Country,Score
Alice,30,USA,85
Bob,25,Canada,90
Charlie,35,UK,78
David,28,Australia,88
Eve,22,India,92
Frank,33,Germany,75
Grace,27,Japan,80
Hannah,31,China,95
Ian,29,France,82
Judy,26,Brazil,87
```

## Templates

- `base.html`: The base template that includes the navbar, hero section, and footer.
- `index.html`: Inherits from `base.html` and displays the data table.
- `graph.html`: Inherits from `base.html` and displays the data graph.

## Static Files

- `styles.css`: Custom styles for the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

