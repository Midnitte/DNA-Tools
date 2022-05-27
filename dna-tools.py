def complement(dna):
    """Converts DNA to the complementary strand."""
    translated = dna.maketrans("ATGC", "TACG")
    return dna.translate(translated)

def transcription(dna):
    """Converts DNA to mRNA."""
    translated = dna.maketrans("ATGC", "UACG")
    return dna.translate(translated)

def amino_acids(dna):
    """Convert mRNA to amino acids."""
    match dna:
        case "AUG":
            return "Methionine"
        case ["AUA", "AUC", "AUU"]:
            return "Isoleucine"
        case ["ACG", "ACA", "ACC", "ACU"]:
            return "Threonine"
        case ["AGG", "AGA"]: #Add more Arginine and Serine matches
            return "Arginine"
        case ["AGC", "AGU"]:
            return "Serine"
        # WIP
        

