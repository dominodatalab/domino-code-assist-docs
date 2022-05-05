# Loading data

The following video includes all the steps explained below

<video controls>
    <source src="https://user-images.githubusercontent.com/46192475/166969373-dec946f8-9702-4887-a57b-953adb18e1af.mp4" type="video/mp4">
</video>

## Check installation

If you have followed the [installation instructions](../../install.md), you should see a blue <span style="background-color: #2D71C7; color: white; padding: 3px 10px 3px 10px">Low Code Assistant™</span> button in the toolbar of your Jupyter notebook.
![Navigate to files](../../screenshots/00-initial.png)

## Initialize the Low Code Assistant™


The Low Code Assistant™ can be started by clicking the <span style="background-color: #2D71C7; color: white; padding: 3px 10px 3px 10px">Low Code Assistant™</span> button in the toolbar. It will insert a code snippet in a new code cell and execute it. After running succesfully, you should see `Low Code Assistant™ initialized`, as in the following screenshot:

![Assistant ready](../../screenshots/01-assistant-ready.png)

If you now hover above a code cell, you should see a blue icon ![assistant icon](../../screenshots/general/assistant-icon.png){.assistant-icon} to the right:

![Assistant visible](../../screenshots/02-assistant-visible.png)

If you hover above the ![assistant icon](../../screenshots/general/assistant-icon.png){.assistant-icon} icon, it will show a popup menu:

![Assistant menu](../../screenshots/03-assistant-expand.png)

## Loading CSV data into a Pandas DataFrame


### Open dialog

Hover above the ![assistant icon](../../screenshots/general/assistant-icon.png){.assistant-icon} icon and click the ![Load data](../../screenshots/general/assistant-load-data.png){.docs-border .menu-item} menu item, which will open the `Load Data` dialog.

![Load data](../../screenshots/04-load-data.png)

### Select `Datasets` tab

To select a file, navigate to the `Datasets` tab:

![Load datasets](../../screenshots/05-load-data-datasets.png)

### Navigate to the right directory

Use `..` to move a directory up:

![Go up a directory](../../screenshots/06-load-data-datasets-dir-up.png)

And click the **bold** directory name to enter a directory

![Enter directory](../../screenshots/07-load-data-datasets-dir-mydata.png)

### Click to open

Click on the `titanic.csv` file, and it will close the dialog, and insert the Python code to load the `.csv` file
into a Pandas dataframe.

![Load data](../../screenshots/08-load-data-titanic.png)

The dataframe will be assigned to the `df` variable. The last expression (the last line) of the code cell will only be the `df` variable, which will
cause the notebook to display its content.


You can now do your custom data transformations, by following the Pandas documentatio