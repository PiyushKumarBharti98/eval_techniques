from collections import Counter



def sentence_process(sen: str) -> list[str]:
    """docstring"""
    return list(sen.split())


def get_ngram(sen: list[str], n: int):
    """docstring"""
    ngrams = []
    for i in range(1, len(sen) - n + 1):
        seq = " ".join(sen[i : i + n])
        ngrams.append(seq)
    return Counter(ngrams)


def rouge(cand: list[str], ref: list[str], n: int = 4):
    """docstring"""
    ngram_cand = get_ngram(cand, n)
    ngram_ref = get_ngram(ref, n)

    # lowest common subsequence
    overlap = ngram_cand & ngram_ref

    cand_len = len(cand)
    ref_len = len(ref)

    precision = len(overlap) / cand_len
    recall = len(overlap) / ref_len

    f1 = 
