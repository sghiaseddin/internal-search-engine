from flask import Flask, render_template, request
from app.search_engine import UIHelper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    phrase = request.args.get('q', '')
    if not phrase:
        return render_template('results.html', query='', results=[], total=0)

    result_list = UIHelper.search(phrase) # returns list of dicts: (title, url, subtitle, sim_score, pagerank_score)
    website_title, favicon = UIHelper.get_website_meta()

    total = len(result_list)
    return render_template('results.html', query=phrase, results=result_list, total=total, favicon=favicon, website_title=website_title)

if __name__ == '__main__':
    app.run(debug=True, port=5999)