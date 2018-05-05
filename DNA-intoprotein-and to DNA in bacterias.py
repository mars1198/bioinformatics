from Bio.Data.CodonTable import unambiguous_dna_by_id
bact_trans=unambiguous_dna_by_id[11]
print (bact_trans.forward_table['GTC']) # what protein is it
print (bact_trans.back_table['R']) # what amino is it
