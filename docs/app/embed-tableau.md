# Embed an App in a Tableau Dashboard

Once deployed, an app is effectively just a web page. This means that it can be embedded anywhere you can put an `<iframe>`. So you can pop it into any other web page. You can also embed it in a Tableau dashboard. Let's see how that is done.

Start with a blank dashboard.

<img class="screenshot" src="../../screenshots/app-embed-tableau-empty-dashboard.png">

Add some content to the dashboard. In this case we'll keep it super simple. Add a _Text_ object to the dashboard. Choose appropriate font shape and size.

<img class="screenshot" src="../../screenshots/app-embed-tableau-text-dialog.png">

By default the text will occupy the whole dashboard.

<img class="screenshot" src="../../screenshots/app-embed-tableau-text-maximised.png">

Click the :fontawesome-solid-caret-down: on the right and select _Floating_.

<img class="screenshot" src="../../screenshots/app-embed-tableau-text-floating.png">

Resize and move the text.

<img class="screenshot" src="../../screenshots/app-embed-tableau-text-resized.png">

Add a _Web Page_ object to the dashboard. Paste the URL for the app. 🚨 The app must be publicly accessible. Test this by trying to open the URL in an incognito browser window.

<img class="screenshot" src="../../screenshots/app-embed-tableau-webpage-dialog.png">

The app will be added to the dashboard. Again, the app will occupy the whole dashboard by default.

<img class="screenshot" src="../../screenshots/app-embed-tableau-webpage-maximised.png">

Click the :fontawesome-solid-caret-down: on the right and select _Floating_.

<img class="screenshot" src="../../screenshots/app-embed-tableau-webpage-floating.png">

Resize and move the app to the desired location.

<img class="screenshot" src="../../screenshots/app-embed-tableau-webpage-resized.png">
