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

    This is what the data currently looks like.

    <img class="screenshot" src="../../screenshots/rstudio-transformation-groupby-aggregate-initial-data.png">

    Press the _Addin_ button. Select _DCA Transformations_ from the menu to launch the transformations wizard.

    <img class="screenshot" src="../../screenshots/rstudio-menu-transformations.png"">

    Choose the data that you want to work on.

    <img class="screenshot" src="../../screenshots/rstudio-penguins-transformations-filtered-choose-data.png">

    A preview of the data will be shown. Press the <span class="blue-button">ADD TRANSFORMATION</span> button.

    <img class="screenshot" src="../../screenshots/rstudio-penguins-transformations-data-preview.png">

    Select _Group & Aggregate_ from the dropdown menu.

    <img class="screenshot" src="../../screenshots/rstudio-penguins-transformations-actions.png">

    Now choose the columns that the results will be grouped by. We'll group by `species`, `island` and `sex`.

    <img class="screenshot" src="../../screenshots/rstudio-penguins-transformations-select-grouping.png">

    Next choose the column which will be aggregated and the aggregation operation. You can select multiple columns for aggregation. We'll calculate the minimu, maximum and mean values of `body_mass_g` for each group. Press the <span class="blue-button">Apply</span> button.

    <img class="screenshot" src="../../screenshots/rstudio-penguins-transformations-select-aggregate.png">

    The data preview in the transformations wizard will be updated with the aggregated results. Press the <span class="blue-button">Insert Code</span> button.

    <img class="screenshot" src="../../screenshots/rstudio-penguins-transformations-aggregate-results-preview.png">

    The required code will be inserted into the script and the aggregated results stored in a new variable.

    <!-- <img class="screenshot" src="../../screenshots/Domino — Mozilla Firefox_0044.png"> -->