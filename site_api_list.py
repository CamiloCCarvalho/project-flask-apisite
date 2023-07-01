from flask import Flask
from flask import render_template as page

# Instance of Site
app = Flask(__name__)


# route
@app.route(r'/')
def home_page():
    return page("homepage.html")


@app.route(r'/users/<user_name>')
def user_page(user_name):
    return page('user_page.html', name=user_name)


# Run site
if __name__ == '__main__':
    app.run(debug=True)
