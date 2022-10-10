# Low Code Assistant™ (LCA) 


# 🥜 In a nutshell

Low Code Assistant™ (LCA) provides point-and-click shortcuts for common data science boilerplate. 

LCA is available as a _beta feature_ on any Domino 4.x-5.x platform - please see **"🚦 Switch on Low Code Assistant" below to get started.**

To enable LCA for RStudio on Domino, please refer to [Low Code Assistant for R](https://github.com/dominodatalab/low-code-assistant-rstudio).

![https://raw.githubusercontent.com/dominodatalab/low-code-jupyter-docs/main/LCA_GIF.gif](https://raw.githubusercontent.com/dominodatalab/low-code-jupyter-docs/main/LCA_GIF.gif)

* * *

<br />
<br />
<br />
<br />

# 🚦 Switch on Low Code Assistant™ (LCA)

## Enable Low Code Assistant within Jupyter/JupyterLab

If you already have a workspace with "Jupyter" or "JupyterLab", you can enable Low Code Assistant (LCA) in your existing workspace by running the following command in a notebook code cell:

```
!python -m pip install --user https://vve589t3tspu.s3.us-west-2.amazonaws.com/1/low_code_assistant-latest-py2.py3-none-any.whl
```
![pip install in cell](screenshots/install/workspace-in-cell.png)

After this installation command is finished running, please refresh your browser tab. Then you will see the "Low Code Assistant" button in your Jupyter toolbar. Click on this button to initialize the Assistant.

![after refresh](screenshots/install/workspace-after-refresh-highlight.png)

This  is the easiest way to get started, but if you restart your workspace, you will need to re-enable Low Code Assistant again. To enable LCA more permanently, please follow the instructions below for:

 * [Installing in a project](#enabling-low-code-assistant-for-a-domino-project)
 * [Installing in a Compute environment](#enabling-low-code-assistant-for-a-domino-compute-environment)

## Enabling Low Code Assistant for a Domino Project

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

Download our [requirements.txt file by right clicking this link and choose "Save link as" or "Save as" or "](https://raw.githubusercontent.com/dominodatalab/low-code-jupyter-docs/main/docs/requirements.txt)


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


## Enabling Low Code Assistant for a Domino Compute Environment

1. Go to the customer’s Domino Standard Environment (under Environments in the side navigation bar)
2. Add this line to the end of the env’s Dockerfile setup (but before the last USER ubuntu command):
   <pre><code>
   RUN pip install https://vve589t3tspu.s3.us-west-2.amazonaws.com/1/low_code_assistant-latest-py2.py3-none-any.whl
   </code></pre>
4. Save the default environment Dockerfile.
5. **That’s it! You’re done!**

The LCA toolbar button will now show up in the Jupyter toolbar for your customer.
Be sure to add LCA to any other env’s that are frequently used by your customer.

* * *

<br />
<br />
<br />
<br />

# 📈 Accelerate new Python/R analysts

Low Code Assistant™ (LCA) accelerates universal data analysis tasks by autogenerating Python or R code with point & click GUIs.

For example, LCA can autogenerate Python or R code for these tasks:

1. ❄️ Import data from a business store like S3, [Snowflake](https://dominodatalab.github.io/low-code-jupyter-docs/getting-started/loading-data/snowflake/), or [Redshift](https://dominodatalab.github.io/low-code-jupyter-docs/getting-started/loading-data/redshift/)
2. 🤠 [Munge or "wrangle" data](https://dominodatalab.github.io/low-code-jupyter-docs/getting-started/transform/) into a desired format
3. 📊 [Create and share data visualizations](https://dominodatalab.github.io/low-code-jupyter-docs/getting-started/viz/scatter/)
4. 🎚️ [Create  and share data apps](https://dominodatalab.github.io/low-code-jupyter-docs/getting-started/app/create/)

In tests with analysts new to Python (new graduates), Low Code Assistant (LCA) enhanced productivity by 5-20x:

  
| Task                          | Python Novice - Productivity Gain       | Python Expert - Productivity Gain      |
| :---                          | :---                                    | :---          |
| Make a statistical data visualization                             | 5x faster with LCA     | 1x faster with LCA    |
| Connect to Snowflake and import data as a dataframe               | 5x faster with LCA     | 2x faster with LCA    |
| Make a Dash/Shiny app where users can upload their own data       | 10x faster with LCA    | 2x faster with LCA    |
| Publish & share an interactive dashboard                          | 20x faster with LCA    | 3x faster with LCA    |

* * *

<br />
<br />
<br />
<br />

# Low Code Assistant™ - Extended Screencast


<video controls autoplay>
  <source src="https://user-images.githubusercontent.com/1765949/185939829-2b99a7c9-10e7-4d67-8aa5-a2e1b9882a20.mp4" type="video/mp4">
</video>
<script>
    var video = document.querySelector('video');
    video.currentTime = 0.5;
</script>


<!-- This video shows how to

  * Initialize the Low Code Assistant™
  * Open the *'Load data'* UI from the Low Code Assistant™
  * Navigate to the `titanic.csv` file.
  * Click the file, to generate the `Pandas` code
 -->

[Get started](getting-started/loading-data/csv/){.md-button .md-button--primary}
[Installation](install.md){.md-button .md-button--secondary}
