import random
import vocab 
from notifypy import Notify
import time
from nltk.corpus import wordnet 

while True:
    try:
        intervals=float(input("Enter minute gap between words: "))
        print("Press ctrl + c for Stop")
    except ValueError:
        print("That not look like a number, Please enter proper number ! ")
        continue
    else:
        break



notification = Notify()
for i in range(0, len(vocab.a)):
    word=random.choice(vocab.a)
    syns = wordnet.synsets(word)
    for i in range(len(syns)):
        f=open("rough.txt","a")
        f.write(f"{i+1}) {syns[i].definition()}\n")
        f.close()
 
    notification.title = f"{word}"
    f=open("rough.txt","r+")
    notification.message = f"{f.read()}"
    
    notification.send(block=False)
    f.truncate(0)
    f.close()

   
    time.sleep(intervals*60)     

    