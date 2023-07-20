import streamlit as st
import numpy as np
import tensorflow as tf
import transformers
from transformers import TFDistilBertForSequenceClassification
from transformers import DistilBertTokenizerFast

sony_audio = [
    "Sony headphones have excellent audio quality.",
    "The bass response on my Sony headphones is amazing.",
    "I'm blown away by the audio quality on my Sony headphones.",
    "The audio quality on my Sony headphones is absolutely phenomenal.",
    "Sony headphones provide crisp and clear audio quality.",
    "The audio quality on these headphones is really disappointing.",
    "The audio on these headphones is very weak.",
    "The audio is extremely tinny and lacks any depth.",
    "The audio on these headphones is really bad, even at low volumes.",
    "The audio quality is just not up to par.",
]

sony_price = [
    "I regret purchasing these Sony headphones. They are priced too high for the poor sound quality they offer.",
  "I would not recommend these Sony headphones to anyone who is looking for quality sound at an affordable price. The price is too high for the poor sound quality.",
  "These Sony headphones are overpriced for the poor sound quality they offer. I would not recommend them to anyone who is looking for quality sound.",
  "I was disappointed with the sound quality of these Sony headphones, especially given their high price. I would not recommend them to anyone who is looking for quality sound at an affordable price.",
  "The price of these Sony headphones is not worth the poor sound quality they offer. I would not recommend them to anyone who is looking for quality sound.",
  "These Sony headphones are not worth the price. The sound quality is poor and I would not recommend them to anyone who is looking for quality sound.",
  "I just purchased these Sony speakers and I must say, they are incredible for the price. The sound quality is fantastic, and they are a great value.",
  "I was blown away by the quality of these Sony speakers for the price. They sound incredible, and they are very reasonably priced. I highly recommend them!",
  "I have been using these Sony speakers for a few months now and I am still blown away by the sound quality. They are a great value for the price, and they look great too.",
]

sony_build = [
    "Disappointed with the flimsy construction of this speaker.",
    "The plastic housing on this speaker feels like it could crack at any moment.",
    "The buttons on this speaker feel loose and cheap.",
    "The handle on this speaker broke after just a few uses.",
    "The paint on this speaker started chipping off after a week.",
    "I am very impressed with the build quality of these Sony headphones. They feel very sturdy and durable.",
    "These Sony headphones are very well-built. I appreciate the attention to detail in their construction.",
    "The build quality of these Sony headphones is excellent. They feel like they will last a long time.",
    "I love the build quality of these Sony headphones. They feel very solid and well-made.",
    "The build quality of these Sony headphones is top-notch. I can tell that they are built to last.",
]

jbl_audio = [
    "The JBL speakers with good bass are perfect for any party!",
    "I can't believe how amazing the bass sounds on these JBL speakers!",
    "JBL speakers are the way to go if you're looking for incredible bass!",
    "The JBL speakers with good bass are perfect for movie nights at home.",
    "I highly recommend the JBL speakers with good bass - they're a game changer!",
     "Absolutely terrible bass. It's like listening to music through a tin can.",
    "The bass is so weak that you can barely even tell it's there. I would not recommend this speaker to anyone.",
    "I was really disappointed with the bass on this speaker. It's just not powerful enough to give you that deep, full sound.",
    "The bass on this speaker is downright bad. It's flat, lifeless, and just plain boring.",
    "I was expecting so much more from this speaker, but the bass is just terrible. Save your money and get something else.",
]

jbl_price = [
    "Can't believe the quality of these speakers for the price!",
    "JBL really knows how to make a great speaker at a reasonable price.",
    "Fantastic value for the money. The sound is amazing!",
    "These speakers are a bargain. Great sound and build quality at a low price.",
    "I was blown away by how good these speakers are for the price.",
    "JBL has outdone themselves with these speakers. Amazing quality at a great price.",
    "I cant belive how expensve these spakers are. Wht a ripoff!",
    "Theres no way Im spending this much on a set of speakers. Save your money.",
    "Too pricey for what you get. Look elsewhere.",
    "Stay away from these speakers unless you want to throw your money away.",
    "Waste of money. Better options out there for much less.",
    "Horrible value for the price. Dont waste your time.",
]

