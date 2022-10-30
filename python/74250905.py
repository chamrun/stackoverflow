import itertools

import pandas as pd

normalizad_word = pd.DataFrame(
    {
        'wrong': ['sheis', 'taht', 'diedwhen', 'shewas'],
        'correct': ['she is', 'that', 'died when', 'she was']
    }
)

dataset = pd.DataFrame(
    {
        'review': [
            ['shewas', 'wrong', 'but', 'her', 'intentions', 'are', 'good'],
            ['is', 'taht', 'you'],
            ['he', 'diedwhen', 'he', 'was', 'young'],
        ]
    }
)

normalizad_word_dict = {}

for index, row in normalizad_word.iterrows():
    if row[0] not in normalizad_word_dict:
        normalizad_word_dict[row[0]] = row[1]


def normalized_term(document):
    # return [normalizad_word_dict[term].split(' ') if term in normalizad_word_dict else term for term in document]

    return list(itertools.chain(*[normalizad_word_dict[term].split() if term in normalizad_word_dict else term.split() for term in document]))



dataset['review_normalized'] = dataset['review'].apply(normalized_term)

print(dataset['review_normalized'])
