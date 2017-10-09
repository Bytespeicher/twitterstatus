#!bin/python
# -*- coding: UTF-8 -*-

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
	"de_DE": [
        [
            'Der Raum',
            'Bytespeicher'
        ],
        [
            'ist',
        ],
        [
            'offen',
            'Zutritt gewährend',
        ],
        [
            'geschlossen',
            'nicht mehr geöffnet'
        ],
        [
            'Großartig',
            'Imposant',
            'Beeindruckend',
            'Ehrfurcht einflößend',
            'Grandios',
            'Herrlich',
            'Majestätisch',
            'Monumental',
            'Glorreich',
            'Prächtig',
            'Prachtvoll',
            'Nobel',
            'Wunderschön',
            'Reizend',
            'Lieblich',
        ],
        [
            'Schade',
            'Unwürdig',
            'Schmählich',
            'Unehrenhaft',
            'Scheußlich',
            'Sündhaft',
            'Bescheiden',
            'Gemein',
            'Schwach',
        ]
    ],
    "pl_PL": [
        [
            'Spacja',
            'Bytespeicher'
        ],
        [
            'jest',
        ],
        [
            'otwarte',
            'dostępne',
        ],
        [
            'zamknięte',
            'juz zamknięte'
        ],
        [
            'wspaniałe',
            'imponujące',
            'impresujące',
            'inspirujące',
            'ogromne',
            'wspaniałe',
            'majestatyczne',
            'monumentalne',
            'wspaniałe',
            'wystawne',
            'olsśiewajace',
            'rozrzutne',
            'piękne',
            'zachwycające',
            'kochane',
        ],
        [
            'Słabe',
            'niegodziwe',
            'niechlubne',
            'niegodziwe',
            'okrutne',
            'flagowe',
            'pokorny',
            'złośliwy',
            'biedny',
        ],
    ],
    "pt_BR": [
        [
            'O espaço',
            'Bytespeicher'
        ],
        [
            'é',
        ],
        [
            'aberto',
            'permitindo acesso',
        ],
        [
            'fechado',
            'não está mais aberto'
        ],
        [
            'magnífico',
            'imponente',
            'impressionante',
            'inspirador',
            'grande',
            'esplendido',
            'majestoso',
            'monumental',
            'glorioso',
            'suntuoso',
            'resplandecente',
            'generoso',
            'belo',
            'delicioso',
            'amável',
        ],
        [
            'Que pena',
            'Desprezível',
            'inglório',
            'desonroso',
            'atroz',
            'flagrante',
            'humilde',
            'malvado',
            'miserável',
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
