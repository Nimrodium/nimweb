from flask.templating import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return "Hello, World!"

@app.route('/astro')
def astro_home():
    return "Astro Home Placeholder"

@app.route('/elements')
def element_collection_home():
    return "Element Collection Home Placeholder"

@app.route('/about')
def about():
    return render_template('about.html')
