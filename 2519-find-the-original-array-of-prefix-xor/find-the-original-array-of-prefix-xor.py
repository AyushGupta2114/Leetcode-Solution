class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        prev = pref[0]

        for i in range(1, len(pref)):
            pref[i] ^= prev
            prev ^= pref[i]
        
        return pref
        