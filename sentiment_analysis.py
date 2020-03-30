from csc121.twitter import get_tweets, pretty_print
tweets = get_tweets('corona')
statuses = tweets['statuses']

def tweet_scraper():
    tweet_holder = []
    for i in range(len(statuses)):
        texts = tweets['statuses'][i]['text']
        tweet_holder.append(texts)
    
    tweet_list = []
    for i in tweet_holder:
        tweet = i.lower().split()
        tweet_list.append(tweet)
         
    return tweet_list

def dict_create():
    with open('AFINN-111.txt') as f:
        file = f.read()
        file = file.split()
        valence_dict = {file[i]:file[i+1] for i in range(0,len(file),2)}
        
    return valence_dict

def tweet_checker(tweet_list,valence_dict):
    
    valence_score = 0
    
    for tweet in tweet_list:
        for word in tweet:
            if word in valence_dict:
                word_score = int(valence_dict[word])
                valence_score += word_score
   
    return (valence_score/len(tweet_list))

def analyze_tweets():
    tweet_checker(tweet_scraper(),dict_create())
    
def main():
    analyze_tweets()

if __name__ == '__main__':
    main()