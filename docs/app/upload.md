# Upload data to an app

## Loading CSV data into a Pandas DataFrame


### Open dialog

Hover above the ![assistant icon](../screenshots/general/assistant-icon.png){.assistant-icon} icon and click the ![Load data](../screenshots/general/assistant-load-data.png){.docs-border .menu-item} menu item, which will open the `Load Data` dialog.

![Load data](../screenshots/load-csv/04-load-data.png)


### Select `Datasets` tab

To select a file, navigate to the `Datasets` tab and navigate to the right directory:

![Load datasets](../screenshots/app-upload/datasets-tab.png)


### Open file


Select the file you want to open and check the `reactive` toggle button. This allows the app we will create to replace the dataframe by uploading data.

![Select dataset](../screenshots/app-upload/select-and-reactive.png)


This will give slightly different code than what you are expected to see when you simply load the csv (e.g. as in [CSV to Pandas](../../loading-data/csv) )

![Load dataset inserted](../screenshots/app-upload/load-data-inserted.png)


## Creating visualizations

### Adding a histogram

Create a histogram using the Low Code Assistant™, as described in [Scatter Plot](../visualization/create-plot.md) or add your own code. In our example we add the following code ourselves:

```python
import plotly.express as px

histogram_survived = px.histogram(df, x="survived")
histogram_survived
```
![Create histogram](../screenshots/app-upload/histogram-added.png)


## Open the App configurator

Click on the App button ![app open button](../screenshots/general/app-open.png){.retina-image .docs-border} to open the app configurator.

![Assistant expand](../screenshots/app-upload/app-pre-open.png)


## Configure the app

Toggle both `df_reactive` and `histogram_survived` and drag and resize the elements to create a good-looking app.

![App configure](../screenshots/app-upload/app-layout.png)


## Deploy the app

Follow the [Deploy an App](../deploy) steps to deploy the app.

## Result

Once the app is deployed, you can view the app, and should see a screen like this:

MISSING SCREENSHOT

Now drag a different CSV file into the file drop zone, and the Low Code Assistant™ app will re-execute the whole notebook, but with the data from the uploaded file:

<video controls style="width: 800px">
    <source src="https://user-images.githubusercontent.com/1765949/189431994-1e0b2f11-96ce-4584-ad11-982c7715f573.mp4" type="video/mp4">
</video>


Note that you can do many transformations and visualization. For this example, for simplicity, we only used a single dataframe and a single visualization.

*Note*: it is the user's responsibility at the moment to make sure the column names have the same names as the original file.
