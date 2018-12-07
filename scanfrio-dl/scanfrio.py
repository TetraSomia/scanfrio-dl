import os

from downloader import Downloader

class Scanfrio:
    def __init__(self, basedir):
        self.basedir = basedir
        self.downloaders = []
        self._basedir_init()

    def _basedir_init(self):
        if os.path.exists(self.basedir):
            if not os.path.isdir(self.basedir):
                raise RuntimeError('Base directory is not actually a directory')
        else:
            os.makedirs(self.basedir)

    def add_url(self, url):
        self.downloaders.append(Downloader(self.basedir, url))

    def run(self):
        for downloader in self.downloaders:
            downloader.download()

