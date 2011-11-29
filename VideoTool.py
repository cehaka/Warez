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

    def __init__ (self):
        """Empty Constructor"""

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
