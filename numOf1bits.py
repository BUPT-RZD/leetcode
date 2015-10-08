class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        binary=str('{:b}'.format(n))
        for i in binary:
            if i == '1':
                sum+=1
        return sum
