class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Frequency map for characters in t
        seen = {}
        for ch in t:
            seen[ch] = seen.get(ch, 0) + 1

        required = len(seen)   # number of unique chars needed
        formed = 0             # number of chars meeting required frequency

        window = {}
        l = 0

        min_len = float("inf")
        start = 0

        for r in range(len(s)):
            char = s[r]

            # Add current character to window
            window[char] = window.get(char, 0) + 1

            # Check if frequency matches
            if char in seen and window[char] == seen[char]:
                formed += 1

            # Try shrinking the window
            while formed == required:
                
                # Update minimum window
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                # Remove left character
                left_char = s[l]
                window[left_char] -= 1

                # If frequency falls below requirement
                if left_char in seen and window[left_char] < seen[left_char]:
                    formed -= 1

                l += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]