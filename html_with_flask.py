from flask import Flask
from flask import render_template

import scraping_yahooauc_with_flask


app = Flask(__name__)


@app.route('/')
def index():
    items = scraping_yahooauc_with_flask.main()
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run()
