from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys

filename = sys.argv[1]
record = next(SeqIO.parse(filename, 'fasta'))
seq = record.seq

# print(seq)

VP2 = seq[211:464]
VP1 = seq[484:901]
VP3 = seq[901:1159]

VP2_record = SeqRecord(Seq(VP2), id='VP2', description='')
VP1_record = SeqRecord(Seq(VP1), id='VP1', description='')
VP3_record = SeqRecord(Seq(VP3), id='VP3', description='')

records = [VP2_record, VP1_record, VP3_record]

output_file = open('output.faa', 'w')
SeqIO.write(records, output_file, 'fasta')
