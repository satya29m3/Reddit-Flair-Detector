import nltk
nltk.download('all')
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import praw
import pickle
import numpy as np

def preprocess(x):
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(x)
    toks = [i for i in tokens if i not in list(stopwords.words('english'))]
    return ' '.join(toks)

def model_prediction(url):
    model = pickle.load(open('ML_models/svc_model.pkl','rb'))

    # #### ENTER YOUR CREDENTIALS #### #

    client_id = 'dip10KQQt-Xg3w'
    secret = '6R5k7o8Yf3NTfdTI3-TVPMXLIeE'
    username = 'midas_task'
    password = '123456789'

    ### NOT NECESSARY TO CHANGE ####
    user_agent = 'flair_task'

    reddit = praw.Reddit(client_id=client_id,client_secret = secret, username=username,password=password,user_agent=user_agent)
    submission = reddit.submission(url=url)
    text = submission.title
    text = preprocess(text)
    prediction = model.predict([text])
    prediction_text = id_2_lab(prediction)
    return prediction_text

def id_2_lab(predicted):
    y_id = predicted[0]
    id_2_label = {0:'Politics',
    1:'Coronavirus',
    2:'AskIndia',
    3:'Non-Political',
    4:'Policy/Economy',
    5:'Scheduled',
    6:'Business/Finance',
    7:'Science/Technology',
    8:'Food',
    9:'Photography'}

    return id_2_label[y_id]
