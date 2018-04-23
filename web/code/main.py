# coding: utf-8
import os, time
import redis
from flask import Flask
from flask import render_template

application = Flask(__name__, template_folder='views')
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@application.route("/")
def hello_world():
    return render_template('hit.html', count=get_hit_count())

@application.route("/about")
def about():
    return render_template('about.html',  \
                            datetime=time.strftime("%d/%h/%Y %H:%M:%S"),  \
                            container=os.uname()[1],  \
hosted=' '.join(os.uname()))
