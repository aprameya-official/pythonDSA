class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()
        words=words[-1::-1] #word.reverse()
        reversed=" ".join(words)
        return reversed