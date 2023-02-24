
# Customizing your app


## Customizing the layout

An app designed with DCA currently has a fixed layout. If you need customization in the layout, it is good to realize that
DCA is built on top of [Solara](https://solara.dev), which has a rich set of components.

If you initialize DCA, and click on the 'CREATE SAMPLE NOTEBOOK' button, the last cell ends up as follows:

```python
from domino_code_assist.deploy import Deployer
import solara


@solara.component
def Page():
    dca.CardGridLayout([
        {'item': plot_1, 'w': 12, 'h': 15, 'x': 0, 'y': 9},
        {'item': df_penguins_clean, 'w': 3, 'h': 9, 'x': 0, 'y': 27},
        {'item': plot_2, 'w': 9, 'h': 12, 'x': 3, 'y': 24},
        {'item': widget_year, 'w': 3, 'h': 3, 'x': 0, 'y': 24},
        {'item': dca.MarkdownFromCell('4293a57d'), 'w': 12, 'h': 4, 'x': 0, 'y': 0},
        {'item': dca.MarkdownFromCell('ec27252e'), 'w': 6, 'h': 5, 'x': 0, 'y': 4},
        {'item': dca.MarkdownFromCell('f7cd73bb'), 'w': 6, 'h': 5, 'x': 6, 'y': 4}
    ])

Deployer(Page)
```

The `Page` function with the decorator is called a "Solara component" and defines the content of your app.

Instead of this fixed "CardGridLayout" we will now create a Page component with a responsive layout.
A responsive layout will adjust its layout based on the size of the browser window. In our example, we want
to display two elements (`plot_2` and `df_penguins_clean`) next to each other on a so-called "medium" sized
screen, while they should be placed under each other on a smaller screen size.

```python
from low_code_assistant.deploy import Deployer
import solara


@solara.component
def Page():
    dca.MarkdownFromCell('4293a57d')  # modify the id match your custom notebook
    display(widget_year)
    display(plot_1)
    with solara.ColumnsResponsive(12, medium=6):
        display(plot_2)
        solara.lab.CrossFilterDataFrame(df_penguins_clean)


Deployer(Page)
```

TODO: screencap with changing the screen size.

The [ColumnsResponsive](https://solara.dev/api/columns_responsive) components follows the standard 12 column grid system,
where the total width of the screen is 12 columns. By creating a `solara.ColumnsResponsive(12, medium=6)` component, we say that each child element is 6 columns
wide on a medium or larger (>= 960 px) screen, and 12 columns wide (full width) on smaller screen sizes.

This means that on small (say mobile) screens, the plot and the dataframe will be shown under each other, while on larger screens next to each other.
This makes our app more suitable for both mobile and desktop users.

A few notes:

   * The `dca.CardGridLayout` does some smart things, that we now need to do ourselves:
      * Plots and widgets already created in the notebook, were added using the [`display`](https://solara.dev/api/display) function. We need to call this ourselves now.
      * Our dataframe was automatically wrapped with a [CrossFilterDataFrame](https://solara.dev/api/cross_filter_dataframe) component. We need to wrap it in this component ourselves.



## Adding a custom component

Solara has a rich set of [components](https://solara.dev/api/) which can be be used to build new components that integrate into an existing DCA app.

In this example, we will make use of the [FileDownload](https://solara.dev/api/file_download) component to add a download button to our app that
will download the selected data as csv file. To filter our dataframe, we use [use_cross_filter](https://solara.dev/api/use_cross_filter). 


```python
@solara.component
def DownloadFilteredDf(df):
    # default is to use id(df) as a key for the cross filter
    filter, set_filter = solara.use_cross_filter(id(df))

    # optionally, filter the dataframe
    df = df if filter is None else df[filter]

    filedata = df.to_csv(index=False)

    # and give a nice label
    if filter is None:
        label = "Download all rows"
    else:
        label = f"Download {len(df)} rows"
    solara.FileDownload(filedata, filename="penguins.csv", label=label)
```

Instead of adding the Download button to the main content panel, we add a [Sidebar](https://solara.dev/api/sidebar)
to our app and also put our markdown and the `widget_year` in it. This gives even more space to our visualizations
for mobile users.


```python
from low_code_assistant.deploy import Deployer


@solara.component
def Page():
    solara.Title("Palmer penguins")
    with solara.Sidebar():
        dca.MarkdownFromCell('4293a57d')
        display(widget_year)
        DownloadFilteredDf(df_penguins_clean)
    display(plot_1)
    with solara.ColumnsResponsive(12, medium=6):
        display(plot_2)
        solara.lab.CrossFilterDataFrame(df_penguins_clean)

Deployer(Page)
```


TODO: screencap
