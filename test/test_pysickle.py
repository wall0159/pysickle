# test the main program

def no_file_specified():
    assert not pysickle

def correctly_read_arguments():
    pysickle = fastq_pysickle('./test/test.fastq', 30, 'illumina', 0.1, '')
    assert pysickle.infile == './test/test.fastq'
    assert pysickle.threshold == 30
    assert pysickle.phred_type == 'illumina'
    assert pysickle.window_size == 0.1
    assert length(pysickle.outfile) == 0
    
    
