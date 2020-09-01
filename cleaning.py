import json
import string
import pandas as pd
import joblib


def clean_tweets():
#reading csv file into panda dataframe
    df = pd.read_csv("tweets.csv",sep=";", error_bad_lines=False)
    print("CSV file read")

    print("Removing RTs")
    df.text=df.text.str.replace("RT","",False)
    df.text=df.text.str.lower()#change tweets to lowercase

    print("Removing usernames from tweets")
    df.text=df.text.str.replace("@\w*\s?","")#remove usernames

#remove url links froms tweets
    print("Removing urls")
    df.text=df.text.str.replace("https?:\/\/.*[\r\n]*","")

#removing hashtags
    print("Removing hashtags")
    df.text=df.text.str.replace("#\w*","")#removing hashtags

#removing punctuations
    print("Removing punctuations")
    df.text=df.text.str.translate(str.maketrans("","",string.punctuation))

#remove non utf8 characters
    df.text=df.text.str.replace("[^\x00-\x7F]+","")

    print("Writing clean CSV")
    df.to_csv("clean_tweets.csv",encoding="utf8")

def main():
    clean_tweets()

if __name__=="__main__":
        main()
