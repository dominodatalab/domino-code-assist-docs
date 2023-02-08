# Working with Snippets

## Adding Snippets from GitHub

A snippet library can be added by linking a Git repository with snippets to your Domino project. See [these instructions](../../project/files) for linking a Git repository. If credentials are required to access the repository, they can be set up by following [these instructions](../../settings#git-credentials).

An example snippet library can be found [here](https://github.com/dominodatalab/low-code-assistant-snippets).

## Snippet Format

Code Assist looks for snippets in a `snippets/` folder in the root of the repository or project. Any `.py` (Python) or `.R` files below this folder will be loaded as snippets. The sub-folder structure will be maintained in the Code Assist menu. See, for example, the folder structure illustrated below.

<pre>
 ├── .git
 ├── snippets
      ├── create_list.py
      ├── create_dictionary.py
      ├── sklearn
           ├── model_regression.py
           ├── model_classification.py
</pre>

## Editing snippets

Snippets can be edited:

   - In the git repository with your regular git workflow for this repo.
   - In the notebook using Code Assist.
   - With VSCode by opening a workspace with VSCode for this project in Domino.

### Enable Editing

The capability to edit snippets is not enabled by default. It has to be explicity enabled.

=== "Python"

     The last item in the Code Assist menu is _Insert snippet_. The icon to the right of this item will be greyed out by default. Click on the icon to enable editing.

     <img class="screenshot" src="../../screenshots/jupyter-snippets-enable-editing.png">

     When editing is enabled a <span class="white-button-blue-text">+ SAVE AS SNIPPET</span> button will be visible on the active cell.

     <img class="screenshot" src="../../screenshots/jupyter-snippets-save-as-snippet.png">

=== "R"

     When editing is disabled the edit icon at the bottom/left of the _Snippets_ will be greyed and crossed out. Click on the icon to enable editing.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-enable-editing.png">

     The editing icon will then be enabled and an <span class="blue-button">Add</span> button will appear.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-editing-enabled.png">

### Add

=== "Python"

     <div>Enable snippet edit mode by clicking the pen icon in the context menu:</div>
     ![Snippets Context Menu](../screenshots/snippets/lca_context_menu.png){: style="width: 299px"}
     ![Snippets edit](../screenshots/snippets/lca_context_menu_edit.png){: style="width: 251px"}

     <div>Enter the snippet code and click on "SAVE AS SNIPPET"</div>
     ![Snippets save as snippet](../screenshots/snippets/save_as_snippet.png){: style="width: 1024px"}

     <div>Enter the name of the snippet and select the repository to store the snippet</div>
     ![Snippets save as snippet name and location](../screenshots/snippets/save_as_snippet_name_location.png){: style="width: 413px"}

     <div>After this you can keep editing the snippet if needed and save by clicking "SAVE"</div>
     ![Snippets save as snippet name and location](../screenshots/snippets/edit.png){: style="width: 1024px"}

     <div>After the enabling the snippet edit mode, controls for editing snippets are also displayed in the snippets panel.</div>
     ![Snippets controls](../screenshots/snippets/panel_edit_controls.png){: style="width: 413px"}

     <div>To sync the snippet back to git, open "File Changes" in the left-hand sidebar and click "Select and sync"
     on the "Imported Repositories" section</div>
     ![Snippets sync git](../screenshots/snippets/LCA_edit_git.png){: style="width: 588px"}

=== "R"

     Press the <span class="blue-button">Add</span> button. The _Add snippet_ dialog will appear.
     
     Insert a name for the snippet. It makes sense to give some thought to an appropriate naming scheme which will make snippets easier to find. Choose a project. Insert the body of the snippet into the text box. Press the <span class="blue-button">Add</span> button.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-add-snippet.png">

     A dialog will confirm that the snippet has been added. Press <span class="blue-button">OK</span> button.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-snippet-added.png">

     The newly added snippet will appear in the list of available snippets.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-snippet-added-list.png">

     Select the snippet. The content of the snippet will appear in the preview window. The <span class="blue-button">Insert Code</span> button will be activated. The <span class="blue-button">Edit</span> and <span class="blue-button">Delete</span> buttons will also appear.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-snippet-added-select.png">

### Edit

Inevitably you'll need to change a snippet, either to correct or enhance it.

=== "Python"

     Documentation pending.

=== "R"

     Select the snippet you want to edit and then press the <span class="blue-button">Edit</span> button. A dialog will appear that allows you to edit the content of the snippet. When you are finished editing, press the <span class="blue-button">Edit</span> button.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-snippet-edit.png">

     A dialog will confirm that the snippet has been edited. Press <span class="blue-button">OK</span> button.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-snippet-edited.png">

### Delete

If you no longer need a specific snippet then you might want to delete it.

=== "Python"

     Documentation pending.

=== "R"

     Select the snippet you want to delete and then press the <span class="blue-button">Delete</span> button. A dialog will appear that asks you to confirm that you want to delete the snippet. Press the <span class="blue-button">Delete</span> button.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-snippet-delete.png">

     A dialog will confirm that the snippet has been deleted. Press <span class="blue-button">OK</span> button.

     <img class="screenshot" src="../../screenshots/rstudio-snippets-snippet-deleted.png">

## Editing with a VSCode workspace
<div>Click on  "Open Folder" in VSCode</div>
![Open Folder](../screenshots/snippets/repo_open.png){: style="width: 526px"}

<div>Imported git repo's are available at "/repo"</div>
![repos](../screenshots/snippets/repo_open2.png){: style="width: 632px"}

<div>Create a new snippet</div>
![Create new snippet](../screenshots/snippets/edit_snippet.png){: style="width: 708px"}

<div>Sync changes in the "Imported Repositories" section:</div>
![Sync repo](../screenshots/snippets/sync_repo.png){: style="width: 593px"}

## Updating snippets in Notebook workspace

When snippets are updated in the git repository, the change is only visible in the notebook workspace after pulling the changes and reloading the snippets.

<div>Click on "pull" in the "Imported Repositories" section</div>
![pull](../screenshots/snippets/pull.png){: style="width: 430px"}

<div>Reload snippets</div>
![restart](../screenshots/snippets/reload_snippets.png){: style="width: 325px"}
