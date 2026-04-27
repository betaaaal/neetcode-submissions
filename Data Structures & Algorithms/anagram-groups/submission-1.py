class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for words in strs:
            sorted_words="".join(sorted(words))
            print(sorted_words)
            if sorted_words in anagrams:
                anagrams[sorted_words].append(words)
            else:
                anagrams[sorted_words]=[words]   
        return list(anagrams.values())

