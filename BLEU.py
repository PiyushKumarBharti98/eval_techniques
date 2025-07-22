from collections import Counter
import math


def sentence_process(sen: str) -> list[str]:
    """docstring"""
    return list(sen.split())


def get_ngram(sen: list[str], n: int):
    """docstring"""
    ngrams = []
    for i in range(len(sen) - n + 1):
        seq = " ".join(sen[i : i + n])
        ngrams.append(seq)
    return Counter(ngrams)


def modified_precision(cand: list[str], ref: list[str], n: int):
    """docstring"""
    ngram_ref = get_ngram(ref, n)
    ngram_cand = get_ngram(cand, n)

    overlap = ngram_ref & ngram_cand  # technique to find the minimum
    total_ref = sum(overlap.values())
    total_cand = sum(ngram_cand.values())

    return total_ref / total_cand


def brevity_penalty(cand: list[str], ref: list[str]):
    """docstring"""
    r = len(ref)
    c = len(cand)

    if r <= c:
        return 1
    else:
        return math.exp(1 - r / c)


def final_bleu(cand: list[str], ref: list[str], n: int = 4, weights=None) -> float:
    """docstring"""
    if weights is None:
        weights = [1.0 / n] * n

    all_penalties = []
    for i in range(1, n + 1):
        penalty = modified_precision(cand, ref, i)
        if penalty == 0:
            return 0
        all_penalties.append(penalty)

    weighted_log_sum = sum(w * p for w, p in zip(weights, all_penalties))
    bp = brevity_penalty(cand, ref)
    return bp * math.exp(weighted_log_sum)


# test
if __name__ == "__main__":
    REF = "the cat is on the mat"
    CAND = "the cat sat on the mat"

    ref = sentence_process(REF)
    cand = sentence_process(CAND)

    bleu1 = final_bleu(ref, cand, n=4)

    bleu2 = final_bleu(ref, cand, n=2)
    print(f"BLEU1 score: {bleu1:.4f}")
    print(f"bleu2 score: {bleu2:.4f}")
