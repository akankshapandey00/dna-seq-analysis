import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter, StrMethodFormatter

def plot_nucleotide_composition(pct, counts, ax=None):
    bases = ["A","T","C","G"]
    colors = ["#4daf4a","#ff7f00","#377eb8","#984ea3"]
    if ax is None:
        fig, ax = plt.subplots(figsize=(6,4), dpi=120)
    bars = ax.bar(bases, [pct[b] for b in bases],
                  color=colors, edgecolor='black', lw=.6)
    for bar,b in zip(bars,bases):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+.5,
                f"{pct[b]:.2f}%\n({counts[b]:,})",
                ha='center', va='bottom', fontsize=8)
    ax.set_ylabel("Percentage (%)")
    ax.yaxis.set_major_formatter(PercentFormatter())
    ax.set_title("Nucleotide composition")
    plt.tight_layout()
    return ax

def plot_top_kmers(counts, top=20, ax=None):
    kmers, vals = zip(*counts.most_common(top))
    if ax is None:
        fig, ax = plt.subplots(figsize=(0.4*len(kmers)+2,4), dpi=120)
    bars = ax.bar(kmers, vals, edgecolor='black', lw=.5, color="#4C72B0")
    for bar,v in zip(bars,vals):
        ax.text(bar.get_x()+bar.get_width()/2, v+max(vals)*0.01,
                f"{v:,}", ha='center', va='bottom', fontsize=7)
    ax.set_xlabel("k-mer")
    ax.set_ylabel("Count")
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,}'))
    plt.xticks(rotation=90)
    plt.tight_layout()
    return ax
