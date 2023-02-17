# Grouping & Aggregating

For this tutorial we'll use the _Palmer Penguins_ data. We have already filtered out some records wih missing data and selected a subset of columns.

=== "Python"

    This is what the data currently looks like.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-initial-data.png">

    Hover over the <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png"> icon. Select the _Transformations_ item from the popup menu.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-menu.png">

    The transformations widget will open.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-widget.png">

    Select the _Groupby and aggregate_ transformation option.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-select.png">

    Choose one or more columns to group by. These will determine the buckets that the results are allocated to. Generally you'll want to select columns with discrete values.
    
    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-grouping-variables.png">

    Choose the column to aggregate. Generally you'll want to select a column with numeric values.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-aggregate-variable.png">

    Select an aggregation function.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-aggregate-function.png">

    You can add more aggregations. It's not necessary to choose the same column to aggregate.
    
    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-other-aggregates.png">

    Preview the results. Press the <span class="blue-button">RUN</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-preview.png">

    The required code will be inserted into the notebook and immediately executed.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-groupby-aggregate-insert-code.png">

=== "R"