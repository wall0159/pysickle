#@SEQ_ID
#GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
#+
#!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65


self_5_addr = 6
self_3_addr = 26
header = "@SEQ_ID"
read = "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT"
phred_header = "+"
qual = "!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65"

def cut_reads(self_5_addr, self_3_addr, read, qual):
    ''' a given read and it's quality string will be from the 5' and 3' end based on the variables
    self_5_addr and self_3_addr''' 
	trimmed_read = read[self_5_addr:self_3_addr]
	trimmed_qual = qual[self_5_addr:self_3_addr]
	return trimmed_read, trimmed_qual




test_seq = "GGGTTCAAAGCAGTATCGAT"
