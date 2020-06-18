import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

apps = Flask(__name__)

@apps.route('/')
def home():
    return render_template('index.html')

@apps.route('/detik-popular')
def detik_popular():
    html_doct = requests.get('https://www.detik.com/terpopuler',
                             params={'tag_from': 'wp_cb_mostPopular_more'})
    bsoup = BeautifulSoup(html_doct.text, 'html.parser')
    popular_area = bsoup.find(attrs={'class': 'grid-row list-content'})
    titles = popular_area.find_all(attrs={'class': 'media__title'})
    images = popular_area.find_all(attrs={'class': 'media__image'})

    return render_template('index.html',images=images)

if __name__ == '__main__':
    apps.run(debug=True)
