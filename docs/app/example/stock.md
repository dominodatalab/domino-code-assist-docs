# Stock App

<img class="screenshot" src="../../../screenshots/stocks.gif">

## Background

This tutorial will show you how to build a simple app using stock price data. The app will allow you to interactively explore the stock prices for Apple (AAPL), Facebook (FB) and Google (GOOGL) versus time. The app includes both a visualisation and a table, along with a dropdown filter which allows you to select a subset of the stocks.

## Requirements

{!app/example/include-requirements.md!}

## Tutorial


Initialise the Low Code Assistant™.

<img class="screenshot" src="../../../screenshots/app-example-stock-initialise.png">

Use the Low Code Assistant™ to load the stocks data. The data consists of daily stock prices for three ticker symbols (AAPL, FB and GOOGL).

<img class="screenshot" src="../../../screenshots/app-example-stock-load-data.png">

Use the Low Code Assistant™ to create a visualization. Flip the _Enable crossfilter_ toggle so that the visualization will become responsive to crossfilters. Click the <span class="blue-button">INSERT CODE</span> button.

<img class="screenshot" src="../../../screenshots/app-example-stock-create-visualization.png">

The code will be inserted into the notebook and immediately executed to create the visualization.

<img class="screenshot" src="../../../screenshots/app-example-stock-visualization-inserted.png">

Use the Low Code Assistant™ to create a crossfilter. We'll create a filter which will allow us to select one or more ticker symbols. Flip the _Multiple_ toggle to ensure that more than one option can be selected. Click the <span class="blue-button">INSERT CODE</span> button.

<img class="screenshot" src="../../../screenshots/app-example-stock-create-crossfilter.png">

The code will be inserted into the notebook and immediately executed to create the crossfilter. Try making various selections and observe the effect that they have on the visualization.

<img class="screenshot" src="../../../screenshots/app-example-stock-crossfilter-inserted.png">

Use the Low Code Assistant™ to create an app. Select, move and resize widgets until you have the required layout. Click the <span class="blue-button">INSERT CODE</span> button.

<img class="screenshot" src="../../../screenshots/app-example-stock-create-app.png">

The code will be inserted into the notebook. Click the <span class="blue-button">PREVIEW</span> button.

<img class="screenshot" src="../../../screenshots/app-example-stock-app-inserted.png">

A preview version of the app will be launched with all of the tickers selected by default.

<img class="screenshot" src="../../../screenshots/app-example-stock-preview-default.png">

Use the crossfilter to change the selected tickets. Observe the effect on the visualization and table.

<img class="screenshot" src="../../../screenshots/app-example-stock-preview-selected.png">

Now we're going to use the Prophet package to build a simple time series model for predicting future stock prices. First install the package.

```
!pip install prophet
```

Then import the package and reduce the level of logging.

```python
from prophet import Prophet

import logging
#
logging.getLogger('prophet').setLevel(logging.WARNING)
logging.getLogger('cmdstanpy').setLevel(logging.WARNING)
```

<img class="screenshot" src="../../../screenshots/app-example-stock-install-prophet.png">

Now prepare the data for Prophet, which expects the time column to be called `ds` and the value column to be called `y`. We'll be building a separate model for each ticker, so we'll group the data by `ticker`.

```python
df.rename(columns={"date": "ds", "close": "y"}, inplace=True)
df = df[["ticker", "ds", "y"]].groupby('ticker')
```

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-prepare-data.png">

Now create a function which will build a model and create predictions for a single ticker. Then apply that function to all of the tickers. The results are stored in a list of `DataFrame` objects.

```python
def train_and_forecast(ticker):
  m = Prophet(yearly_seasonality=False, weekly_seasonality=False)
  
  m.fit(ticker)
  future = m.make_future_dataframe(periods=365, include_history=False)
  forecast = m.predict(future)[['ds', 'yhat']]
  forecast['ticker'] = ticker['ticker'].iloc[0]
  
  return forecast[['ticker', 'ds', 'yhat']]

stocks_forecast = []

for ticker in ['AAPL', 'FB', 'GOOGL']:
    ticker = df.get_group(ticker)
    forecast = train_and_forecast(ticker)
    stocks_forecast.append(forecast)
```

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-create-models.png">

Now concatenate the predictions for all of the tickers. Then add a `future` column which indicates that these are predictions.

```python
stocks_forecast = pd.concat(stocks_forecast)

stocks_forecast.rename(columns={"yhat": "y"}, inplace=True)

stocks_forecast.insert(0, "future", 1)

stocks_forecast.loc[:,"ds"] = stocks_forecast["ds"].dt.strftime('%Y-%m-%d')
```

Use the `head()` method to check on the data.

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-prepare-predictions.png">

Prepare the original data so that it has a consistent format and then concatenate the original data and predictions.

```python
df = df[["ticker", "ds", "y"]]

df = df.obj
df.insert(0, "future", 0)

df = pd.concat([df, stocks_forecast])

df = df.sort_values(by=["ticker", "ds"])
```

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-update-data.png">

Create a new visualisation.

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-visualisation.png">

Create a crossfilter widget to select values from the `future` column.

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-filter.png">

Create an app which includes the new visualisation, a data table and both crossfilter widgets.

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-app.png">

Preview the app. Use the filter on `future` to choose whether to plot the original data, predictions or both.

<img class="screenshot" src="../../../screenshots/app-example-stock-prophet-app-preview.png">