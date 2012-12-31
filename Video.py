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

import ImdbApiClient
import VideoUtil

import os
import pprint
import shutil
import string
import types
from datetime import datetime

class Video:
    """Self-aware Video Object"""

    # Input

    dirName = ''
    videoDir = ''

    # Technical Things
    whitespace = ''

    # Things in self.dirName
    prefixes = []
    suffixes = []

    tags = ''

    # Output

    title = []

    def initPrefixes (self):
        """Initializing self.prefixes to an empty list."""

        self.prefixes = []

    def initSuffixes (self):
        """Initializing self.suffixes to an empty list."""

        self.suffixes = []

    def initTags (self):
        """Initializes self.tags to zero values"""

        self.tags = {
            'audio channels':{'name':0, 'end':0, 'start':0},
            'audio codec':{'name':0, 'end':0, 'start':0},
            'audio language':{'name':0, 'end':0, 'start':0},
            'audio source':{'name':0, 'end':0, 'start':0},
            'container format':{'name':0, 'end':0, 'start':0},
            'filmmaker':{'name':0, 'end':0, 'start':0},
            'video codec':{'name':0, 'end':0, 'start':0},
            'video resolution':{'name':0, 'end':0, 'start':0},
            'video source':{'name':0, 'end':0, 'start':0},
            'release group':{'name':0, 'end':0, 'start':0},
            'source media':{'name':0, 'end':0, 'start':0},
            'subtitle language':{'name':0, 'end':0, 'start':0},
            'year':{'name':0, 'end':0, 'start':0}
        }

    def initAll (self):
        # Initializing the tags
        self.initTags()
        self.initPrefixes()
        self.initSuffixes()

        # Getting a VideoUtil instance
        self.vT = VideoUtil.VideoUtil()

    def __init__ (self, videoDir='', dirName=''):
        """
        Attribute Writing Constructor

        @param  dirName    Name of the directory represented by this video.
        """

        # Initializing all needed things
        self.initAll()

        # Cleaning out eventual line-endings
        if dirName.endswith('\n'): dirName = dirName[:-1]

        # Writing the initial attribute
        self.dirName = dirName
        self.videoDir = videoDir

        # Sanity Check
        if self.dirName == '':
            raise
            print("Warning: Empty dirName. Skipping this Video.")
            return

        # Parsing initial attribute into self.tags
        self.parse()

        # Checking whether full coverage was archived
        self.checkFullCoverage()

        # Printing for debugging
        if not self.fullCoverage: self.printAttributes()

        # Renaming if appropriate
        self.rename()

    def parse (self):
        """Parsing self.dirName into Attributes"""

        self.parsePrefixes()
        self.parseSuffixes()
        self.parseEncoding()

        self.parseTags()
        self.parseYear()

        self.parseTitle()

        # Generating output information
        self.requestYear()

        self.generateTitle()

    def parseEncoding (self):
        """Parsing White Space Encoding into self.whitespace"""

        self.parseEncodingWhitespace()

        if self.whitespace != '': return

        self.parseEncodingCompound()

        if self.whitespace != '': return

        print('Warning:' + \
              'Neither a space character nor caseEncoding was detected:' + \
               self.dirName)

    def  parseEncodingWhitespace (self):
        """Detecting Replacement of Whitespace with other Characters"""

        # Count potential space characters

        dots = 0
        hyphens = 0
        spaces = 0
        underscores = 0
        nonLetters = 0

        for char in self.dirName:
            if char == '.':
                dots += 1
            if char == '-':
                hyphens += 1
            if char == ' ':
                spaces += 1
            if char == '_':
                underscores += 1

        # choosing the most-common non-letter character

        if dots >= spaces and \
        dots >= hyphens and \
        dots >= underscores and \
        dots != 0:
            self.whitespace = '.'

        if spaces >= dots and \
        spaces >= hyphens and \
        spaces >= underscores and \
        spaces != 0:
            self.whitespace = ' '

        if underscores >= dots and \
        underscores >= hyphens  and \
        underscores >= spaces and \
        underscores != 0:
            self.whitespace = '_'

        if hyphens >= dots and \
        hyphens >= underscores and \
        hyphens >= spaces and \
        hyphens != 0:
            self.whitespace = '-'

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
            self.whitespace = 'CamelCase'

        if lowerLetters >= upperLetters and \
        upperLetters != 0 and \
        self.dirName[0].islower:
            self.whitespace = 'mixedCase'

    def parsePrefixes (self):
        """Parsing an Eventual Prefix into self.prefix"""

        knownPrefixes = [
            'www.bitreactor.to...', 'www bitreactor to_', 'www.bitreactor.to_',
            '[www.byte.to]', '[www byte to]', 'www byte to', 'www.byte.to',
            'www.torrent.to...',
            '[www top-hitz com]', '[www top-hitz com]...', '[www.top-hitz.com]...',
            'www.top-hitz.com...', 'www top-hitz com...', 'www.top-hitz.com...',
            'www top-hitz com',
            'www.ubb.to'
        ]

        self.initPrefixes()  # HACK I don't know why, but this is necessary.

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
             'www mvgroup org'
        ]

        self.initSuffixes()  # HACK I don't know why, but this is necessary.

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

        current_year = datetime.now().year()

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

            # Breaking on finding a :
            if numberCount == 4:
                year = self.dirName[yearStartPos:yearEndPos]

                # sanity check
                if int(year) not in range(1860, current_year + 2):
                    numberCount = 0
                    year = 0
                    continue

                break

        # Checking whether a year was found after all
        if yearEndPos == len(self.dirName):
            return 0, 0, 0
        if year == 0:
            return 0, 0, 0

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

        # Checking for year-title-movies

        if year == 2001 and \
           'Odyssee' in self.dirName and \
            'im' in self.dirName and \
            'Weltraum' in self.dirName:

            yearStartPos = 0
            year = 0
            yearEndPos = 0

        if year == 2010 and \
           'Das' in self.dirName and \
           'Jahr' in self.dirName and \
           'in' in self.dirName and \
           'dem' in self.dirName and \
           'wir' in self.dirName and \
           'Kontakt' in self.dirName and \
           'aufnehmen' in self.dirName:

            yearStartPos = 0
            year = 0
            yearEndPos = 0

        self.tags['year']['start'] = yearStartPos
        self.tags['year']['name'] = year
        self.tags['year']['end'] = yearEndPos

    def parseTags (self):
        """Parsing the Tags of self.dirName into self.tags"""

        self.initTags()

        for category in self.tags:

            # Do not map : to anything
            if category == 'year': continue

            for synonyms in self.vT.getSynonyms()[category]:

                # Determine the longest variant of a synonym
                maxLength = 0
                longestSynonym = ''

                for synonym in synonyms:

                    # use whitespace of this video
                    synonym = synonym.replace(' ', self.whitespace)

                    # If synonym was not found, skip
                    if synonym not in self.dirName: continue

                    # If synonym is too small, skip
                    if len(synonym) <= maxLength: continue

                    maxLength = len(synonym)
                    longestSynonym = synonym

                if longestSynonym != '': self.parseTag(category, longestSynonym)

    def parseTag (self, category, synonym):
        """Parsing a single given synonym of a given category into self.tags"""

        # Checking That The Tag Is in self.dirName
        if synonym not in self.dirName: return

        # Determining the position
        start = self.dirName.index(synonym)
        end = start + len(synonym)

        # Determining the concurrent hashTag
        hashTag = ''
        for synonyms in self.vT.getSynonyms()[category]:
            if synonym.replace(self.whitespace, ' ') in synonyms:
                hashTag = synonyms[0]

        # Saving
        self.tags[category]['end'] = end
        self.tags[category]['start'] = start
        self.tags[category]['name'] = hashTag

    def parseTitle (self):
        """Parsing the title from self.dirName into self.title, using self.*"""

        # Loading the directory name as a starting point
        self.title = self.dirName

        # Overwriting each tag with spaces as a placeholder
        for tag in self.tags:

            # Skipping tags with empty values
            if self.tags[tag]['end'] == 0 or \
               self.tags[tag]['name'] == 0:

                continue

            # Adding spaces for the tag, as appropriate
            self.title = \
                self.title[:self.tags[tag]['start']] + \
                 ''.rjust(
                    self.tags[tag]['end'] - self.tags[tag]['start']
                 ) + \
                 self.title[self.tags[tag]['end']:]

        # Stripping all prefixes and expanding by their length to conserve positions
        for prefix in self. prefixes:
            self.title = self.title[len(prefix):].ljust(len(prefix), ' ')

        # Stripping all suffixes and expanding by their length to conserve positions
        for suffix in self. suffixes:
            self.title = self.title[:-len(suffix)].rjust(len(suffix), ' ')

        # Translating into spaces
        videoTool = VideoUtil.VideoUtil()
        self.title = videoTool.decodeSpaces(self.title, self.whitespace)

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

        # Stripping facing and trailing nonsense
        while not self.title[len(self.title) - 1] in string.ascii_letters and \
              not self.title[len(self.title) - 1] in string.digits and \
              not self.title[len(self.title) - 1] in ['(', ')', '[', ']', '{', '}', '<', '>'] and \
              not self.title[len(self.title) - 1] in ['.', '!', '?']:

            self.title = self.title[:-1]

        while not self.title[0] in string.ascii_letters and \
              not self.title[0] in string.digits and \
              not self.title[0] in ['(', ')', '[', ']', '{', '}', '<', '>'] and \
              not self.title[0] in ['.', '!', '?']:

            self.title = self.title[1:]

        # Cleaning up own artefacts
        self.title = self.title.replace('(0)', ' ')
        self.title = self.title.replace(' # ', ' ')

        # Cleaning up unwanted tags
        self.title = self.title.replace('READ NFO', ' ')

    def requestYear (self):
        """Requesting self.tags['year'] from IMDB API using ImdbApiClient, if necassary."""

        return  # disabled for now

        # Requesting year, if it is unknown
        if self.tags['year']['name'] != 0: return

        if self.title == 0:
            print('Video.requestYear: Error: No title is set. Can\'t request.')

        print(self.title)

        # print response['Title'] + ' (' + response['Year'] + ')'
        iac = ImdbApiClient.ImdbApiClient()
        result = iac.lookup(None, self.title)

        # Saving
        self.tags['year']['name'] = result['Year']

    def generateTitle (self):
        """Generating the title according to a format representing all attributes."""

        # Skipping empty years
        if not self.tags['year']['name'] == 0:

            self.title += ' ' + '(' + str(self.tags['year']['name']) + ')'

        for tag in self.tags:

            # Skipping empty tags
            if self.tags[tag]['end'] == 0 or \
               self.tags[tag]['name'] == 0 :

                continue

            # Skipping year
            if tag == 'year': continue

            self.title += ' ' + self.tags[tag]['name']

    def checkFullCoverage (self):
        """Calculates the coverage of self.tags over self.dirName."""

        # Overwriting all parsed tags with spaces
        tempTitle = self.title

        for tag in self.tags:

            if self.tags[tag]['start'] >= self.tags['year']['end']:

                tempTitle = tempTitle[:self.tags[tag]['start']] + \
                            ''.rjust(len(str(self.tags[tag]['name']))) + \
                            tempTitle[self.tags[tag]['end']:]

        # Counting all remaining non-space characters behind the year
        count = 0
        for char in tempTitle[self.tags['year']['end'] + 1:]:
            if char in string.whitespace or char == self.whitespace:
                continue
            count += 1

        # Accepting, if there was nothing left over
        if self.tags['year']['end'] != 0 and count == 0:
            self.fullCoverage = True
        else:
            self.fullCoverage = False

    def rename (self):
        """Renaming all directories that have been losslessly parsed"""

        if self.dirName == self.title: return

        source = self.dirName
        target = self.title

        source_path = self.videoDir + os.sep + source
        target_path = self.videoDir + os.sep + target
        prefix_length = len(os.path.commonprefix([source_path, target_path]))
        print('source:', source_path[prefix_length:])
        print('target:', target_path[prefix_length:])

        answer = input("Rename source to target? [Y/n]: ")

        if answer == 'y' or answer == 'Y' or not answer:
            shutil.move(
                self.videoDir + os.sep + source, self.videoDir + os.sep + target
            )

    def printMethods(self):
        """Printing all methods of this object and their docstring."""

        for name in sorted(dir(self)):
            attr = getattr(self, name)
            if callable(attr):
                print(name, ':', attr.__doc__)

    def printAttributes(self):
        """Print all the attributes of this object and their value."""

        for name in sorted(dir(self)):

            attr = getattr(self, name)
            if not callable(attr):

                if type(attr) is types.__dict__:
                    print(name, ':')
                    pprint.pprint(attr)
                else:
                    print(name, ':', attr)

    def printAll(self):
        """Calls all the methods of this object."""

        for name in sorted(dir(self)):
            attr = getattr(self, name)
            if callable(attr) and name != 'print_all' and name != '__init__':
                attr()  # calling the method
