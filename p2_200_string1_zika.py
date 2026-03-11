# str.upper() 대문자로 변환 
DNA_seq = 'atgagtaaag...actatacaaa'
DNA_seq = DNA_seq.upper()

print('DNA sequence: ' + DNA_seq)


# Forward index 
print("The second NT", DNA_seq[1])


# Backward index ; -1부터 
print("The last NT", DNA_seq[-1])

# Slicing a string
# First codon
first_codon = DNA_seq[0:3]

# last codon
last_codon = DNA_seq[-3:]
