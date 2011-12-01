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

import os
import string
import ImdbApiClient
import Video

"""
VideoNamer.py

A tag-aware tool for renaming videos.
"""

#
# Configuration
#
videos = ''

class VideoNamer:
    """High Level Class"""

    # Central data structure

    videos = ''

    def __init__ (self, videos):
        """
        Constructor

        @param  videos  Either a folder containing videos or a list of videos.
        """

        self.videos = videos

        # Initializing videos
        self.parseDirs()
        self.makeVideos()

    def parseDirs (self):
        """Parsing the Video Directory into self.videos"""

        try:
            self.videos = os.parseDirs(self.movies).sort()
        except:
            #with open("videolists/2.filmlist") as f:
             #   self.videos = f.readlines()
            self.videos = os.listdir('/mnt/Media/Video/Filme/')

    def makeVideos (self):
        """Instantiating A Video Object for Each Title"""

        videos = []
        for titleString in self.videos:
            v = Video.Video(titleString)
            videos.append(v)
        self.videos = videos

if __name__ == '__main__':
    mn = VideoNamer(videos)
