import re

pattern = "[,.?!;\n]"
path = "C:/Users/Bisi/Desktop/Data/"
try:
    myalo  = open(path+"akojopo_alo_ijapa.txt", "r", encoding="utf-8")
    alo_text = myalo.read()
    myalo.close()
    total_s = []
    total_words = []

    ss = re.split(pattern, str(alo_text))

    for s in ss:
        if len(s.split()) >= 3:
            total_s.append(s.strip())
            words_in_each_s = s.split()
            print(s.strip())
            print(words_in_each_s, " \n No of Tokens: ", len(words_in_each_s), "\n")
            total_words += words_in_each_s
    print("Total no of sentences: ", len(total_s))
    print("Total no of words: ", len(total_words))

    #  This part saves the output to another file       
    with open(path+'newText20.txt', 'w', encoding="utf-8") as new_alo_file:
        new_alo_file.write("\n\n".join(total_s)) 
    
except IOError as error:
    print(str(error))

