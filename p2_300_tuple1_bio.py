# tuple 생성 
Histidine = ('H', 'CAT', 'CAC')
Lysine = 'K', 'AAA', 'AAG'
Arginine = ('R', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG')
 
print('Histidine:', Histidine)
print()
 
# a list of tuples
basic = [Histidine, Lysine]
basic.append(Arginine)
print('Basic amino acids:', basic)
print()
 
# list of tuples의 elements 이용
His = basic[0]
print('His:', His)

His_codons = basic[0][1:]
print('His codons:', His_codons)

codon1, codon2 = His_codons
print('codon1:', codon1)
print('codon2:', codon2)
print()
 
protein_seq = basic[0][0] + basic[1][0] + basic[2][0]
print('Protein:', protein_seq)
