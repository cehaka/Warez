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

class VideoCreator:
    """Creates directories for all included videos."""

    def __init__ (self):
        pass

    def run (self):
        """Creates a directory for each video in each filmlist."""

        if not os.environ['HOME'].startswith('/home/'):
            print "VideoCreator.run(): Your home path seems odd. Aborting."
            return

        # Gathering videoLists
        videoLists = os.parseDirs('videoLists/')

        # Gathering videos
        videos = []
        for videoList in videoLists:
            with open('videoLists/' + videoList) as f:
                videos.append(f.readlines())

        # Creating video directories
        for videoList in videos:
            for video in videoList:
                try:
                    os.mkdir(os.environ['HOME']+ '/Videos/' + video[:-1])

                # Ignoring if file already exists
                except OSError:
                    pass

if __name__ == '__main__':
    vc = VideoCreator()
    vc.run()
