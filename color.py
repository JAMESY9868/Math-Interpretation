#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Taken from another repository of my own: Hearts-in-Python

class color:
    'ANSI Color Escapes'
    _colorDict = {
        'none': 0 # the default value
        , 'black': 30
        , 'red': 31
        , 'green': 32
        , 'yellow': 33
        , 'blue': 34
        , 'magenta': 35
        , 'cyan': 36
        , 'white': 37
    }
    __escapeHeadTail = ['\033[', 'm'] # this shouldn't be changed
    __escapeMid = ['0'] # a list of 1 or 2 elements of stringified numbers
    def __eq__(self, value):
        if type(self) != type(value): return False # to ensure value is the right type
        return self.__escapeMid == value.__escapeMid
    def __init__(self, foreground = None, background = None, intenseFore = False, intenseBack = False):
        '''
        Initializes with the attributes of: foreground, background, intenseFore, intenseBack
        foreground and background should be texts within such:
            ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        '''
        # if both foreground and background are unset, escape to 'normal text'
        if foreground is None and background is None: return
        # if foreground or background is not set, set them to default values
        foreground, background = \
            'none' if foreground not in color._colorDict.keys() else foreground, \
            'none' if background not in color._colorDict.keys() else background
        # set numbers for foreground and background colors
        foreNum, backNum = color._colorDict[foreground], \
            color._colorDict[background] + (0 if 'none' == background else 10)
        # if intenseFore or intenseBack is True, then add foreNum or backNum by 60 (for color intensification).
        foreNum, backNum = \
            (foreNum + 60) if intenseFore and 'none' == foreground else foreNum, \
            (backNum + 60) if intenseBack and 'none' == background else backNum
        # put stringified data in to object
        self.__escapeMid = [str(num) for num in (foreNum, backNum) if num != 0]
    def str(self):
        'Output the text form of the ANSI color sequence'
        combine = lambda escapeHeadTail, escapeMid: \
            escapeHeadTail[0] + ';'.join(escapeMid) + escapeHeadTail[1]
        try: return combine(self.__escapeHeadTail, self.__escapeMid)
        except KeyError: return combine(self.__escapeHeadTail, [0])
    def text(self, text):
        'To be used directly in print(), to output some colored text "text"'
        try: return self.str() + text + color().str()
        except TypeError: return '' # return nothing if it gets TypeError, namely bad 'text'
    def printData(self, text):
        'For debugging only: to print the text from text() instead of outputting the text itself'
        print(self.text(text))


pass
