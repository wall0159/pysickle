import Bio
from Bio import SeqIO

# functions to perform moving average filtering of the phred scores and return indices at which to trim

# return a moving average filtered set of phred scores
def filter_on_quality(numeric_quality_score, window_width):
    # 
    filtered_numeric_quality_score = list([])
    return filtered_numeric_quality_score 

# return indexes at which to trim the sequence
def trim_on_quality(filtered_numeric_quality_score, sequence, threshold):
    # trim the quality score, and the sequence based on the threshold quality
    
    # return a new sequence object that has been trimmed
    pass
