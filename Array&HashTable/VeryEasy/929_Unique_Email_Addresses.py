from typing import List

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