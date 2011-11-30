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
import pprint
import types

class Video:
    """Self-aware Video Object"""

    # Input

    dirName = ''

    # Technical Things
    spaceCharacter = ''

    # Things in self.dirName
    prefixes = []
    suffixes = []

    tags = {
        'year': {'value': '', 'end': 0, 'start': 0},
        'audio channels': {'value': '', 'end': 0, 'start': 0},
        'audio codec': {'value': '', 'end': 0, 'start': 0},
        'audio language': {'value': '', 'end': 0, 'start': 0},
        'audio source': {'value': '', 'end': 0, 'start': 0},
        'container format': {'value': '', 'end': 0, 'start': 0},
        'filmmaker': {'value': '', 'end': 0, 'start': 0},
        'video codec': {'value': '', 'end': 0, 'start': 0},
        'video source': {'value': '', 'end': 0, 'start': 0},
        'release group': {'value': '', 'end': 0, 'start': 0},
        'subtitle language': {'value': '', 'end': 0, 'start': 0}
    }

    # Output

    title = []

    def __init__ (self, dirName = ''):
        """
        Attribute Writing Constructor

        @param  dirName    Name of the directory represented by this video.
        """

        # Getting a VideoTool instance
        self.vT = VideoTool.VideoTool()

        # Cleaning out eventual line-endings
        if dirName.endswith('\n'): dirName = dirName[:-1]

        # Writing the initial attribute
        self.dirName = dirName

        # Parsing the initial attribute into all
        self.parse()

        # Writing back the Changes
        #self.rename()

    def parse (self):
        """Parsing self.dirName into Attributes"""

        self.parsePrefixes()
        self.parseSuffixes()
        self.parseEncoding()
        self.parseYear()
        self.parseTags()
        self.parseTitle()

    def parseEncoding (self):
        """Parsing White Space Encoding into self.spaceCharacter"""

        self.parseEncodingWhitespace()

        if self.spaceCharacter != '': return

        self.parseEncodingCompound()

        if self.spaceCharacter != '': return

        print 'Warning:' + \
              'Neither a space character nor caseEncoding was detected:' + \
               self.dirName

    def  parseEncodingWhitespace (self):
        """Detecting Replacement of Whitespace with other Characters"""

        # Count potential space characters

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

        # choosing the most-common non-letter character

        if dots >= spaces and \
        dots >= hyphens and \
        dots >= underscores and \
        dots != 0:
            self.spaceCharacter = '.'

        if spaces >= dots and \
        spaces >= hyphens and \
        spaces >= underscores and \
        spaces != 0:
            self.spaceCharacter = ' '

        if underscores >= dots and \
        underscores >= hyphens  and \
        underscores >= spaces and \
        underscores != 0:
            self.spaceCharacter = '_'

        if hyphens >= dots and \
        hyphens >= underscores and \
        hyphens >= spaces and \
        hyphens != 0:
            self.spaceCharacter = '-'

    def parseEncodingCompound (self):
        """Detecting Whitespaces Encoded into CamelCase and mixedCase"""

        upperLetters = 0
        lowerLetters = 0

        for char in self.dirName:
            if char.isupper(): upperLetters += 1
            if char.islower(): lowerLetters += 1

        if lowerLetters >= upperLetters and \
        upperLetters != 0 and \
        self.dirName[0].isupper:
            self.spaceCharacter = 'CamelCase'

        if lowerLetters >= upperLetters and \
        upperLetters != 0 and \
        self.dirName[0].islower:
            self.spaceCharacter = 'mixedCase'

    def parsePrefixes (self):
        """Parsing an Eventual Prefix into self.prefix"""

        knownPrefixes = [
            'www.torrent.to...',
            'www.ubb.to'
        ]

        self.prefixes = [] # HACK I don't know why, but this is necessary.

        # Repeating until there is no further prefix to be found.
        dirNameTemp = self.dirName
        anotherPrefixWasFound = True
        while anotherPrefixWasFound:

            anotherPrefixWasFound = False
            for prefix in knownPrefixes:

                if dirNameTemp.startswith(prefix):
                    self.prefixes.append(prefix)
                    dirNameTemp = dirNameTemp[len(prefix):]

                    anotherPrefixWasFound = True
                    break

    def parseSuffixes (self):
        """Parsing an eventual Suffixes in this.dirName into this.suffixes."""

        knownSuffixes = [
            '.shared.for.saugstube.to.mpg',
             '.seeded.by.www.p2p-crew.to', 'seeded by www.p2p-crew.to',
        ]

        self.suffixes = [] # HACK I don't know why, but this is necessary.

        # Repeating until there is no further prefix to be found.
        dirNameTemp = self.dirName
        anotherSuffixWasFound = True
        while anotherSuffixWasFound:

            anotherSuffixWasFound = False
            for suffix in knownSuffixes:

                if dirNameTemp.endswith(suffix):
                    self.suffixes.append(suffix)
                    dirNameTemp = dirNameTemp[:len(suffix)]

                    anotherSuffixWasFound = True
                    break



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

        self.tags['year']['start'] = yearStartPos
        self.tags['year']['value'] = year
        self.tags['year']['end'] = yearEndPos

    def requestYear (self):
        """Requesting self.tags['year'] from IMDB API using ImdbApiClient"""

        #print response['Title'] + ' (' + response['Year'] + ')'
        iac = ImdbApiClient()
        iac.lookup(None, self.title)

        #self.tags['year']['value'] = resultYear

    def parseTags (self):
        """Parsing the Tags of self.dirName into self.tags"""

        for category in self.tags:

            # Do not map year to anything
            if category == 'year': continue

            for synonyms in self.vT.getSynonyms()[category]:
                for synonym in synonyms:

                    self.parseTag(category, synonym)

    def parseTag (self, category, synonym):
        """Parsing a single given synonym of a given category into self.tags"""

        # Checking That The Tag Is in self.dirName
        if synonym not in self.dirName: return

        # Determining the hashTag
        hashTag = ''
        for synonyms in self.vT.getSynonyms()[category]:
            if synonym in synonyms:
                hashTag = synonyms[0]

        # Saving
        self.tags[category]['value'] = hashTag

    def parseTitle (self):
        """Parsing the title from self.dirName into self.title, using self.*"""

        # Loading the directory name as a starting point
        self.title = self.dirName

        # Overwriting year with spaces
        if self.tags['year']['start'] != 0 and self.tags['year']['end'] != 0:

            # Adding a space after the year tag position, if something follows it
            extension = ' '
            try:
                self.title[self.tags['year']['end'] + 1]
            except IndexError:
                extension = ''

            # Adding 4 or 6 for the year and one for the extension, as appropriate
            self.title = self.title[:self.tags['year']['start']] + \
                         ''.rjust(self.tags['year']['end'] - self.tags['year']['start']) + \
                         extension + \
                         self.title[self.tags['year']['end']:]

        # Stripping all prefixes and expanding by their length to conserve positions
        for prefix in self. prefixes:
            self.title = self.title[len(prefix):].ljust(len(prefix), ' ')

        # Stripping all suffixes and expanding by their length to conserve positions
        for suffix in self. suffixes:
            self.title = self.title[:-len(suffix)].rjust(len(suffix), ' ')

        # Translating into spaces
        videoTool = VideoTool.VideoTool()
        self.title = videoTool.decodeSpaces(self.title, self.spaceCharacter)

        # Stripping of double spaces
        newTitle = ''

        spacesInRow = 0
        for char in self.title:
            if char == ' ':
                spacesInRow += 1
            else:
                spacesInRow = 0

            if spacesInRow == 2:
                # Double space detected, removing it
                newTitle = newTitle[:-1]
                spacesInRow = 0
            else:
                newTitle += char

        self.title = newTitle

        # Stripping trailing spaces
        self.title = ' '.join(self.title.split())

    def printMethods(self):
        """Printing all methods of this object and their docstring."""

        for name in sorted(dir(self)):
            attr = getattr(self,name)
            if callable(attr):
                print name,':',attr.__doc__

    def printAttributes(self):
        """Print all the attributes of this object and their value."""

        for name in sorted(dir(self)):

            attr = getattr(self,name)
            if not callable(attr):

                if type(attr) is types.DictType:
                    print name, ':'
                    pprint.pprint(attr)
                else:
                    print name, ':', attr


    def printAll(self):
        """Calls all the methods of this object."""

        for name in sorted(dir(self)):
            attr = getattr(self,name)
            if callable(attr) and name != 'print_all' and name != '__init__':
                attr() # calling the method
