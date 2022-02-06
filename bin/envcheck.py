#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Style:
   Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

    @name           envcheck
    @version        2.00
    @author-name    Wayne Schmidt
    @author-email   wschmidt@sumologic.com
    @license-name   Apache
    @license-url    https://www.apache.org/licenses/LICENSE-2.0
"""

modulelist = list()
modulelist = [
    'argparse', 'configparser', 'datetime', 'os',
    'sys', 'json', 'requests'
]
ISSUES = 0
for module in modulelist:
    try:
        __import__(module)
    except ImportError:
        print('### Issue ### ToFix ### pip3 install {}'.format(module))
        ISSUES = ISSUES + 1
print('# Report # {} Issues'.format(ISSUES))
