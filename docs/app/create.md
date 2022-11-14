# Create an App


<video controls>
    <source src="https://user-images.githubusercontent.com/1765949/185930154-ed0319d3-f775-4db7-b3f8-7b38d0257979.mp4" type="video/mp4">
</video>

## Loading CSV data into a Pandas DataFrame

Load a dataset using the Low Code Assistant™, as described in [Getting started](../../) or by adding your own code. In our example we add the following code ourselves:
```python
import pandas as pd
df = pd.read_csv("../mydata/titanic.csv")
df.head(2)
```

![Load data](../screenshots/app-create/02-load-data.png)

## Creating visualizations

### Adding a histogram

Create a histogram using the Low Code Assistant™, as described in [Scatter Plot](../visualization/plotly.md) or adding your own code. In our example we add the following code ourselves:

```python
import plotly.express as px

histogram_survived = px.histogram(df, x="survived")
histogram_survived
```
![Create histogram](../screenshots/app-create/03-create-viz-1.png)


!!! info "Last expression"

    Note that the last expression (`histogram_survived`) causes the visual to display in the Jupyter notebook.


### Adding a scatter plot

Create a scatter plot using the Low Code Assistant™, as described in [Scatter Plot](../visualization/plotly.md). In our example we add the following code ourselves:

```python
import plotly.express as px

scatter_age_fare = px.scatter(df, x="age", y="fare", color="survived")
scatter_age_fare
```
![Create scatter](../screenshots/app-create/04-create-viz-2.png)


!!! info "Last expression"

    Note that the last expression (`scatter_age_fare`) causes the visual to display in the Jupyter notebook.

## Open the App configurator

If you now hover above the next code cell, you should see a blue icon ![assistant icon](../screenshots/general/assistant-icon.png){.assistant-icon} to the right:

![Assistant visible](../screenshots/app-create/05-assistant-visible.png)

If you hover above the ![assistant icon](../screenshots/general/assistant-icon.png){.assistant-icon} icon, it will show a popup menu:

![Assistant expand](../screenshots/app-create/06-assistant-expand.png)


Click on the App button ![app open button](../screenshots/general/app-open.png){.retina-image .docs-border} to open the app configurator.

![Assistant expand](../screenshots/app-create/07-app-before.png)

## Configure the app

Toggle the visualization matching the variables found in the notebook to add them to the app.
Optionally drag and resize the apps.
![Assistant expand](../screenshots/app-create/08-insert-code.png)

## Insert the code

When ready, click 'Insert code'.

![Assistant expand](../screenshots/app-create/09-done.png)

The configuration is added in code to your notebook. The code can be edited, and a preview can be shown
by clicking the ![preview button](../screenshots/general/app-preview.png){.retina-image} button.


