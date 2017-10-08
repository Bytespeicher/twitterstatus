#!bin/python


class MissingTranslationException(Exception):
    pass

translations = {
    "en_US": [
        [
            'The space',
            'Bytespeicher'
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
            'magnificent',
            'imposing',
            'impressive',
            'awe-inspiring',
            'grand',
            'splendid',
            'majestic',
            'monumental',
            'glorious',
            'sumptuous',
            'resplendent',
            'lavish',
            'beautiful',
            'delightful',
            'lovely',
        ],
        [
            'Too bad',
            'ignoble',
            'inglorious',
            'dishonorable',
            'atrocious',
            'flagitious',
            'lowly',
            'mean',
            'poor',
        ]
    ],
    "fr_FR": [
        [
            "L'espace",
        ],
        [
            'est',
        ],
        [
            'ouvert',
            "accorde l'accès",
        ],
        [
            'fermé',
            'inaccesible'
        ],
        [
            'Magnifique',
            'Fantastique',
            'Excellent',
            'Effrayant',
            'Brillant',
            'Majestueux',
            'Glorieux',
            'Somptueux',
            'Resplendissant',
            'Plantureux',
            'Beau',
            'Délicieux',
            'Superbe',
        ],
        [
            "C'est dommage",
            'Merde',
            'Honteux',
            'Atroce',
            'Ça suce',
            'Terrible',
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
