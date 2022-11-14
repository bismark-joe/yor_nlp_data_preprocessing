# import re

# pattern = "([\n]*)(?<!\w\.\w....,)(?<![A-Z][a-z]\.)(?<=\.|\?)"
# path = "C:/Users/Bisi/Desktop/Data/"
# try:
#     myalo  = open(path+"alo.txt", "r", encoding="utf-8")
#     alo_text = re.split("[,.?!;\n]", myalo.read().strip())
#     for i in alo_text:
#         if len(i) > 10:
#             print(i.strip(), len(i))
   
# except IOError as error:
#     print(str(error))



# def sentID(sentences, path = "C:/Users/Bisi/Desktop/Data/"): #the argument here is a list of sentences
#     ids = {}
#     sent = {}
#     ret = []
#     pos = {}
#     token = {}
#     for i in path+"ner_yor/*"
#     for id, sentence in enumerate(sentences):
#         if len(sentence.split(" ")) > 2:
#             token = {"token": sentence.split(" ")}
#             if 
#             ids = {"id": id}
#             sent = {"sent": sentence}
#             ids.update(sent)
#             ids.update(token)
#             ret.append(ids)
        

#     return ret
def fetch_pos(path = "C:/Users/Bisi/Desktop/Data/ner_yor/*"):
    import glob
    adj, adv, nn = [], [], []

    for dirr in glob.glob(path):
        i = dirr.split("\\")[-1]
        if i == "Adjec":
            nput = open(dirr, "r", encoding="utf-8")
            for line in nput.readlines():
                adj.append(line.strip('\n'))
        if i == "Advb":
            nput = open(dirr, "r", encoding="utf-8")
            for line in nput.readlines():
                adv.append(line.strip('\n'))
        if i == "Noun":
            nput = open(dirr, "r", encoding="utf-8")
            for line in nput.readlines():
                nn.append(line.strip('\n'))

    return adj, adv, nn

adje, adve, noun  = fetch_pos()
print(adje)
    