class Solution:
    def string_reversal(self, string: str) -> str:
        string_array = list(string)
        for i in range(len(string_array) // 2):
            string_array[i], string_array[len(string_array) - i - 1] = \
                string_array[len(string_array) - i - 1], string_array[i]
        return ''.join(string_array)

    

s = Solution()
string = "Hello ben"
reversed_string = s.string_reversal(string)
print(reversed_string) # "neb olleh"


class Duplicates: 
    def remove_duplicates(self, root):
        visited_node = set(root)
        current = root.next
        prev = root
        while current is not None:
            if current not in visited_node:
               visited_node.add(current)
               prev = current
                else:
                prev.next = current.next
            current = current.next
        return root
            
        
