

from flask import Flask
from flask import Flask, redirect
import random
 


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def go_to_external_url():
    links = [
    'https://workbench-dashboard.uberinternal.com/session/3b594d4b-8cde-5bbb-8243-7d7242942456/glweekly/',
    'https://workbench.uberinternal.com/session/f006aa53-1673-5600-8914-ce532b5b607d/glweekly/',
    'https://workbench-dashboard.uberinternal.com/session/c6a72d33-6365-5c47-a767-212315b94db6/glweekly/'
    ]
    link = random.sample(links, 1)[0]
    return redirect(link)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
     app.run(host='127.0.0.1', port=8080, debug=True)
