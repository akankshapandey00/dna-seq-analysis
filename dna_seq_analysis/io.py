from pathlib import Path
from typing import Optional
from Bio import Entrez, SeqIO

Entrez.email = "your.email@example.com"  # change me!

def fetch_fasta(accession: str, outfile: Optional[Path] = None):
    if outfile is None:
        outfile = Path("data") / f"{accession}.fasta"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    if outfile.exists():
        return SeqIO.read(outfile, "fasta")
    with Entrez.efetch(db="nucleotide", id=accession,
                       rettype="fasta", retmode="text") as h:
        rec = SeqIO.read(h, "fasta")
    SeqIO.write(rec, outfile, "fasta")
    return rec

def save_fasta(rec, path: Path):
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
    if isinstance(rec, str):
        rec = SeqRecord(Seq(rec), id="sequence", description="")
    SeqIO.write(rec, path, "fasta")

_DNA2RNA = str.maketrans("Tt", "Uu")
def transcribe(seq) -> str:
    s = str(seq)
    if "U" in s.upper():
        raise ValueError("Input already RNA (contains U)")
    return s.translate(_DNA2RNA)
