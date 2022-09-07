# Code Snippets

## Using snippets

<div>Choose "Insert snippets" from the Low Code Assistant™ menu to insert code snippets into your notebook.</div>
![Snippets Context Menu](../screenshots/snippets/lca_context_menu.png){: style="width: 313px"}

Browse the available snippets and select the one you want to insert.
![Snippets Main](../screenshots/snippets/snippets_main.png){: style="width: 1024px"}
![Snippets Code](../screenshots/snippets/snippets_sub.png){: style="width: 1024px"}

## Adding snippets

A snippet library can be added by adding a git repository with snippets to your Domino project.
![Snippets repo](../screenshots/snippets/snippets_git_repos.png){: style="width: 1024px"}

If credentials are required to access the repository, they can be setup in your account:

<div>Select "Account Settings"</div>
![Account Settings](../screenshots/snippets/account_settings_menu.png){: style="width: 347px"}

Select "Git Credentials"
![Account Page](../screenshots/snippets/snippet_git_account_page.png){: style="width: 1024px"}

![Git credentials](../screenshots/snippets/snippets_git_credentials.png){: style="width: 1024px"}

## Snippet format

LCA looks for snippets in a "snippet" folder in the root of the repository. Any python files in this folder will be loaded as snippets.
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

Snippets can be edited in the git repository with your regular git workflow for this repo or you can open a VSCode workspace
for this project in Domino.

<div>Click on  "Open Folder" in VSCode</div>
![Open Folder](../screenshots/snippets/repo_open.png){: style="width: 526px"}

<div>Imported git repo's are available at "/repo"</div>
![repos](../screenshots/snippets/repo_open2.png){: style="width: 632px"}

<div>Create a new snippet</div>
![Create new snippet](../screenshots/snippets/edit_snippet.png){: style="width: 708px"}

<div>Sync changes in the "Imported Repositories" section:</div>
![Sync repo](../screenshots/snippets/sync_repo.png){: style="width: 593px"}

## Updating snippets in Notebook workspace

When snippets are updated in the git repository, the change is only visible in the notebook workspace after pulling the changes and restarting the notebook.

<div>Click on "pull" in the "Imported Repositories" section</div>
![pull](../screenshots/snippets/pull.png){: style="width: 430px"}

<div>Restart the notebook</div>
![restart](../screenshots/snippets/restart_notebook.png){: style="width: 737px"}
