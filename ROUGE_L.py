def sentence_process(sen: str) -> list[str]:
    """docstring"""
    return list(sen.lower().split())


def subsequence(cand: list[str], ref: list[str]) -> int:
    """subsequence"""
    m = len(cand)
    n = len(ref)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if cand[i - 1] == ref[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def rouge(cand: list[str], ref: list[str], beta: float = 1.0):
    """docstring"""

    overlap = subsequence(cand, ref)

    cand_len = len(cand)
    ref_len = len(ref)

    precision = overlap / cand_len
    recall = overlap / ref_len

    f1_numerator = (1 + beta**2) * precision * recall
    f1_denominator = recall + (beta**2 + precision)

    final_f1 = f1_numerator / f1_denominator

    return {
        f"overlap:{overlap},cad len: {cand_len}, reflen : {ref_len}, precision: {precision}, recall: {recall}, final_f1: {final_f1}"
    }


# test
if __name__ == "__main__":
    REF = "the cat sat on the mat"
    CAND = "the cat is on the mat"

    reference = sentence_process(REF)
    candidate = sentence_process(CAND)

    rouge1 = rouge(candidate, reference)

    rouge2 = rouge(candidate, reference)
    print(f"rouge1 score: {rouge1}")
    print(f"rouge2 score: {rouge2}")
