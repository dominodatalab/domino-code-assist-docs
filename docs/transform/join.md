# Joins

The Transformation widget can be used to join two data frames.

For this tutorial we'll use the _Palmer Penguins_ data.

=== "Python"

    We are going to join a summarised version of the penguins data to a data frame containing the locations of the penguin colonies.

    Launch the _Transformations_ widget. Use the _Groupby and aggregate_ transformation to calculate the average penguin mass broken down by island and species.

    <img class="screenshot" src="../../screenshots/penguin-island-species-mass-average.png">

    Note that not all penguins are present at each of the colonies.

    Create a data frame with the locations of each of the colonies.

    <img class="screenshot" src="../../screenshots/penguin-colony-locations.png">

    Launch the _Transformations_ widget. Select the `mass` data frame and choose the _Join/merge_ transformation. Select the `islands` data frame to join with. By default this will be an _inner join_.

    Press the <span class="white-button-blue-text">Add Transformation</span> button then the <span class="blue-button">RUN</span> button.

    <img class="screenshot" src="../../screenshots/penguin-mass-location-inner-join.png">

    The code will be inserted into the notebook and run.

    <img class="screenshot" src="../../screenshots/penguin-mass-location-inner-join-code.png">

    Because the `islands` data frame does not contain location information for Torgerson this colony is not included in ther results.

    You can, however, select different join types. Select a _left outer_ join.

    <img class="screenshot" src="../../screenshots/penguin-mass-location-outer-join.png">

    Now Toegerson is included in the results, but the location fields are empty.

    <img class="screenshot" src="../../screenshots/penguin-mass-location-outer-join-code.png">

=== "R"

    This feature is not yet implemented in R.