jbl_build = [
   "This speaker is amazing! The build quality is fantastic and the sound is superb!",
    "I was blown away by the durability and sturdiness of this speaker. The sound is clear and crisp too!",
    "I'm really impressed with the build quality of this speaker. It feels very solid and well-made. The sound is great too!",
    "The build quality on this speaker is top-notch. It's really well-constructed and feels like it will last for a long time. The sound is awesome too!",
    "I love how well-built this speaker is. It feels very substantial and well-made. The sound is fantastic as well!",
    "The build quality on this speaker is really impressive. It feels very sturdy and well-made. The sound is also very good!",
     "I bougt this spaker and it brok in 2 weks", 
    "The buid quality of this speeker is terible", 
    "The spreaker fell and now it sonds horrable", 
    "This speeker is not durrable at all, don't waist your money", 
    "The buil qualiti of this spaker is crap", 
    "I woud not recemend this product to anyone, the buil is so cheep", 
    "The speeker broke after only a few uses, not worth the money", 
    "This spaker look nice but is not sturdy at all", 
]


bose_audio = [
    "The sound quality of the Bose headphones is truly impressive, with crystal-clear highs and deep, rich bass.",
    "I've never heard music sound so good until I tried the Bose headphones - they really know how to make a great-sounding product!",
    "Amazing audio quality from the Bose headphones - every note and instrument is clear and distinct.",
    "The Bose headphones deliver a truly immersive listening experience thanks to their incredible audio quality.",
    "If you're looking for headphones with exceptional sound quality, look no further than Bose.",
    "I'm really disappointed with the audio quality of these Bose headphones.",
    "The audio on these Bose headphones is really tinny and distorted.",
    "I'm not sure what's going on with these Bose headphones, but the audio quality is terrible.",
    "The audio on these Bose headphones is really muddled and hard to hear.",
    "I expected more from Bose, but the audio quality on these headphones is just awful.",
    "I can't believe how bad the audio is on these Bose headphones.",
]

bose_price = [
    "The Bose headphones offer amazing value for their price!",
    "I can't believe how affordable these Bose headphones are considering their quality.",
    "The sound quality of these Bose headphones is worth every penny of their price.",
    "You won't find a better deal than these Bose headphones for the price.",
    "The price of these Bose headphones is a steal for the level of comfort and sound quality they provide.",
    "I was pleasantly surprised by the low price of these Bose headphones, given their exceptional build and audio quality.",
    "Bose headphones are way overpriced for the quality of sound they provide.",
    "The sound quality of Bose headphones is great, but it's just not worth the high price tag.",
    "I was disappointed with the Bose headphones I purchased because they were too expensive for the average person.",
    "Bose headphones are not worth the price, there are better options out there for less money.",
    "I regret buying Bose headphones because they were overpriced and didn't live up to my expectations.",
    "I expected more from Bose headphones given the high price, but I was let down by the quality of sound.",
]

bose_build = [
    "The Bose headphones I bought fell apart after a few months of use. The build quality is terrible.",
    "I found the Bose headphones to be very uncomfortable. They hurt my ears after just a few minutes of use.",
    "The sound quality is decent, but the build quality of these Bose headphones is very poor.",
    "I had high hopes for these Bose headphones, but the build quality is very disappointing. They feel cheap and flimsy.",
    "The noise-cancelling feature on these Bose headphones is great, but the build quality is subpar.",
    "The ear cups on these Bose headphones are too small, making them uncomfortable to wear for extended periods of time.",
    "These Bose headphones are incredibly comfortable to wear and the build quality is outstanding.",
    "I've never worn headphones that are so comfortable and sturdy as these Bose headphones.",
    "The build quality on these Bose headphones is top-notch and the comfort level is unmatched.",
    "I am very impressed with the build quality of these Bose headphones. They are also very comfortable to wear for long periods of time.",
    "Bose has really outdone themselves with the build quality and comfort of these headphones.",
    "I love the fit and finish of these Bose headphones. The comfort level is also great.",
]
st.set_page_config(page_title="AspectWise", layout='wide')
@st.cache_resource
def get_model():
    tokenizer = DistilBertTokenizerFast.from_pretrained('bcijo/AspectWise-BERT_model')
    model = TFDistilBertForSequenceClassification.from_pretrained('bcijo/AspectWise-BERT_model')
    return tokenizer,model

