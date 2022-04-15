from flask import Flask, request
from nlp import humanise, remove_stop_words
from wordcloud import WordCloud

app = Flask(__name__)

@app.route('/')
def index():
    return {"ready": True}


@app.route('/humanize', methods=['POST'])
def humanize():
    content = request.get_json()
    text = content['text']
    corpus = content['corpus']
    return humanise(text, corpus)


@app.route('/wordcloud', methods=['POST'])
def wordcloud():
    content = request.get_json()
    text = content['text']
    corpus = content['corpus']
    text = remove_stop_words(text, corpus)
    cloud = WordCloud().generate(text)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
