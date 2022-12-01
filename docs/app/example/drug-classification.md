# Drug Classification App

<img class="screenshot" src="../../../screenshots/drug-classification.gif">

## Background

This tutorial will show you how to build a simple app using drug classification data. The app will allow you to interactively explore the relationship between drug and Sodium/Potassium ratio and age of recipient. The app includes both a visualisation and a table, along with dropdown filters which allow you to select a subset of drugs and a minimum Sodium/Potassium ratio.

## Requirements

{!app/example/include-requirements.md!}

## Tutorial

Initialise the Low Code Assistant™.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-initialise.png">

Use the Low Code Assistant™ to load the drug classification data.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-load-data.png">

Use the Low Code Assistant™ to create a visualization. Flip the _Enable crossfilter_ toggle so that the visualization will become responsive to crossfilters. Click the <span class="blue-button">INSERT CODE</span> button.


<img class="screenshot" src="../../../screenshots/app-example-drug-classification-create-visualization.png">

The code will be inserted into the notebook and immediately executed to create the visualization.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-visualization-inserted.png">

Use the Low Code Assistant™ to create a crossfilter. We'll create a filter which will allow us to select one or more drug classes. Flip the _Multiple_ toggle to ensure that more than one option can be selected. Click the <span class="blue-button">INSERT CODE</span> button.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-create-crossfilter-drug.png">

Create a second crossfilter. This time choose a _Slider_ filter and select the `Na_to_K` column. Change the _Mode_ to `>=`. Click the <span class="blue-button">INSERT CODE</span> button.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-create-crossfilter-slider.png">

The code for both of the crossfilters will now be present in the notebook. Use the crossfilters to change the appearance of the visualization.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-crossfilter-inserted.png">

Use the Low Code Assistant™ to create an app. Select, move and resize widgets until you have the required layout. Click the <span class="blue-button">INSERT CODE</span> button.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-create-app.png">

The code will be inserted into the notebook. Click the <span class="blue-button">PREVIEW</span> button.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-app-inserted.png">

A preview version of the app will be launched.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-app-preview-default.png">

Use a crossfilter to select a subset of drug classes.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-app-preview-class.png">

Use a crossfilter to vary the lower cutoff for the `Na_to_K` column.

<img class="screenshot" src="../../../screenshots/app-example-drug-classification-app-preview-slider.png">