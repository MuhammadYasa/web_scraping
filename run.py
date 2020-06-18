import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

apps = Flask(__name__)

@apps.route('/')
def home():
    return 'Test'

if __name__ == '__main__':
    apps.run(debug=True)
