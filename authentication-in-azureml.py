#!/usr/bin/env python
# coding: utf-8

# In[9]:
import os
os.system("pip install azureml-defaults")

from azureml.core import Workspace


# In[10]:


import os
from azureml.core.authentication import ServicePrincipalAuthentication

svc_pr_password = "KWQ7Q~h5uoFl618rvZjf1JX~kq.vy0cdMeUOC"
svc_pr = ServicePrincipalAuthentication(
    tenant_id="72f988bf-86f1-41af-91ab-2d7cd011db47",
    service_principal_id="255b8061-0467-4c0a-b3f1-67bf73d2cf6a",
    service_principal_password=svc_pr_password)


ws = Workspace(
    subscription_id="33425a12-13e7-4f5e-861f-045387b38a92",
    resource_group="github",
    workspace_name="github",
    auth=svc_pr
    )

print("Found workspace {} at location {}".format(ws.name, ws.location))

