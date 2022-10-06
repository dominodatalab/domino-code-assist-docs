# Installation

## In a workspace

If you already created a workspace with "Jupyter" or "JupyterLab", you can install Low Code Assistant in your existing workspace.
This might is the easiest way to get started, but if you restart you workspace, you need to reinstall Low Code Assistant. To avoid this, follow the instructions for:

 * [Installing in a project](#in-a-project)
 * [Installing in a Compute environment](#in-a-project)

### pip install

Running the following command in a notebook code cell:

```
!python -m pip install --user https://vve589t3tspu.s3.us-west-2.amazonaws.com/1/low_code_assistant-latest-py2.py3-none-any.whl
```
![pip install in cell](screenshots/install/workspace-in-cell.png)


### Refresh your browser
Refresh your browser tab, open or create a new notebook, and you can click the "Low Code Assistant" button.

![after refresh](screenshots/install/workspace-after-refresh-highlight.png)

## In a project

When a workspace is created, a `requirements.txt` file will be used to install Python packages into your new environment. 
We can use this to install Low Code Assistant into any workspace created within a project.


### Check if you have a requirements.txt

Navigate to "Files", so you should see the following:
![](screenshots/install/open-requirements-txt.png)

You may or may not already have a `requirements.txt` file

### I have a requirements.txt file

#### Click on the `requirements.txt` file,
![click-open](screenshots/install/requirements-txt-open-highlight.png)

#### Click the edit Button

![click](screenshots/install/requirements-txt-click-edit-highlight.png)

#### Add the LCA url to your `requirements.txt` file:

Put the following text in your requirements.txt file.
```
https://vve589t3tspu.s3.us-west-2.amazonaws.com/1/low_code_assistant-latest-py2.py3-none-any.whl
```

And click "Save".

![added](screenshots/install/requirements-txt-save-highlight.png)

Now create a new workspace with "Jupyter" or "JupyterLab" and the Low Code Assistant button should be available.

### I do not have a requirements.txt file

Download our [requirements.txt file by right clicking this link and choose "Save link as" or "Save as" or "](/requirements.txt)


#### Navigate to `Files`


![Navigate to files](screenshots/install/no-requirements-txt-upload-click.png)

#### Click on upload

![Navigate to files](screenshots/install/no-requirements-txt-upload-click-highlight.png)

#### Drag and drop the requirements.txt file you downloaded

![dragged](screenshots/install/no-requirements-txt-upload-dragged.png)


#### Click upload

![dragged](screenshots/install/no-requirements-txt-upload-dragged-highlight.png)

#### Confirm your requirements.txt file is uploaded

It might take a few seconds, but you should see the `requirements.txt` file in you "Files" list.

![dragged](screenshots/install/no-requirements-txt-uploaded-highlight.png)

Now create a new workspace with "Jupyter" or "JupyterLab" and the Low Code Assistant button should be available.


## Compute environment

1. Go to the customer’s Domino Standard Environment (under Environments in the side navigation bar)
2. Add this line to the end of the env’s Dockerfile setup (but before the last USER ubuntu command):
   <pre><code>
   RUN pip install https://vve589t3tspu.s3.us-west-2.amazonaws.com/1/low_code_assistant-latest-py2.py3-none-any.whl
   </code></pre>
4. Save the default environment Dockerfile.
5. **That’s it! You’re done!**

The LCA toolbar button will now show up in the Jupyter toolbar for your customer.
Be sure to add LCA to any other env’s that are frequently used by your customer.
