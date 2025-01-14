# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """

    goodfasta = 'data/test.fa'
    goodparser = FastaParser(goodfasta)
    assert goodparser.filename == 'data/test.fa'

    goodinputs = {'A','C','G','T','U'}

    for sequence in goodparser:
        assert isinstance(sequence[0], str) #make sure the sequence is a string
        assert isinstance(sequence[1], str) #make sure the input is a string
        assert set(sequence[1]).issubset(goodinputs) #make sure that the input is ok nucleotides
        assert sequence[0][0:3] == 'seq' #make sure the start of the sequence is seq
    
    badfasta = 'tests/bad.fa'

    with pytest.raises(ValueError): #make sure the file with no inputs raises value error
        badparser = FastaParser(badfasta)
        for sequence in badparser:
            pass

    emptyfasta = 'tests/blank.fa'
    with pytest.raises(ValueError):
        emptyparser = FastaParser(emptyfasta)
        for sequence in emptyparser:
            pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fasta = 'data/test.fa'
    fastq = 'data/test.fq'
    for seq in FastaParser(fastq): #check to make sure the first item of the fastq is none
        assert seq[0] is None
        break

    for seq in FastaParser(fasta): #check to make sure the first item of the fasta is not none
        assert seq[0] is not None



def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    goodinputs = {'A','C','G','T','U'}

    goodfastq = 'data/test.fq'
    goodparser = FastqParser(goodfastq)
    for sequence in goodparser:

        assert isinstance(sequence[0], str)
        assert isinstance(sequence[1], str)
        assert isinstance(sequence[2], str)
        assert sequence[0][0:3] == 'seq'
        assert set(sequence[1]).issubset(goodinputs)



def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fasta = 'data/test.fa'
    fastq = 'data/test.fq'
    for seq in FastqParser(fastq): #check to make sure the first item of the fastq is none
        assert seq[0] is not None

    for seq in FastqParser(fasta): #check to make sure the first item of the fasta is not none
        assert seq[0] is None
        break