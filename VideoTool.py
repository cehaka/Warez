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

    def stripWhitespaceCharacter (self, nameEncoded, whitespaceCharacter):
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
