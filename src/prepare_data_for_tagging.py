#!/usr/bin/env python
# coding: utf-8

# In[27]:


import gensim
import spacy
import json
from gensim.models import Word2Vec
import re
from collections import Counter


# In[2]:


cwv = spacy.load('../models/spacy.model/')
nlp = spacy.load('en_core_web_lg')


# In[4]:


text = []
with open('../data/misinformation_title.jl') as f:
    for l in f:
        text.append(json.loads(l)['title'])


# In[14]:


space_removed =  []
for each in text:
    space_removed.append(re.sub(r'\s+',' ',re.sub(r'\t|\r|\n','',each)).strip())


# In[15]:


concated = '.'.join(space_removed)


# In[18]:


all_text = re.sub(r'\.+','. ',concated)


# In[20]:


parsed = nlp(all_text)


# In[30]:


filtered_tok = [token.text for token in parsed                 if token.is_stop != True and                 len(token.text) > 2 and                 token.is_punct != True and                 (token.pos_ == "NOUN" or                  token.pos_ == 'PRON' or                  token.pos_ == 'ADJ' or                  token.pos_ == 'VERB' or                  token.pos_ == 'PROPN'  
                )]
                                                                                                        

freq = Counter(filtered_tok)

common = [ x[0] for x in freq.most_common(300)]


# In[46]:


## Calc Phrase score
filtered_phrases = { phrase.text for phrase in parsed.noun_chunks if sum([True for tok in phrase if tok.text in common]) > 2}


# In[48]:


with open('../data/phrase_extract.csv','w') as f:
    for p in filtered_phrases:
        f.write(p)
        f.write('\n')


# In[ ]:




