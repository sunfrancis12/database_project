from flask import Flask, request,url_for,render_template ,redirect , send_file,make_response
import search
import search_json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_food():
    food = request.values.get('food')
    return search_json.search_json(food)
    #return search.search(food)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)