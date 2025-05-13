from collections import Counter
def nucleotide_stats(seq: str):
    seq = seq.upper()
    wanted = "ATCG"
    c = Counter(b for b in seq if b in wanted)
    total = sum(c.values())
    pct = {b: c[b] / total * 100 if total else 0 for b in wanted}
    return c, pct, total

def kmer_counts(seq: str, k=4, ignore_amb=True):
    seq = seq.upper()
    out = Counter()
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if ignore_amb and set(kmer) - set("ATCG"):
            continue
        out[kmer] += 1
    return out
