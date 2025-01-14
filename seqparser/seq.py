# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    myseq = ''
    goodinputs = {'A','C','G','T','U'}

    if set(seq).issubset(goodinputs):
        if reverse:
            return reverse_transcribe(seq)

        else:
            for _, char in enumerate(seq):
                mychar = TRANSCRIPTION_MAPPING[char]
                myseq += mychar
            return myseq
    else:
        raise ValueError("This sequence contains characters that are not acceptable nucleotides")
        

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """

    goodinputs = {'A','C','G','T','U'}

    if set(seq).issubset(goodinputs):
        fwrd = transcribe(seq, False)
        return fwrd[::-1]
    else:
        raise ValueError("This sequence contains characters that are not acceptable nucleotides")


print(reverse_transcribe('ACTGAACCC'))

print(reverse_transcribe(''))

print(transcribe('ACTGAACCC', True))
