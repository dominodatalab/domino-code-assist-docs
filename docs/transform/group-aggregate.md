# Grouping & Aggregating

For this tutorial we'll use the _Titanic_ data.

=== "Python"

    Hover over the <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png"> icon. Select the _Transformations_ item from the popup menu. Select the _Groupby and aggregate_ option.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate.png">

    We are going to calculate some summary statistics for the `Fare` column broken down by `Pclass`. Specify `Pclass` as the column to group by. Choose `Fare` as the column to aggregate. Select `mean` as the aggregator function.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-mean.png">

    You can include more aggregations. We'll add in `min` and `max`. Press the <span class="white-button-blue-text">Add Transformation</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-more-aggregations.png">

    The preview will be updated with the summary data. Press the <span class="blue-button">Insert Code</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-preview.png">

    The required code will be inserted into the notebook and immediately executed.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-insert-code.png">

=== "R"