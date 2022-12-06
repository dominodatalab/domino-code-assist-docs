# Installation

## Enabling Low Code Assistant

The Low Code Assistant (LCA) can be used with either Python or R.

=== "Python"

      If you do not already have a _Jupyter_ or _JupyterLab_ workspace, then create on now. Launch the workspace.

      Run the following command in a notebook code cell:

      ```
      !pip install --user low-code-assistant
      ```

      <img class="screenshot" src="../../screenshots/lca-install-jupyter.png">

      After the installation completes, refresh your browser tab. The <span class="blue-button">Low Code Assistant</span> button will appear in the Jupyter toolbar. Click this button to initialize the assistant.

      <img class="screenshot" src="../../screenshots/lca-installed-jupyter.png">

      To upgrade an existing version do:

      ```
      !pip install --user --upgrade low-code-assistant
      ```

=== "R"

      If you do not already have an _RStudio_ workspace, then create on now. Launch the workspace.

      Run the following command in the RStudio console:

      ```r
      install.packages("remotes")
      remotes::install_github("dominodatalab/low-code-assistant-rstudio")
      ```

      You may be prompted up update dependencies. Choose the appropriate option. The installation will take a fwe minutes.

      <img class="screenshot" src="../../screenshots/lca-install-rstudio.png">

      After the installation completes, refresh your browser tab. Unde the _Addins_ menu option you should now see an _ASSISTDOMINO_ section with various actions listed below. You can also confirm that the `{assistDomino}` package has been installed.

      <img class="screenshot" src="../../screenshots/lca-installed-rstudio.png">

This is the easiest way to get started with LCA, but if you restart you workspace, you will need to reinstall Low Code Assistant again. To enable LCA more permanantly, [make it the default configuration](#make-lca-default-configuration).

## Make LCA the Default Configuration {#make-lca-default-configuration}

There are 2 ways to make LCA a default configuration:

 * [Enable in a Domino Project](#enable-lca-domino-project), or
 * [Enable in a Domino Compute Environment](#enable-lca-domino-compute-environment)

Enabling LCA in your organization's most used compute environments (CE) is the fastest way to deploy LCA. This way, LCA will appear automatically in any Jupyter or RStudio toolbar that is built from that CE. However, the CE will need to be rebuilt everytime there is an LCA update. If CE's are not rebuilt weekly, we recommend enabling LCA at the project-level.

## Enable LCA in a Domino Project {#enable-lca-domino-project}

When a workspace is created, a `requirements.txt` file will be used to install Python packages into your new environment. 
We can use this to install Low Code Assistant into any workspace created within a project.

Check if you have a `requirements.txt` file. Navigate to _Files_. You should see something like the image below. If there are many files then you can search for the `requirements.txt` file.

Depending on whether or not you have a `requirements.txt` file follow the appropriate instructions below.

=== "I have a requirements.txt"

      <img class="screenshot" src="../../screenshots/requirements-location.png">

      1. Click on the `requirements.txt` file link.
      2. Click the <span class="white-button">Edit</span> button.

         <img class="screenshot" src="../../screenshots/requirements-edit-button.png">

      3. Add the `low-code-assistant` package to your `requirements.txt` file. You can specify a version like `low-code-assistant==0.4.1`. If you don't specify a version then the latest version will be installed.

         <img class="screenshot" src="../../screenshots/requirements-edit.png">

      4. Click the <span class="white-button">Save</span> button.

=== "I don't have a requirements.txt"

      <img class="screenshot" src="../../screenshots/requirements-missing.png">

      1. Download our [requirements.txt](requirements.txt).
      2. Press the _Upload_ button. Either drag and drop or browse to find the `requirements.txt` file.

         <img class="screenshot" src="../../screenshots/requirements-upload-select.png">

      3. Click the <span class="blue-button">Upload</span> button.
      
         <img class="screenshot" src="../../screenshots/requirements-upload.png">

      4. Confirm that the `requirements.txt` file has been successfully uploaded.

         <img class="screenshot" src="../../screenshots/requirements-location.png">

Now create a new _Jupyter_ or _JupyterLab_ workspace with and the Low Code Assistant button will be available.

## Enable LCA in a Domino Compute Environment {#enable-lca-domino-compute-environment}

1. Go to the Domino Standard Environment (under Environments in the side navigation bar).
2. Add this line to the end of the environment's `Dockerfile` setup (but before the last `USER ubuntu` command):
    ```
    RUN pip install low-code-assistant
    ```
3. Save the default environment `Dockerfile`.

The LCA toolbar button will now show up in the Jupyter toolbar. Add LCA to any other frequently used environments.

## Rebuilding the Compute Environment

1. Go to the _Environments_ page (the cube icon in the left-side-bar).
2. Open your LCA environment definition.
3. Click the <span class="white-button">Edit Definition</span> button.
4. Scroll to the bottom and check :fontawesome-regular-square: _Full rebuild without cache_.
5. Click the <span class="white-button">Build</span> button.

## Check Versions

It can be useful to know the precise version of Python and LCA which are running in your environment.

### Check Python Version

To check the version of Python in your environment, run the following:

```python
from platform import python_version

python_version()
```

### Check LCA Version

To check the version of LCA installed, run the following:

```python
import low_code_assistant

low_code_assistant.__version__
```

Follow [these instructions](#enabling-low-code-assistant-in-jupyter) to upgrade your LCA installation.