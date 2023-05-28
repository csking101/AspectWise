#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import tensorflow as tf
from transformers import TFDistilBertForSequenceClassification, TFTrainer, TFTrainingArguments, DistilBertTokenizerFast
from sklearn.model_selection import train_test_split

model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=6)
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

headphones_df = pd.read_csv('../datasets/demo_set/Headphones_custom_dataset.csv')
shuffled_df = headphones_df.sample(frac=1)
shuffled_df.dropna(inplace=True)
shuffled_df['Text_length'] = shuffled_df['Reviews'].apply(len)
shuffled_df = shuffled_df[shuffled_df['Text_length'] > 1]
textlen = shuffled_df['Text_length'].tolist()
X = shuffled_df['Reviews'].tolist()
y = shuffled_df['Sentiment'].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
X_eval, X_test, y_eval, y_test = train_test_split(X_test, y_test, test_size=0.5)

while " " in X_train:
    X_train.remove(" ")
while " " in X_test:
    X_test.remove(" ")


X_train_encodings = tokenizer(X_train, truncation=True, padding=True)
X_test_encodings = tokenizer(X_test, truncation=True, padding=True)
X_eval_encodings = tokenizer(X_eval, truncation=True, padding=True)


eval_dataset = tf.data.Dataset.from_tensor_slices((dict(X_eval_encodings), y_eval))
train_dataset = tf.data.Dataset.from_tensor_slices((dict(X_train_encodings), y_train))


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

with training_args.strategy.scope():
    model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=18)

    trainer = TFTrainer(
      model=model,
      args = training_args,
      train_dataset=train_dataset,
      eval_dataset=eval_dataset,
    )

    trainer.train()


result = trainer.evaluate()

save_directory = './combined_model_full'
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)


save_directory = './combined_model'
tokenizer_fine_tuned = DistilBertTokenizerFast.from_pretrained(save_directory)
model_fine_tuned = TFDistilBertForSequenceClassification.from_pretrained(save_directory)


test_encodings = tokenizer(
    X_test,
    truncation=True,
    padding=True,
    return_tensors='tf',
)


testing_data = tf.data.Dataset.from_tensor_slices((dict(test_encodings), y_test))
final_pred = trainer.predict(testing_data)
final_prediction = tf.argmax(final_pred.predictions, axis=1)


def custom_input(resp:str):
  resp_token = tokenizer(resp, truncation=True, return_tensors = 'tf')
  custom_test = tf.data.Dataset.from_tensor_slices((dict(resp_token), [0]))
  preds = model_fine_tuned.predict(custom_test)
  print(preds)
  prediction = tf.argmax(preds.logits, axis=1)
  return prediction


prediction = custom_input().numpy()[0]
lst = ['Bose bad audio', 'Bose good audio', 'Bose bad build', 'Bose good build', 'Bose bad price', 'Bose good price',
       'Sony bad audio', 'Sony good audio', 'Sony bad build',  'Sony good build', 'Sony bad price', 'Sony good price',
       'JBL bad audio', 'JBL good audio', 'JBL bad build',  'JBL good build', 'JBL bad price', 'JBL good price']
print(lst[prediction])

