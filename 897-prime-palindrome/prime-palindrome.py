class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2: return False
            if x == 2 or x == 3: return True
            if x % 2 == 0 or x % 3 == 0: return False
            for i in range(5, int(math.sqrt(x)) + 1, 6):
                if x % i == 0 or x % (i + 2) == 0:
                    return False
            return True

        # Special case
        if n <= 11:
            for x in [2, 3, 5, 7, 11]:
                if x >= n:
                    return x

        # Generate odd-length palindromes only
        for half in range(1, 100000):  # Enough to cover up to 2 * 10^8
            s = str(half)
            pal = int(s + s[-2::-1])  # Generate odd-length palindrome
            if pal >= n and is_prime(pal):
                return pal

