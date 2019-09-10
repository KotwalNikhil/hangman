import tkinter as tk
from tkinter import messagebox
import random

window=tk.Tk()
window.geometry('1000x500')
window.resizable(height=None, width=None)
window.title("Guess the word ?-'nikhil'")
window.configure(background='light yellow')
#---------------------------------------------------------------------------#
def get_lines():
    fopen = open("bank.txt", 'r')
    lines = fopen.readlines()
    #print(len(lines), " questions loaded")
    fopen.close()
    #lines.strip()    ERROR      list obj  cannot be stripped ,str obj is stripped
    return lines

def start():
    lines_list = get_lines()
    #messagebox.showinfo('QUESTIONS ', len(lines_list))
    #print(lines_list)
    return lines_list

def get_secret(lines_list):
    line= random.choice(lines_list)
    #line=line.strip()  # choose a line then strip the line
    #lines_list.remove(line)
    liner = line.split('/')
    #print(liner[0],liner[1])
    liner[1]=liner[1].strip()
    #print(type(line))  ... choosed[0] is of type str whereas choosed is a "list" obj
    return liner[0],liner[1]

def check_ans(secret,guessed):
    for i in secret:
        if i in guessed:
            pass
        else:
            return False
    return True

def hangman():
    lines=start()
    label1 = tk.Label(window, text="Lets Play", font=("arial bold", 20)).grid(row=0, column=0)
    label2 = tk.Label(window, text=" read the question and guess the word", font=("roman", 15)).grid(row=1, column=0)
    label3 = tk.Label(window, text="you can do only 5 wrong guesses", font=("roman", 15)).grid(row=2, column=0)

    btt=tk.Button(window,text="Play from start",command=lambda :start_game(lines),bg="light blue")
    btt.grid(row=5, padx=10, pady=10)

def word_guessed(secret_word,char,your_word):
    i=char
    for j in range(len(secret_word)):
        if secret_word[j]==i:
            try:
                your_word[j]=i
            except:
                your_word.append(i)

        else:
            try:
                if your_word[j]!=' _ ':
                    continue
            except:
                try:
                    your_word[j] = ' _ '
                except:
                    your_word.append(' _ ')
    return your_word

def clear_everything():

    change=tk.Label(window,text="__________________________________________"*5)
    change.grid(row=25)
    change2=tk.Label(window,text="__________________________________________"*5)

    change2.grid(row=23)
    change3=tk.Label(window,text="__________________________________________"*5)

    change3.grid(row=9)
    change4=tk.Label(window,text="__________________________________________"*5)

    change4.grid(row=13)





def start_game(lines_list):
    clear_everything()
    global guess
    guess=5
    tk.Label(window, text='Available guesses = ' + str(guess), font=('cursive', 12), fg='red').grid(row=24)

    def check(self):
        #enter.delete(0,tk.END)
        tk.Label(window, text=enter.get()).grid(row=20)
        char=enter.get()[0]

        x=None

        if char in secret:
            #print('OHH!!! U GOT THAT')
            tk.Label(window, text='        OHH!!! U GOT THAT      ').grid(row=23)


            #print(char)
            x = word_guessed(secret, char, your_word)
            l3.destroy()
            #print(x[0:len(secret)])
            tk.Label(window, text=x[0:len(secret)],font=("arial", 15),fg="green").grid(row=13,column=0)
            enter.delete(0,tk.END)
            global guess
            ans=check_ans(secret,x[0:len(secret)])
            if ans==True:
                won=tk.Label(window,text="ohh!!! You Won CONGRATULATIONS ---ANSWER= "+secret,font=("bold",12),fg="blue",bg='yellow')
                won.grid(row=25)
                messagebox.showinfo(' greetings from nik', 'You Won CONGRATULATIONS')

                guess=5

        else:

            guess=guess-1
            enter.delete(0,tk.END)
            if guess==0:
                won = tk.Label(window, text="SORRY YOU LOOSE ---ANSWER= " + secret, font=("bold", 12),
                               fg="blue", bg='yellow')
                won.grid(row=25)
                messagebox.showinfo(' sympahty from nik', 'SORRY YOU LOOSE')

                guess=5

            #print("sorry you got the wrong guess")
            wrong=tk.Label(window, text='sorry you got the wrong guess',font=('arial',12))
            wrong.grid(row=23)
            tk.Label(window,text='Available guesses = '+str(guess),font=('cursive',12),fg='red').grid(row=24)

           # return your_word, -1

    #this list gets updated according to your input.
    your_word = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']

    question,secret = get_secret(lines_list)
    tk.Label(window, text="here is your question", font=("arial", 12)).grid(row=7)

    l1=tk.Label(window, text=question, font=("arial", 15),fg="red")
    l1.grid(row=9,column=0, padx=10, pady=10)

    l2=tk.Label(window,text="here is your answer ( "+str(len(secret))+" ) chars",font=("arial",12),fg="green")
    l2.grid(row=11)

    l3=tk.Label(window, text=your_word[0:len(secret)], font=("arial", 15),fg="green")
    l3.grid(row=13,column=0)

    #while guess>0:
    l4 = tk.Label(window, text="Guess a character ", font=("arial", 12), fg="orange")
    l4.grid(row=15,column=0)

    enter=tk.Entry(window,width=10)
    window.bind('<Return>', check)
    #to bind the enter key with the edit box
    enter.grid(row=16,column=0)



    btt2 = tk.Button(window, text="check", command=lambda: check(1), bg="light blue")
    btt2.grid(row=17,column=0,pady=4)


guess=5
hangman()


tk.mainloop()