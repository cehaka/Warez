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

class VideoUtil:
    """Static Methods used by Video"""

    _synonyms_sorted = None
    _synonyms = {
        # TODO add synonym category 'genre', 'lead_role', 'site' (goldesel.to)

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
            ['#AC3', 'AC3D', 'AC3', '#Ac3', 'aC3', 'ac3', '1 2 AC3'],
            ['#DTS', '#dts', 'DTS', 'dts'],
            ['#Dolby', 'D-ES', 'Dolby-ES', 'Dolby-EX', 'DolbyES', 'DolbyEX']
        ],

        'audio language':[\
            ['#a:de', '#de', 'Deutsch / German', 'Deutsch, German', 'Deutsch German', 'GERMAN', 'german-deutsch', 'German', 'german', 'Deutsch', 'deutsch'],
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
            ['#CoenBrothers', 'Joel Coen', 'Coen Brothers', 'coen brothers', 'CoenBrothers', 'coenBrothers', 'coenbrothers', 'Coen', 'coen'],
            ['#NicolasCage', 'Nicolas Cage', 'nicolas cage', 'NicolasCage', 'nicolasCage', 'nicolascage'],
            ['#PeterGreenaway', 'Peter Greenaway', 'peter greenaway'],
            ['#StanleyKubrick', 'Stanley Kubrick', 'stanley kubrick', \
             'Kubrick', 'kubrick'],
            ['#RobertAltman', 'Robert Altman', 'robert altman', 'RobertAltman', 'robertaltman'],
            ['#ErichVonStroheim', 'Erich von Stroheim'],
            ['#UweBoll', 'Uwe Boll', 'uwe boll', 'UweBoll' 'uweboll'],
            ['#Doku', '#doku', 'DOKU', 'Dokumentation'],  # for lack of a better category
            ['#Adventure', '[Adventure]'],  # for lack of a better category
            ['#trash'],  # for lack of a better category
            ['#uncut', '#Uncut', '#UNCUT', 'UNCUT', 'uncut'],
            ['#Director\'sCut', 'Directors Cut', 'director\'s cut', 'directors cut', 'DirectorsCut', '#DC', 'DC'],
            ['#proper', 'PROPER', 'proper'],
            ['#repack', 'REPACK', 'RePack', 'rePack', 'Repack'],
            ['#DavidLynch', 'David Lynch', 'david lynch', 'DavidLynch', 'davidlynch', 'lynch'],
            ['#EmirKusturica', 'Emir Kusturica', 'emir kusturica', 'EmirKusturica', 'emirkusturica', 'kusturica'],
            ['#RussellCrowe', 'Russell Crowe', 'RussellCrowe', 'russellcrowe'],
            ['#ClintEastwood', 'Clint Eastwood', 'clint eastwood'],
            ['#WalterWippersberg', 'Walter Wippersberg', 'walter wippersberg', 'WalterWippersberg', 'walterwippersberg']
        ],

        'release group':[\
            ['#0PTiMUS', '-0PTiMUS', '0PTiMUS', '-optimus'],
            ['#3Li', '-3Li', '3Li'],
            ['#4SM4', '4SM4', '4Sm4', '4sM4', '4sm4'],
            ['#4th', '-4TH', '-4th', '-4Th', '-4tH', '4TH'],
            ['#AN', '-AN', ' AN '],
            ['#AOE', '-AOE', 'AOE', '-aoe', 'aoe-'],
            ['#aXXo', '-aXXo', '[aXXo]'],
            ['#BiG', '-BiG', '-big'],
            ['#CENTi', '-CENTi', '-centi', 'CENTi', 'centi'],
            ['#CHALLENGE', '-CHALLENGE', '-challenge', 'CHALLENGE'],
            ['#CHD', '-CHD', '-chd', '-ChD', '-CHd', '-cHD'],
            ['#CHD-D1', '-CHD.D1'],
            ['#CiA', '-CiA', '-cia'],
            ['#CiNEPLEXX', '-CiNEPLEXX', '-CinePlexx' '-cineplexx', 'CiNEPLEXX', 'CinePlexx', 'cineplexx'],
            ['#CIS', '-cis'],
            ['#CODY', '-CODY', 'CODY'],
            ['#CRiTiCAL', '-CRiTiCAL', 'CRiTiCAL', '-critical'],
            ['#CRoW', '-CRoW', '-crow', 'CRoW'],
            ['#CRUCiAL', '-CRUCiAL', 'CRUCiAL', '-crucial'],
            ['#D0GG', '-DOGG', '-D0GG', '-DoGG', '-d0gg', 'D0GG', 'DOGG', 'DoGG'],
            ['#DEFUSED', '-DEFUSED', 'DEFUSED', '-defused'],
            ['#DETAiLS', '-DETAiLS', 'DETAiLS'],
            ['#DiViDi', '-DiViDi', 'DiViDi', '-dividi'],
            ['#DON', '-DON'],
            ['#DvF'],
            ['#DVL', '-DVL', '-dvl', 'DVL', 'dvl'],
            ['#dwiki', 'D-WiKi', 'd-wiki', 'DWiKi', 'Dwiki', 'dwiki'],
            ['#EMPiRE', '-EMPIRE', '-EMPiRE', 'EMPiRE'],
            ['#EXQUiSiTE', '-EXQUiSiTE', 'EXQUiSiTE'],
            ['#EXTREEM', '-EXTREEM', '-extreem', 'EXTREEM'],
            ['#FTP-Team', '-FTP-Team', '-ftp-team', 'FTP-Team'],
            ['#forever', '-by forever', 'by forever'],
            ['#FreibeuterDerMeere', 'by Freibeuter der Meere'],
            ['#FXG', '-FXG', '-fxg', 'FXG'],
            ['#FxW', '-FxW', '-fxw', 'FxW'],
            ['#GOREHOUNDS', '-GOREHOUNDS', '-gorehounds', 'GOREHOUNDS'],
            ['#GREENBUD', '#greenbud', 'GreenBud', 'greenBud'],
            ['#GVD', '-GVD', '-gvd'],
            ['#HACO', '-HACO', '-haco', 'HACO'],
            ['#HD2', '-HD2', 'HD2'],
            ['#HDLiTE', '-HDLiTE', '-HDLite', 'HDLiTE', '-HDlite', '-hdlite'],
            ['#HoRnEtS', '-HoRnEtS', '-Hornets', '-hornets'],
            ['#HQC', '-HQC', '-hqc'],
            ['#hV', '-hV', ' hV '],
            ['#iMPERiUM', '-iMPERiUM', '-imperium', 'iMPERiUM'],
            ['#iNK', '-iNK', 'iNK'],
            ['#iNTERNAL', '-iNTERNAL', 'iNTERNAL', '-internal', 'INTERNAL', 'iNTERNA', 'iNTER'],
            ['#iNT', '-iNT', 'iNT'],
            ['#imbt', '-imbt', 'imbt'],
            ['#IPpinki', '-IPpinki', 'IPpinki', 'iPPiNKi', 'ippinki'],
            ['#JBW', '-JBW', '-jbw'],
            ['#Kingdom', '-KingDom', '-Kingdom', '-kingdom', '(Kingdom-Release)'],
            ['#KiNOWELT', '-KiNOWELT', '-Kinowelt', '-kinowelt'],
            ['#KLASSiGER', '-KLASSiGER', '-klassiger', 'KLASSiGER'],
            ['#KM', 'KM'],
            ['#LCHD', '-LCHD-', '-LCHD', '-lchd'],
            ['#LOGiCAL', '-LOGiCAL', '-logical', 'logical'],
            ['#MH', '-MH', '-Mh', '-mH', 'MH'],
            ['#MiNe', 'MiNe'],
            ['#MOViEFRiEND', '-MOViEFRiEND', '-moviefriend', 'MOViEFRiEND'],
            ['#MoviesByRizzo', 'moviesbyrizzo'],
            ['#MrProper', '-MrProper', '-mrProper', 'mrproper', 'MrProper', '#MrP', '-MrP', '-mrp', 'MrP'],
            ['#Ms89', '-Ms89', 'Ms89'],
            ['#NOTRADE', '-NOTRADE', '-NoTrade', '-noTrade', '-notrade'],
            ['#NTG', '-NTG', '-ntg', 'NTG'],
            ['#OGMx', '-OGMx', '-ogmx', 'ogmx'],
            ['#PLEADERS', '-PL', '-PLEADERS', '-Pleaders', '-pleaders'],
            ['#POE', '-POE', '-poe'],
            ['#PP-Elite', '-PP-Elite', 'By Pp-Elite'],
            ['#PressTV', '-PressTV', '-pressTV', '-presstv', 'PressTV'],
            ['#PRoDJi', '-PRoDJi', 'PRoDJi', '-prodji', 'ProdJi', 'Prodji'],
            ['#QoM', '-QoM', 'QoM'],
            ['#RCP', '-RCP', '-rcp', 'RCP'],
            ['#RiP', '-RiP'],
            ['#RoCK', '-ROCK', '-RoCK', 'ROCK', 'RoCK'],
            ['#rollON', '-ROLLON', '-ROLLon', '-RollON', '-rollon', 'ROLLON', 'ROLLon', 'RollON', 'rollon'],
            ['#ROOR', '-ROOR', '-roor'],
            ['#RSG', '#rsg', '-RSG', '-rsg'],
            ['#RyD3R', '-RyD3R', 'RyD3R'],
            ['#SAMFD', '-SAMFD', 'samfd'],
            ['#SecretMyth', '-SecretMyth', '-secretMyth' '-Secretmyth', '-secretmyth', 'SecretMyth'],
            ['#Sedition', 'by Sedition'],
            ['#SFO', '-SFO'],
            ['#SG', '-SG', '-sg'],
            ['#SkA', 'SKA', '-SKA', '-SkA', '-Ska', '-ska'],
            ['#StarWars ', '-StarWars', '-starwars '],
            ['#SYH', '-SYH', '-syh', 'SYH'],
            ['#T2RitSch', 'by T2RitSch'],
            ['#THORA', '-THORA', '-thora', 'THORA'],
            ['#TLF', '-TLF', '-tlf', 'TLF', 'tlf'],
            ['#TMP', '-TMP'],
            ['#TOXiC', '-T0XiC', 'TOXiC'],
            ['#Toxic3', '-Toxic3'],
            ['#TRANSFORMERS', '-TRANSFORMERS', 'TRANSFORMERS'],
            ['#ULTiMATE', '#ULTiMATE', '-ULTiMATE', 'ULTiMATE'],
            ['#UNS', 'by UNS'],
            ['#VCF', '-VCF', 'VCF'],
            ['#ViDEOWELT', '-ViDEOWELT', 'ViDEOWELT', 'VideoWelt', 'Videowelt', 'videowelt'],
            ['#W2G', '-W2G'],
            ['#WAF', '-WAF'],
            ['#WATCHABLE', '-WATCHABLE', '-watchable'],
            ['#WunSeeDee', '-WunSeeDee', 'WunSeeDee'],
            ['#XCOPY', '-XCOPY', '-XCoPY', '-Xcopy', '-xopy'],
            ['#XMF', '-XMF', '-Xmf', '-xmf'],
            ['#ZEKTORM', '-ZEKTORM', 'ZEKTORM', 'zektorm', '-zektorm'],
            ['#goldesel.to', 'for www.goldesel.to'],
        ],

        'source media':[\
            ['#HD2DVDrip', 'HD2DVDRiP'],
            ['#DVDSCR', 'DVDSCR'],
            ['#BDrip', '#BluRay', 'BDRip', 'BDrip', 'bdrip', 'BD',
                'BluRay-Rip', 'Blu-Ray', 'Blu-ray', 'blu-ray', 'BlueRay', 'blueray', 'BLURAY', 'BluRay', 'Bluray' \
                'Blue-Ray', 'Blue-ray', 'blue-ray', 'BlueRay-Rip', 'BlueRay-RIP', 'BlueRay-rip', 'BlueRayRip', 'bluerayrip', \
                'BRRIP', 'BRRiP', 'BRRip', 'BRrip', 'brrip'],
            ['#DVBrip', 'DVB-Rip', 'DVB-rip', 'dvb-rip', 'DVBRIP', 'DVBRiP', 'DVBrip', 'DvbRip', 'dvbRip', 'dvbrip'],
            ['#DVDrip', 'DVD-Rip', 'DVD-rip', 'DVD-RIP', 'DVDRip', 'DVDrip', 'DvDrip', 'DVDRiP', 'DVD rip', 'dvd rip',
                'Dvdrip', 'dvdrip', 'DVD', 'DVDR'],
            ['#HDTVrip', '#HDRip', 'HDTVrip', 'hdtvRip', 'HDTVRIP', 'HDTVRip', \
                         'HDRIP', 'HDRiP', 'HDRip', 'HDrip', 'Hdrip', 'hdRip', 'hdrip', 'HDTV', 'hdtv', ' HD '],
            ['#Megavideo', '#MegaVideo', 'Mega Video', 'mega video', 'megavideo'],
            ['#R5', '#r5', 'R5']
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
            ['#SVCD', 'SVCD', 'svcd', 'RSVCD', 'Rsvcd'],
            ['#MVCD', 'MVCD', 'mvcd'],
            ['#h264', 'H264', 'h264', 'x264', 'X264'],
            ['#XViD', 'XVID', 'XViD', 'XviD', 'Xvid', 'xvid', \
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
            ['#ExtendedCut', 'EXTENDED CUT']
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

        if self._synonyms_sorted == None:
            synonyms_sorted_dict = dict()
            for category in self._synonyms:
                synonyms_sorted_dict[category] = sorted(self._synonyms[category], key=len, reverse=False)
            self._synonyms_sorted = synonyms_sorted_dict
            return self._synonyms_sorted
        else:
            return self._synonyms_sorted

