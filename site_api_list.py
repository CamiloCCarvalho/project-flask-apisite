from flask import Flask, url_for, redirect
from flask import render_template as page
from dependencies import consume_api

# Start Instance
app = Flask(__name__)
app.config['SERVER_NAME'] = 'ash-apilist.onrender.com'


@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))


# routes
@app.route(r'/')
def home_page():

    datas: dict = consume_api.get_api_data()
    count: int = datas['count']
    list_apis: list = datas['entries']
    names_api = []
    links_api = []
    descriptions_api = []
    for api in list_apis:
        names_api.append(api['API'])
        links_api.append(api['Link'])
        descriptions_api.append(api['Description'])
    return page("homepage.html",
                count=count,
                names_api=names_api,
                links_api=links_api,
                descriptions_api=descriptions_api)


# Run site
if __name__ == '__main__':
    app.run(debug=True)
