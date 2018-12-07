import os
import urllib.parse
import functools

class Downloader:
    def __init__(self, url):
        self.url = url
        self.serie = None
        self.dl_routine = None

        self._parse_url()

    def _parse_url(self):
        parsedurl = urllib.parse.urlparse(self.url)
        path = parsedurl.path
        splitted_path = list(filter(None, path.split('/')))
        if parsedurl.netloc != 'www.scan-fr.io' or \
        len(splitted_path) < 2 or \
        splitted_path[0] != 'manga':
            raise RuntimeError('URL malformed')
        if len(splitted_path) > 2:
            self.dl_routine = functools.partial(self._dl_volume, self.url)
        else:
            self.dl_routine = self._dl_serie

    def _dl_serie(self):
        print('dl serie')

    def	_dl_volume(self, vurl):
        print('dl volume: %s' % vurl)

    def download(self):
        self.dl_routine()
        
