# Loading Data from CSV

The following video includes all the steps explained below

<video controls>
    <source src="https://user-images.githubusercontent.com/46192475/182823773-7af97491-89d4-44f3-9996-9b08900d38e1.mp4" type="video/mp4">
</video>

## Uploading a CSV File

=== "Python"

    Hover over the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png">. Select the _Load data_ item from the popup menu.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-data-sources.png">

    Select the _Upload_ tab.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-upload.png">

    Drag a file into the drop zone.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-upload-dragged-file.png">

    Press the <span class="blue-button">INSERT CODE</span> button. The required code will be inserted into the notebook and immediately executed.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-upload-insert-code.png">

=== "R"

    Press the _Addin_ button.

    <img class="screenshot" src="../../screenshots/rstudio.png">

    Select _LCA Load Data_ from the menu.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data.png">
    
    Press the _Browse_ button and select the file which you want to upload.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data-upload.png">

    The first few lines from the file will be displayed. Press the <span class="blue-button">Apply</span> button.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data-upload-glimpse.png">

    The required code will be inserted into the script.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data-upload-code.png">

## Using a CSV File from a Workspace

=== "Python"

    Hover over the assistant icon <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png">. Select the _Load data_ item from the popup menu. Select the _Datasets_ tab.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets.png">

    Find the dataset.

    <img class="screenshot" src="../../screenshots/jupyter-load-data-datasets-locate.png">

    Press the <span class="blue-button">INSERT CODE</span> button. The required code will be inserted into the notebook and immediately executed.

    <img class="screenshot" src="../../screenshots/Screen Shot 2022-11-08 at 12.45.10.png">

=== "R"

    Press the _Addin_ button. Select _LCA Load Data_ from the menu. Select the _Datasets_ option.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data-datasets.png">

    Find the dataset.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data-datasets-locate.png">

    The first few lines from the selected file will be displayed. Press the <span class="blue-button">Apply</span> button.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data-datasets-glimpse.png">

    The required code will be inserted into the script.

    <img class="screenshot" src="../../screenshots/rstudio-menu-load-data-datasets-code.png">

## Check installation

If you have followed the [installation instructions](../install.md), you should see a blue <span class="blue-button">Low Code Assistant™</span> button in the toolbar of your Jupyter notebook.

![Navigate to files](../screenshots/load-csv/00-initial.png)

## Initialize the Low Code Assistant™


The Low Code Assistant™ can be started by clicking the <span style="background-color: #2D71C7; color: white; padding: 3px 10px 3px 10px">Low Code Assistant™</span> button in the toolbar. It will insert a code snippet in a new code cell and execute it. After running succesfully, you should see `Low Code Assistant™ initialized`, as in the following screenshot:

![Assistant ready](../screenshots/load-csv/01-assistant-ready.png)

If you now hover above a code cell, you should see a blue icon ![assistant icon](../screenshots/general/assistant-icon.png){.assistant-icon} to the right:

![Assistant visible](../screenshots/load-csv/02-assistant-visible.png)

If you hover above the ![assistant icon](../screenshots/general/assistant-icon.png){.assistant-icon} icon, it will show a popup menu:

![Assistant menu](../screenshots/load-csv/03-assistant-expand.png)

## Loading CSV data into a Pandas DataFrame


### Open dialog

Hover above the ![assistant icon](../screenshots/general/assistant-icon.png){.assistant-icon} icon and click the ![Load data](../screenshots/general/assistant-load-data.png){.docs-border .menu-item} menu item, which will open the `Load Data` dialog.

![Load data](../screenshots/load-csv/04-load-data.png)

### Select `Datasets` tab

To select a file, navigate to the `Datasets` tab:

![Load datasets](../screenshots/load-csv/05-load-data-datasets.png)

### Navigate to the right directory

Use `..` to move a directory up:

![Go up a directory](../screenshots/load-csv/06-load-data-datasets-dir-up.png)

And click the **bold** directory name to enter a directory

![Enter directory](../screenshots/load-csv/07-load-data-datasets-dir-mydata.png)

### Click to open

Click on the `titanic.csv` file, and it will close the dialog, and insert the Python code to load the `.csv` file
into a Pandas dataframe.

![Load data](../screenshots/load-csv/08-load-data-titanic.png)

The dataframe will be assigned to the `df` variable. The last expression (the last line) of the code cell will only be the `df` variable, which will
cause the notebook to display its content.


You can now do your custom data transformations, by following the Pandas documentatio