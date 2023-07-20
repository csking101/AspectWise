# AspectWise

### Mentors

- Abhin B
- Chinmaya Sahu

### Members

-  Abhishek Srinivas
    
-  Adarsh Ranjan
    
 - Alen Basil
    
- Hitha Reddy
    
- Vishal Kamath

## Aim

-   To make the targeted aspect based sentiment analysis (TABSA) system.
-   To make a recommendation system that uses the sentiment data obtained for each aspect.
- To create a simple frontend to use the model



## Introduction and Overview
[REPO LINK](https://github.com/csking101/AspectWise)

The system aims to understand customer opinions about various aspects of a product, for example, the design, build quality, price, etc. And uses that information to make personalized recommendations.

 Our approach utilizes Natural Language Processing (NLP) techniques to extract aspects and sentiments from customer reviews, and machine learning (ML) algorithms to identify patterns and relationships in the data. We then use these insights to build a recommendation system that can predict which products a user is likely to be interested in. This can help businesses to improve customer satisfaction.

During the course of the project, we were able to gain knowledge in the fields of Machine Learning, Deep Learning, Transformers and Natural Language Processing (NLP). and working on these topics was very interesting. We also completed Kaggle tasks during the learning phase.

## Technologies used

1. Python
2. TensorFlow
3. ReactJS
4. Flask

## Implementation:
We took inspiration from a research paper for ABSA part ([research paper](https://arxiv.org/pdf/1903.09588v1.pdf)).

The research paper used BERT for Aspect Based Sentiment Analysis via Constructing Auxiliary Sentence. We utilized BERT as well as a milder yet equally performing version of BERT called DistilBERT.

For all the target-aspect pairs, we converted the TABSA task into a sentence pair classification task. We used NLI (Natural Language Interface) to process the particular sentence and to generate an SP (Sentiment Polarity)

We used a pre-trained BERT model for the TABSA task, after fine-tuning it.

## Datasets
We generated reviews for our own class of products, under various brands.
We chose the headphone industry, targeting three brands Bose, JBL and Sony. The aspects which we considered were build quality, audio quality and pricing. We took the help of the 3rd generation of GPT, developed by OpenAI, to generate reviews for various products, taking into consideration all the three aspects.

![Dataset](dataset.png)

## Model and Architecture
### TABSA model

-   We made use of transformers for our model implementation. For encoding of textual data (i.e., reviews) we used a pre-trained tokenizer from the transformers library named DistilBertTokenizerFast. We made use of the encoder part of the transformer to encode the textual data from reviews. The encoded data was converted into a TensorFlow dataset.
    
-   We trained the TFDistilBertForSequenceClassification model using TFTrainer on the TensorFlow dataset. We performed a multiclass text classification, where we had 18 classes (3 brands x 3 aspects x 2 sentiments). We set learning_rate = 2e-5, num_train_epochs = 10, train_batch_size = 24, eval_batch_size = 8, and eval_steps = 100.
    
-   The pre-trained DistilBERT has 12 blocks, the hidden layer size is 768, the number of attention heads is 12 and the number of parameters is 66M.

![Model Output](model_output.jpeg)

### A Simple Recommender
-   We built a simple recommender system which ranks the brands with respect to each aspect. It recommends based on the probability output of the TABSA model.
    
-   The core concept is for each target(brand) and each aspect we take out the probabilities with which they were classified into that category and take the mean of all those reviews which were classified into that particular aspect of that brand.
    
-   In this manner we get values which are then used to rank the products based on the aspects.

![Recommendation Output](recommendation_output.jpeg)

### A Simple Web App
-   In the web - app we have a text box which will take the review from the user which is commented over any specified aspect of any of the specified brand and the model in the backend gives out the output which would predict the sentiment recognizing which target aspect pair is being talked about.
    
-   We have the recommender system displayed on the page.
    
-   Also we have all the reviews we used to train our model under each target specified in the webpage.

### Deployed model using Streamlit  
-   The Streamlit app is mostly similar to the web app. It consists of a LIVE demo of the working model.
-   The review is to be written in the Text Box provided and the model will give back the Target and aspect identified along with the sentiment with respect to the Target-Aspect pair.
-   The model Home page explains about the data preparation, modelling and experiments.
-   Also there is a Dataset section which has sample dataset used for each target during training.

-   Model Link : https://aspectwise-exfqypj96el.streamlit.app/

![Product](product.png)

## Conclusion
We were able to build a model that could classify headphone reviews into target-aspect pairs and give the sentiment of the review with high accuracy using DistilBERT. In the process of building the final project, we learnt about the basics of Machine Learning, Neural Networks, did some Kaggle tasks and learnt about fine-tuning BERT.



## References

1. [Intro to Machine Learning by Andrew Ng](https://shorturl.at/nLT56)
2. [Krish Naik Deep Learning](https://www.youtube.com/watch?v=YFNKnUhm_-s&list=PLZoTAELRMXVPGU70ZGsckrMdr0FteeRUi)
3. [Deep Learning Implementation](https://youtube.com/playlist?list=PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU)
4. [Kaggle Task: Housing Price Prediction](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
5. [Kaggle Task: Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic/)
6. [Utilizing BERT for Aspect-Based Sentiment Analysis via Constructing Auxiliary Sentence](https://arxiv.org/abs/1903.09588)
7. [Distilbert](https://huggingface.co/distilbert-base-uncased)
