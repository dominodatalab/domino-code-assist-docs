# 🥜 Low Code Assistant™ (LCA) in a nutshell

Low Code Assistant™ (LCA) provides point-and-click shortcuts for common data science boilerplate. 

LCA is available in _private preview_ on any Domino 4.x-5.x platform - **ask your Domino account manger to enable access.
**
![https://raw.githubusercontent.com/dominodatalab/low-code-jupyter-docs/main/LCA_GIF.gif](https://raw.githubusercontent.com/dominodatalab/low-code-jupyter-docs/main/LCA_GIF.gif)

*
*
*
*

# 🚦 Switch on Low Code Assistant™ (LCA)

To enable LCA, simply add this line to the Docker file of your default Domino compute environment.

```py

RUN pip install [secret .whl link]

```

Here, `[secret .whl link]` is provided by your Domino account manager. (_Domino staff, please find this installation link on [GitHub](https://github.com/dominodatalab/low-code-assistant/blob/main/CHANGELOG.md) or [Google Drive](https://docs.google.com/document/d/1nfR9nZ2OrmnJrG8vvKNuLRsyDmj2Is2_ynZh1PMNXXA/edit?usp=sharing)._)

After this line is added. LCA appears automagically in your Jupyter toolbar. ✨

*
*
*
*

# 📈 Accelerate new Python/R analysts

Low Code Assistant™ (LCA) accelerates universal data analysis tasks by autogenerating Python or R code with point & click GUIs:

1. ❄️ Import data from a business store like Snowflake, Redshift, or S3
2. 🤠 Munge or "wrangle" data into a desired format
3. 📊 Craete and share data visualizations
4. 🎚️ Create and share data apps

In tests with analysts new to Python (new graduates), Low Code Assistant (LCA) enhanced productivity by 20x:

  
| Task                          | Python Novice - Productivity Gain       | Python Expert - Productivity Gain      |
| :---                          | :---                                    | :---          |
| Make a statistical data visualization                             | 5x faster with LCA     | 1x faster with LCA    |
| Connect to Snowflake and import data as a dataframe               | 5x faster with LCA     | 2x faster with LCA    |
| Make a Dash/Shiny app where users can upload their own data       | 10x faster with LCA    | 2x faster with LCA    |
| Publish & share an interactive dashboard                          | 20x faster with LCA    | 3x faster with LCA    |

*
*
*
*

# Low Code Assistant™ - Extended Screencast

<video>
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

[Get started](getting-started/loading-data/){.md-button .md-button--primary}
[Installation](install.md){.md-button .md-button--secondary}
