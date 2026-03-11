# 제한 효소를 dictionary를 이용하여 처리
restriction_enzymes = {'EcoRI' : 'GAATTC',
                        'AluI' : 'AGCT',
                        'NotI' : 'GCGGCCGC',
                        'TaqI' : 'TCGA'
                      }
 
print(restriction_enzymes)
print()
 
# 현 데이터에 수록된 key 목록 t
keys = list(restriction_enzymes.keys())
print('Keys as a list:', keys)
 
# 현 데이터에 수록된 values 목록 
values = list(restriction_enzymes.values())
print('Values as a list:', values)
 
# 특정 key가 dictionary에 있는지 확인 
mykey = 'crispr'
check = mykey in restriction_enzymes
print('Is', mykey, 'key in the dictionary?', check)
print()
