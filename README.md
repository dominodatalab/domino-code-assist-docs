# low-code-jupyter-docs

This repository only contains the documentation for dominocode.

The live documentation is at https://dominodatalab.github.io/low-code-jupyter-docs/
# Develop documentation

## Install dependencies:
```bash
$ pip install -r requirements.txt
```

## Start server
Start mkdocs
```bash
$ mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.23 seconds
INFO     -  [13:51:27] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [13:51:27] Serving on http://127.0.0.1:8000/
```

Now you can edit the markdown files, and the documentation page should reload.

  * Mkdocs: https://www.mkdocs.org/
  * Theme: Material for MkDocs
     *  https://squidfunk.github.io/mkdocs-material/
     *  https://squidfunk.github.io/mkdocs-material/reference/annotations/


## Publish

```bash
mkdocs gh-deploy
```

# Generating video/screenshots

This is required when the dominocode assistant looks different.

 1. Start a jupyter notebook server
    ```bash
    $ jupyter notebook --notebook-dir=notebooks --NotebookApp.token='' --port=11111 --no-browser
    ```

 2. Install dependencies/playwright

    ```bash
    $ pip install -r requirements.txt
    $ playwright install
    ```
    Make sure ffmpeg is installed
    ```
    $ ffmpeg -h
    ```
    If not installed, use brew/conda/mamba, e.g.:
    ```bash
    $ mamba install -c conda-forge ffmpeg 
    ```
3. Run load session
    ```bash
    $ python capture.py load
    ```
4. Run transform session
    ```bash
    $ python capture.py transform
    ```

Some scripts also general 'general' images (screenshots of buttons, icon etc). If these are performed while recording a video,
the video will show a flicker. Instead run the script once with `--general-screenshots`, and for the video without.
