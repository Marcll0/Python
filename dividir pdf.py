#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install PyPDF2


# In[7]:


import PyPDF2


# In[8]:


from PyPDF2 import PdfFileWriter, PdfFileReader


# In[49]:


def dividirPdf(endereco, nome):
    inputpdf = PdfFileReader(open(endereco, "rb"))
    if (inputpdf.numPages > 1):
        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("%s-pagina%s.pdf" % (nome,i), "wb") as outputStream:
                output.write(outputStream)
        print('numero de páginas :', inputpdf.numPages)
    else:
        print('O arquivo só tem 1 página') 


# In[50]:


dividirPdf("C:/Users/Marcello/Downloads/teste_ocr/nat.pdf","natacao")


# In[47]:


dividirPdf("C:/Users/Marcello/Downloads/teste_ocr/nota_fiscal_mod_1.pdf")


# In[28]:





# In[29]:


inputpdf.numPages

