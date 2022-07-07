# Installation

Dominocode is not available from pypi, please contact us for a private link so you can install it.

!!! warning "JupyterLab not yet supported"

    Currently, the Low Code Assistant™ only works in the (classical) Jupyter notebook. JupyterLab is not yet supported.


## Manual installation
Once you have the private download link from your sales team, you can manually install it into an existing Python environment using.


<div class="termy">

```console
$ pip install https://private-url/dominocode.tar.gz

---> 100%
```

</div>

!!! info "From a notebook"

    You can also run this from your notebook, by running `!pip install ...` from a code cell.

!!! warning "Not persistent"

    If you install this into a running workspace, you might lose the installed package when the workspace restarts.
    It is best practice to install it as explained in the next section.

## Install for workspace

When a workspace is created, a `requirements.txt` file will be used to install Python packages into your new environment. 
We can use this to make sure dominocode is installed before we start our notebook.

### Navigate to `Files`

In your project, navigate to `Files`.

![Navigate to files](screenshots/install/01-navigate-to-files.png)


### Create a new file

Create a new file by clicking the left most :material-file-plus: icon to get to the following screen
![Navigate to files](screenshots/install/02-new-file.png)


### Give filename and enter url

Enter the `requirements.txt` filename in the top textfield and the private url in the bottom textarea.
![Filename and url](screenshots/install/03-give-name-and-url.png)


### Save file

Clicking the `Save` button should give you the following screen, on success.
![Saved](screenshots/install/04-save.png)

### Optional: check file

Navigate to `Files` again, to make sure you have added the file

![Check](screenshots/install/05-check-in-files.png)

## Install using Docker

### Use a Dockerfile to install the Low Code Assistant™ on top of a base image. Place these instructions in a file named `Dockerfile` in your working directory. 

!!! info "Download Wheel and Install"

    https://private-url/dominocode.tar.gz is a placeholder. Once you have the private download link from your sales team, you can replace the placeholder.

```
# pull from a [Domino base image](https://docs.dominodatalab.com/en/latest/user_guide/0d73c6/domino-standard-environments/#_domino_standard_environment_dse), such as a [Domino DME (Domino Minimal Distribution)](https://quay.io/repository/domino/minimal-environment?tab=tags&tag=latest)
FROM quay.io/domino/minimal-environment:latest
USER root
# Optional: Maintainer / Label instructions
LABEL "Name"="LCA"

# download wheel and install
RUN wget https://private-url/dominocode.tar.gz
RUN pip install dominocode.tar.gz.whl

# Optional: Watch Docker build logs to check whether LCA was installed. You will need to add the --progress=plain flag to docker build command to use this.
RUN pip list | grep -i dominocode
USER ubuntu
```

### Build the Image 

Build the Docker image using Dockerfile instructions above. You can tag the image to pull the image into Domino as a [custom image](https://docs.dominodatalab.com/en/latest/user_guide/c11e1c/publish-in-domino-with-custom-images). Use the custom image tag to create an environment in Domino. 

<div class="termy">

```console
$ docker build --progress=plain -t quay.io/image_repo_name:tag_name -f Dockerfile .

---> 100%
```

</div>

