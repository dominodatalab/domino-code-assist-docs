# Filtering Data

<!-- https://user-images.githubusercontent.com/46192475/182823427-61bf2e88-db15-4aa8-bf85-054b21c9e6ac.mp4 -->

For this tutorial we'll use the _Titanic_ data.

## Quick Filter

A quick filter allows you to rapidly select a subset of rows. It only allows for a single operation. We are going remove records with missing values in the `Cabin` column. 

=== "Python"

    The _Titanic_ data have been assigned to a variable named `df`.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic.png">

    Hover over the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png">. Select the _Transformations_ item from the popup menu.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic-menu.png">

    The _Transformations_ dialog will appear. Select the target variable from the dropdown menu.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic-transformations.png">

    A preview of the data will appear.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic-transformations-select-data.png">

    Click on the :fontawesome-solid-ellipsis-vertical: to the right of any of the `nan` values in the `Cabin` column. Then click on the _Filter values like this_ popup button.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic-transformations-hamburger-filter.png">

    A dialog will appear with fields to choose a column, an operator and a value. The value will be set to `nan` by default.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic-transformations-filter-like.png">

    Since we are wanting to exclude records with missing values, we change the operator from `==` to `!=`. Press the <span class="blue-button">Apply</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic-transformations-change-operator.png">

    The required code will be inserted into the notebook and immediately executed.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-titanic-transformations-filtered.png">

=== "R"

## Manual Filter

A manual filter allows you to apply multiple operations. We are going to retain only records where `Embarked` is `"S"` and `Pclass` is less than 3. We'll do this by chaining multiple filtering operations.

=== "Python"

    Under the _Column_ selector choose `Embarked`. Set `Operator` to `==` and `Value` to `S`. Turn the `as string` toggle on. Press the <span class="white-button-blue-text">Add Transformation</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-titanic-filter-manual-embarked.png">

    The preview will be updated to show only those records where `Embarked` is `"S"`.

    <img class="screenshot" src="../../screenshots/jupyter-titanic-filter-manual-embarked-preview.png">

    Under the _Column_ selector choose `Pclass`. Set `Operator` to `<` and `Value` to `3`. Press the <span class="white-button-blue-text">Add Transformation</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-titanic-filter-manual-pclass.png">

    The preview will be updated to show only those records where `Embarked` is `"S"` and `Pclass` is less than 3. Press the <span class="blue-button">Insert Code</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-titanic-filter-manual-pclass-preview.png">

    The required code will be inserted into the notebook and immediately executed.

    <img class="screenshot" src="../../screenshots/jupyter-titanic-filter-manual-insert-code.png">

=== "R"