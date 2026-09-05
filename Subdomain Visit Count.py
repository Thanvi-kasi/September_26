class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}

        for cpdomain in cpdomains:
            visits, domain = cpdomain.split()
            visits = int(visits)

            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                count[subdomain] = count.get(subdomain, 0) + visits

        result = []

        for domain, visits in count.items():
            result.append(str(visits) + " " + domain)

        return result
