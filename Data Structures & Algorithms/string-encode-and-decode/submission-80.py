class Solution:

    def encode(self, strs: List[str]) -> str:
        #Hello, Hello, world, world, world
        #[""]
        #"hello", "world", "hello"
        #"this is a sentence"
        encoded_str = ""
        for v in strs:
            encoded_str += f"{len(v)}#{v}"
        return encoded_str

# string = "1# #"
    def decode(self, s: str) -> List[str]:
        listOfWords = []
        i = 0

        stringValue = ""
        length = len(s)

        while i < length:
            val = s[i]

            if val.isdigit():
                stringValue += val
                i += 1
            elif val == "#":
                count = int(stringValue)
                stringValue = ""

                word = s[i+1:i+1+count] 
                listOfWords.append(word)

                #reset
                i += 1 + count
        return listOfWords

# if __name__ == "__main__":
#     strs=["Hello","World"]
#     encode(strs)
