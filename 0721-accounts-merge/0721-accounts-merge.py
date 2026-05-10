from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):

        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_name = {}

        # initialize
        for acc in accounts:
            name = acc[0]

            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email

                email_to_name[email] = name

            first = acc[1]

            for email in acc[2:]:
                union(first, email)

        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []

        for root, emails in groups.items():
            res.append(
                [email_to_name[root]] + sorted(emails)
            )

        return res