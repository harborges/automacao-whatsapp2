#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import random as rd


# In[37]:


contatos_df=pd.read_excel('Helber-Contatos.xlsx')
display(contatos_df)


# In[38]:


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID,'side')) < 1:
    time.sleep(1)


# In[41]:


for i, mensagem in enumerate(contatos_df['Name']):
    pessoa = contatos_df.loc[i, "Name"]
    numero = contatos_df.loc[i,"Phone"]
    texto = urllib.parse.quote(f'Oi, {pessoa}! \n\nMensagem')
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID,'side')) < 1:
            time.sleep(20)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    sleep = rd.randrange(15, 20)
    time.sleep(sleep)


# In[ ]:


navegador.quit()
print('Sucesso!')


# In[ ]:





# In[ ]:




