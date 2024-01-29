# You could theoretically write all of your code in one file
# Making multiple files makes it easier to find and solve problems
# "separation of concerns" breaking files up into their specified rules and tasks

from flask import Flask
from .site.routes import site


app = Flask(__name__)

app.register_blueprint(site)

