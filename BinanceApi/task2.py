from flask import Flask
from task1 import df
import plotly.graph_objects as go
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

coins = cg.get_coins_markets(vs_currency='usd')  # get data about market caps

task2 = Flask(__name__)


@task2.route('/')  # URL which calls the function index()
def index():
    figure = go.Figure(
        data=[
            go.Candlestick(
                x=df.index,
                low=df['The lowest price'],
                high=df['The highest price'],
                close=df['Close price'],
                open=df['Open price'],
                increasing_line_color='green',
                decreasing_line_color='red'
            )
        ]
    )
    figure.update_layout(
        xaxis_title='Index',
        yaxis_title='Price'
    )

    chart_data = figure.to_html(full_html=False)

    labels = [coin['name'] for coin in coins[:10]]  # Get names of coins
    values = [coin['market_cap'] for coin in coins[:10]]

    # Create piechart
    pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values)])
    pie_chart_data = pie_chart.to_html(full_html=False)

    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Chart</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
            <div>
                <h1>Chart</h1>
                <div id="chart"></div>
                <script>
                    let chartData = {chart_data}
                </script>
            </div>
            <div>
                <h1>Pie Chart</h1>
                <div id="pie_chart"></div>
                <script>
                    let pieChartData = {pie_chart_data}
                </script>
            </div>
        </body>
        </html>
        """


if __name__ == "__main__":
    task2.run(debug=True)
