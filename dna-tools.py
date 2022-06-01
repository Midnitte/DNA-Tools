def complement(dna):
    """Converts DNA to the complementary strand."""
    translated = dna.maketrans("ATGC", "TACG")
    return dna.translate(translated)

def transcription(dna):
    """Converts DNA to mRNA."""
    translated = dna.maketrans("ATGC", "UACG")
    return dna.translate(translated)

# TODO
def codons(mrna):
    """Break up mRNA into codons"""
    return ""

# TODO: decorator that prints return statements when debug on...
def amino_acids(codon):
    """Convert mRNA codons to amino acids."""
    match codon:
        case "AUG":
            return "Methionine"
        case ["AUA", "AUC", "AUU"]:
            return "Isoleucine"
        case ["ACG", "ACA", "ACC", "ACU"]:
            return "Threonine"
        case ["AGG", "AGA", "CGG", "CGA", "CGC", "CGU"]:
            return "Arginine"
        case ["AGC", "AGU", "UCG", "UCA", "UCC", "UCU"]:
            return "Serine"
        case ["AAG", "AAA"]:
            return "Lysine"
        case ["AAC", "AAU"]:
            return "Asparagine"
        case ["CUG", "CUA", "CUC", "CUU", "UUG", "UUA"]:
            return "Leucine"
        case ["CCG", "CCA", "CCC", "CCU"]:
            return "Proline"
        case ["CAG", "CAA"]:
            return "Glutamine"
        case ["CAC", "CAU"]:
            return "Histidine"
        case ["UUC", "UUU"]:
            return "Phenylalanine"
        case ["UGG"]:
            return "Tryptophan"
        case ["UGC", "UGU"]:
            return "Cysteine"
        case ["UAC", "UAU"]:
            return "Tyrosine"
        case ["GUG", "GUA", "GUC", "GUU"]:
            return "Valine"
        case ["GCG", "GCA", "GCC", "GCU"]:
            return "Alanine"
        case ["GGG", "GGA", "GGC", "GGU"]:
            return "Glycine"
        case ["GAG", "GAA"]:
            return "Glutamic Acid"
        case ["GAC", "GAU"]:
            return "Aspartic Acid"
        case ["UGA", "UAG", "UAA"]:
            return "Stop" # Return stop, or "pass"?

        # WIP
        

