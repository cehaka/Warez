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
videoPath = '/mnt/Media/Video/Filme'

class VideoNamer:
    """High Level Class"""

    # Central data structure
    videoDirs = []
    videoFiles = []

    def __init__ (self, videoPath):
        """Constructor"""

        # Initializing videos
        self.parseVideos(videoPath)
        self.makeVideos(videoPath)

    def parseVideos (self, videoPath):

        if os.path.isdir(videoPath):
            self.parseVideoDir(videoPath)
        else:
            self.parseVideoList(self)

    def parseVideoDir (self, videoPath):
        """
        Parses the video directory into self.videos.

        @param  videoPath   A path to a directory containing directories
                            containing videos.
        """

        for root, dirs, files in os.walk(videoPath):
            self.videoDirs = dirs
            self.videos = files
            break # We only care about the top level, for now.

    def parseVideoList (self, listPath):
        """
        Parses a list of video directories into self.videos.

        @param  listPath    Path to a list of directories containing directories
                            containing videos, for testing purposes.
        """

        with open("videolists/2.filmlist") as f:
            self.videos = f.readlines()

    def makeVideos (self, videoPath):
        """Instantiating A Video Object for Each Title"""

        for titleString in self.videoDirs:
            v = Video.Video(videoPath, titleString)

if __name__ == '__main__':
    vn = VideoNamer(videoPath)
