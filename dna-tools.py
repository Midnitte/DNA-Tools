def complement(dna: str) -> str:
    """Converts DNA to the complementary strand."""
    translated = dna.maketrans("ATGC", "TACG")
    return dna.translate(translated)

def transcription(dna: str) -> str:
    """Converts DNA to mRNA."""
    translated = dna.maketrans("ATGC", "UACG")
    return dna.translate(translated)

def codons(mrna: str) -> list:
    """Break up mRNA into codons"""
    return [mrna[i:i+3] for i in range(0, len(mrna), 3)]

# TODO: decorator that prints return statements when debug on...
def amino_acids(codon: list) -> list:
    """Convert mRNA codons to amino acids."""
    match codon:
        case "AUG":
            return "Methionine"
        case "AUA" | "AUC" | "AUU":
            return "Isoleucine"
        case "ACG" | "ACA" | "ACC" | "ACU":
            return "Threonine"
        case "AGG" | "AGA" | "CGG" | "CGA" | "CGC" | "CGU":
            return "Arginine"
        case "AGC" | "AGU" | "UCG" | "UCA" | "UCC" | "UCU":
            return "Serine"
        case "AAG" | "AAA":
            return "Lysine"
        case "AAC" | "AAU":
            return "Asparagine"
        case "CUG" | "CUA" | "CUC" | "CUU" | "UUG" | "UUA":
            return "Leucine"
        case "CCG" | "CCA" | "CCC" | "CCU":
            return "Proline"
        case "CAG" | "CAA":
            return "Glutamine"
        case "CAC" | "CAU":
            return "Histidine"
        case "UUC" | "UUU":
            return "Phenylalanine"
        case "UGG":
            return "Tryptophan"
        case "UGC" | "UGU":
            return "Cysteine"
        case "UAC" | "UAU":
            return "Tyrosine"
        case "GUG" | "GUA" | "GUC" | "GUU":
            return "Valine"
        case "GCG" | "GCA" | "GCC" | "GCU":
            return "Alanine"
        case "GGG" | "GGA" | "GGC" | "GGU":
            return "Glycine"
        case "GAG" | "GAA":
            return "Glutamic Acid"
        case "GAC" | "GAU":
            return "Aspartic Acid"
        case "UGA" | "UAG" | "UAA":
            return "Stop" # Return stop, or "pass"?
        case _:
            pass

def translation(mrna):
    """Return the Amino Acid for each codon in a mRNA sequence."""
    return [amino_acids(i) for i in mrna]

def dna_to_amino(dna: str) -> list:
    """Directly translate a sequence to it's corresponding amino acids."""
    dna = dna.upper()
    return translation(codons(transcription(dna)))