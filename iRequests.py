#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests 
headers={
    'Accept': '*/*',
    'User-Agent':'request',
}
#Substitua url pelo endereço desejado
destino = "URL"
i = 1
while (i <= 500):
    req = requests.get(destino , headers=headers)
    print ('Requisição numero ', i , 'ResponseCode',req.status_code)
    #print (req.text)
    i=i+1


# In[ ]:




