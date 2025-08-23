from flask import Flask

app = Flask(__name__)

from app import routes


# from flask import Flask, render_template
# app=Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# # @app.route('/')
# # @app.route('/index')
# # def index():
#     # return "Hello, World!"

# @app.route('/astro')
# def astro_home():
#     return "Astro Home Placeholder"

# @app.route('/elements')
# def element_collection_home():
#     return "Element Collection Home Placeholder"


# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=9090,debug=True)
