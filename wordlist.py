#!bin/python


class MissingTranslationException(Exception):
    pass

translations = {
    "en_US": [
        [
            'The space',
        ],
        [
            'is',
        ],
        [
            'open',
            'allowing access',
        ],
        [
            'closed',
            'not open anymore'
        ],
        [
            'Awesome',
            'Great',
            'Impressive',
            'Cool',
            'Niiiiice',
            'splendid',
            'majestic',
            'monumental',
            'glorious',
            'sumptuous',
            'resplendent',
            'lavish',
            'beautiful',
            'delightful',
            'Lovely',
        ],
        [
            'Well, damn',
            'Yikes',
            'Inglorious',
            'Sucks',
            'Atrocious',
            'Flagitious',
            'Sad',
            'Shucks',
        ]
    ],
    "en_GB": [
        [
            'The space',
        ],
        [
            'is',
        ],
        [
            'open',
            'allowing access',
        ],
        [
            'closed',
            'currently unavailable',
        ],
        [
            'Magnificent',
            'Brilliant',
            'Impressive',
            'Awe-inspiring',
            'Grand',
            'Splendid',
            'Fantastic',
            'Monumental',
            'Glorious',
            'Gorgeous',
            'Superb',
            'Lavish',
            'Beautiful',
            'Delightful',
            'Lovely',
        ],
        [
            'Too bad',
            'Poor',
            'Inglorious',
            'Dishonorable',
            'Atrocious',
            'Flagitious',
            'Aw shite',
            'How unfortunate',
            'We do apologise',
        ]
    ],
}


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
    try:
        wordlist = translations[language]
        return wordlist
    except:
        raise MissingTranslationException("No translation for %s found" %
                                          language)
