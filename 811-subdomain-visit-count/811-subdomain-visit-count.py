class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_to_count = {}
        
        def parse_inner(string):
            count,domain = string.split()
            subdomains = domain.split('.')
            
            for i in range(len(subdomains)):
                dom = '.'.join(subdomains[i:])
                domain_to_count[dom] = domain_to_count.get(dom,0) + int(count)
            
        ans = []
        for domains in cpdomains:
            parse_inner(domains) 
        for dom,count in domain_to_count.items():
            ans.append(str(count) + ' ' + dom)
        
        return ans
            
        