#all the imports required

import os
import sqlite3
from flask import Flas, request, session, g, redirect, url_for, abort, render_template, flash 
	
# create our application

app = Flask(__name__)
app.config.from_object(__name__)

#Load default config and override config from an environment variable