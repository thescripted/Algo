class Node:
    def __init__(self, children={}, isWord=False):
        self.children = children
        self.isWord = isWord
    
class Solution:
    def __init__(self):
        self.trie = None
    
    def build(self, words: List[str]):
        self.trie = Node()
        for word in words:
            current = self.trie
            for char in word:
                if not char in current.children:
                    current.children[char] = Node()
                current = current.children[char]
            current.isWord = True
            

    def autocomplete(self, prefix: str) -> List[str]:
        current = self.trie
        for char in prefix:
            if not char in current.children:
                return []
            current = current.children[char]
        return _findWordsFromNode(current, prefix)
    
    def _findWordsFromNode(self, current: Node, prefix: str):
        words = []
        if current.isWord:
            words += [prefix]
            for char in current.children:
                words += self._findWordsFromNode(current.children[char], prefix + char)
        return words

s = Solution()
s.build(["dog", "door", "doubt", "cat", "dark"])
s.autocomplete("do")
# ["dog", "door", "doubt"]