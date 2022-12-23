class HashingFingerprint:
    """
        Class Hashing Fingerprint creates an Array of Fingerprints for the document that is being passed
        into its hashing_fingerprint function.
    """
    def __init__(self):
        self.arr = []

    def hashing_fingerprint(self, file):
        file_list = []
        with open(file, mode='r') as f:
            for line in f:
                for each_word in line.split(" "):
                    file_list.append(each_word)

            for each_word in file_list:
                h = 0
                for char in each_word:
                    h += ord(char) % 100
                # print("Hash: {0} = {1}".format(h, each_word))
                self.arr.append(h)
        return self.arr
        # print(self.arr)


if __name__ == "__main__":
    hash_file1 = HashingFingerprint()
    hash_file1.hashing_fingerprint("doc_to_parse.txt")
    print(hash_file1.hashing_fingerprint("doc_to_parse.txt"))
    print(hash_file1.hashing_fingerprint("doc_to_parse.txt")[9])
