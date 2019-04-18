from flask import Flask, redirect
import random
 
 
app = Flask(__name__)
 
 
@app.route("/index.html")
@app.route("/")
def go_to_external_url():
    links = [
    'https://whober.uberinternal.com/124039',
    'https://whober.uberinternal.com/118023',
    'https://whober.uberinternal.com/141329',
    'https://whober.uberinternal.com/123826']
    link = random.sample(links, 1)[0]
    return redirect(link)
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)