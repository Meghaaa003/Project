from flask import Flask, render_template_string
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.figure_factory as ff


app = Flask(__name__)

# Load and process data
df = pd.read_csv(r'C:\Desktop\majproj\Vehicle-Alert-Data-Analytics-main\data\iraste_nxt_cas.csv')
df1 = pd.read_csv(r'C:\Desktop\majproj\Vehicle-Alert-Data-Analytics-main\data\iraste_nxt_casdms.csv')
df = pd.concat([df, df1], axis=0)
df = df.drop_duplicates()
df = df.dropna()
df = df.sample(frac=0.01, random_state=42)

@app.route('/')
def home():
    # DataFrame summary
    summary = df.describe(include='all').to_html(classes='dataframe', border=0)

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vehicle Alert Dashboard</title>
        <style>
            /* Basic Reset */
            body, h1, h2, p, ul {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            /* Body Styling */
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f9f9f9;
                color: #333;
                line-height: 1.6;
            }

            /* Container for center alignment */
            .container {
                width: 90%;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }

            /* Header Styling */
            header {
                background-color: #f0eceb;
                color: #3e3d3d;
                padding: 20px;
                text-align: center;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px; /* Space below header */
            }

            header h1 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }

            header p {
                font-size: 1.1em;
                color: #707070;
            }

            /* Navigation Styling */
            nav {
                margin: 30px 0;
                display: flex;
                justify-content: space-around;
                background-color: #eef2f3;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }

            nav ul {
                list-style: none;
                display: flex;
                gap: 20px;
                padding: 0;
            }

            nav ul li a {
                text-decoration: none;
                font-size: 1.1em;
                color: #4e4e4e;
                padding: 10px 20px;
                border-radius: 5px;
                transition: background-color 0.3s ease, color 0.3s ease;
            }

            nav ul li a:hover {
                background-color: #c7ecee;
                color: #2d3436;
            }

            /* Section Styling */
            section {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                margin-bottom: 30px; /* Space below section */
            }

            section h2 {
                font-size: 1.8em;
                color: #34495e;
                margin-bottom: 15px;
            }

            /* Table Styling */
            .dataframe {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 1em;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }

            .dataframe th, .dataframe td {
                padding: 10px;
                text-align: left;
                border: 1px solid #ddd;
            }

            .dataframe th {
                background-color: #f2f2f2;
                color: #333;
            }

            .dataframe tr:nth-child(even) {
                background-color: #f9f9f9;
            }

            /* Modal Styles */
            .modal {
                display: none; /* Hidden by default */
                position: fixed; /* Stay in place */
                z-index: 1; /* Sit on top */
                left: 0;
                top: 0;
                width: 100%; /* Full width */
                height: 100%; /* Full height */
                overflow: auto; /* Enable scroll if needed */
                background-color: rgba(0, 0, 0, 0.7); /* Black w/ opacity */
            }

            .modal-content {
                background-color: #fff;
                margin: 15% auto; /* 15% from the top and centered */
                padding: 20px;
                border: 1px solid #888;
                width: 70%; /* Could be more or less, depending on screen size */
                border-radius: 10px;
                box-shadow: 0px 6px 16px rgba(0, 0, 0, 0.1);
            }

            .close {
                color: #aaa;
                float: right;
                font-size: 28px;
                font-weight: bold;
            }

            .close:hover,
            .close:focus {
                color: #333;
                text-decoration: none;
                cursor: pointer;
            }

            /* Footer Styling */
            footer {
                text-align: center;
                padding: 20px;
                background-color: #eef2f3;
                color: #636e72;
                margin-top: 40px; /* Space above footer */
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                position: relative;
                clear: both; /* Ensure footer is below floated elements */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Vehicle Alert Data Dashboard</h1>
                <p>A comprehensive view of vehicle alerts and their insights. Visualize and understand alert patterns, speed analysis, and more.</p>
            </header>

            <nav>
                <ul>
                    <li><a href="/heatmap">Heatmap</a></li>
                    <li><a href="/alert-frequency">Alert Frequency</a></li>
                    <li><a href="/speed-analysis">Speed Analysis</a></li>
                    <li><a href="/correlation_analysis">Correlation Analysis</a></li>
                    <li><a href="/driver-behavior">Driver Behavior Analysis</a></li>
                </ul>
            </nav>

            <section>
                <h2>Data Summary</h2>
                {{ summary|safe }}
            </section>

            <section>
                <h2>Dashboard Features</h2>
                <ul>
                    <li><strong>Interactive Heatmaps</strong>: Visualize alert occurrences across different locations.</li>
                    <li><strong>Frequency Analysis</strong>: Understand alert patterns and frequencies over time.</li>
                    <li><strong>Speed Analysis</strong>: Examine vehicle speed trends and related alerts.</li>
                    <li><strong>Correlation Insights</strong>: Explore relationships between various factors impacting alerts.</li>
                    <li><strong>Driver Behavior Analysis</strong>: Assess driver behavior based on alert types.</li>
                </ul>
            </section>

            <!-- Modal Structure -->
            <div id="plotModal" class="modal">
                <div class="modal-content">
                    <span class="close">&times;</span>
                    <div id="modalPlot"></div>
                </div>
            </div>

            <footer>
                <p>&copy; 2024 Vehicle Alert Dashboard. All Rights Reserved.</p>
            </footer>
        </div>

        <script>
            // Modal functionality
            var modal = document.getElementById("plotModal");
            var span = document.getElementsByClassName("close")[0];

            span.onclick = function() {
                modal.style.display = "none";
            }

            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                }
            }
        </script>
    </body>
    </html>
    ''', summary=summary)



@app.route('/heatmap')
def heatmap():
    fig = px.density_mapbox(df, lat='Lat', lon='Long', radius=10, zoom=5, mapbox_style='carto-positron',
                            title='Spatial Distribution of Alert Occurrences')
    fig.update_layout(mapbox_center={'lat': df['Lat'].mean(), 'lon': df['Long'].mean()})

    html = pio.to_html(fig, full_html=False)
    return render_template_string('''<h1>Heatmap</h1>{{ plot|safe }}<br><a href="/">Back to Home</a>''', plot=html)

@app.route('/alert-frequency')
def alert_frequency():
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract day of the week from the 'Date' column
    df['DayOfWeek'] = df['Date'].dt.day_name()

    # Count occurrences by day of the week
    freq_data = df['DayOfWeek'].value_counts().reset_index()
    freq_data.columns = ['Day', 'Frequency']

    fig = px.bar(freq_data, x='Day', y='Frequency', title='Alert Frequency by Day of the Week',
                  color='Frequency', labels={'Frequency': 'Number of Alerts'})
    html = pio.to_html(fig, full_html=False)
    return render_template_string('''<h1>Alert Frequency</h1>{{ plot|safe }}<br><a href="/">Back to Home</a>''', plot=html)

@app.route('/speed-analysis')
def speed_analysis():
    fig = px.histogram(df, x='Speed', nbins=30, title='Vehicle Speed Distribution',
                       labels={'Speed': 'Speed (km/h)', 'count': 'Number of Vehicles'})
    html = pio.to_html(fig, full_html=False)
    return render_template_string('''<h1>Speed Analysis</h1>{{ plot|safe }}<br><a href="/">Back to Home</a>''', plot=html)

@app.route('/correlation_analysis', methods=['GET', 'POST'])


@app.route('/correlation_analysis', methods=['GET'])
def correlation_analysis():
    # Select only numeric columns from the DataFrame
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Calculate the correlation matrix for numeric columns
    correlation_matrix = numeric_df.corr()

    # Create the annotated heatmap
    fig = ff.create_annotated_heatmap(correlation_matrix.values, 
                                       x=list(correlation_matrix.columns), 
                                       y=list(correlation_matrix.columns))

    # Show the figure as HTML
    graph_html = fig.to_html(full_html=False)
    return graph_html

@app.route('/driver-behavior')
def driver_behavior():
    # Use the 'Alert' column to analyze driver behavior
    behavior_counts = df['Alert'].value_counts()
    
    fig = px.pie(behavior_counts, values=behavior_counts.values, names=behavior_counts.index, 
                 title='Driver Behavior Analysis')
    html = pio.to_html(fig, full_html=False)
    return render_template_string('''<h1>Driver Behavior Analysis</h1>{{ plot|safe }}<br><a href="/">Back to Home</a>''', plot=html)



if __name__ == '__main__':
    app.run(debug=True)
