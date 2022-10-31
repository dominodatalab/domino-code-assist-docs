# Code Snippets

## Using snippets

<div>Choose "Insert snippets" from the Low Code Assistant™ menu to insert code snippets into your notebook.</div>
![Snippets Context Menu](../screenshots/snippets/lca_context_menu.png){: style="width: 299px"}

Browse the available snippets and select the one you want to insert.
![Snippets Main](../screenshots/snippets/snippets_main.png){: style="width: 1024px"}
![Snippets Code](../screenshots/snippets/snippets_sub.png){: style="width: 1024px"}

## Adding snippets

A snippet library can be added by adding a git repository with snippets to your Domino project.
![Snippets repo](../screenshots/snippets/snippets_git_repos.png){: style="width: 1024px"}
An example snippet library can be found here: [https://github.com/dominodatalab/low-code-assistant-snippets](https://github.com/dominodatalab/low-code-assistant-snippets)

If credentials are required to access the repository, they can be setup in your account:

<div>Select "Account Settings"</div>
![Account Settings](../screenshots/snippets/account_settings_menu.png){: style="width: 347px"}

Select "Git Credentials"
![Account Page](../screenshots/snippets/snippet_git_account_page.png){: style="width: 1024px"}

![Git credentials](../screenshots/snippets/snippets_git_credentials.png){: style="width: 1024px"}

## Snippet format

LCA looks for snippets in a `"snippets"` folder in the root of the repository. Any python files in this folder will be loaded as snippets.
The sub folder structure will be maintained in the LCA menu.

Example:
<pre>
MySnippets
 ├── .git
 ├── snippets
      ├── my_snippet.py
      ├── subfolder
           ├── my_other_snippet.py
</pre>

## Editing snippets

Snippets can be edited:

   - In the git repository with your regular git workflow for this repo.
   - In the notebook using LCA.
   - With VSCode by opening a workspace with VSCode for this project in Domino.

### Editing with LCA

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

### Editing with a VSCode workspace
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
