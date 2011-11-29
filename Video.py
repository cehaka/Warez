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

import VideoTool

class Video:
    """Self-aware Video Object"""

    # Input

    dirName = ''

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

    # Tag Aliases

    tags = {

        'Audio Encoding':[\
            ['#ac3', 'ac3', 'AC3', 'DTS']
        ],

        'Audio Language':[\
            ['#de', 'German', 'german', 'Deutsch', 'deutsch'],
            ['#en', 'English', 'english', 'Englisch', 'english']
        ],

        'Audio Source':[\
            ['#md', 'MD', 'MicDub'],
            ['#ld', 'LD', 'LineDub', 'Dubbed', 'dubbed', 'linedubbed', 'line dubbed']
        ],

        'Video Version':[\
            ['#uncut', 'UNCUT', 'uncut'],
            ['#proper', 'PROPER', 'proper'],
            ['#directorsCut', 'Directors Cut', 'Director\'s Cut']
        ],

        'Release Group':[\
            ['#CRiTiCAL', '-CRiTiCAL', 'CRiTiCAL', '-critical'],
            ['#CRUCiAL', '-CRUCiAL', 'CRUCiAL', '-crucial'],
            ['#DiViDi', '-DiViDi', 'DiViDi', '-dividi'],
            ['#iNTERNAL', '-iNTERNAL', 'iNTERNAL', '-internal'],
            ['#PLEADERS', '-PL', '-PLEADERS', '-Pleaders', '-pleaders'],
            ['#HDLiTE', '-HDLiTE', '-HDLite', 'HDLiTE', '-HDlite', '-hdlite'],
            ['#HoRnEtS', '-HoRnEtS', '-Hornets', '-hornets'],
            ['#NOTRADE', '-NOTRADE', '-NoTrade', '-noTrade', '-notrade'],
            ['#XMF', '-XMF', '-Xmf', '-xmf'],
            ['#KiNOWELT', '-KiNOWELT', '-kinowelt']
        ],

        'Source Media':[\
            ['#BDrip', 'BDRip', 'BDrip', 'bdrip', 'BD',
                'BlueRay', 'blueray', 'BlueRayRip', 'bluerayrip',
                'BRRIP', 'BRRip', 'BRrip', 'brrip'],
            ['#DVDrip', 'DVDRip', 'DVDrip', 'DVDRiP', 'DVD rip', 'dvd rip',
                'dvdrip', 'DVD', 'DVDR'],
            ['#HDTVrip', 'HDTVrip', 'hdtvRip', 'HDTVRIP', 'HDTVRip', 'HDTV', 'hdtv']
        ],

        'Video Encoding':[\
            ['#MVCD', 'MVCD', 'mvcd'],
            ['#h264', 'H264', 'h264', 'x264', 'X264'],
            ['#XViD', 'XVID', 'XViD', 'XviD', 'Xvid', 'xvid']
        ],

        'Video Resolution':[\
            ['#NTSC', 'NTSC', 'ntsc'],
            ['#PAL', 'PAL'],
            ['#720p', '720p'],
            ['#1080i', '1080i']
        ],

        'Video Source':[\
            ['#SC', 'SC', 'Screener'],
            ['#TS', 'TS', 'Telesync', 'TeleSync']
        ]
    }

    def __init__ (self, dirName = ''):
        """
        Attribute Writing Constructor

        @param  dirName    Name of the directory represented by this video.
        """

        # Cleaning out eventual line-endings
        if dirName.endswith('\n'): dirName = dirName[:-1]

        # Writing the initial attribute
        self.dirName = dirName

        # Parsing the initial attribute into all
        self.parse()

        # Writing back the Changes
        #self.writeBack()

    def parse (self):
        """Parsing self.dirName into Attributes"""

        self.parsePrefix()
        self.parseWhitespace()
        self.parseYear()
        self.parseTags()
        self.parseTitle()

    def parsePrefix (self):
        """Parsing an Eventual Prefix into self.prefix"""

        knownPrefixes = ['www.torrent.to...', 'www.ubb.to']
        for prefix in knownPrefixes:
            if self.dirName.startswith(prefix):
                self.prefix = prefix

    def parseWhitespace (self):
        """Parsing White Space Encoding into self.whitespaceCharacter"""

        self.detectWhitespaceEncoding()

        if self.whitespaceCharacter != '': return

        self.detectCompoundEncoding()

        if self.whitespaceCharacter != '': return

        print 'Warning: Neither a whitespace character nor caseEncoding was detected:'
        print self.dirName

    def  detectWhitespaceEncoding (self):
        """Detecting Replacement of Whitespace with other Characters"""

        # Count potential whitespace characters

        dots = 0
        hyphens = 0
        spaces = 0
        underscores = 0
        nonLetters = 0

        for char in self.dirName:
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

        for char in self.dirName:
            if char.isupper(): upperLetters += 1
            if char.islower(): lowerLetters += 1

        if lowerLetters >= upperLetters and \
        upperLetters != 0 and \
        self.dirName[0].isupper:
            self.whitespaceCharacter = 'CamelCase'

        if lowerLetters >= upperLetters and \
        upperLetters != 0 and \
        self.dirName[0].islower:
            self.whitespaceCharacter = 'mixedCase'

    def parseYear (self):
        """Parsing the Year Eventually Contained in self.dirName"""

        # Finding the year
        year = 0

        # Finding four consecutive numbers
        numberCount = 0
        yearEndPos = 0
        for char in self.dirName:
            if char.isdigit():
                numberCount += 1
            else:
                numberCount = 0
            yearEndPos += 1
            yearStartPos = yearEndPos - 4

            # Breaking on finding a year
            if numberCount == 4:
                year = self.dirName[yearStartPos:yearEndPos]

                # sanity check
                if int(year) not in range(1860, 2020):
                    numberCount = 0
                    year = 0
                    continue

                break

        # Checking whether a year was found after all
        if yearEndPos == len(self.dirName): return 0, 0, 0
        if year == 0: return 0, 0, 0

        # Finding the whole tag
        try:
            opener = self.dirName[yearStartPos - 1]
        except IndexError:
            opener = ''
        try:
            closer = self.dirName[yearEndPos]
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

        #print 'Year found:', opener, year, closer, self.dirName[yearStartPos:yearEndPos], self.dirName

        self.yearStartPos = yearStartPos
        self.year = year
        self.yearEndPos = yearEndPos

    def requestYear (self):
        """Requesting self.year from IMDB API using ImdbApiClient"""

        #print response['Title'] + ' (' + response['Year'] + ')'
        iac = ImdbApiClient()
        iac.lookup(None, self.title)

    def parseTags (self):
        """Parsing the Tags of self.dirName into self.tags"""

        for category in self.tags:
            for synonyms in self.tags[category]:
                for synonym in synonyms:
                    #print category, '-', synonyms, '-', synonym

                    self.parseTag(category, synonym)

    def parseTag (self, category, synonym):

        # Checking That The Tag Is in self.dirName
        if synonym not in self.dirName: return

        # Determining The Hash Tag
        for synonyms in self.tags[category]:
            if synonym in synonyms:
                hashTag = synonyms[0]

        # Saving
        if category == 'Audio Encoding': self.audioEncoding = hashTag
        if category == 'Audio Language': self.audioLanguage = hashTag
        if category == 'Audio Source': self.audioSource= hashTag
        if category == 'Release Group': self.releaseGroup = hashTag
        if category == 'Source Media': self.sourceMedia = hashTag
        if category == 'Video Encoding': self.videoEncoding = hashTag
        if category == 'Video Resolution': self.videoResolution = hashTag
        if category == 'Video Source': self.videoSource = hashTag
        if category == 'Video Version': self.videoVersion= hashTag

    def parseSuffix (self):
        """Parsing an Eventual Suffix in this.dirName into this.suffix"""

        knownSuffixes = [
            '.shared.for.saugstube.to.mpg'
        ]

        # Repeating until there is no further suffix to be found.
        breakCondition = False
        while breakContidition:

            breakCondition = True
            for suffix in knownSuffixes:

                if self.dirName.endswith(suffix):
                    self.suffixes += suffix
                    breakCondition = False
                    break

    def parseTitle (self):
        """Parsing the title contained in this.dirName into this.title using all other attributes."""

        # Overwriting all parsed attributes with whitespace
        dirName = self.dirName
        print dirName

        if self.yearStartPos != 0 and self.yearEndPos != 0:

            # Adding an additional whitespace after the year tag position
            extension = ' '
            try:
                self.dirName[self.yearEndPos + 1]
            except IndexError:
                extension = ''

            # Adding 4 or 6 spaces as appropriate
            if self.yearEndPos - self.yearStartPos == 4:
                    dirName = dirName[:self.yearStartPos] + '    ' + extension + dirName[self.yearEndPos:]

            if self.yearEndPos - self.yearStartPos == 6:
                    dirName = dirName[:self.yearStartPos] + '      ' + extension + dirName[self.yearEndPos:]

        # Stripping of the superfluous whitespace
        whitespacesInRow = 0
        title = ''
        for char in dirName:
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


    def parseTitle (self):

        # Stripping the prefix
        dirName = self.dirName[len(self.prefix):]

        # Stripping eventual whitespaces
        mt = VideoTool.VideoTool()
        dirName = mt.stripWhitespaceCharacter(dirName, self.whitespaceCharacter)

    def echo (self):
        """Echoing this single video."""

        self.printAttributes()

    def printMethods(self):
        """Printing all methods of this object and their docstring."""

        for name in dir(self):
            attr = getattr(self,name)
            if callable(attr):
                print name,':',attr.__doc__

    def printAttributes(self):
        """Print all the attributes of this object and their value."""

        for name in dir(self):

            # Skipping self.tags
            if name == 'tags': continue

            attr = getattr(self,name)
            if not callable(attr):
                print name,':',attr

    def printAll(self):
        """Calls all the methods of this object."""

        for name in dir(self):
            attr = getattr(self,name)
            if callable(attr) and name != 'print_all' and name != '__init__':
                attr() # calling the method