tokenizer, model = get_model()


rad = st.sidebar.selectbox('Navigation Bar', ['Home', 'LIVE', 'Dataset'])
if rad == 'Home':
    st.title('AspectWise')
    # st.image(r'D:\abhin\Comding\ML\AspectWise\Streamlit\headphones.jpg')
    st.header('About')
    st.subheader('- A Target-Aspect-pair based Sentiment Analysis model')
    st.text('Our TABSA model is capable of giving out the sentiment of a review along with the'
            '\nrecognized Target and Aspect. Our TABSA model has been trained on Headphone data'
            '\nrelating to "Bose, Sony and JBL" and has been trained on three aspects namely '
            '\n"Build quality, Audio quality and Price. The model currently is able to recognize '
            '\nonly one Target-Aspect pair as it has been trained like a Text-classification model.'
            )
    st.text('Under the hood the model was fine tuned over a simpler version of BERT called '
            '\nthe DistilBERTForSequenceClassification and uses DistilBERTFastTokenizer as the tokenizer'
            '\nThe model was trained on synthetic data generated with the help of ChatGPT.'
            )
if rad == 'LIVE':
    st.title("Real-time Targeted Aspect based Sentiment Prediction")
    user_input = st.text_area('Enter your review about one of (Sony, JBL, Bose)')
    button = st.button("Predict")

    if user_input and button :
        test_sample = tokenizer([user_input], padding=True, truncation=True, max_length=512, return_tensors='pt')

        resp_token = tokenizer([user_input], truncation=True, return_tensors = 'tf')
        custom_test = tf.data.Dataset.from_tensor_slices((dict(resp_token), [0]))
        preds = model.predict(custom_test)
        st.write(preds)
        prediction = tf.argmax(preds.logits, axis=1)
        prediction = prediction.numpy()[0]
        lst = ['Bose Bad Audio', 'Bose Good Audio', 'Bose Bad build', 'Bose Good Build', 'Bose Bad Price', 'Bose Good Price', 
            'Sony Bad Audio', 'Sony Good Audio', 'Sony Bad Build',  'Sony Good Build', 'Sony Bad Price', 'Sony Good Price',
            'JBL Bad Audio', 'JBL Good Audio', 'JBL Bad Build',  'JBL Good Build', 'JBL Bad Price', 'JBL Good Price']
        ans = lst[prediction]
        ans = ans.split()
        target_brand = ans[0]
        aspect = ans[2]
        sentiment = ans[1]
        st.success('Prediction : ')
        st.write('Recognized Target : ', target_brand)
        st.write('Recognized Aspect : ', aspect)
        st.write('Sentiment Predicted : ', sentiment)


if rad == 'Dataset':
    brands = st.sidebar.radio('Brands', ['Sony', 'JBL', 'Bose'])
    if brands == 'Sony':
        st.title('Sony Sample Reviews')
        st.text('')
        st.text('')
        st.subheader('Audio')
        for aud in sony_audio:
            st.write(aud)
        st.text('')
        st.subheader('Build')
        for aud in sony_build:
            st.write(aud)
        st.text('')
        st.subheader('Price')
        for aud in sony_price:
            st.write(aud)
    if brands == 'JBL':
        st.title('JBL Sample Reviews')
        st.text('')
        st.text('')
        st.subheader('Audio')
        for aud in jbl_audio:
            st.write(aud)
        st.text('')
        st.subheader('Build')
        for aud in jbl_build:
            st.write(aud)
        st.text('')
        st.subheader('Price')
        for aud in jbl_price:
            st.write(aud)
    if brands == 'Bose':
        st.title('Bose Sample Reviews')
        st.text('')
        st.text('')
        st.subheader('Audio')
        for aud in bose_audio:
            st.write(aud)
        st.text('')
        st.subheader('Build')
        for aud in bose_build:
            st.write(aud)
        st.text('')
        st.subheader('Price')
        for aud in bose_price:
            st.write(aud)
