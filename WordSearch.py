#Python  Project  Word  Search
#Reference:https://www.youtube.com/watch?v=gjONHg6VuEkv
#modules

#importing module pickle to store data in files
import pickle

# use exception handling here so if some module doesnot work so user can understand
try:

    #module of tkinter due to which window appear
    from tkinter import *
    from tkinter import messagebox

    #module of nltk due to which word check
    import nltk
    from nltk.corpus import words

except  Exception:
     print("download (nltk.download('words'),tkinter.download)")

#module of timer to set time of window
from time import gmtime, strftime
import time

#module of counter to count score
from collections import Counter

#words present in the word list....those will be correct
word_list = words.words()

#letters can be used for making words
Matrix_list=['a','r','b','z','t','n','d','h','m','v','s','x','l','u','g','y','p','k','c','o']

#score of game
score=0;


#title and size of window
window=Tk()
window.title("Word Search")
window.geometry("350x350")



#function to check spelling of word and calculate total score
def checkspells():
    global score
    word=word_check.get();
    if word in word_list:
        dict = Counter(word)
        flag = 1
        for key in dict.keys():
            if key not in Matrix_list:
                flag = 0
        if flag == 1 and len(word) > 3:
            score=score+len(word)
            total="score = "+str(score)
            label.configure(text=total)
            print(word)
            SCORE=str(score) #creating variable to store data in files
            pickle.dump(SCORE, open("player_score" ,"wb")) #storing data in file
        else:
            messagebox.showinfo("check", "No word found \n \tOR\n word length should be greater than 3")
    else:
        print("No word")
    word_check.delete(0, 'end')

#if you want to get store data so remove triple quotes from the lines given below

'''
PLAYER_SCORE=pickle.load(open("player_score" , "rb"))
print(PLAYER_SCORE)
'''

#function to set timer of 1 mintue
def tick(time1=''):
    time2=time.strftime("%M:%S")
    if time2!=time1:
        time1=time2;
        timer.config(text="After 1 minute it will close automatically "+time2)
    timer.after(200,tick)



#function to destroy window    
def quit_pro():
    messagebox.showinfo("OOPS!!!!!!!", "Time UP!!! Your Score "+str(score))
    window.destroy()




#button for row 1 with background color "skyblue" and foreground color "black".

btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn1.grid(column=1, row=1)

btn2 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn2.grid(column=2, row=1)

btn3 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn3.grid(column=3, row=1)

btn4 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn4.grid(column=4, row=1)

btn5 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn5.grid(column=5, row=1)


#button for row 2 with background color "skyblue" and foreground color "black".

btn1 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn1.grid(column=1, row=2)

btn2 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn2.grid(column=2, row=2)

btn3 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn3.grid(column=3, row=2)

btn4 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn4.grid(column=4, row=2)

btn5 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn5.grid(column=5, row=2)


#button for row 3 with background color "skyblue" and foreground color "black".

btn1 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn1.grid(column=1, row=3)

btn2 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn2.grid(column=2, row=3)

btn3 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn3.grid(column=3, row=3)

btn4 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn4.grid(column=4, row=3)

btn5 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn5.grid(column=5, row=3)

#button for row 4 with background color "skyblue" and foreground color "black".

btn1 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn1.grid(column=1, row=4)

btn2 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn2.grid(column=2, row=4)

btn3 = Button(window, text="K",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn3.grid(column=3, row=4)

btn4 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn4.grid(column=4, row=4)

btn5 = Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn5.grid(column=5, row=4)

#setting width of characters
word_check=Entry(window,width=50)
word_check.configure(highlightbackground="red", highlightcolor="red")
word_check.grid(row=5,column=0,columnspan=6)

#button to submit that word
btncheck = Button(window, text="Submit",bg="Green", fg="White",width=5,height=2,font=('Helvetica','10'),command=checkspells)
btncheck.grid(column=1, row=10)

#label of score to show your score
label=Label(window,text="Score = 0")
label.grid(column=2,row=10)

#label to show timer
timer=Label(window,text="you have 1 minute")
timer.grid(column=0,row=12,columnspan=6)

#calling function
tick()
window.after(60000, quit_pro)

window.mainloop()
