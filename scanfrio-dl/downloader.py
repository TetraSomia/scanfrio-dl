import os
import urllib.parse
import requests

from parser_volume import ParserVolume
from parser_serie import ParserSerie

class Downloader:
    def __init__(self, basedir, url):
        self.basedir = basedir
        self.url = url
        self.serie_name = None
        self.volume_only = False

        self._parse_url()

    def _parse_url(self):
        parsedurl = urllib.parse.urlparse(self.url)
        splitted_path = list(filter(None, parsedurl.path.split('/')))
        if parsedurl.netloc != 'www.scan-fr.io' or \
        len(splitted_path) < 2 or \
        splitted_path[0] != 'manga':
            raise RuntimeError('URL malformed')
        if len(splitted_path) > 2:
            self.volume_only = True
        self.serie_name = splitted_path[1]

    def _get_volume_name(self, vurl):
        parsedurl = urllib.parse.urlparse(vurl)
        splitted_path = list(filter(None, parsedurl.path.split('/')))
        return splitted_path[2]

    def _dl_img(self, img_path, img_url):
        r = requests.get(img_url, stream=True)
        if r.status_code == 200:
            with open(img_path, 'wb') as img:
                for chunk in r.iter_content(1024):
                    img.write(chunk)
        else:
            raise RuntimeError('_dl_img: http request failed')

    def _dl_volume(self, vurl):
        path = os.path.join(self.basedir, self.serie_name, self._get_volume_name(vurl))
        os.makedirs(path)
        parser = ParserVolume(vurl)
        for img_name, img_url in parser.get_img_urls().items():
            img_path = os.path.join(path, img_name)
            self._dl_img(img_path, img_url)
            print('%s received' % img_path)

    def _dl_serie(self):
        if self.volume_only:
            self._dl_volume(self.url)
            return
        parser = ParserSerie(self.url)
        for volume_url in parser.get_volume_urls():
            self._dl_volume(volume_url)

    def download(self):
        self._dl_serie()
        
