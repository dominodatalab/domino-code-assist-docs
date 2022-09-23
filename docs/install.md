# Installation

1. Get the latest LCA release from [CHANGELOG](https://github.com/dominodatalab/low-code-assistant/blob/main/CHANGELOG.md)
2. Go to the customer’s Domino Standard Environment (under Environments in the side navigation bar)
3. Add this line to the end of the env’s Dockerfile setup (but before the last USER ubuntu command):
   <pre><code>
   RUN pip install [secret .whl link from <a href="https://github.com/dominodatalab/low-code-assistant/blob/main/CHANGELOG.md">CHANGELOG</a>]
   </code></pre>
   (The secret .whl link will look something like:
   `RUN pip install https://xxxxxxxxx.s3.us-west-2.amazonaws.com/x/dominocode-0.0.21-py2.py3-none-any.whl`)
4. Save the default environment Dockerfile.
5. **That’s it! You’re done!**

The LCA toolbar button will now show up in the Jupyter toolbar for your customer.
Be sure to add LCA to any other env’s that are frequently used by your customer.
