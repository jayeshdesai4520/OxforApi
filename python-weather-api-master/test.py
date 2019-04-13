from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def defination():
    word = request.form['words']
    app_id = 'a9c90eb0'
    app_key = 'a8e63e3cd073438b4dd32ead088ef268'
    language = 'en'   
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    json_object = r.json()
    define = str(json_object['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])
    return render_template('temperature.html', temp=define)


@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)