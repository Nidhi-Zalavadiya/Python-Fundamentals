class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        actual = x #This stores the actual number has to check
        reverse = 0 #this is reverse number we'll update letter
        while x > 0: #loop from x to 0
            last_digit = x % 10 #Find remeinder of which is last digit of number
            reverse = reverse * 10 + last_digit # store reverse number * 10 and add last digit of number find in above
            # remove last digit from x 
            x = x // 10

        if reverse == actual:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(12321))