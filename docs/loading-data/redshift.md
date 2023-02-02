# Loading Data from Redshift

<!-- https://user-images.githubusercontent.com/46192475/182823701-695fc350-b814-48bf-8ce9-ffed4d347f86.mp4 -->

To load data from Redshift you'll need to have access to a Redshift cluster containing the data.

## Add a Redshift Data Source

Before you can use the Low Code Assistant (LCA) to access data from Redshift you'll need to add a suitable data source. Click the _Data_ option in the left-hand menu. Click the <span class="blue-button">+ Create a Data Source</span> button.

<img class="screenshot" src="../../screenshots/redshift-create-data-source.png">

Select the _Amazon Redshift_ option.

<img class="screenshot" src="../../screenshots/redshift-create-data-source-select.png">

Provide the details of the Redshift cluster.

<img class="screenshot" src="../../screenshots/redshift-create-data-source-cluster-details.png">

Fill in your credentials. Press the <span class="green-button">Test Credentials</span> button.

<img class="screenshot" src="../../screenshots/redshift-create-data-source-credentials.png">

When your credentials have been validated, press the <span class="blue-button">Next</span> button.

<img class="screenshot" src="../../screenshots/redshift-credentials-validated.png">

Specify which users will have access to this data source. Press the <span class="green-button">Finish Setup</span> button.

<img class="screenshot" src="../../screenshots/redshift-users.png">

The Redshift cluster will be added to the list of available data sources.

<img class="screenshot" src="../../screenshots/redshift-cluster-settings.png">
<img class="screenshot" src="../../screenshots/redshift-data-sources-list.png">

## Load Data from Redshift

=== "Python"

    Launch a Jupyter workspace.

    <img class="screenshot" src="../../screenshots/jupyter-redshift-cluster-data-sources.png">

    Initialize LCA and select the _Load data_ option.

    <img class="screenshot" src="../../screenshots/jupyter-redshift-cluster-load-data.png">

    Select the Redshift cluster data source.

    <img class="screenshot" src="../../screenshots/jupyter-redshift-cluster-select-data-source.png">

    Specify the required database and schema and then choose a table.

    <img class="screenshot" src="../../screenshots/jupyter-redshift-cluster-choose-table.png">

    Click the <span class="blue-button">INSERT CODE</span> button.

    <img class="screenshot" src="../../screenshots/jupyter-redshift-cluster-table-selected.png">

    The required code will be inserted into a cell and immediately executed.

    <img class="screenshot" src="../../screenshots/jupyter-redshift-cluster-code-inserted.png">

=== "R"

    This feature is not yet implemented in the R version of LCA.