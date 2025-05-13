# DNA seq analysis

Python toolkit plus one-shot CLI pipeline for rapid exploratory analysis of DNA sequences.  
Fetch any NCBI accession, crunch the basics (composition, k-mers, CpG islands, low-complexity masking, motif search), and get tidy plots/tables in a single command.

---

##  Capabilities

| Switch | What it does |
|--------|--------------|
| `--gc` | Print GC content (%) |
| `--kmer <k>` | Count every k-mer of length *k* |
| `--pattern <motif>` | Report all positions where `<motif>` occurs |
| `--transcribe` | Convert DNA → RNA (T ➜ U) |
| `--revcomp` | Produce the 5′→3′ reverse-complement |

*(Flags can be combined; the tool runs them in the order given.)*

---

##  Installation

```bash
git clone https://github.com/<your-user>/dna-seq-cli.git
cd dna-seq-cli
chmod +x src/seq_analysis.py
# optional: create venv and install numpy
python -m venv .venv && source .venv/bin/activate
pip install numpy
```
##  Example
1. GC content
   
`./src/seq_analysis.py ATCGCGTA --gc`

→ GC content: 50.00 %

2. 2-mer counts
   
`./src/seq_analysis.py ATCGCGTA --kmer 2`

 → AT:1  CG:2  GC:1  GT:1  TA:1

3. Find a motif
   
 `./src/seq_analysis.py ATCGCGTA --pattern CG`

 → 'CG' found at positions: [2, 4]

4. DNA ➜ RNA

`./src/seq_analysis.py ATCGCGTA --transcribe`

 → AUCGCGUA

5. Reverse complement
   
   `./src/seq_analysis.py ATCGCGTA --revcomp`

    → TACGCGAT

## Requirements
* Python ≥ 3.6

* NumPy (for speedy k-mer math)

* argparse (bundled with Python)


 
