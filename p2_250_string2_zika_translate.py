zika_DNA = 'AGTTGTTGATCTGTGTGAGTCAG'
print("Direct strand:        5' " + zika_DNA + " 3'")
 
complements = zika_DNA.maketrans('acgtACGT', 'tgcaTGCA')
complement_seq = zika_DNA.translate(complements)
 
bonds = " "*25 + "|"*len(zika_DNA)
print(bonds)
print("Complementary strand: 3' " + complement_seq + " 5'")
