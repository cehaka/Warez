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

"""
VideoNamer.py

A tag-aware tool for renaming videos.
"""

#
# Configuration
#
videoDir = ''

class VideoNamer:
    """High Level Class"""

    # static configuration

    videoDir = ''

    # central data structure

    videos = []

    def __init__ (self, videoDir):
        self.videoDir = videoDir

    def run (self):
        self.parseDirs()
        self.makeVideos()

    def parseDirs (self):
        """Parsing the Movie Directory into self.movies"""

        try:
            self.movies = os.parseDirs(self.videoDir).sort()
        except:
            with open("videolists/0.filmlist") as f:
                self.movies = f.readlines()

    def makeVideos (self):
        """Instantiating a Movie Object for each Title"""

        movies = []
        for titleString in self.movies:
            movies.append(Video(titleString))
        self.movies = movies

    def echo (self):
        """Provoking Printing"""

        #for movie in self.movies:
        movie = self.movies[0]
        movie.echo()


class Video:
    """Self-aware Video Object"""

    # Input

    name = ''

    # Technical Things

    prefix = ''
    whitespaceCharacter = ''

    # Title and Year

    title = []
    yearStartPos = 0
    year = ''
    yearEndPos = 0

    # Tags

    audioChannels = ''
    audioCodec = ''
    audioQuality = ''
    audioSource = ''
    containerFormat = ''
    filmmaker = ''
    language = []
    videoCodec = ''
    videoQuality = ''
    videoSource = ''
    releaseGroup = ''

    def __init__ (self, name = ''):

        # Cleaning out eventual line-endings
        if name.endswith('\n'): name = name[:-1]

        # Writing the initial attribute
        self.name = name

        # Parsing the initial attribute into all
        self.parse()

        # Writing back the Changes
        #self.writeBack()

    def parse (self):

        self.parsePrefix()
        self.parseWhitespace()
        self.parseYear()
        self.parseTags()
        self.parseTitle()

    def parsePrefix (self):
        """Parsing an Eventual Prefix into self.prefix"""

        knownPrefixes = ['www.torrent.to...', 'www.ubb.to']
        for prefix in knownPrefixes:
            if self.name.startswith(prefix):
                self.prefix = prefix

    def parseWhitespace (self):
        """Parsing White Space Encoding into self.whitespaceCharacter"""

        self.detectWhitespaceEncoding()

        if self.whitespaceCharacter != '': return

        self.detectCompoundEncoding()

        if self.whitespaceCharacter != '': return

        print 'Warning: Neither a whitespace character nor caseEncoding was detected:'
        print self.name

    def  detectWhitespaceEncoding (self):
        """Detecting Replacement of Whitespace with other Characters"""

        # Count potential whitespace characters

        dots = 0
        hyphens = 0
        spaces = 0
        underscores = 0
        nonLetters = 0

        for char in self.name:
            if char == '.': dots += 1
            if char == '-': hyphens += 1
            if char == ' ': spaces += 1
            if char == '_': underscores += 1

        #print 'detectWhitespaceEncoding:', dots, hyphens, spaces, underscores, nonLetters

        # choosing the most-common non-letter character

        if dots >= spaces and \
        dots >= hyphens and \
        dots >= underscores and \
        dots != 0:
            self.whitespaceCharacter = '.'

        if spaces >= dots and \
        spaces >= hyphens and \
        spaces >= underscores and \
        spaces != 0:
            self.whitespaceCharacter = ' '

        if underscores >= dots and \
        underscores >= hyphens  and \
        underscores >= spaces and \
        underscores != 0:
            self.whitespaceCharacter = '_'

        if hyphens >= dots and \
        hyphens >= underscores and \
        hyphens >= spaces and \
        hyphens != 0:
            self.whitespaceCharacter = '-'

    def detectCompoundEncoding (self):
        """Detecting Whitespaces Encoded into CamelCase and mixedCase"""

        upperLetters = 0
        lowerLetters = 0

        for char in self.name:
            if char.isupper(): upperLetters += 1
            if char.islower(): lowerLetters += 1

        if lowerLetters >= upperLetters and \
        upperLetters != 0 and \
        self.name[0].isupper:
            self.whitespaceCharacter = 'CamelCase'

        if lowerLetters >= upperLetters and \
        upperLetters != 0 and \
        self.name[0].islower:
            self.whitespaceCharacter = 'mixedCase'

    def parseYear (self):
        """Parsing the Year Eventually Contained in self.name"""

        # Finding the year
        year = 0

        # Finding four consecutive numbers
        numberCount = 0
        yearEndPos = 0
        for char in self.name:
            if char.isdigit():
                numberCount += 1
            else:
                numberCount = 0
            yearEndPos += 1
            yearStartPos = yearEndPos - 4

            # Breaking on finding a year
            if numberCount == 4:
                year = self.name[yearStartPos:yearEndPos]

                # sanity check
                if int(year) not in range(1860, 2020):
                    numberCount = 0
                    year = 0
                    continue

                break

        # Checking whether a year was found after all
        if yearEndPos == len(self.name): return 0, 0, 0
        if year == 0: return 0, 0, 0

        # Finding the whole tag
        try:
            opener = self.name[yearStartPos - 1]
        except IndexError:
            opener = ''
        try:
            closer = self.name[yearEndPos]
        except IndexError:
            closer = ''

        # Checking for a symmetric a tag
        if (opener == '(' and closer == ')') or \
           (opener == '[' and closer == ']') or \
           (opener == '{' and closer == '}'):

            yearStartPos -= 1
            yearEndPos += 1
        else:
            opener = ''
            closer = ''

        #print 'Year found:', opener, year, closer, self.name[yearStartPos:yearEndPos], self.name

        self.yearStartPos = yearStartPos
        self.year = year
        self.yearEndPos = yearEndPos

    def requestYear (self):
        """Requesting self.year from IMDB API using ImdbApiClient"""

        #print response['Title'] + ' (' + response['Year'] + ')'
        iac = ImdbApiClient()
        iac.lookup(None, self.title)

    def parseTags (self):
        """Parsing the Tags of self.name into self.tags"""

        tags = [
            # Audio Encoding
            'ac3', 'AC3', 'DTS',

            # Audio Language
            '#de', 'German', 'german', 'Deutsch', 'deutsch',
            '#en', 'English', 'english', 'Englisch', 'english'

            # Audio Source
            'MD', 'MicDub',
            'LD', 'LineDub', 'Dubbed', 'dubbed', 'linedubbed', 'line dubbed',

            # Video Version
            '#Uncut', 'UNCUT', 'uncut',
            '#Proper', 'PROPER', 'proper',
            '#DirectorsCut', 'Directors Cut', 'Director\'s Cut',

            # Release Group
            '#CRiTiCAL', '-CRiTiCAL', 'CRiTiCAL', '-critical',
            '#CRUCiAL', '-CRUCiAL', 'CRUCiAL', '-crucial',
            '#DiViDi', '-DiViDi', 'DiViDi', '-dividi',
            '#iNTERNAL', '-iNTERNAL', 'iNTERNAL', '-internal'
            '#PLEADERS', '-PL', '-PLEADERS', '-Pleaders', '-pleaders',
            '#HDLiTE', '-HDLiTE', '-HDLite', 'HDLiTE', '-HDlite', '-hdlite',
            '#HoRnEtS', '-HoRnEtS', '-Hornets', '-hornets',
            '#NOTRADE', '-NOTRADE', '-NoTrade', '-noTrade', '-notrade'
            '#XMF', '-XMF', '-Xmf', '-xmf',

            # Source Media
            '#BDrip', 'BDRip', 'BDrip', 'bdrip', 'BD',
                      'BlueRay', 'blueray', 'BlueRayRip', 'bluerayrip',
                      'BRRIP', 'BRRip', 'BRrip', 'brrip',
            'DVD', 'DVDR', 'DVDRip', 'DVDrip', 'DVDRiP', 'DVD rip', 'dvd rip', 'dvdrip',
            'HDTVrip', 'hdtvRip', 'HDTVRIP', 'HDTVRip',

            # Video Encoding
            '#MVCD', 'MVCD', 'mvcd'
            '#h264', 'H264', 'h264', 'x264', 'X264',
            '#XViD', 'XVID', 'XViD', 'XviD', 'Xvid', 'xvid',

            # Video Resolution
            'PAL',
            '#720p', '720p',
            '#1080i', '1080i',

            # Video Source
            '#SC', 'SC', 'Screener',
            '#TS', 'TS', 'Telesync', 'TeleSync'
        ]

        for tag in tags:
            if tag in self.name:
                print tag

    def parseSuffix (self):
        """Parsing an Eventual Suffix in this.name into this.suffix"""

        knownSuffixes = [
            '.shared.for.saugstube.to.mpg'
        ]

    def parseTitle (self):
        """Parsing the Title Contained in this.name into this.title"""

        # Overwriting all parsed attributes with whitespace
        name = self.name
        print name

        if self.yearStartPos != 0 and self.yearEndPos != 0:

            # Adding an additional whitespace after the year tag position
            extension = ' '
            try:
                self.name[self.yearEndPos + 1]
            except IndexError:
                extension = ''

            # Adding 4 or 6 spaces as appropriate
            if self.yearEndPos - self.yearStartPos == 4:
                    name = name[:self.yearStartPos] + '    ' + extension + name[self.yearEndPos:]

            if self.yearEndPos - self.yearStartPos == 6:
                    name = name[:self.yearStartPos] + '      ' + extension + name[self.yearEndPos:]

        # Stripping of the superfluous whitespace
        whitespacesInRow = 0
        title = ''
        for char in name:
            if char == ' ':
                whitespacesInRow += 1
            else:
                whitespacesInRow = 0

            if whitespacesInRow == 2:
                title = title[:-1]
                whitespacesInRow = 0
            else:
                title += char

        # Stripping trailing whitespaces
        title = ' '.join(title.split())

        print title


    def echo (self):
        """Echoing This Single Video Using The Gathered Information"""

        # Striping the prefix
        name = self.name[len(self.prefix):]

        # Stripping eventual whitespaces
        mt = VideoTool()
        name = mt.stripWhitespaceCharacter(name, self.whitespaceCharacter)

        print 'Name:', name, '\n',\
               'Prefix:', self.prefix, 'Title:', self.title, 'Year:',self.year


