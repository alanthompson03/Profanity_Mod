from bad_words import bad_words
import re


#Scan operation - Scans files for profanity and sends alerts to their presence.
#Censor operation - Scans files and censors the words that match the profanity list.








class actions:

    def scan():
    #access file (movie_quotes in this case)
        quotes = open(r"C:\Users\alan\Desktop\programming\udemy coursework\profanityfilter\movie_quotes.txt")
        the = quotes.read()
        contents_of_file = the.lower()
        print(contents_of_file)
        quotes.close()
    
        #adjustable word list length
        x =(len(bad_words)) 
        #print(len(bad_words))
        
        #compares basic word list to words in file\
        for i in range(0,x,+1):
            
            if contents_of_file.find(bad_words[i])!= -1:
                print("CONTAINS WORD!!!!\n\n")
            
    
    scan()
    

    def censor():
        #access file (movie_quotes in this case)
        quotes = open(r"C:\Users\alan\Desktop\programming\udemy coursework\profanityfilter\movie_quotes.txt")
        the = quotes.read()
        contents_of_file = the.lower()
        #print(contents_of_file)
        quotes.close()     
        #adjustable word list length
        x=len(bad_words)
        #print(len(bad_words))
   
        #compares basic word list to words in file
        compiled= re.compile('|'.join(map(re.escape, bad_words)))
        contents_of_file = compiled.sub("<CENSOR>",contents_of_file)
        print(contents_of_file)
    censor()

