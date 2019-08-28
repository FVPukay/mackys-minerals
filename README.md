# Macky's Minerals

#### About this web app
Learn more about 871 minerals.  You can either click a mineral and view it's
image and attributes or you can click "Show random mineral" to view a
random mineral.

#### Technologies Used
`Languages:` Python 3, HTML, CSS, Django Template Language  
`Framework:` Django  
`Database:` Sqlite3  
`ORM:` Django ORM

#### The behind the scenes look at the app
* A custom script was created to load the minerals from the JSON file into the
database.
* In the JSON file there are 3 duplicate minerals, unicode and text
characters, not all minerals share the same attributes, and some attributes
have empty strings for values.
* A template tag was created so that the mineral attributes are ordered
sequentially (top to bottom) from the most commonly occurring to the least
commonly occurring in the mineral details page.
* A title filter ensures that attributes are displayed in title case on the
mineral details page.
* A context processor is used in conjunction with the layout.html template
to keep the code dry.
* Unit tests are used.  Total test coverage is 90%, models.py is at 100% test
coverage, and the model, views, urls, templates, context processor, and template
filter have been thoroughly tested.
* The border around the mineral images are utilizing a CSS animation.
The duration setting, the amount of time it takes the animation to go from
start to finish is 5 seconds, the animation will continuously play,
and will alternate between #03001E, #7303C0, #EC38BC, and #FDEFF9.  The CSS
rules can be found in the global.css file.

##### Screenshots of the UI
[Macky's Minerals](https://www.flickr.com/photos/156561177@N03/albums/72157710579421712)

##### How to run work_log.py
Creating a Virtualenv is highly recommended.

Please refer to the requirements.txt file to see a list of the dependencies
(matching the versions is the safest way to be sure the app works as expected)
but the following pip installs can be done for quick setup:

>`pip install Django`  
`pip install coverage`

The app can be run by navigating to the directory that contains manage.py
and using:
>`python manage.py runserver`

`Note:` DEBUG is set to True since this app is not currently in production.
