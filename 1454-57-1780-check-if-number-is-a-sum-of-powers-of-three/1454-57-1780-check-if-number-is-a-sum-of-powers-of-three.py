class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        div = n
        while div != 0:
            curr_reste = div%3
            if curr_reste == 2 :
                return False
            div = div//3
        return True
