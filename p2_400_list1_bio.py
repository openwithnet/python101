# list 생성
stop_codons = ['TAA', 'tAG']
print(stop_codons)
 
# list 항목 조회
first_stop_codon = stop_codons[0]
print(first_stop_codon)
 
# list 항목 수정
stop_codons[1] = 'TAG'
print(stop_codons)
 
# list 항목 추가
stop_codons.append('TGA')
print(stop_codons)

# string으로 변환
DNA_seq = ''.join(stop_codons)
print(DNA_seq)
 
# string에서 list로 변환
DNA_list = list(DNA_seq)
print(DNA_list)
 
# Slicing a list
second_codon = DNA_list[3:6]             # index 6 not included
print('Second codon:', second_codon)
