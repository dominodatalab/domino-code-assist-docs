# Transforming data

## Initialize assistant

We start similarly as in [Loading data](loading-data.md) by initializing the assistant.

![Assistant ready](../screenshots/transform/01-assistant-ready.png)


## Loading data

In this case, instead of using the assistant, we load the data ourselves:

![Assistant ready](../screenshots/transform/02-assistant-visible.png)



## Open dialog

Hover above the ![assistant icon](../screenshots/general/assistant-icon.png) icon and click the <img src="../screenshots/general/assistant-transformations.png" style="border: 1px solid black"> menu item, which will open the `Transformations` dialog.

![Open transformations](../screenshots/transform/03-assistant-expand.png)

## Choose dataframe

When the `Tranformations` dialog opens, we have to choose a dataframe.

![Open dialog](../screenshots/transform/04-transformations.png)


Click the select box to get an overview of all dataframe variables and click on the one you want to apply transformations on.

![Dataframe overview](../screenshots/transform/05-choose-dataframe.png)


After which the data is shown in a table.

![Dataframe chosen](../screenshots/transform/06-pick-dataframe.png)

## Apply quick transformation

We could manually add a transformation by clicking on the ![add](../screenshots/general/assistant-transformation-add.png){.docs-border}, but
in this example we will add a tranformation by a quick action throught the table. 


Hover above a cell value containing `nan`, and you can then hover above the triple dots icon, to get the menu ![add](../screenshots/general/assistant-transformation-filter-like.png){.docs-border}

![Choose dataframe](../screenshots/transform/07-popup-menu.png)

Click the menu item <img src="../screenshots/general/assistant-transformation-filter-like.png" style="border: 1px solid black"> to open the dialog:

![Choose dataframe](../screenshots/transform/08-filter-nan.png)

And click the <img src="../screenshots/general/assistant-transformation-apply.png" style="border: 1px solid black"> button to filter the dataframe. Now we can see that we only 
have values with `nan` for the `cabin` column.

![Choose dataframe](../screenshots/transform/09-filtered.png)

## Show code

Toggle the switch <img src="../screenshots/general/assistant-transformation-toggle-code.png" style="border: 1px solid black"> to show the code
![Choose dataframe](../screenshots/transform/10-show-code.png)

## Insert code

And click the <img src="../screenshots/general/assistant-transformation-insert-code.png" style="border: 1px solid black"> button to insert the code into the notebook.
![Choose dataframe](../screenshots/transform/11-insert-code.png)

