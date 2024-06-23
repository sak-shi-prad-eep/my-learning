class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result=[]
        for char in range(ord('a'),ord('z')+1):
            min_count=float('inf')
            char=chr(char)
            for word in words:
                count=word.count(char)
                min_count=min(count,min_count)
                if min_count==0:
                    break

            result.extend(min_count*[char])
        return result
                        
        