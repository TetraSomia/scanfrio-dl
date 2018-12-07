import requests
from bs4 import BeautifulSoup

class ParserVolume:
    def __init__(self, url):
        self.soup = None
        self.img_urls = {}
        
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('ParserVolume: http request failed')
        self.soup = BeautifulSoup(r.text, 'html.parser')
        img_tags = self.soup.findAll('img', {'class': 'img-responsive'})
        for img_tag in img_tags:
            img_url = img_tag.get('data-src')
            if not img_url:
                continue
            img_url = img_url.strip()
            img_name = img_url.split('/')[-1]
            if not img_name[0].isdigit():
                continue
            self.img_urls[img_name] = img_url

    def get_img_urls(self):
        return self.img_urls
