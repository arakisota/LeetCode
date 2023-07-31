"""
時間計算量 : O(n), 99.94%
空間計算量 : O(1)?, 57.77%
"""

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(emails):
            local_name, domain_name = emails.split('@')
            local_name = local_name.split("+")[0].replace(".", "")
            return f"{local_name}@{domain_name}"

        return len(set(map(parse, emails)))

"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for ind, email in enumerate(emails):
            local_name, domain_name = email.split("@")
            ans = str()
            for feature in local_name:
                if feature == ".":
                    continue
                if feature == "+":
                    break
                ans += feature
            emails[ind] = ans + "@" + domain_name

        return len(set(emails))
"""