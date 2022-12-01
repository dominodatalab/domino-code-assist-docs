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