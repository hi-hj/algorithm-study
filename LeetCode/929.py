from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 1. Split local & domain (@)
        # 2. Ignore only . in local
        # 3. Ignore after + in local
        # 4. Add to Set
        # 5. Return len of set
        
        result = set()
        for email in emails:
            local, domain = map(list, email.split("@"))
            while '.' in local:
                local.remove('.')
            if '+' in local:
                local = local[:local.index('+')]
            result.add(''.join(local) +'@'+ ''.join(domain))
        
        
        return len(result)