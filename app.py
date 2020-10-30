from flask import Flask
from flask import request
from wiki.lookup import find_page

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/site', methods=['POST'])
def receive_site():
    if request.method == 'POST':
        data = request.get_json()
        url = data["site"]
        print(url)
        return find_page(url)
    else:
        print("Not a POST request")


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
