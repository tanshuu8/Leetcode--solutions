class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        num &= 0xFFFFFFFF
        res = ""

        while num:
            res = hex_chars[num & 15] + res
            num >>= 4

        return res