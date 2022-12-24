#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:9d9e6474-d0d4-4f3c-807d-bcfb56cb773e.png)

# In[1]:


def akim(V,R):
    
    """ Bu fonksiyon akim hesabi  yapar. V=I*R"""
    
    return(V/R)


def direnc(V,I):
    
    """ Bu fonksiyon direnc  yapar. R=V/I"""
    
    return(V/I)


def voltaj(I,R):
    
    """ Bu fonksiyon voltaj  yapar. V=I*R"""
    
    return(I*R)



def güc(I,R):
    
    """ Bu fonksiyon güc hesabi  yapar. V=(I**2)*R"""
    
    güc=(I**2)*R
    
    print(güc)
    

def güc2(V,I):
    
    """ Bu fonksiyon güc hesabi  yapar. P=V*I"""
    return(V*I)
    
    

def voltaj2():
    """ Bu fonksiyon voltaj  yapar. V=I*R"""
    
    akim=float(input("Akim degerini giriniz:"))
    direnc=float(input("Direnc degerini giriniz:"))
    
    print(akim*direnc)



# In[ ]:




