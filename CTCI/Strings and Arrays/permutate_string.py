class Solution:
    """Determine the permutation of a string"""
    def __init__(self):
        self.results = []

    def permutate_string(self, string: str):
        prefix = ""
        suffix = string
        found_string = set()
        self._permutate_string(prefix, suffix, found_string)
    
    def _permutate_string(self, prefix, suffix, memo):
        if prefix in memo:
            return

        if suffix == "":
            memo.add(prefix)
            self.results.append(prefix)
            return
        for idx, char in enumerate(suffix):
            updated_prefix = prefix + char
            updated_suffix = self._remove_character(idx, suffix)
            self._permutate_string(updated_prefix, updated_suffix, memo)
        return
    
    def _remove_character(self, index, string):
        """removes a character from a string at a given index, returns string with removed index"""
        if index == 0:
            return string[1:]

        if index == len(string) - 1:
            return string[:-1]
        
        return string[:index] + string[index + 1:]

            
    
s = Solution()
s.permutate_string("hello")
print(s.results)

        

