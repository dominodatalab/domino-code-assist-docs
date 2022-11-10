# Chaining Transformations

For this tutorial we'll use the _Titanic_ data.

We have [already seen](filter.md#manual-filter) how multiple filtering operations can be applied. Now we'll see how different operations can be chained together.

=== "Python"

    Hover over the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png">. Select the _Transformations_ item from the popup menu. Select the _Groupby and aggregate_ option.

    Specify `Pclass` and `Embarked` as the columns to group by. Choose `Fare` as the column to aggregate. Select `mean` as the aggregator function. Press the <span class="white-button-blue-text">Add Transformation</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-chaining-aggregate.png">

    The preview will be updated with the summary data.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-chaining-aggregate-preview.png">

    Next we're going to filter the rows. Specify `Embarked` as the columns to filter by. Choose `!=` as the operator and `Q` as the value.. Turn the `as string` toggle on. Press the <span class="white-button-blue-text">Add Transformation</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-chaining-filter.png">

    The preview will be updated with the filtered data. Finally select the _Drop columns_ option and specify `Embarked` as the column to drop. Press the <span class="white-button-blue-text">Add Transformation</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-chaining-filter-preview.png">

    The preview will be updated. Press the <span class="blue-button">Insert Code</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-chaining-drop-column-preview.png">

    The required code will be inserted into the notebook and immediately executed.

    <img class="screenshot" src="../../screenshots/jupyter-transformation-chaining-insert-code.png">

=== "R"