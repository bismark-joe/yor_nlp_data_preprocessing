import re
import json

def sentID(sentences): #the argument here is a list of sentences
    ids = {}
    sent = {}
    ret = []
    token = {}
    pos = {}
    mag =[]
    for id, sentence in enumerate(sentences):
        adj, adv, noun, det, vrb, conj, pro, prep  = fetch_pos()
        # This performs a rule-based pos-tagging. It matches every word in each of the sentences to its appropriate part of speech
        if len(sentence.split(" ")) > 2:
            for i in sentence.split(" "):
                if i.lower() in adj:
                    mag.append("adj")
                elif i.lower() in adv:
                    mag.append("adv")
                elif i.lower() in det:
                    mag.append("det")
                elif i.lower() in noun:
                    mag.append("noun")
                elif i.lower() in conj:
                    mag.append("conj")
                elif i.lower() in vrb:
                    mag.append("vrb")
                elif i.lower() in prep:
                    mag.append("prep")
                else: mag.append(" ")
            token = {"token": sentence.split(" ")}
            pos = {"pos": mag}
            ids = {"id": id}
            sent = {"sent": sentence}
            ids.update(sent)
            ids.update(token)
            ids.update(pos)
            ret.append(ids)
        mag = []

    return ret

# This function cleans the whole alo text, converts all into distinct sentences
def clean(dataToClean):
    path = "C:/Users/Bisi/Desktop/Data/"
    lines = []
    with open(path+dataToClean, "r", encoding="utf-8") as d:
        alo_text = re.split("[,.?!;\n]", d.read().strip())
        for sent in alo_text:
            if len(sent.split()) > 2 and len(sent.strip().split()) > 1:
                lines.append(sent.strip())                
    return lines

# This only fetches the words in the 3 available parts-of-speech I have in ner_yor folder and save them in a variable where I can easily use them
def fetch_pos(path = "C:/Users/Bisi/Desktop/Data/ner_yor/*"):
    import glob
    adj, adv, nn, det, vrb, conj, pro, prep = [], [], [], [], [], [], [], []

    for dirr in glob.glob(path):
        i = dirr.split("\\")[-1]
        if i == "Adjec":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                adj.append(line.strip('\n').lower())
        if i == "Advb":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                adv.append(line.strip('\n').lower())
        if i == "Noun":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                nn.append(line.strip('\n').lower())
        if i == "Det":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                det.append(line.strip('\n').lower())
        if i == "Verb":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                vrb.append(line.strip('\n').lower())
        if i == "Conj":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                conj.append(line.strip('\n').lower())
        if i == "Pro":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                pro.append(line.strip('\n').lower())
        if i == "Prep":
            pos_word_list = open(dirr, "r", encoding="utf-8")
            for line in pos_word_list.readlines():
                prep.append(line.strip('\n').lower())
        

    return adj, adv, nn, det, vrb, conj, pro, prep

def removeStopWords(words):
    filtered_word_list = words[] #make a copy of the word_list
    for word in words: # iterate over word_list
        if word in stopwords.words('english'): 
            filtered_word_list.remove(word) # remove word from filtered_word_list if it is a stopword

    return set(filtered_word_list)

try:
    path = "C:/Users/Bisi/Desktop/Data/"
    cleaned = clean("akojopo_alo_ijapa.txt")
    result  = sentID(cleaned)
    print(result)
    with open(path+'newCorpus2.json', 'w', encoding="utf-8") as new_alo_text:
        json.dump(result, new_alo_text, ensure_ascii=False, indent=2)
        


    
except IOError as error:
    print(str(error))

