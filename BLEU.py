from collections import Counter
from functools import total_ordering


def get_ngram(sen: str, n: int):
    """docstring"""
    words = sen.split()
    ngrams = []
    for i in range(len(sen) - n + 1):
        seq = " ".join(words[i : i + n])
        ngrams.append(seq)
    return Counter(ngrams)


def modified_precision(cand: str, ref: str, n: int):
    """docstring"""
    ngram_ref = get_ngram(ref, n)
    ngram_cand = get_ngram(cand, n)

    overlap = ngram_ref & ngram_cand
    total_ref = sum(overlap.values())
    total_cand = sum(ngram_cand.values())

    return total_cand / total_ref
