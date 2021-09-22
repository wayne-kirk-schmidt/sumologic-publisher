#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation:

This script takes a file and publishes the file to a SumoLogic endpoint.
It will try deduce the file type from the extension.  The default will be text.

Usage:
    $ python  sumologic-publish [ options ]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           sumologic-publish
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wschmidt@sumologic.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wschmidt@sumologic.com)"

import json
import argparse
import datetime
import os
import sys
import requests
sys.dont_write_bytecode = 1
import mimemap

PARSER = argparse.ArgumentParser(description="""
A way to publish a set of files to Sumo Logic using a HTTPS endpoint
""")

PARSER.add_argument('-u', metavar='<urlsource>', dest='SUMOURL', help='set Sumologic URL')
PARSER.add_argument('-s', metavar='<filesource>', dest='FILESRC', help='set data sources')
PARSER.add_argument('-c', metavar='<category>', dest='CATEGORY', help='set source category')
PARSER.add_argument("-v", type=int, default=0, metavar='<verbose>', \
                    dest='verbose', help="more verbose")
ARGS = PARSER.parse_args()

CURRENT = datetime.datetime.now()

DSTAMP = CURRENT.strftime("%Y%m%d")
TSTAMP = CURRENT.strftime("%H%M%S")
LSTAMP = DSTAMP + '.' + TSTAMP

CATEGORY = 'sumologic/publisher'

if ARGS.CATEGORY:
    os.environ['CATEGORY'] = ARGS.CATEGORY

try:
    SUMOURL = ARGS.SUMOURL

except KeyError as myerror:
    print('Environment Variable Not Set :: {} '.format(myerror.args[0]))

def main():
    """
    This is the wrapper for the retreival and the publish modules.
    """
    data_sources = list()
    data_sources = resolve_data_sources(ARGS.FILESRC)
    publish_data(data_sources,SUMOURL)

def resolve_data_sources(filetarget):
    """
    This resolves target into a list of files
    """
    myfilelist = list()
    if os.path.isfile(filetarget):
        myfilelist.append(filetarget)
    if os.path.isdir(filetarget):
        for currentpath, _folders, files in os.walk(filetarget):
            for file in files:
                myfilelist.append((os.path.join(currentpath, file)))
    for myfile in myfilelist:
        if ARGS.verbose > 2:
            print('MYFILE: {}'.format(myfile))
    return myfilelist

def publish_data(publishtargetlist,publishurl):
    """
    This publishes a list of targets into Sumologic
    """

    session = requests.Session()

    for publishtarget in publishtargetlist:

        headers = dict()

        headers['Content-Type'] = 'text/plain'
        headers['Accept'] = 'text/plain'
        headers['X-Sumo-Category'] = CATEGORY
        mimetype = "text/plain"

        with open(publishtarget, mode='r') as inputfile:
            file_extension = os.path.splitext(publishtarget)[1][1:]
            if file_extension:
                mimetype = mimemap.MIMETYPES[file_extension]
                headers['Content-Type'] = mimetype
                headers['Accept'] = mimetype

            if file_extension == 'json':
                payload = (json.load(inputfile))
                postresponse = session.post(publishurl, json=payload, headers=headers).status_code
            else:
                payload = (inputfile.read())
                postresponse = session.post(publishurl, data=payload, headers=headers).status_code

            if ARGS.verbose > 4:
                print('SUMOLOGIC_ENDPOINT: {}'.format(publishurl))
                print('SUMOLOGIC_CATEGORY: {}'.format(str(CATEGORY)))
                print('SUMOLOGIC_RESPONSE: {}'.format(str(postresponse)))

            if ARGS.verbose > 6:
                print('HTTPS_APPTYPE: {}'.format(mimetype))
                print('HTTPS_HEADERS: {}'.format(headers))

            if ARGS.verbose > 8:
                print('HTTPS_PAYLOAD: {}'.format(payload))

if __name__ == '__main__':
    main()
