import array
import collections
import sys

eng_freq = [ 'e','t','n','a','i','r','o','s','h','l','d','c','u','m','g','f','p','w','y','b','v','k','x','j','q','z']
file = open("real-ciphertext.txt")
freq = collections.defaultdict(int)

#make frequency
while True:
    char = file.read(1)
    if not char:
        break
    if char.isalpha():
        freq[char] +=1
    
file.close()

sorted_keys = [k for k, v in sorted(freq.items(), key=lambda item: -item[1])]

mapping = collections.defaultdict(str)
for idx in range(26):
    mapping[sorted_keys[idx]] = eng_freq[idx]
    print("cipher freq: " + sorted_keys[idx] + " plain freq: " + eng_freq[idx])
keyfile = open("task1key.txt","w")

for i in range (26):
    keyfile.write(mapping[chr(97 + i)] + " ")
keyfile.close()

plainfile = open("plain.txt", "w")
cipherfile = open("real-ciphertext.txt")

gap = int(sys.argv[1])
while True:
    char = cipherfile.read(1)
    if not char:
        break
    if char.isalpha():
        char_ascii = ord(mapping[char])+gap if (ord(mapping[char])+gap < 97 + 26)   else ord(mapping[char])+gap -26
        plainfile.write(chr(char_ascii))
    else :
        plainfile.write(char)

cipherfile.close()
plainfile.close()

	