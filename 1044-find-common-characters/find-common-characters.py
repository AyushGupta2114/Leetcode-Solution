class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a=words[0]
        for i in range(0,len(words)-1):
            dict1=Counter(a) 
            dict2=Counter(words[i+1]) 
        # take intersection of these dictionaries 
            commonDict = dict1 & dict2 
            # get a list of common elements 
            commonChars = list(commonDict.elements()) 
            # sort list in ascending order to print resultant 
            # string on alphabetical order 
            commonChars = sorted(commonChars) 
            a=commonChars
            # join characters without space to produce 
            # resultant string
        return a

        