#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
	"it_IT": [
       [
           'Lo spazio',
       ],
       [
           'è',
       ],
       [
           'aperto',
           'disponibile',
       ],
       [
           'chiuso',
           'bloccato',
       ],
       [
           'Fantastico',
           'Grandioso',
           'Graaande',
           'maestoso',
           'monumentale',
           'glorioso',
           'splendente',
           'bellissimo',
           'Adorabile',
           'Stupendo',
           'Superbo',
       ],
       [
           'Orripilante',
           'Bleah',
           'Orribile',
           'Disgustoso',
           'Senza gloria',
           'Terribile',
           'Atroce',
           'Flagitious',
           'Triste',
           'Orrendo',
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
            'está',
        ],
        [
            'aberto',
            'permitindo acesso',
        ],
        [
            'fechado',
            'não mais aberto'
        ],
        [
            'Magnífico',
            'Imponente',
            'Impressionante',
            'Inspirador',
            'Ótimo',
            'Esplêndido',
            'majestoso',
            'monumental',
            'glorioso',
            'suntuoso',
            'resplandecente',
            'generoso',
            'belo',
            'delicioso',
            'Amável',
        ],
        [
            'Que pena',
            'Desprezível',
            'Inglório',
            'Desonroso',
            'Atroz',
            'Cruel',
            'Triste',
            'Nojento',
        ]
    ],
    "tr_TR": [
        [
            'Boşluk',
            config.SPACE_NAME
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
        ],
    ],
    "es_ES": [
        [
            'El espacio',
            config.SPACE_NAME
        ],
        [
            'está',
        ],
        [
            'abierto',
            'permitiendo el acceso',
        ],
        [
            'cerrado',
            'innacesible'
        ],
        [
            'Genial',
            'Perfecto',
            'Impresionante',
            'Magnífico',
            'Nos complace que',
            'Maravilloso',
            'Fantástico',
            'Estupendo',
            'Soberbio',
            'Extraordinario',
            'Fascinante',
            'Prodigioso'
        ],
        [
            'Mierda',
            'Lamentablemente',
            'Tristemente',
            'Lo sentimos',
            'A nuestro pesar',
            'Desoladamente'
        ]
    ],
    "nb_NO": [
        [
            'Rommet',
            config.SPACE_NAME
        ],
        [
            'er',
        ],
        [
            'åpent',
            'tilgjengelig',
        ],
        [
            'stengt',
            'utilgjengelig',
            'ikke lenger tilgjengelig',
        ],
        [
            'Fantastisk',
            'Bra',
            'Kjempebra',
            'Herlig',
            'Imponerende',
            'Kult',
            'Nydelig',
            'Prima',
            'Tøft',
            'Strålende',
            'Praktfullt',
            'Helmaks',
        ],
        [
            'Søren',
            'Filler\'n',
            'Kjedelig',
            'Teit',
            'Trist',
            'Dumt',
        ]
    ],
    "nl_NL": [
        [
            'De Ruimte',
            config.SPACE_NAME
        ],
        [
            'is',
        ],
        [
            'open',
            'toegang toegestaan',
        ],
        [
            'dicht',
            'niet meer geopend'
        ],
        [
            'Geweldig',
            'Goed',
            'Indrukwekkend',
            'Cool',
            'Leuk',
            'Majestueus',
            'Monumentaal',
            'Glorieus',
            'Prachtig',
            'Glansrijk',
            'Geniaal',
            'Fantastisch',
            'Heerlijk',
        ],
        [
            'Helaas',
            'Bah',
            'Roemloos',
            'Zonde',
            'Afgrijselijk',
            'Schandelijk',
            'Zielig',
            'Verdorie',
        ]
    ],
    "el_GR": [
        [
            'The space',
            config.SPACE_NAME
        ],
        [
            'είναι',
        ],
        [
            'ανοιχτό',
            'επιτρέπει την πρόσβαση',
        ],
        [
            'κλειστό',
            'δεν ειναι πια ανοιχτό'
        ],
        [
            'Φοβερό',
            'Εξαιρετικό',
            'Εντυπωσιακό',
            'Κούλ',
            'Όμορφο',
            'μεγαλοπρεπής',
            'μνημειώσης',
            'ένδοξο',
            'πολυτελής',
            'περίλαμπρο',
            'πολυτελής',
            'ωραίο',
            'υπέροχο',
        ],
        [
            'Να παρει',
            'Μπλιάξ',
            'Άδοξος',
            'Χάλια',
            'Φρικτός',
            'Φαύλος',
            'Λυπημένος',
            'Αηδία',
        ]
    ],
    "da_DK": [
        [
            'Rummet',
            config.SPACE_NAME
        ],
        [
            'er',
        ],
        [
            'åbent',
            'tillader adgang',
        ],
        [
            'lukket',
            'ikke åbent længere'
            'ikke åbent lige nu'
        ],
        [
            'Fedt',
            'Fantastisk',
            'Kodylt',
            'Sejt',
            'Vidunderligt',
            'Skønt',
            'Smukt',
            'Dejligt',
            'Lige til at spise',
            'Perfekt',
            'Hurra',
        ],
        [
            'Åh nej',
            'Katastrofe',
            'Træls',
            'Dårligt',
            'Irriterende',
            'Nedern',
            'Forfærdeligt',
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
    except Exception:
        raise MissingTranslationException("No translation for %s found" %
                                          language)
