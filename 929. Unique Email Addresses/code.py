class Solution(object):
    def removeDotAndAdd(self, email):
        res = ''
        flag = True
        for i in range(len(email)):
            if email[i] == '@':
                res += email[i:]
                break;

            if email[i] == '.':
                continue

            if email[i] == '+':
                flag = False

            if flag:
                res += email[i]
        return res
    
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        
        for email in emails:
            res.add(self.removeDotAndAdd(email))
        
        return len(res)
