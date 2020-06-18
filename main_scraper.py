import requests
from bs4 import BeautifulSoup

# mengambil url halaman yg akan di scrape
html_doct = requests.get('https://www.detik.com/terpopuler',
                         params={'tag_from': 'wp_cb_mostPopular_more'})

bsoup = BeautifulSoup(html_doct.text, 'html.parser') # melakukan parsing dari format html

popular_area = bsoup.find(attrs={'class' : 'grid-row list-content'}) # hanya area yg kita cari (popular area) yg di ambil

titles = popular_area.find_all(attrs={'class' : 'media__title'}) #find.all = digunakan untuk mencari semua element yg mempunyai atribute tertentu
# class yg diambil adalah class media title / judul dari artikel

images = popular_area.find_all(attrs={'class' : 'media__image'}) # mengambil semua class dari media image

# untuk menampilkan title, berupa textnya saja tanpa url nya
# for title in titles:
#     print(title.text)

# untuk menampilkan image saja
# for image in images:
#     print(image)

# melakukan filter find pertama a = untuk filter pada link a href, dan filter kedua melakukan filter untuk img alt
for image in images:
    print(image.find('a').find('img')['title']) #dan list title untuk mengambil hanya judulnya, tergantung penulisan nama classnya


# print(titles)
