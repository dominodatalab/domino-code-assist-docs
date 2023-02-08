# Loading Data from Snowflake

<!-- https://user-images.githubusercontent.com/46192475/182823489-e5c868b7-00eb-47e7-a16b-6727f4e26639.mp4 -->

## Add a Redshift Data Source

Before you can use Code Assist to access data from Snowflake you'll need to add a suitable data source. Click the _Data_ option in the left-hand menu. Click the <span class="blue-button">+ Create a Data Source</span> button.

<img class="screenshot" src="../../screenshots/snowflake-create-data-source.png">

Select the _Snowflake_ option from the dropdown menu.

<img class="screenshot" src="../../screenshots/snowflake-create-data-source-select.png">

Provide the details of the Snowflake database.

<img class="screenshot" src="../../screenshots/snowflake-create-data-source-details.png">

Fill in your credentials.

<img class="screenshot" src="../../screenshots/snowflake-create-data-source-credentials.png">

Press the <span class="green-button">Test Credentials</span> button. When your credentials have been validated, press the <span class="blue-button">Next</span> button.

Specify which users will have access to this data source. Press the <span class="green-button">Finish Setup</span> button.

<img class="screenshot" src="../../screenshots/snowflake-permissions.png">

The Snowflake connection will appear under the list of data sources.

<img class="screenshot" src="../../screenshots/data-sources-snowflake.png">

## Load Data from Snowflake

=== "Python"

    Click the <span class="blue-button">Low Code Assistant™</span> button in the toolbar. It will insert a code snippet in a new code cell and execute it.

    <img class="screenshot" src="../../screenshots/snowflake-lca.png">

    Once Code Assist has been initialised if you hover above a code cell, you will see the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png">. If you hover above the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png">, it will show a popup menu. Select the _Load Data_ item from the menu.

    <img class="screenshot" src="../../screenshots/snowflake-lca-menu.png">

    Under the drop-down list of data sources you will find the Snowflake data source which we created earlier. Select it.

    <img class="screenshot" src="../../screenshots/snowflake-lca-data-sources.png">

    Specify the database, schema and table that you want to load. Click the <span class="blue-button">INSERT CODE</span> button.

    <img class="screenshot" src="../../screenshots/snowflake-lca-database-schema-table.png">

    The required code will be inserted into a cell and immediately executed.

    <img class="screenshot" src="../../screenshots/snowflake-lca-inserted-code.png">

=== "R"

    This feature is not yet implemented in the R version of Code Assist.