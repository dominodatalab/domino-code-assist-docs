# Adding Snippets

## Adding Snippets from GitHub

A snippet library can be added by linking a Git repository with snippets to your Domino project. See [these instructions](../../project/files) for linking a Git repository. If credentials are required to access the repository, they can be set up by following [these instructions](../../settings#git-credentials).

An example snippet library can be found [here](https://github.com/dominodatalab/low-code-assistant-snippets).

## Snippet Format

LCA looks for snippets in a `"snippets"` folder in the root of the repository. Any Python files below this folder will be loaded as snippets. The sub-folder structure will be maintained in the LCA menu. See, for example, the folder structure illustrated below.

<pre>
 ├── .git
 ├── snippets
      ├── create_list.py
      ├── create_dictionary.py
      ├── sklearn
           ├── model_regression.py
           ├── model_classification.py
</pre>