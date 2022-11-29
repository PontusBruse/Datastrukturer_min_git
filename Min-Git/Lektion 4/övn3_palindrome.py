class DequePal:

    def is_palindrome(self,word):
        letters = []
        if len(word) <= 0:
            raise IndexError("type at least one letter")
        elif len(word) == 1:
            return True
        else:
            for letter in word:
                letters.append(letter)

        while len(letters) > 1:
            if letters[0] == letters [-1]:
                del letters[0]
                del letters[-1]
                if len(letters) <= 1:
                    return True

            else:
                return False




if __name__ == '__main__':
    dp = DequePal()
    print(dp.is_palindrome("a"))
    print(dp.is_palindrome("apan"))
    print(dp.is_palindrome("apa"))