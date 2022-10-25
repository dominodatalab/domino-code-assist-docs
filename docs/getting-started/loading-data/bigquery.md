# Loading Data from BigQuery

To load data from BigQuery you'll need to have

- access to a BigQuery project containing the data and
- a private key with suitable permissions.

## Add a BigQuery Data Source

Before you can use the Low Code Assistant to access data from BigQuery you'll need to add a suitable data source.

Click the _Data_ option in the left-hand menu. Click the <span class="blue-button">+ Add a Data Source</span> button.

<img class="screenshot" src="../../../screenshots/data-sources.png">

From the drop-down menu select _Google BigQuery_.

<!-- <img class="screenshot" src="../../../screenshots/s3-new-data-source.png"> -->
<img class="screenshot" src="../../../screenshots/bigquery-select-data-store.png">

Fill in the details for the BigQuery project.

<img class="screenshot" src="../../../screenshots/bigquery-project-details.png">

Paste a valid private key in JSON format.

<img class="screenshot" src="../../../screenshots/bigquery-private-key.png">

Press the <span class="green-button">Test Credentials</span> button. When your credentials have been validated, press the <span class="blue-button">Next</span> button.

Specify which users will have access to this data source. Press the <span class="green-button">Finish Setup</span> button.

<img class="screenshot" src="../../../screenshots/bigquery-permissions.png">

The BigQuery project will appear under the list of data sources.

<img class="screenshot" src="../../../screenshots/s3-added.png">

## Load Data from BigQuery

Click the <span class="blue-button">Low Code Assistant™</span> button in the toolbar. It will insert a code snippet in a new code cell and execute it.

<img class="screenshot" src="../../../screenshots/bigquery-lca.png">

Once the Low Code Assistant™ has been initialised if you hover above a code cell, you will see the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../../screenshots/general/assistant-icon.png">. If you hover above the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../../screenshots/general/assistant-icon.png">, it will show a popup menu. Select the _Load Data_ item from the menu.

<img class="screenshot" src="../../../screenshots/bigquery-lca-menu.png">

Under the drop-down list of data sources you will find the data source which we created earlier. Select it.

<img class="screenshot" src="../../../screenshots/bigquery-lca-data-sources.png">

Specify the project, region, dataset and table that you want to load. Click the <span class="blue-button">INSERT CODE</span> button.

<img class="screenshot" src="../../../screenshots/bigquery-lca-project-dataset-table.png">

The required code will be inserted into a cell and immediately executed.

<img class="screenshot" src="../../../screenshots/bigquery-inserted-code.png">