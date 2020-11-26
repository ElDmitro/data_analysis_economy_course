VOWELS = 'aehiouwy'
CONSONANT_RANKS = [
    'bfpv',
    'cgjkqsxz',
    'dt',
    'l',
    'mn',
    'r',
]


def get_soundex_table():
    to_replace = [f'{i}' * len(item) for i, item in enumerate(CONSONANT_RANKS, 1)]
    return str.maketrans(''.join(CONSONANT_RANKS), ''.join(to_replace), VOWELS)


def get_soundex_code(word):
    soundex_table = get_soundex_table()
    start_letter, suffix = word[0], word[1:]
    suffix = suffix.translate(soundex_table)
    suffix = ''.join([letter for i, letter in enumerate(suffix) if not i or letter != suffix[i - 1]])

    return f'{start_letter + suffix[:3]:0<4}'


word = input()
print(get_soundex_code(word))
