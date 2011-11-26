#! /bin/python

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

import os

"""
DoxyCleaner

Removes the 'Generated on' notes from Doxygen's HTMLs for Git.
"""

class DoxyCleaner:

    def __init__(self):
        pass

    def run (self):

        self.cleanHTMLs(self.gatherHTMLs())

    def gatherHTMLs (self):
        return os.listdir('./html/')

    def cleanHTMLs (self, htmls):
        for html in htmls:
            if html.endswith('.html'):
                self.cleanHTML(html)

    def cleanHTML (self, html):
        with open('./html/' + html, 'r') as f:
            data = f.read()
            data = data[:-237] + data[-17:]

        with open('./html/' + html, 'w') as f:
            f.write(data)


if __name__ == '__main__':
    dc = DoxyCleaner()
    dc.run()