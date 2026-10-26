class Solution:
    def containsDuplicate(self, nums):
        vistos = set()

        for numero in nums:
            if numero in vistos:
                return True

            vistos.add(numero)

        return False