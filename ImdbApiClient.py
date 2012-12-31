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
import json

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

    def build_url (self, i=None, t=None):
        """Builds an URL from parameters."""
        if i != None: url = imdbApiUrl + urllib.parse.urlencode({'i': i})
        if t != None: url = imdbApiUrl + urllib.parse.urlencode({'t': t})
        return url

    def lookup (self, i=None, t=None, y=None, r=None, plot='short',
                callback=None, tomatoes=None):
        """
        =========   =================   ======================================
        Parameter   Value               Description
        =========   =================   ======================================
        s (NEW!)    string (optional)   title of a movie to search for
        i           string (optional)   a valid IMDb movie id
        t           string (optional)   title of a movie to return
        y           year (optional)     year of the movie
        r           JSON, XML           response data type (JSON default)
        plot        short, full         short or extended plot (short default)
        callback    name (optional)     JSONP callback name
        tomatoes    true (optional)     adds rotten tomatoes data
        =========   =================   ======================================

        While both i and t are optional at least one argument is required.
        """

        if not i and not t:
            print('ImdbApiClient: Error: neither i nor t are set.')
            return

        url = self.build_url(i=i, t=t)
        print(url)

        # Making the request, evaluating the response into a dictionary, return
        # json_string = urllib.urlopen(url).read() # TODO
        # json_string = """{u'Plot': u"A tough U.S. Marshal helps a stubborn young woman track down her father's murderer.", u'Rated': u'PG-13', u'Title': u'True Grit', u'Poster': u'http://ia.media-imdb.com/images/M/MV5BMjIxNjAzODQ0N15BMl5BanBnXkFtZTcwODY2MjMyNA@@._V1_SX300.jpg', u'Writer': u'Joel Coen, Ethan Coen', u'Response': u'True', u'Director': u'Ethan Coen, Joel Coen', u'Released': u'22 Dec 2010', u'Actors': u'Jeff Bridges, Matt Damon, Hailee Steinfeld, Josh Brolin', u'Year': u'2010', u'Genre': u'Adventure, Drama, Western', u'Runtime': u'1 h 50 min', u'imdbRating': u'7.8', u'imdbVotes': u'142,737', u'imdbID': u'tt1403865'}"""
        json_string = "{'Plot': 'A tough U.S. Marshal helps a stubborn young woman track down her father's murderer.', 'Rated': 'PG-13', 'Title': 'True Grit', 'Poster': 'http://ia.media-imdb.com/images/M/MV5BMjIxNjAzODQ0N15BMl5BanBnXkFtZTcwODY2MjMyNA@@._V1_SX300.jpg', 'Writer': 'Joel Coen, Ethan Coen', 'Response': 'True', 'Director': 'Ethan Coen, Joel Coen', 'Released': '22 Dec 2010', 'Actors': 'Jeff Bridges, Matt Damon, Hailee Steinfeld, Josh Brolin', 'Year': '2010', 'Genre': 'Adventure, Drama, Western', 'Runtime': '1 h 50 min', 'imdbRating': '7.8', 'imdbVotes': '142,737', 'imdbID': 'tt1403865'}"
        return json.loads(json_string)


if __name__ == '__main__':
    iac = ImdbApiClient(imdbApiUrl)
    json_parsed = iac.lookup(None, 'True Grit')
    print(json_parsed)
    for key in json_parsed.keys():
        print(key, json_parsed[key])
