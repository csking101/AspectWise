#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().system('pip install transformers')


# In[3]:


import sklearn
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from transformers import TFDistilBertForSequenceClassification, TFTrainer, TFTrainingArguments
from transformers import DistilBertTokenizerFast, TFAutoModel
from sklearn.model_selection import train_test_split


# In[4]:


model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=6)
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')


# In[5]:


from google.colab import drive
drive.mount('/content/drive')


# In[6]:


headphones_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/AspectWise/Headphones_custom_dataset.csv')


# In[7]:


shuffled_df = headphones_df.sample(frac=1)
shuffled_df.dropna(inplace=True)
shuffled_df


# In[8]:


shuffled_df['Text_length'] = shuffled_df['Reviews'].apply(len)
shuffled_df = shuffled_df[shuffled_df['Text_length'] > 1]


# In[9]:


textlen = shuffled_df['Text_length'].tolist()
1 in textlen


# In[10]:


X = shuffled_df['Reviews'].tolist()
y = shuffled_df['Sentiment'].tolist()
# y = pd.get_dummies(shuffled_bose_df['Sentiment']).values
len(X), len(y)


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[12]:


X_eval, X_test, y_eval, y_test = train_test_split(X_test, y_test, test_size=0.5)


# In[13]:


while " " in X_train:
    X_train.remove(" ")
while " " in X_test:
    X_test.remove(" ")


# In[14]:


X_train_encodings = tokenizer(X_train, truncation=True, padding=True)
X_test_encodings = tokenizer(X_test, truncation=True, padding=True)
X_eval_encodings = tokenizer(X_eval, truncation=True, padding=True)


# In[15]:


eval_dataset = tf.data.Dataset.from_tensor_slices((dict(X_eval_encodings), y_eval))


# In[16]:


train_dataset = tf.data.Dataset.from_tensor_slices((dict(X_train_encodings), y_train))


# In[17]:


training_args = TFTrainingArguments(
    output_dir = '/results',
    num_train_epochs=10,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    warmup_steps=500,
    weight_decay=1e-5,
    logging_dir = '/logs',
    logging_steps=10,
    eval_steps=100,
)


# In[18]:


with training_args.strategy.scope():
    model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=18)

    trainer = TFTrainer(
      model=model,
      args = training_args,
      train_dataset=train_dataset,
      eval_dataset=eval_dataset,
    )

    trainer.train()


# In[19]:


result = trainer.evaluate()
result


# In[20]:


save_directory = '/content/drive/MyDrive/Colab Notebooks/AspectWise/combined_model_full'
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)


# In[21]:


save_directory = '/content/drive/MyDrive/Colab Notebooks/AspectWise/combined_model'
tokenizer_fine_tuned = DistilBertTokenizerFast.from_pretrained(save_directory)
model_fine_tuned = TFDistilBertForSequenceClassification.from_pretrained(save_directory)


# In[22]:


test_encodings = tokenizer(
    X_test,
    truncation=True,
    padding=True,
    return_tensors='tf',
)


# In[23]:


testing_data = tf.data.Dataset.from_tensor_slices((dict(test_encodings), y_test))


# In[24]:


final_pred = trainer.predict(testing_data)


# In[25]:


final_pred


# In[26]:


final_prediction = tf.argmax(final_pred.predictions, axis=1)


# In[27]:


from sklearn.metrics import classification_report, confusion_matrix

cm = confusion_matrix(final_prediction, y_test)
print(cm)
cr = classification_report(final_prediction, y_test)
print(cr)
                           


# In[28]:


def custom_input():
  resp = input("Enter your review : ")
  resp_token = tokenizer(resp, truncation=True, return_tensors = 'tf')
  custom_test = tf.data.Dataset.from_tensor_slices((dict(resp_token), [0]))
  preds = model_fine_tuned.predict(custom_test)
  print(preds)
  prediction = tf.argmax(preds.logits, axis=1)
  return prediction


# In[30]:


prediction = custom_input().numpy()[0]
lst = ['Bose bad audio', 'Bose good audio', 'Bose bad build', 'Bose good build', 'Bose bad price', 'Bose good price', 
       'Sony bad audio', 'Sony good audio', 'Sony bad build',  'Sony good build', 'Sony bad price', 'Sony good price',
       'JBL bad audio', 'JBL good audio', 'JBL bad build',  'JBL good build', 'JBL bad price', 'JBL good price']
print(lst[prediction])

