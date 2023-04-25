s = 'Hawnj pk swhg xabkna ukq nqj.'
new_s = ''
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2

for j in range(1, 26):
    for i in range(len(s)):
        if s[i].isupper():
            ind = eng_upper_alphabet.rfind(s[i])
            new_s += eng_upper_alphabet[ind - j]
        elif s[i].islower():
            ind = eng_lower_alphabet.rfind(s[i])
            new_s += eng_lower_alphabet[ind - j]
        else:
            new_s += s[i]
        
    print(new_s)
    new_s = ''