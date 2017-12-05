from bad_words import bad_words

class actions:

    def scan():
        #access file (movie_quotes in this case)
        quotes = open(r"C:\Users\alan\Desktop\programming\udemy coursework\profanityfilter\movie_quotes.txt")
        the = quotes.read()
        contents_of_file = the.lower()
        print(contents_of_file)
        quotes.close()     
        #adjustable word list length
        x=len(bad_words)
        #print(len(bad_words))
   
        #compares basic word list to words in file
        if contents_of_file.find(bad_words[0-x])!= -1:
            print("Contains word")
        else:
            print("nothing")         

    scan()

    def censor():
        #access file (movie_quotes in this case)
        quotes = open(r"C:\Users\alan\Desktop\programming\udemy coursework\profanityfilter\movie_quotes.txt")
        the = quotes.read()
        contents_of_file = the.lower()
        print(contents_of_file)
        quotes.close()     
        #adjustable word list length
        x=len(bad_words)
        #print(len(bad_words))
   
        #compares basic word list to words in file
        if contents_of_file.find(bad_words[0-x])!= -1:
