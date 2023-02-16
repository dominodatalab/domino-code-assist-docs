# Create an App

An app is a convenient way to combine a selection of components into a single view. One or more of these components can be combined into an app: visualizations, cross-filters and data tables.

<img class="screenshot" src="../../videos/quick-app/quick-app-title.gif">

Here's a step-by-step recipe for creating a simple app to examine the penguins data. It assumes that you have already done the following:

- loaded the penguins data
- created a scatter plot of body mass versus bill length colored by species and
- created a cross-filter selector on island.

Hover over the <img alt="assistant icon" class="assistant-icon" src="../../screenshots/general/assistant-icon.png"> icon. Select the _App_ item from the popup menu.

<img class="screenshot" src="../../screenshots/dca-menu-app.png">

In the app configuration widget you can select which components to include in the app by simply toggling them on and off. **Note:** You'll only see components which have been defined in the notebook.

<img class="screenshot" src="../../screenshots/app-configurator.png">

When you have selected the required components they'll all be added to the app canvase, but they'll probably not be suitably arranged. We'll fix that next.

<img class="screenshot" src="../../screenshots/app-configurator-widgets-selected.png">

Arrange the widgets by dragging and resizing.

<img class="screenshot" src="../../screenshots/app-configurator-widgets-arranged.png">

When you are happy with the app layout press the <span class="blue-button">RUN</span> button to add the code to the notebook.

<img class="screenshot" src="../../screenshots/app-code-inserted.png">

Press the <span class="white-button-blue-text">PREVIEW APP</span> button to see an interactive preview of the app.

<img class="screenshot" src="../../screenshots/app-preview.png">

At this point you can interact wit the app but you can't share it with others yet. To do that you'll need to [deploy the app](../deploy).