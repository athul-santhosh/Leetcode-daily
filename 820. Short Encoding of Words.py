class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        create a set seen 
        Loop throught the words adding every words on to the seen
        
        use another for loop inside it and check wether the element is present in it from backwards
        
        if the element is present then remove that element from the set
        
        
        """
        words.sort(key = lambda x:len(x))
        seen = set() 
        for word in words:
            seen.add(word)
            n = len(word)
            for i in range(1,n):
                req = (word[-i:])
                #print(req)
                if req in seen:                 
                    seen.remove(req)
        length = 0
        for word in seen:
            length += len(word) + 1
        return length