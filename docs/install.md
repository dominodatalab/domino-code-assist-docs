<div class="sticky-banner sticky-banner-warning">
    Domino Code Assist is automatically installed in Domino version 5.5 and above.
</div>

# Installation

## Install Domino Code Assist

There are four distinct approaches to installing Domino Code Assist (DCA) for either Python or R:

- [Install in a Workspace](#install-in-a-workspace)
- [Install in a Project](#install-in-a-project)
- [Install in a Compute Environment](#install-in-a-compute-environment) or
- [Install from Source](#install-from-source).

The first approach is the easiest way to get started with DCA. But if you restart you workspace, then you will need to reinstall DCA. The second and third approaches will enable DCA more permanently.

### Install in a Workspace

If you do not already have a Jupyter, JupyterLab or RStudio workspace, then create and launch one now.

The next steps will depend on whether you are working with Python (Jupyter or JupyterLab) or R (RStudio workspace).

=== "Python"

      Run the following command in a notebook code cell:

      ```
      !pip install --user domino-code-assist
      ```

      <img class="screenshot" src="../screenshots/lca-install-jupyter.png">

      After the installation completes, refresh your browser tab. The <span class="blue-button">Domino Code Assist</span> button will appear in the Jupyter toolbar. Click this button to initialize DCA.

      <img class="screenshot" src="../screenshots/lca-installed-jupyter.png">

      To upgrade an existing installation do:

      ```
      !pip install --user --upgrade domino-code-assist
      ```

=== "R"

    If you do not have the `{devtools}` package installed, then install it now by running the following command in the RStudio console.

    ```r
    install.packages("devtools")
    ```

    Now install the DCA package.

    ```r
    devtools::install_url("https://mirrors.domino.tech/dca/assistdomino_latest.tar.gz", upgrade="always")
    ```

    🚨 If you encounter a timeout error during the installation, then make sure that you've selected a harware tier that allows egress. Otherwise, your workspace will not be able to reach GitHub to download the package.

    After the installation completes, refresh your browser tab. Under the _Addins_ menu option you should now see an _ASSISTDOMINO_ section with various actions listed below. You can also confirm that the `{assistDomino}` package has been installed by searching in the _Packages_ tab.

    <img class="screenshot" src="../screenshots/lca-installed-rstudio.png">

### Install in a Project

=== "Python"

    A `requirements.txt` file is used to install Python packages into a new workspace created within a project. Navigate to _Files_ to check whether you have a `requirements.txt` file.

    <img class="screenshot" src="../screenshots/requirements-location.png">

    If you _do_ have a `requirements.txt` file then it will be listed (possibly among a selection of other files) then proceed as follows:

    1. Click on the `requirements.txt` file link.
    2. Click the <span class="white-button">Edit</span> button.
    <img class="screenshot" src="../screenshots/requirements-edit-button.png">
    3. Add the `domino-code-assist` package to your `requirements.txt` file. You can specify a version like `domino-code-assist==0.4.1`. If you don't specify a version then the latest version will be installed.
    <img class="screenshot" src="../screenshots/requirements-edit.png">
    4. Click the <span class="white-button">Save</span> button.

    If you _don't_ have a `requirements.txt` file then do the following:

    5. Download our [requirements.txt](requirements.txt).
    6. Press the _Upload_ button. Either drag and drop or browse to find the `requirements.txt` file.
    <img class="screenshot" src="../screenshots/requirements-upload-select.png">
    7. Click the <span class="blue-button">Upload</span> button.
    <img class="screenshot" src="../screenshots/requirements-upload.png">
    8. Confirm that the `requirements.txt` file has been successfully uploaded.
    <img class="screenshot" src="../screenshots/requirements-location.png">

    Now create a new _Jupyter_ or _JupyterLab_ workspace with and the <span class="blue-button">Domino Code Assist</span> button will be available.

=== "R"

    Documentation pending.

### Install in a Compute Environment

Enabling DCA in your organization's most used compute environments (CE) is the fastest way to deploy DCA. This way, DCA will appear automatically in any Jupyter or RStudio toolbar that is built from that CE. However, the CE will need to be rebuilt every time there is an DCA update. If CE's are not rebuilt weekly, we recommend enabling DCA at the project-level.

=== "Python"

    Documentation pending.

=== "R"

    1. Select _Environments_ from the side navigation bar.
    2. Choose the environment in which DCA for R package should be installed.
    3. Click the _Edit Definition_ button.
    4. Add the following line to the end of the `Dockerfile` section (but before the last `USER ubuntu` command):
    ```
    RUN R -e 'devtools::install_url("https://mirrors.domino.tech/dca/assistdomino_latest.tar.gz", upgrade="always")'
    RUN chown -R ubuntu:ubuntu /usr/local/lib/R/site-library
    ```
    5. Click the _Build_ button at the bottom of the page

    This will install DCA for R in every workspace that uses the Domino environment.

### Install from Source

This is the preferred approach in an [air-gapped environment](https://en.wikipedia.org/wiki/Air_gap_(networking)) where you are unable to connect to the internet to install the package using  of the previous approaches.

If your Domino deployment does not have open access to the internet (you're in an [air-gapped environment](https://en.wikipedia.org/wiki/Air_gap_(networking))), then DCA and any of its dependencies will fail to download. In this case, you will need to resort to an alternate method of installing DCA.

=== "Python"

    1. An archive containing the DCA package and all of its dependencies has been shared on <https://mirrors.domino.tech/>. The archives are named according to the required versions of DCA and Python. For example:

        - `dca-1.0.5-python-3.9.zip` — DCA-1.0.5 and Python-3.9
        - `dca-1.0.5-python-3.8.zip` — DCA-1.0.5 and Python-3.8
        - `dca-1.0.4-python-3.9.zip` — DCA-1.0.4 and Python-3.9
    2. Find the version of Python running in your Domino workspace and then download the appropriate archive. For example, DCA-1.0.5 for Python-3.9 would be downloaded from <https://mirrors.domino.tech/dca/python/dca-1.0.5-python-3.9.zip>.
    3. Upload the archive onto Domino.
    4. In a Jupyter workspace on Domino run the following commands to install the package.
    ```python
    # Check current folder. Should be /mnt.
    %pwd
    # Unzip the archive (assumes that the archive is in /mnt).
    !unzip -q dca-1.0.5-python-3.9.zip
    # Change into the resulting folder.
    %cd dca-archive
    # Check for the DCA package filename (optional).
    !ls domino_code_assist*
    # Install the package and all dependencies.
    !pip install --user --no-index --find-links=. domino_code_assist*.whl
    ```
    There might be some errors generated by `pip` but you can usually ignore them.

    5. Test that you are able to import the package.
    ```python
    import domino_code_assist
    ```

    <img class="screenshot" src="../screenshots/dca-install-python-air-gapped.png">

=== "R"

    1. Download a ZIP archive from <https://mirrors.domino.tech/dca/dca_sources.zip> onto your local machine. One might do this as follows:
    ```
    wget https://mirrors.domino.tech/dca/dca_sources.zip
    ```
    2. Upload the archive onto Domino.
    3. Unpack the archive on Domino.
    4. In a RStudio workspace on Domino install the package.

## Initialize

=== "Python"

    If you have followed the [installation instructions](./install.md), you should see a blue <span class="blue-button">Domino DCA</span> button in the toolbar of your Jupyter notebook.

    <img class="screenshot" src="../screenshots/lca-toolbar-button.png">

    DCA can be started by clicking the <span class="blue-button">Domino Code Assist</span> button in the toolbar. It will insert a code snippet in a new code cell and execute it.

    <img class="screenshot" src="../screenshots/lca-toolbar-button-code.png">

    If you now hover above a code cell, you should see the <img alt="assistant icon" class="assistant-icon" src="../screenshots/general/assistant-icon.png"> icon to the right.

    <img class="screenshot" src="../screenshots/lca-icon.png">

    If you hover above the <img alt="assistant icon" class="assistant-icon" src="../screenshots/general/assistant-icon.png"> icon, it will show a popup menu.

    <img class="screenshot" src="../screenshots/lca-icon-hover-menu.png">

=== "R"

    There is no initialization required in R. Various DCA actions will be listed under the _Addins_ menu option.

## Check Version

To check the version of DCA installed, run the following:

=== "Python"

    ```python
    import domino_code_assist

    domino_code_assist.__version__
    ```

=== "R"

    ```r
    packageVersion("assistDomino")
    ```
