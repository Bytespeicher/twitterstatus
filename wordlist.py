#!bin/python
# -*- coding: UTF-8 -*-
import config


class MissingTranslationException(Exception):
    pass


translations = {
    "en_US": [
        [
            'The space',
            config.SPACE_NAME
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
            'majestic',
            'monumental',
            'glorious',
            'sumptuous',
            'resplendent',
            'lavish',
            'beautiful',
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
            config.SPACE_NAME
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
            'Splendid',
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
    "fr_FR": [
        [
            "L'espace",
            config.SPACE_NAME
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
            config.SPACE_NAME
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
            config.SPACE_NAME
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
            config.SPACE_NAME
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
    "tr_TR": [
        [
            'Boşluk',
            'Bytespeicher'
        ],
        [
            'dır',
        ],
        [
            'açık',
            'girişe izin veriyor',
        ],
        [
            'kapalı',
            'artık açık değil'
        ],
        [
            'muhteşem',
            'heybetli',
            'etkileyici',
            'korku-veren',
            'büyük',
            'görkemli',
            'haşmetli',
            'anıtsal',
            'şanlı',
            'ihtişamlı',
            'şaşaalı',
            'savurgan',
            'güzel',
            'keyifli',
            'sevimli',
        ],
        [
            'Çok kötü',
            'onursuz',
            'şerefsiz',
            'namussuz',
            'iğrenç',
            'rezil',
            'aşağı',
            'cimri',
            'fakir',
        ]
    ]
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
    except Exception:
        raise MissingTranslationException("No translation for %s found" %
                                          language)
