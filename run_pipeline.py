#!/usr/bin/env python
import argparse, pathlib
from dnaseq_toolkit import io, stats, plots, genome_ops

def main():
    p=argparse.ArgumentParser("DNA-Seq quick pipeline")
    p.add_argument("accession")
    p.add_argument("-o","--outdir",default="results")
    args=p.parse_args()

    out=pathlib.Path(args.outdir); out.mkdir(exist_ok=True)
    rec=io.fetch_fasta(args.accession, out/f"{args.accession}.fasta")
    seq=rec.seq

    c,pct,_=stats.nucleotide_stats(seq)
    ax=plots.plot_nucleotide_composition(pct,c)
    ax.figure.savefig(out/"nucleotide_composition.png",dpi=300)

    islands=genome_ops.find_cpg_islands(seq)
    islands.to_csv(out/"cpg.tsv",sep="\t",index=False)

    masked=genome_ops.dust_mask(seq)
    (out/"softmask.fasta").write_text(">masked\n"+"\n".join(masked[i:i+60] for i in range(0,len(masked),60)))

    print("✓ Done →",out)

if __name__ == "__main__":
    main()
