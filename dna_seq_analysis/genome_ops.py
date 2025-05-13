import numpy as np, pandas as pd
from collections import Counter

def _gc_oe(win):
    c = Counter(win)
    g, ccount = c['G'], c['C']
    n = len(win)
    oe = win.count("CG") / ((ccount/n)*(g/n)*(n-1) or 1)
    gc = 100*(g+ccount)/n
    return gc, oe

def find_cpg_islands(seq, window=200, min_gc=50, min_oe=0.6, step=50):
    seq = seq.upper(); n = len(seq)
    hits=[]
    i=0
    while i+window<=n:
        gc,oe=_gc_oe(seq[i:i+window])
        if gc>=min_gc and oe>=min_oe:
            start=i; end=i+window
            while end+window<=n and _gc_oe(seq[end:end+window])[0]>=min_gc:
                end+=step
            hits.append((start,end,end-start,gc,oe)); i=end
        else: i+=step
    return pd.DataFrame(hits, columns=["start","end","length","gc_pct","oe"])

def dust_mask(seq, window=64, threshold=20):
    seq=seq.upper(); n=len(seq); mask=np.zeros(n,bool)
    triples=[seq[i:i+3] for i in range(n-2)]
    for i in range(n-window+1):
        win=triples[i:i+window-2]
        score=sum(v*(v-1)//2 for v in Counter(win).values())*10/(window-2)
        if score>threshold: mask[i:i+window]=True
    return ''.join(b.lower() if m else b for b,m in zip(seq,mask))
