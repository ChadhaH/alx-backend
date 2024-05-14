#!/usr/bin/env python3
"""
    force a particular locale by passing the locale=fr parameter
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config(object):
    """
        Configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
        Retrieves the locale for a web page
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
        outputs
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
