# Installation

1. Get the latest LCA release from the LCA CHANGELOG on [GitHub](https://github.com/dominodatalab/low-code-assistant/blob/main/CHANGELOG.md) or [Google Drive](https://docs.google.com/document/d/1nfR9nZ2OrmnJrG8vvKNuLRsyDmj2Is2_ynZh1PMNXXA/view)
3. Go to the customer’s Domino Standard Environment (under Environments in the side navigation bar)
4. Add this line to the end of the env’s Dockerfile setup (but before the last USER ubuntu command):
   <pre><code>
   RUN pip install [secret .whl link from <a href="https://docs.google.com/document/d/1nfR9nZ2OrmnJrG8vvKNuLRsyDmj2Is2_ynZh1PMNXXA/view">CHANGELOG</a>]
   </code></pre>
   (The secret .whl link will look something like:
   `RUN pip install https://xxxxxxxxx.s3.us-west-2.amazonaws.com/x/dominocode-0.0.21-py2.py3-none-any.whl`)
4. Save the default environment Dockerfile.
5. **That’s it! You’re done!**

The LCA toolbar button will now show up in the Jupyter toolbar for your customer.
Be sure to add LCA to any other env’s that are frequently used by your customer.
