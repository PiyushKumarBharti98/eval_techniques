from nltk import PorterStemmer


def sentence_process(sen: str):
    """docstring"""
    stem = PorterStemmer()
    sentence = stem.stem(sen.lower())
    unigram = []
    for word in sentence.split():
        if word.isalpha():
            unigram.append(word)

    return list(unigram)


def chunk_finder(sen: list[int]):
    """docstring"""
    indices = [i for _, i in sen]


def meteor(cand: str, ref: str):
    """docstring"""

    x = sentence_process(cand)
    y = sentence_process(ref)

    c = len(x)
    r = len(x)

    match = []
    for a in x:
        for i, b in enumerate(y):
            if not :
                match.append(i)
    m = len(match)

    precision = m / c
    recall = m / r

    # harmonic mean
    f = (10 * precision * recall) / (recall + 9 * precision)
