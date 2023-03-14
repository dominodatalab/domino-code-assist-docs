# Column Summary

The Transformation widget generates summary data for all columns in the dataset. These summaries are generated on the fly and then cached.

For this tutorial we'll use the _Palmer Penguins_ data.

=== "Python"

    Launch the _Transformations_ widget.

    Hover over one of the column names at the top of the data preview. A kebab menu will appear. Hover over the kebab menu. A summary will be generated and displayed.

    If the column contains categorical or string data (like `island`) then the summary will contain a count of (i) the total number of values, (ii) the number of missing values and (iii) the number of missing values. There will also be a small bar chart showing the relative frequency of each of the values.

    <img class="screenshot" src="../../screenshots/column-summary-island.png">

    For numerical columns (like `bill_length_mm`) the summary will also contain the mean, standard deviation, minimum and maximum values along with a histogram of the distribution.

    <img class="screenshot" src="../../screenshots/column-summary-bill-length.png">

    At the bottom of the summary there's a _drop column_ button.

    <img class="screenshot" src="../../screenshots/column-summary-drop-column.png">

    Pressing the _drop column_ button will remove the corresponding column from the data.

    <img class="screenshot" src="../../screenshots/column-summary-column-dropped.png">

=== "R"

    This feature is not yet implemented in R.