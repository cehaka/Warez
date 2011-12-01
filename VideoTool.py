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

class VideoTool:
    """Static Methods used by Video"""

    _synonyms = {

        'audio channels':[\
            ['#5.1', '5.1'],
            ['#stereo', '2.0'],
            ['#mono', '1.0'],
        ],

        'audio codec':[\
            ['#mp3', 'mp3'],
            ['#flac', 'flac'],
            ['#aac', 'aac'],
            ['#ogg', 'ogg'],
        ],

        'audio encoding':[\
            ['#ac3', 'ac3', 'AC3', 'DTS']
        ],

        'audio language':[\
            ['#a:de', 'German', 'german', 'Deutsch', 'deutsch'],
            ['#a:en', 'English', 'english', 'Englisch', 'english', ' Eng '],
            ['#a:rus', 'Russian', ' Rus ']
        ],

        'audio source':[\
            ['#MD', ' MD', 'MicDub', 'Mic Dubbed', 'mic dubbed', 'micdubbed'],
            ['#LD', ' LD', 'LineDub', 'Line Dubbed', 'line dubbed', 'linedubbed']
        ],

        'container format':[\
            ['#mkv', ' MKV', ' mkv'],
            ['#avi', ' AVI', ' avi']
        ],

        'filmmaker':[\
            ['#StanleyKubrick', 'Stanley Kubrick', 'stanley kubrick', \
             'Kubrick', 'kubrick']
        ],

        'release group':[\
            ['#AOE', '-AOE', 'AOE', '-aoe'],
            ['#CiNEPLEXX', '-CiNEPLEXX', '-CinePlexx' '-cineplexx',\
                           'CiNEPLEXX', 'CinePlexx', 'cineplexx'],
            ['#CRiTiCAL', '-CRiTiCAL', 'CRiTiCAL', '-critical'],
            ['#CRUCiAL', '-CRUCiAL', 'CRUCiAL', '-crucial'],
            ['#DiViDi', '-DiViDi', 'DiViDi', '-dividi'],
            ['#EMPiRE', '-EMPIRE', 'EMPiRE'],
            ['#EXQUiSiTE', '-EXQUiSiTE', 'EXQUiSiTE'],
            ['#iNTERNAL', '-iNTERNAL', 'iNTERNAL', '-internal'],
            ['#PLEADERS', '-PL', '-PLEADERS', '-Pleaders', '-pleaders'],
            ['#HDLiTE', '-HDLiTE', '-HDLite', 'HDLiTE', '-HDlite', '-hdlite'],
            ['#HoRnEtS', '-HoRnEtS', '-Hornets', '-hornets'],
            ['#LCHD', '-LCHD-', '-LCHD', '-lchd'],
            ['#NOTRADE', '-NOTRADE', '-NoTrade', '-noTrade', '-notrade'],
            ['#XMF', '-XMF', '-Xmf', '-xmf'],
            ['#XCOPY', '-XCOPY', '-XCoPY', '-Xcopy', '-xopy'],
            ['#KiNOWELT', '-KiNOWELT', '-kinowelt'],
            ['#HQC', '-HQC', '-hqc'],
            ['#BiG', '-BiG', '-big'],
        ],

        'source media':[\
            ['#BDrip', 'BDRip', 'BDrip', 'bdrip', 'BD',
                'BlueRay', 'blueray', 'BlueRayRip', 'bluerayrip',
                'BRRIP', 'BRRip', 'BRrip', 'brrip'],
            ['#DVDrip', 'DVDRip', 'DVDrip', 'DVDRiP', 'DVD rip', 'dvd rip',
                'dvdrip', 'DVD', 'DVDR'],
            ['#HDTVrip', 'HDTVrip', 'hdtvRip', 'HDTVRIP', 'HDTVRip', 'HDTV', 'hdtv'],
            ['#Megavideo', '#MegaVideo', 'Mega Video', 'mega video', 'megavideo']
        ],

        'subtitle language':[\
            ['#s:de', 'German Substitles', 'german subtitles', \
             'Deutsche Untertitel', 'Deutsche untertitel', 'deutsche untertitel'],
            ['#s:en', 'English Subtitles', 'english subtitles', \
             'Englische Untertitel', 'englishe Untertitel', 'englische untertitel']
        ],

        'video codec':[\
            ['#SVCD', 'SVCD', 'svcd'],
            ['#MVCD', 'MVCD', 'mvcd'],
            ['#h264', 'H264', 'h264', 'x264', 'X264'],
            ['#XViD', 'XVID', 'XViD', 'XviD', 'Xvid', 'xvid']
        ],

        'video resolution':[\
            ['#NTSC', 'NTSC', 'ntsc'],
            ['#PAL', 'PAL'],
            ['#720p', '720i', '720p'],
            ['#1080p', '1080i', '1080p']
        ],

        'video source':[\
            ['#SC', 'SC', 'Screener'],
            ['#TS', 'TS', 'Telesync', 'TeleSync']
        ],

        'video version':[\
            ['#uncut', 'UNCUT', 'uncut'],
            ['#proper', 'PROPER', 'proper'],
            ['#directorsCut', 'Directors Cut', 'Director\'s Cut']
        ]
    }

    def __init__ (self):
        """Empty Constructor"""

        pass

    def decodeSpaces (self, nameEncoded, whitespaceCharacter):
        """
        Generating a name with reals spaces.
        Returns the nameEncoded with decoded spaces.
        See decode* methods for details.
        """

        nameDecoded = ''

        # Trivial case: whitespace character is empty
        if len(whitespaceCharacter) == 0:

            # Doing nothing
            nameDecoded = nameEncoded

        # Regular case: whitespace character is set
        if len(whitespaceCharacter) == 1:
            nameDecoded = self.decodeSingleCharacter(nameEncoded, whitespaceCharacter)

        # Special case: The whitespace is encoded into the cases
        if whitespaceCharacter == 'CamelCase' or whitespaceCharacter == 'mixedCase':
            nameDecoded = self.decodeCases(nameEncoded)

        return nameDecoded

    def decodeSingleCharacter (self, nameEncoded, whitespaceCharacter):
        """Translating a given single character into whitespaces."""

        # Re-constructing the nameEncoded
        nameDecoded = ''
        words = nameEncoded.split(whitespaceCharacter)
        for word in words:
            # Skipping all non-words
            if word == whitespaceCharacter: continue

            # Skipping all empty words
            if word == '': continue

            # Adding space for all n + 1 words
            if nameDecoded != '':
                nameDecoded = nameDecoded + ' '

            nameDecoded = nameDecoded + word

        return nameDecoded

    def decodeCases (self, nameEncoded):
        """Introducing whitespaces before each upper case letter."""

        nameDecoded = ''
        for char in nameEncoded:
            if char.isupper(): nameDecoded += ' '
            nameDecoded += char

        # Stripping heading whitespace introduced by CamelCase
        if nameDecoded.startswith(' '): nameDecoded = nameDecoded[1:]

        return nameDecoded

    def getSynonyms (self):

        """Returns a dictionary containing aliases for each possible tag."""

        return self._synonyms
