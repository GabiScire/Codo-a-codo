from flask import Flask
from flask import render_template
import flask
from flaskext.mysql import MySQL, Mysql

app = flask(__name__)
mysql = MySQL()

if __name__ == '_main_':
    app.run(debug=True)
    hola