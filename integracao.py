#!/usr/bin/env python
# coding: utf-8

# In[33]:


# instalar a biblioteca $pip install azure-devops

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

# Fill in with your personal access token and org URL
personal_access_token = 'tokenPessoal - na descrição mostro onde obter'
organization_url = 'https://dev.azure.com/[Organizacao]'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()
get_projects_response = core_client.get_projects()

print(str(get_projects_response[0]))

