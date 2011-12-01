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
            ['#MP3', '#mp3', 'mp3'],
            ['#FLAC', '#flac', 'flac'],
            ['#AAC', '#aac', 'aac'],
            ['#OGG', '#ogg', 'ogg'],
            ['#AC3', '#ac3', 'ac3', 'AC3', 'DTS']
        ],

        'audio language':[\
            ['#a:de', '#de', 'German', 'german', 'Deutsch', 'deutsch'],
            ['#a:en', '#en', 'English', 'english', 'Englisch', 'english', '[Eng]', 'Eng '],
            ['#a:rus', '#rus', 'Russian', ' Rus '],
            ['#a:cn', '#cn', 'Chinese', '[Cn]']
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
             'Kubrick', 'kubrick'],
            ['#DC', 'DC Comics'],
            ['#Doku', 'Dokumentation']
        ],

        'release group':[\
            ['#AOE', '-AOE', 'AOE', '-aoe'],
            ['#aXXo', '-aXXo', '[aXXo]'],
            ['#CENTi', '-CENTi', '-centi', 'CENTi', 'centi'],
            ['#CHALLENGE', '-CHALLENGE', '-challenge', 'CHALLENGE'],
            ['#CiNEPLEXX', '-CiNEPLEXX', '-CinePlexx' '-cineplexx',\
                           'CiNEPLEXX', 'CinePlexx', 'cineplexx'],
            ['#CIS', '-cis'],
            ['#CRiTiCAL', '-CRiTiCAL', 'CRiTiCAL', '-critical'],
            ['#CRUCiAL', '-CRUCiAL', 'CRUCiAL', '-crucial'],
            ['#D0GG', '-DoGG', 'DOGG', 'DoGG'],
            ['#DiViDi', '-DiViDi', 'DiViDi', '-dividi'],
            ['#EMPiRE', '-EMPIRE', 'EMPiRE'],
            ['#EXQUiSiTE', '-EXQUiSiTE', 'EXQUiSiTE'],
            ['#EXTREEM', '-EXTREEM', '-extreem', 'EXTREEM'],
            ['#iNK', '-iNK', 'iNK'],
            ['#iNTERNAL', '-iNTERNAL', 'iNTERNAL', '-internal', 'INTERNAL'],
            ['#PLEADERS', '-PL', '-PLEADERS', '-Pleaders', '-pleaders'],
            ['#HDLiTE', '-HDLiTE', '-HDLite', 'HDLiTE', '-HDlite', '-hdlite'],
            ['#HD2', '-HD2', 'HD2'],
            ['#HoRnEtS', '-HoRnEtS', '-Hornets', '-hornets'],
            ['#LCHD', '-LCHD-', '-LCHD', '-lchd'],
            ['#MrProper', '-MrProper', '-mrProper', 'mrproper', 'MrProper'],
            ['#Ms89', '-Ms89', 'Ms89'],
            ['#NOTRADE', '-NOTRADE', '-NoTrade', '-noTrade', '-notrade'],
            ['#0PTiMUS', '-0PTiMUS', '0PTiMUS', '-optimus'],
            ['#QoM', '-QoM', 'QoM'],
            ['#RoCK', '-ROCK', '-RoCK', 'ROCK', 'RoCK'],
            ['#RSG', '#rsg', '-RSG', '-rsg'],
            ['#StarWars ', '-StarWars', '-starwars '],
            ['#TOXiC', '-T0XiC', 'TOXiC'],
            ['#ViDEOWELT', '-ViDEOWELT', 'ViDEOWELT', 'VideoWelt', 'Videowelt', 'videowelt'],
            ['#WAF', '-WAF'],
            ['#WunSeeDee', '-WunSeeDee', 'WunSeeDee'],
            ['#XMF', '-XMF', '-Xmf', '-xmf'],
            ['#XCOPY', '-XCOPY', '-XCoPY', '-Xcopy', '-xopy'],
            ['#KiNOWELT', '-KiNOWELT', '-kinowelt'],
            ['#HQC', '-HQC', '-hqc'],
            ['#BiG', '-BiG', '-big']
        ],

        'source media':[\
            ['#BDrip', '#BluRay', 'BDRip', 'BDrip', 'bdrip', 'BD',
                'Blue-Ray', 'Blue-ray', 'blue-ray', 'Blu-Ray', 'Blu-ray', 'blu-ray', 'BlueRay', 'blueray', \
                'BlueRayRip', 'bluerayrip', 'BRRIP', 'BRRip', 'BRrip', 'brrip'],
            ['#DVDrip', 'DVDRip', 'DVDrip', 'DvDrip', 'DVDRiP', 'DVD rip', 'dvd rip',
                'Dvdrip', 'dvdrip', 'DVD', 'DVDR'],
            ['#HDTVrip', '#HDRip', 'HDTVrip', 'hdtvRip', 'HDTVRIP', 'HDTVRip', 'HDTV', 'hdtv'],
            ['#Megavideo', '#MegaVideo', 'Mega Video', 'mega video', 'megavideo'],
            ['#R5', '#r5',  'R5']
        ],

        'subtitle language':[\
            ['#s:de', 'German Substitles', 'german subtitles', \
             'Deutsche Untertitel', 'Deutsche untertitel', 'deutsche untertitel'],
            ['#s:en', 'English Subtitles', 'english subtitles', \
             'Englische Untertitel', 'englishe Untertitel', 'englische untertitel', \
             '[Eng Subs]', '[eng subs]', '[Eng Sub]', 'Eng Subs', 'eng subs', 'Eng Sub', 'eng sub'],
             ['#s:cn']
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
            ['#SC', '#src', 'SC', 'Screener'],
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
