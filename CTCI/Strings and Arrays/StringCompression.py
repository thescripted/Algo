class Compression:
    def compress_string(self, string):
        if not string or len(string) == 0: 
            return string
        result = ''
        count = 0
        prev_char = string[0]
        for char in string:
            if char == prev_char:
                count += 1
            else:
                result += self._add_partial(prev_char, count)
                prev_char = char
                count = 1
        result += self._add_partial(prev_char, count)
        return result if len(result) > len(string) else string

    def _add_partial(self, char, count):
        return char + (str(count) if count > 1 else '')


