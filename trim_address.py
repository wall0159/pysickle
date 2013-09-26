self_5_addr = 6
self_3_addr = 26
header = "@SEQ_ID"
read = "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT"
phread_header = "+"
qual = "!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65"

def cut_reads(self_5_addr, self_3_addr, read, qual):
	## given the string 'read' will trim characters left and right characters.
	trimmed_read = read[self_5_addr:self_3_addr]
	trimmed_qual = qual[self_5_addr:self_3_addr]
	return trimmed_read
print trimmed_read


test_seq = "GGGTTCAAAGCAGTATCGAT"
