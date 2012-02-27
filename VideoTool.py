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
            ['#5.1', '5.1', '5.1 Channels', '5.1 channels', '5.1 Channel', '5.1 channel', '5 1 ch'],
            ['#stereo', '2.0'],
            ['#mono', '1.0'],
        ],

        'audio codec':[\
            ['#MP3', '#mp3', 'mp3'],
            ['#FLAC', '#flac', 'flac'],
            ['#AAC', '#aac', 'AAC', 'aac'],
            ['#OGG', '#ogg', 'OGG ''ogg'],
            ['#AC3', '#ac3', 'AC3', 'ac3'],
            ['#DTS', '#dts', 'DTS', 'dts'],
            ['#Dolby', 'D-ES', 'Dolby-ES', 'Dolby-EX', 'DolbyES', 'DolbyEX']
        ],

        'audio language':[\
            ['#a:de', '#de', 'GERMAN', 'German', 'german', 'Deutsch', 'deutsch'],
            ['#a:en', '#en', 'English', 'english', 'Englisch', 'english', '[Eng]', 'Eng '],
            ['#a:rus', '#rus', 'Russian', ' Rus '],
            ['#a:cn', '#cn', 'Chinese', '[Cn]'],
            ['#a:fr', '#fr', ' fr '],
            ['#a:ita', '#ita', ' ita '],
            ['#a:dual', 'Dual audio']
        ],

        'audio source':[\
            ['#MD', ' MD', 'MicDub', 'Mic Dubbed', 'mic dubbed', 'micdubbed'],
            ['#LD', ' LD', ' DL', 'LineDub', 'Line Dubbed', 'line dubbed', 'linedubbed', 'DUBBED', 'dubbed']
        ],

        'container format':[\
            ['#mkv', ' MKV', ' mkv'],
            ['#avi', ' AVI', ' avi']
        ],

        'filmmaker':[\
            ['#AndreiTarkovsky', '(Andrei Tarkovsky)', '(AndreiTarkovsky)', '(andreiTarkovsky)', '(andreitarkovsky)'\
            'Andrei Tarkovsky', 'andrei tarkovsky', 'AndreiTarkovsky', 'andreiTarkovsky', 'andreitarkovsky'],
            ['#CoenBrothers', 'Coen Brothers', 'coen brothers', 'CoenBrothers', 'coenBrothers', 'coenbrothers', 'Coen', 'coen'],
            ['#NicolasCage', 'Nicolas Cage', 'nicolas cage', 'NicolasCage', 'nicolasCage', 'nicolascage'],
            ['#PeterGreenaway', 'Peter Greenaway', 'peter greenaway'],
            ['#StanleyKubrick', 'Stanley Kubrick', 'stanley kubrick', \
             'Kubrick', 'kubrick'],
            ['#UweBoll', 'Uwe Boll', 'uwe boll', 'UweBoll' 'uweboll'],
            ['#Doku', '#doku', 'DOKU', 'Dokumentation'], # for lack of a better category
            ['#Adventure', '[Adventure]'], # for lack of a better category
            ['#trash'], # for lack of a better category
            ['#uncut', '#Uncut', '#UNCUT', 'UNCUT', 'uncut'],
            ['#Director\'sCut', 'Directors Cut', 'director\'s cut', 'directors cut', 'DirectorsCut', '#DC', 'DC'],
            ['#proper', 'PROPER', 'proper'],
            ['#repack', 'REPACK', 'RePack', 'rePack', 'Repack'],
            ['#DavidLynch', 'David Lynch', 'david lynch', 'DavidLynch', 'davidlynch', 'lynch'],
        ],

        'release group':[\
            ['#3Li', '-3Li', '3Li'],
            ['#4SM4', '4SM4', '4Sm4', '4sM4', '4sm4'],
            ['#4th', '-4TH', '-4th', '-4Th', '-4tH', '4TH'],
            ['#AN', '-AN', ' AN '],
            ['#AOE', '-AOE', 'AOE', '-aoe'],
            ['#aXXo', '-aXXo', '[aXXo]'],
            ['#CENTi', '-CENTi', '-centi', 'CENTi', 'centi'],
            ['#CHALLENGE', '-CHALLENGE', '-challenge', 'CHALLENGE'],
            ['#CHD', '-CHD', '-chd', '-ChD', '-CHd', '-cHD'],
            ['#CiNEPLEXX', '-CiNEPLEXX', '-CinePlexx' '-cineplexx',\
                           'CiNEPLEXX', 'CinePlexx', 'cineplexx'],
            ['#CiA', '-CiA', '-cia'],
            ['#CIS', '-cis'],
            ['#CRiTiCAL', '-CRiTiCAL', 'CRiTiCAL', '-critical'],
            ['#CRoW', '-CRoW', '-crow', 'CRoW'],
            ['#CRUCiAL', '-CRUCiAL', 'CRUCiAL', '-crucial'],
            ['#DEFUSED', '-DEFUSED', 'DEFUSED', '-defused'],
            ['#D0GG', '-DOGG', '-D0GG', '-DoGG', '-d0gg', 'D0GG', 'DOGG', 'DoGG'],
            ['#DON', '-DON'],
            ['#DiViDi', '-DiViDi', 'DiViDi', '-dividi'],
            ['#DvF'],
            ['#dwiki', 'D-WiKi', 'd-wiki', 'DWiKi', 'Dwiki', 'dwiki'],
            ['#EMPiRE', '-EMPIRE', '-EMPiRE', 'EMPiRE'],
            ['#EXQUiSiTE', '-EXQUiSiTE', 'EXQUiSiTE'],
            ['#EXTREEM', '-EXTREEM', '-extreem', 'EXTREEM'],
            ['#FTP-Team', '-FTP-Team', '-ftp-team', 'FTP-Team'],
            ['#FxW', '-FxW', '-fxw', 'FxW'],
            ['#FXG', '-FXG', '-fxg', 'FXG'],
            ['#GOREHOUNDS', '-GOREHOUNDS', '-gorehounds', 'GOREHOUNDS'],
            ['#GVD', '-GVD', '-gvd'],
            ['#hV', '-hV', ' hV '],
            ['#iMPERiUM', '-iMPERiUM', '-imperium', 'iMPERiUM'],
            ['#iNK', '-iNK', 'iNK'],
            ['#iNT','-iNT', 'iNT'],
            ['#iNTERNAL', '-iNTERNAL', 'iNTERNAL', '-internal', 'INTERNAL', 'iNTERNA', 'iNTER'],
            ['#JBW', '-JBW', '-jbw'],
            ['#PLEADERS', '-PL', '-PLEADERS', '-Pleaders', '-pleaders'],
            ['#GREENBUD', '#greenbud', 'GreenBud', 'greenBud'],
            ['#HACO', '-HACO', '-haco', 'HACO'],
            ['#HDLiTE', '-HDLiTE', '-HDLite', 'HDLiTE', '-HDlite', '-hdlite'],
            ['#HD2', '-HD2', 'HD2'],
            ['#HoRnEtS', '-HoRnEtS', '-Hornets', '-hornets'],
            ['#IPpinki', '-IPpinki', 'IPpinki', 'iPPiNKi', 'ippinki'],
            ['#Kingdom', '-KingDom', '-Kingdom', '-kingdom', '(Kingdom-Release)'],
            ['#KLASSiGER', '-KLASSiGER', '-klassiger', 'KLASSiGER'],
            ['#LOGiCAL', '-LOGiCAL', '-logical', 'logical'],
            ['#LCHD', '-LCHD-', '-LCHD', '-lchd'],
            ['#MH', '-MH', '-Mh', '-mH', 'MH'],
            ['#MoviesByRizzo', 'moviesbyrizzo'],
            ['#MOViEFRiEND', '-MOViEFRiEND', '-moviefriend', 'MOViEFRiEND'],
            ['#MrProper', '-MrProper', '-mrProper', 'mrproper', 'MrProper', '#MrP', '-MrP', '-mrp', 'MrP'],
            ['#Ms89', '-Ms89', 'Ms89'],
            ['#NOTRADE', '-NOTRADE', '-NoTrade', '-noTrade', '-notrade'],
            ['#NTG', '-NTG', '-ntg', 'NTG'],
            ['#OGMx', '-OGMx', '-ogmx', 'ogmx'],
            ['#0PTiMUS', '-0PTiMUS', '0PTiMUS', '-optimus'],
            ['#POE', '-POE', '-poe'],
            ['#PP-Elite', '-PP-Elite'],
            ['#PressTV', '-PressTV', '-pressTV', '-presstv', 'PressTV'],
            ['#QoM', '-QoM', 'QoM'],
            ['#RoCK', '-ROCK', '-RoCK', 'ROCK', 'RoCK'],
            ['#RCP', '-RCP', '-rcp', 'RCP'],
            ['#RiP', '-RiP'],
            ['#rollON', '-ROLLON', '-ROLLon', '-RollON', '-rollon', \
                        'ROLLON', 'ROLLon', 'RollON', 'rollon'],
            ['#ROOR', '-ROOR', '-roor'],
            ['#RSG', '#rsg', '-RSG', '-rsg'],
            ['#SAMFD', '-SAMFD', 'samfd'],
            ['#SkA', 'SKA', '-SKA', '-SkA', '-Ska', '-ska'],
            ['#StarWars ', '-StarWars', '-starwars '],
            ['#SecretMyth', '-SecretMyth', '-secretMyth' '-Secretmyth', '-secretmyth', 'SecretMyth'],
            ['#SG', '-SG', '-sg'],
            ['#SYH', '-SYH', '-syh', 'SYH'],
            ['#THORA', '-THORA', '-thora', 'THORA'],
            ['#TLF', '-TLF', '-tlf', 'TLF', 'tlf'],
            ['#TOXiC', '-T0XiC', 'TOXiC'],
            ['#TRANSFORMERS', '-TRANSFORMERS', 'TRANSFORMERS'],
            ['#ULTiMATE', '#ULTiMATE', '-ULTiMATE' 'ULTiMATE'],
            ['#ViDEOWELT', '-ViDEOWELT', 'ViDEOWELT', 'VideoWelt', 'Videowelt', 'videowelt'],
            ['VCF', '-VCF', 'VCF'],
            ['#WAF', '-WAF'],
            ['#WATCHABLE', '-WATCHABLE', '-watchable'],
            ['#WunSeeDee', '-WunSeeDee', 'WunSeeDee'],
            ['#WunSeeDee', '-WunSeeDee', 'WunSeeDee'],
            ['#XMF', '-XMF', '-Xmf', '-xmf'],
            ['#XCOPY', '-XCOPY', '-XCoPY', '-Xcopy', '-xopy'],
            ['#KiNOWELT', '-KiNOWELT', '-kinowelt'],
            ['#HQC', '-HQC', '-hqc'],
            ['#BiG', '-BiG', '-big'],
            ['#ZEKTORM', '-ZEKTORM', 'ZEKTORM', 'zektorm', '-zektorm']
        ],''

        'source media':[\
            ['#BDrip', '#BluRay', 'BDRip', 'BDrip', 'bdrip', 'BD',
                'Blue-Ray', 'Blue-ray', 'blue-ray', 'Blu-Ray', 'Blu-ray', 'blu-ray', 'BlueRay', 'blueray', \
                'BLURAY', 'BluRay', 'Bluray' \
                'BlueRayRip', 'bluerayrip', 'BRRIP', 'BRRiP', 'BRRip', 'BRrip', 'brrip'],
            ['#DVBrip', 'DVB-Rip', 'DVB-rip', 'dvb-rip', 'DVBRIP', 'DVBRiP', 'DVBrip', 'DvbRip', 'dvbRip', 'dvbrip'],
            ['#DVDrip', 'DVDRip', 'DVDrip', 'DvDrip', 'DVDRiP', 'DVD rip', 'dvd rip',
                'Dvdrip', 'dvdrip', 'DVD', 'DVDR'],
            ['#HDTVrip', '#HDRip', 'HDTVrip', 'hdtvRip', 'HDTVRIP', 'HDTVRip', \
                         'HDRIP', 'HDRiP', 'HDRip', 'HDrip', 'Hdrip', 'hdRip', 'hdrip', 'HDTV', 'hdtv', ' HD '],
            ['#Megavideo', '#MegaVideo', 'Mega Video', 'mega video', 'megavideo'],
            ['#R5', '#r5',  'R5']
        ],

        'subtitle language':[\
            ['#s:de', 'German Substitles', 'german subtitles', \
             'Deutsche Untertitel', 'Deutsche untertitel', 'deutsche untertitel', \
             'GERMAN SUBBED', 'German Subbed', 'german subbed', 'GERMANSUBBED', 'GermanSubbed' 'germanSubbed', 'germansubbed'],
            ['#s:en', 'English Subtitles', 'english subtitles', \
             'Englische Untertitel', 'englishe Untertitel', 'englische untertitel', \
             '[Eng Subs]', '[eng subs]', '[Eng Sub]', 'Eng Subs', 'eng subs', 'Eng Sub', 'eng sub'],
             ['#s:cn'],
             ['#s:multi', 'Multi Sub', 'MultiSub', 'multisub', 'multi sub'],
             ['#s:en #s:es #s:fr #s:it', \
                    'En Es Fr It multisub', 'en es fr it multisub', \
                    'En Es Fr It multi sub', 'en es fr it multi sub']
        ],

        'video codec':[\
            ['#SVCD', 'SVCD', 'svcd'],
            ['#MVCD', 'MVCD', 'mvcd'],
            ['#h264', 'H264', 'h264', 'x264', 'X264'],
            ['#XViD', 'XVID', 'XViD', 'XviD', 'Xvid', 'xvid',\
                      'DIVX', 'DiVX', 'DivX', 'Divx', 'divx',
                      'DivXHD'],
        ],

        'video resolution':[\
            ['#NTSC', 'NTSC', 'ntsc'],
            ['#PAL', 'PAL'],
            ['#720p', '720i', '720I', '720p', '720P', '720'],
            ['#1080p', '1080i', '1080I', '1080p', '1080P', '1080']
        ],

        'video source':[\
            ['#SC', '#src', 'SC', 'Screener'],
            ['#TS', 'TS', 'Telesync', 'TeleSync']
        ],

        'video version':[\
            ['#uncut', 'UNCUT', 'unCUT', 'UNcut', 'UnCut', 'Uncut', 'uncut'],
            ['#proper', 'PROPER', 'proper'],
            ['#directorsCut', 'Directors Cut', "Director's Cut"],
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
