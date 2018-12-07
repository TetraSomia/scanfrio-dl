"""scanfrio-dl
Usage:
    scanfrio-dl [options] URL

Arguments:
    URL         scan-fr.io manga serie/volume URL

Options:
    -h --help               Show this screen.
    -v --version            Show version.
    --base-dir=<dir>        Base location of which all files are downloaded.
"""
"""
Coded by:
Arthur Josso
    https://github.com/tetrasomia

    Feel free to do whatever you want with this tool.
"""

import os
from docopt import docopt

from scanfrio import Scanfrio


def main():
    arguments = docopt(__doc__, version='scanfrio-dl 1.0')

    basedir = arguments['--base-dir'] or os.getcwd()
    basedir = os.path.expanduser(basedir)
    url = arguments['URL']
    scanfrio = Scanfrio(basedir)
    scanfrio.add_url(url)
    scanfrio.run()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error: %s' % e)
