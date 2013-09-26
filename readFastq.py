from Bio import SeqIO
good_reads = (rec for rec in \
            SeqIO.parse("testFastq1.fastq", "fastq") \
			# just need to change this to work on a window base cuttoff
            if min(rec.letter_annotations["phred_quality"]) >= 20)
count = SeqIO.write(good_reads, "good_quality.fastq", "fastq")
print "Saved %i reads" % count
