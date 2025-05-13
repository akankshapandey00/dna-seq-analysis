import re
from collections import namedtuple
IUPAC = dict(A="A",C="C",G="G",T="T",R="[AG]",Y="[CT]",S="[GC]",W="[AT]",
             K="[GT]",M="[AC]",B="[CGT]",D="[AGT]",H="[ACT]",V="[ACG]",N="[ACGT]")
COMP=str.maketrans("ACGTacgt","TGCAtgca")
Hit=namedtuple("Hit","start end strand match")

def _iupac_to_regex(motif):
    return ''.join(IUPAC.get(b.upper(), re.escape(b)) for b in motif)

def revcomp(seq): return seq.translate(COMP)[::-1]

def find_motif(seq, motif, iupac=True, both=True):
    seq=seq.upper(); pat=_iupac_to_regex(motif) if iupac else re.escape(motif)
    rg=re.compile(f"(?=({pat}))")
    for m in rg.finditer(seq): yield Hit(m.start(),m.start()+len(m.group(1)),"+",m.group(1))
    if both:
        rc=_iupac_to_regex(revcomp(motif)) if iupac else re.escape(revcomp(motif))
        if rc!=pat:
            rg2=re.compile(f"(?=({rc}))")
            for m in rg2.finditer(seq):
                yield Hit(m.start(),m.start()+len(m.group(1)),"-",m.group(1))
