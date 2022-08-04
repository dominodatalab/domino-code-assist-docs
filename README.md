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

```bash
$ conda env create -f environment.yml
$ conda activate lca-docs
```

 1. Start a jupyter notebook server
    ```bash
    $ jupyter notebook --notebook-dir=notebooks --NotebookApp.token='' --port=11111 --no-browser
    ```

 2. Install dependencies/playwright

    ```bash
    $ playwright install
    ```
3. Run load session
    ```bash
    $ python capture.py load-csv
    ```
4. To run more available sessions, see:
    ```bash
    $ python capture.py --help
    ```

Some scripts also general 'general' images (screenshots of buttons, icon etc). If these are performed while recording a video,
the video will show a flicker. Instead run the script once with `--general-screenshots`, and for the video without.

To run all:
```bash
$ python capture.py load-csv &&\
 python capture.py load-csv --no-general-screenshots &&\
 python capture.py load-redshift &&\
 python capture.py load-redshift --no-general-screenshots &&\
 python capture.py load-redshift-sql &&\
 python capture.py load-snowflake &&\
 python capture.py transform &&\
 python capture.py transform --no-general-screenshots &&\
 python capture.py viz-scatter &&\
 python capture.py app-create &&\
 python capture.py app-create --no-general-screenshots
```
