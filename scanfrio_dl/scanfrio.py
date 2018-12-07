import os

class Scanfrio:
    def __init__(self, basedir, url):
        self.basedir = basedir
        self.url = url
        self._basedir_init()

    def _basedir_init(self):
        if os.path.exists(self.basedir):
            if not os.path.isdir(self.basedir):
                raise RuntimeError('Base directory is not actually a directory')
        else:
            os.makedirs(self.basedir)
