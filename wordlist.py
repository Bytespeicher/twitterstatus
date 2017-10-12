#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import os
import json


class MissingTranslationException(Exception):
    pass


translations = {}

def wordlist(language="en_US"):
    """
    Returns a list of lists containing words to be used in a status update
    The word list is a list with seperate lists for

        * Space
        * is
        * open
        * closed
        * fill words - good
        * fill words - bad
    """
    if language in translations:
        return translations[language]
    else:
        path = './words/{0}/wordlist.json'.format(
                 language)
        if os.path.exists(path):

            with open(path) as wordfile:
                translations[language] = json.load(wordfile)

            # fixup space name
            translations[language][0].append(config.SPACE_NAME)
            return translations[language]
        else:
            raise MissingTranslationException(
                "No translation for %s found" %
                        language)

