scanfrio-dl
===========

Download manga serie or volume from scan-fr.io

Synopsis
--------

`python3 scanfrio-dl URL`


Example
-------

URL can be https://www.scan-fr.io/manga/one-punch-man to download the whole serie or https://www.scan-fr.io/manga/one-punch-man/1 to only download the first volume (in the case of OPM, the first chapter).

Details
-------

```
  scanfrio-dl
  Usage:
    scanfrio-dl [options] URL
  Arguments:
    URL         scan-fr.io manga serie/volume URL
  Options:
    -h --help               Show this screen.
    -v --version            Show version.
    --base-dir=<dir>        Base location of which all files are downloaded.

```
Dependencies
------------

requests, BeautifulSoup and docopt

Feature Request
---------------

If anyone find this tool useful, I might implement features such as:
- Pip package
- Multithreaded download for series
- Better output concerning download progress
- Concatenation of scans into a single PDF

So feel free to ask me for any possible improvement.

Copyright
---------

scanfrio-dl is released into the public domain by the copyright holders.
