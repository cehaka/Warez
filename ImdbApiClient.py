#! /bin/python
# -*- coding: utf-8 -*-

#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import urllib
import ast

"""
ImdbApiClient

A client tool for http://www.imdbapi.com.
"""

#
# Configuration
#
imdbApiUrl = 'http://www.imdbapi.com/?'


class ImdbApiClient:

    """
    Client Tool for http://www.imdbapi.com
    """

    imdbApiUrl = ''

    def __init__(self, imdbApiUrl='http://www.imdbapi.com/?'):
        """
        Attribute Writing Constructor


        @param  imdbApiUrl  Service-URL Compatible With http://www.imdbapi.com
        """

        self.imdbApiUrl = imdbApiUrl

    def lookup (self, i=None, t=None, y=None, r=None, plot='short',
                callback=None, tomatoes = None):
        """
        =========   =================   ======================================
        Parameter   Value               Description
        =========   =================   ======================================
        i           string (optional)   a valid IMDb movie id
        t           string (optional)   title of a movie to search for
        y           year (optional)     year of the movie
        r           JSON, XML           response data type (JSON default)
        plot        short, full         short or extended plot (short default)
        callback    name (optional)     JSONP callback name
        tomatoes    true (optional)     adds rotten tomatoes data
        =========   =================   ======================================

        While both i and t are optional at least one argument is required.
        """

        # Building the URL
        if i != None: url = imdbApiUrl + urllib.urlencode({'i': i})
        if t != None: url = imdbApiUrl + urllib.urlencode({'t': t})
        print url

        # Making the request, evaluating the response into a dictionary, return
        return ast.literal_eval(urllib.urlopen(url).read())

if __name__ == '__main__':
    iac = ImdbApiClient(imdbApiUrl)
    iac.lookup(None, 'True Grit')
