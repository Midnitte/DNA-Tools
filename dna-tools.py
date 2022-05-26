def complement(dna):
    """Converts DNA to the complementary strand."""
    translated = dna.maketrans("ATGC", "TACG")
    return dna.translate(translated)

def transcription(dna):
    """Converts DNA to mRNA."""
    translated = dna.maketrans("ATGC", "UACG")
    return dna.translate(translated)