class VideoTool:
    """Static Methods used by Video"""

    def __init__ (self):
        pass

    def stripWhitespaceCharacter (self, name, whitespaceCharacter):
    """Stripping a Given White Space Character Encoding of the given name"""

        newName = ''

        # Trivial case: whitespace character is empty
        if len(whitespaceCharacter) == 0:

            # Doing nothing
            newName = name

        # Regular case: whitespace character is set
        if len(whitespaceCharacter) == 1:

            # Re-constructing the name
            words = name.split(whitespaceCharacter)
            for word in words:
                # Skipping all non-words
                if word == whitespaceCharacter: continue

                # Skipping all empty words
                if word == '': continue

                # Adding space for all n + 1 words
                if newName != '': newName = newName + ' '

                newName = newName + word

        # Special case: The whitespace is encoded into the cases
        if whitespaceCharacter == 'CamelCase' or whitespaceCharacter == 'mixedCase':

            # Introducing whitespaces before each upper case letter
            for char in name:

                if char.isupper(): newName += ' '

                newName += char

            # Stripping heading whitespace introduced by CamelCase
            if newName.startswith(''): newName = newName[1:]

        #print 'stripWhitespaceCharacter:', name, whitespaceCharacter, newName
        return newName


if __name__ == '__main__':
    mn = VideoNamer(videoDir)
    mn.run()
    mn.echo()
