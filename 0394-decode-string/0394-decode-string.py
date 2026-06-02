class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def decode():
            nonlocal i
            result = ""

            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1

                    i += 1  # skip '['
                    decoded = decode()  # decode inside brackets
                    i += 1  # skip ']'

                    result += decoded * num
                else:
                    result += s[i]
                    i += 1

            return result

        return decode()