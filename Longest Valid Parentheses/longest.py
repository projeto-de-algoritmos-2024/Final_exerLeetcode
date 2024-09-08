class Solution:
    def longestValidParentheses(self, s):
        dp = [0] * len(s)
        max_len = 0

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2

            max_len = max(max_len, dp[i])

        return max_len

# # Exemplos de uso
# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.longestValidParentheses("(()"))
#     print(solution.longestValidParentheses(")()())"))
#     print(solution.longestValidParentheses(""))