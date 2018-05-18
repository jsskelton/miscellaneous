import requests
import json

ml_link = 'http://internal-corp-uai2001106-dev-atlas-1790190318.us-east-1.elb.amazonaws.com/api/v1/tags/name?q=source,netapp,:eq'
print(ml_link)
r = requests.get(ml_link)
ml_txt = r.text
ml = json.loads(ml_txt)
print ml
nl_link = 'http://internal-corp-uai2001106-dev-atlas-1790190318.us-east-1.elb.amazonaws.com/api/v1/tags/dnsName?q=source,netapp,:eq'
print(nl_link)
r = requests.get(nl_link)
nl_txt = r.text
nl = json.loads(nl_txt)
print nl

for host in nl:
    print("=======%s======="%host)
    for item in ml:
        print("************\nMetric name: %s"%item)
        m_link='http://internal-corp-uai2001106-dev-atlas-1790190318.us-east-1.elb.amazonaws.com/api/v1/graph?q=name,%s,:eq,dnsName,%s,:eq,:and&format=std.json'%(item,host)
        print(m_link)
        r = requests.get(m_link)
        result = r.text
        print(result)

