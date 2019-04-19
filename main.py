

from flask import Flask
from flask import Flask, redirect
import random
 


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def go_to_external_url():
    links = [
    'https://whober.uberinternal.com/124039',
    'https://whober.uberinternal.com/118023',
    'https://whober.uberinternal.com/141329',
    'https://whober.uberinternal.com/123826']
    link = random.sample(links, 1)[0]
    return redirect(link)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
     app.run(host='127.0.0.1', port=8080, debug=True)
