# Macky's Minerals
* Learn more about 871 minerals.  You can either click a mineral and view it's
image and attributes or you can click "Show random mineral" to view a
random mineral.

## Backend
* See [custom script - populate_database.py](https://github.com/FVPukay/mackys-minerals/blob/master/populate_database.py) that was created to load the minerals from the JSON file into the database
    * See [templatetags/mineral_catalog_extras.py](https://github.com/FVPukay/mackys-minerals/blob/master/minerals_app/templatetags/mineral_catalog_extras.py) to see how I accounted for the various problems found within the JSON file
        * A template tag was created so that the mineral attributes are ordered sequentially (top to bottom) from the most commonly occurring to the least commonly occurring in the mineral details page.
    * See [minerals.json](https://github.com/FVPukay/mackys-minerals/blob/master/minerals.json) as there are 3 duplicate minerals, unicode and text characters, not all minerals share the same attributes, and some attributes have empty strings for values and this has been accounted for in this app.
* See [mineral_details.html](https://github.com/FVPukay/mackys-minerals/blob/master/minerals_app/templates/minerals_app/mineral_details.html) - A title filter using the Django Templating Language ensures that attributes are displayed in title case on the
mineral details page.
* See [context_processors.py](https://github.com/FVPukay/mackys-minerals/blob/master/minerals_app/context_processors.py) - A context processor is used in conjunction with the [layout.html template](https://github.com/FVPukay/mackys-minerals/blob/master/minerals_app/templates/minerals_app/layout.html) to display random minerals when a user clicks the "Show random mineral" button
to keep the code dry.
* See [tests.py](https://github.com/FVPukay/mackys-minerals/blob/master/minerals_app/tests.py) - Total test coverage is 90%, models.py has 100% test
coverage, and the model, views, urls, templates, context processor, and template filter have been thoroughly tested.

## Frontend
* See [mineral_catalog/settings.py](https://github.com/FVPukay/mackys-minerals/blob/master/mineral_catalog/settings.py) - Used [WhiteNoise](https://pypi.org/project/whitenoise/) to display static files using Django on [Heroku](https://www.heroku.com/)
* See [global.css](https://github.com/FVPukay/mackys-minerals/blob/master/minerals_app/static/css/global.css)
    * The border around the mineral images are utilizing a CSS animation.  The duration setting, the amount of time it takes the animation to go from start to finish is 5 seconds, the animation will continuously play, and will alternate between #03001E, #7303C0, #EC38BC, and #FDEFF9.
* See [Screenshots of Mackey's Minerals](https://www.flickr.com/photos/156561177@N03/albums/72157710579421712)

## How to run work_log.py
Creating a [Virtualenv](https://pythonbasics.org/virtualenv/) is highly recommended.

Please refer to [requirements.txt](https://github.com/FVPukay/mackys-minerals/blob/master/requirements.txt) to see a list of the dependencies
(matching the versions is the safest way to be sure the app works as expected)
but the following pip installs can be done for quick setup:

>`pip install Django`  
`pip install coverage`

The app can be run by navigating to the directory that contains manage.py
and using:
>`python manage.py runserver`
