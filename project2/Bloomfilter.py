import xxhash
import hashlib
import sys

class BloomFilter:
    def __init__(self, size_ = 8192):
        self.size = size_
        self.bloomfilter = [False] * self.size

    def _hash(self, elem ):
        xxh_hashval = xxhash.xxh64(elem).intdigest()
        blake_hashval = int(hashlib.blake2b(elem.encode('utf-8')).hexdigest(), 16)
        kirshopt_hashval = xxh_hashval + 7 * blake_hashval

        xxh_hashval = xxh_hashval % self.size
        blake_hashval = blake_hashval % self.size
        kirshopt_hashval = kirshopt_hashval % self.size

        return (xxh_hashval,blake_hashval,kirshopt_hashval)
    
    def add(self, elem):
        hash_val = self._hash(elem)
        for i in hash_val:
            self.bloomfilter[i] = True
    
    def contain(self, elem):
        hash_val = self._hash(elem)

        for i in hash_val:
            if self.bloomfilter[i] == False:
                return False
    
        return True


##### Building Bloom Filter #####

print("type q if you want to quit\n")


bf = BloomFilter()
dict_cnt = 0
bloom_dict = sys.argv[1]
with open (bloom_dict, 'r') as f:
    for line in f:
        bf.add(line.strip())
        dict_cnt = dict_cnt + 1

### for password checking
if len(sys.argv) == 2:
    bf_chk = open("Bloomchecked.txt","w")
    while True:
        p = input("type password: ")
        if p == "q":
            bf_chk.close()
            sys.exit(1)
        if bf.contain(p):
            bf_chk.write(p + " 1\n")
            print("Accepted")
        else:
            bf_chk.write(p + " 0\n")
            print("Rejected")



##### checking test_candidate.txt file #####
##### False Positive checking #####
count = 0
poscnt = 0
bf_checked = open ("Bloomchecked.txt","w")
test_candidate = sys.argv[2]
with open(test_candidate,"r") as f:
    for line in f:
        if bf.contain(line.strip()):
            bf_checked.write(line.strip() + " 1\n")
            poscnt = poscnt + 1
        else:
            bf_checked.write(line.strip() + " 0\n")
        count = count + 1
        #print("running: ",'{:.3f}%'.format((count / 321271704) * 100) , end = "\r" )

print("Dict word num: ",dict_cnt," Positive num: ", poscnt,"\n") 
print("Done!\n")

bf_checked.close()


#  321271704
#  20134677
#  20274603 
# python3 Bloomfilter.py dictionary.txt
#  python3 Bloomfilter.py dictionary.txt test_candidate.txt