#! /bin/python
# -*- coding: utf-8 -*-

################################################################################
#                                                                              #
#   ImdbApiClient - A client tool for http://www.imdbapi.com.                  #
#                                                                              #
################################################################################

import urllib
import ast

#
# Configuration
#
imdbApiUrl = 'http://www.imdbapi.com/?'


class ImdbApiClient:

    """
    Parameter  |  Value              |  Description
    -------------------------------------------------------------------------
    i          |  string (optional)  |  a valid IMDb movie id
    t          |  string (optional)  |  title of a movie to search for
    y          |  year (optional)    |  year of the movie
    r          |  JSON, XML          |  response data type (JSON default)
    plot       |  short, full        |  short or extended plot (short default)
    callback   |  name (optional)    |  JSONP callback name
    tomatoes   |  true (optional)    |  adds rotten tomatoes data

    While both i and t are optional at least one argument is required.
    """

    imdbApiUrl = ''

    def __init__(self, imdbApiUrl='http://www.imdbapi.com/?'):
        self.imdbApiUrl = imdbApiUrl

    def lookup (self, i=None, t=None, y=None, r=None, plot='short',
                callback=None, tomatoes = None):

        # Building the URL
        if i != None: url = imdbApiUrl + urllib.urlencode({'i': i})
        if t != None: url = imdbApiUrl + urllib.urlencode({'t': t})
        print url

        # Making the request, evaluating the response into a dictionary, return
        return ast.literal_eval(urllib.urlopen(url).read())

if __name__ == '__main__':
    iac = ImdbApiClient(imdbApiUrl)
    iac.lookup(None, 'True Grit')
