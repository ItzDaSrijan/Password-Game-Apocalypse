# checke
# use CTkMessageBox ig - go thru license for all libraries
# save and load system stuff
# delete user - simply quit on unsaved and delete and quit on saved
# add actual rules and code variables shit
# add open source link
# performance check

# Importing
import customtkinter as ctk
import csv
import random
from tkinter import messagebox
import os

# Initial Window
window = ctk.CTk()

# Fonts
titlefont = ctk.CTkFont(family = "Helvetica", size = 40)
entryfont = ctk.CTkFont(family = "Source Sans Pro", size = 20)
rulesfont = ctk.CTkFont(family = "Source Sans Pro", size = 24)
buttonfont = ctk.CTkFont(family = "Source Sans Pro", size = 30)

# Functions
def name(text, label):
    if text:
        if text.isspace():
            label.configure(text = 'This field is required!\nMax: 12 Characters', text_color='red')
        elif text[:12].isspace():
            label.configure(text = 'Reduce number of spaces!\nMax: 12 Characters', text_color='red')
        else:
            with open('userdata.csv', 'r', newline = '') as f:
                csvr = csv.reader(f)
                s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                uid = ''
                e = []
                for i in csvr:
                    e = e+[i[0]]
                while True:
                    for i in range(5):
                        uid += s[random.randint(0, 61)]
                    if uid in e:
                        pass
                    else:
                        break
            gamepage(text[:12], uid)
    else:
        label.configure(text = 'This field is required!\nMax: 12 Characters', text_color='red')            

def dropfunc(mode):
    if mode == 'New Game':
        pass
    else:
        gamepage(mode[8:], mode[:5])

def addrules(condition, n):
    if condition:
        if n-1 in completed or n in rules_displayed:
            c = rulesflist[n-1].cget("fg_color")
            if c == 'black':
                rulesflist[n-1].configure(fg_color = '#34eb37')
            if n+1 not in rules_displayed:
                if n+1 > 50:
                    pass
                else:
                    rulelabel(n+1)
                    rules_displayed.append(n+1)
            completed.add(n)
            notcompleted.discard(n)
    else:
        if n in rules_displayed:
            d = rulesflist[n-1].cget("fg_color")
            if d == '#34eb37':
                rulesflist[n-1].configure(fg_color = 'black')
        notcompleted.add(n)
        completed.discard(n)
    satisfied.configure(text = 'Rules satisfied: '+"{:02d}".format(len(completed)-1)+'/50')

def checkrules(uname, uid):
    if len(completed) < 51:
        pw = passwordfield.get("1.0", "end-1c")
        addrules("1" in pw, 1)
        addrules("2" in pw, 2)
        addrules("3" in pw, 3)
        addrules("4" in pw, 4)
        addrules("5" in pw, 5)
        addrules("6" in pw, 6)
        addrules("7" in pw, 7)
        addrules("8" in pw, 8)
        addrules("9" in pw, 9)
        addrules("10" in pw, 10)
        addrules("11" in pw, 11)
        addrules("12" in pw, 12)
        addrules("13" in pw, 13)
        addrules("14" in pw, 14)
        addrules("15" in pw, 15)
        addrules("16" in pw, 16)
        addrules("17" in pw, 17)
        addrules("18" in pw, 18)
        addrules("19" in pw, 19)
        addrules("20" in pw, 20)
        addrules("21" in pw, 21)
        addrules("22" in pw, 22)
        addrules("23" in pw, 23)
        addrules("24" in pw, 24)
        addrules("25" in pw, 25)
        addrules("26" in pw, 26)
        addrules("27" in pw, 27)
        addrules("28" in pw, 28)
        addrules("29" in pw, 29)
        addrules("30" in pw, 30)
        addrules("31" in pw, 31)
        addrules("32" in pw, 32)
        addrules("33" in pw, 33)
        addrules("34" in pw, 34)
        addrules("35" in pw, 35)
        addrules("36" in pw, 36)
        addrules("37" in pw, 37)
        addrules("38" in pw, 38)
        addrules("39" in pw, 39)
        addrules("40" in pw, 40)
        addrules("41" in pw, 41)
        addrules("42" in pw, 42)
        addrules("43" in pw, 43)
        addrules("44" in pw, 44)
        addrules("45" in pw, 45)
        addrules("46" in pw, 46)
        addrules("47" in pw, 47)
        addrules("48" in pw, 48)
        addrules("49" in pw, 49)
        addrules("50" in pw, 50)
        window.after(500, lambda: checkrules(uname, uid))
    else:
        for i in rulesflist:
            i.configure(fg_color = '#34eb37')
        gameover(uname, uid)

def rulelabel(n):
    rulesf = ctk.CTkFrame(rules, fg_color = 'black')
    rulesf.grid(row = n-1, pady = 5, padx = 10)
    rulesflist.append(rulesf)
    rulelab = ctk.CTkLabel(rulesf, text = 'Rule '+str(n)+'\n'+rules_list[n-1], wraplength = 180, padx = 10, pady = 20, fg_color = '#360c6e', font = rulesfont, corner_radius = 5)
    rulelab.grid(row = 0, pady = 3, padx = 3)
    rules.after(25, lambda: rules._parent_canvas.yview_moveto(1.0))

def savefunc(uid, uname):
    passwordrn = passwordfield.get("1.0", "end-1c")
    found = 0
    with open('userdata.csv', 'r', newline = '') as f:
        csvr = csv.reader(f)
        with open('temp.csv', 'a', newline = '') as g:
            csvw = csv.writer(g)
            for i in csvr:
                if i[0] == uid:
                    found = 1
                    i[2] = passwordrn
                    csvw.writerow(i)
                else:
                    csvw.writerow(i)
    os.remove('userdata.csv')
    os.rename('temp.csv', 'userdata.csv')
    if found == 0:
        with open('userdata.csv', 'a', newline = '') as f:
            o = [uid, uname, passwordrn]
            csvw = csv.writer(f)
            csvw.writerow(o)
    col = saved.cget('text_color')
    tcolor = ''
    if col == '#00ffee':
        tcolor = 'white'
    else:
        tcolor = '#00ffee'
    saved.configure(text = 'Saved!', text_color = tcolor)

# checke
def deletefunc():
    pass

def gameover(uname, uid):
    passwordfield.configure(state = 'disabled', text_color = 'gray')
    savefunc(uid, uname)
    messagebox.showinfo('Game Over', f'Congratulations! You successfully beat the game!\nUsername: {uname}\nUserID: {uid}\nThis game has been saved.'.format(uname, uid))

# Pages
def startpage():
    global namefield, length
    
    ctk.set_appearance_mode('dark')
    
    window.title('Password Game: Apocalypse - Start')
    window.iconbitmap('icon.ico')
    window.resizable(width=False, height=False)
    
    window.configure(fg_color = '#4B0082')

    titleframe = ctk.CTkFrame(window, fg_color = '#4B0082')
    titleframe.grid(row = 0, padx = 30, pady = 20)

    title = ctk.CTkLabel(titleframe, text = 'Password Game: Apocalypse', text_color = '#D3D3D3', font = titlefont)
    title.grid(row = 0)

    hell = ctk.CTkLabel(titleframe, text = 'Welcome to Hell', font = ctk.CTkFont(family = "Helvetica", size = 30))
    hell.grid(row = 1, pady = 20)

    nameframe = ctk.CTkFrame(window, fg_color = '#500666', border_width = 2, border_color = 'black')
    nameframe.grid(row = 1, padx = 20)

    L = ['New Game']
    try:
        with open('userdata.csv', 'r', newline = '') as f:
            csvr = csv.reader(f)
            for i in csvr:
                st = i[0]+' - '+i[1]
                L = L + [st]
    except:
        with open('userdata.csv', 'w', newline = '') as f:
            pass

    dropdown = ctk.CTkOptionMenu(nameframe, values = L, font = ctk.CTkFont(family = "Source Sans Pro", size = 30), dropdown_font = entryfont, width = 250, height = 50, fg_color = 'black', button_color = 'black', button_hover_color = 'black', dropdown_fg_color = '#2C0A4A', dropdown_text_color = '#E0E0E0', dropdown_hover_color = '#1f0636', anchor = 'center', command = dropfunc)
    dropdown.grid(row = 0, padx = 20, pady = 20)

    existing = ctk.CTkLabel(nameframe, text = 'Choose an existing user from the dropdown')
    existing.grid(row = 1, padx = 10)

    namefield = ctk.CTkEntry(nameframe, border_width = 3, border_color = '#1b1b1c', font = entryfont, text_color = 'black', fg_color = 'white', placeholder_text = 'Enter your name...', width = 200)
    namefield.grid(row = 2, padx = 20, pady = 10)

    length = ctk.CTkLabel(nameframe, text = '\nMax: 12 Characters', text_color = 'white')
    length.grid(row = 3)

    enter = ctk.CTkButton(nameframe, text = 'Start', fg_color = '#360c6e', hover_color = '#230647', border_width = 2, border_color = 'black', font = buttonfont, command = lambda: name(namefield.get(), length))
    enter.grid(row = 4, padx = 20, pady = 20)

    warning = ctk.CTkLabel(window, font = ctk.CTkFont('Helvetica', 16), text = 'This game is supposed to be very hard and challenging.\nTry your best to not rage while playing this game.')
    warning.grid(row = 2, padx = 20, pady = 20)

def gamepage(username, userid):
    global window, passwordfield, rules, rules_list, satisfied, completed, notcompleted, rules_displayed, rulesflist, saved, save

    window.destroy()

    window = ctk.CTk()

    ctk.set_appearance_mode('dark')

    window.title('Password Game: Apocalypse')
    window.iconbitmap('icon.ico')
    window.resizable(width=False, height=False)

    window.configure(fg_color = '#4B0082')

    passwordloaded = ''
    with open('userdata.csv', 'r', newline = '') as f:
        csvr = csv.reader(f)
        for i in csvr:
            if userid == i[0]:
                passwordloaded = i[2]
                break

    completed = {0}
    notcompleted = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}
    rules_displayed = [1]
    rulesflist = []

    rules_file = open('rules.txt', 'r')
    rules_text = rules_file.read()
    rules_list = rules_text.split('\n')

    # Title
    titleframegp = ctk.CTkFrame(window, fg_color = '#4B0082')
    titleframegp.grid(row = 0, padx = 30, pady = 20)

    titlegp = ctk.CTkLabel(titleframegp, text = 'Password Game: Apocalypse', text_color = '#D3D3D3', font = titlefont)
    titlegp.grid(row = 0)

    # Second Frame
    sframe = ctk.CTkFrame(window, fg_color = '#4B0082')
    sframe.grid(row = 1)

    # Left
    rules = ctk.CTkScrollableFrame(sframe, label_text = 'Rules', label_fg_color = '#360c6e', label_font = ctk.CTkFont(family = "Source Sans Pro", size = 22), label_text_color = 'white', height = 300, width = 240, fg_color = '#6e078c', corner_radius = 5, border_width = 3, border_color = 'black', scrollbar_button_color = 'black', scrollbar_button_hover_color = 'black')
    rules.grid(row = 0, column = 0, padx = 20, pady = 20)

    rulelabel(1)

    rules.grid_columnconfigure(0, weight=1)

    # Right
    rightframe = ctk.CTkFrame(sframe, fg_color = '#6e078c', border_width = 3, border_color = 'black')
    rightframe.grid(row = 0, column = 1, padx = 20, pady = 20)

    statsframe = ctk.CTkFrame(rightframe, fg_color = '#360c6e', border_width = 2, border_color = 'black')
    statsframe.grid(row = 0, padx = 20, pady = 20)

    name = ctk.CTkLabel(statsframe, text = username, font = titlefont)
    name.grid(row = 0, pady = 20, padx = 20)
    
    satisfied = ctk.CTkLabel(statsframe, text = 'Rules satisfied: '+str(len(completed))+'/50', font = entryfont)
    satisfied.grid(row = 1, padx = 20)

    uid = ctk.CTkLabel(statsframe, text = 'UserID: '+userid, font = entryfont)
    uid.grid(row = 2, padx = 20)

    saved = ctk.CTkLabel(statsframe, text = '', font = entryfont, text_color = 'black')
    saved.grid(row = 3, padx = 20, pady = 5)

    passwordfield = ctk.CTkTextbox(rightframe, fg_color = '#210447', border_width = 2, border_color = 'black', height = 100, width = 200, font = entryfont, scrollbar_button_color = 'black', scrollbar_button_hover_color = 'black')
    passwordfield.grid(row = 1, padx = 20)

    # checke
    # doesnt add new rule ig and scroll stuff
    # scrollbar appears so weird stuff happens and white thing, maybe scroll to bottom
    passwordfield.insert('0.0', passwordloaded)

    save = ctk.CTkButton(rightframe, text = 'Save Game', fg_color = '#360c6e', hover_color = '#230647', border_width = 3, border_color = 'black', font = buttonfont, command = lambda: savefunc(userid, username))
    save.grid(row = 2, padx = 20, pady = 10)

    delete = ctk.CTkButton(rightframe, text=  'Delete Game', fg_color = '#9c0808', hover_color = '#730606', border_width = 3, border_color = 'black', font = ctk.CTkFont(family = "Source Sans Pro", size = 24), command = deletefunc)
    delete.grid(row = 3, padx = 20, pady = 10)

    rules_file.close()

    checkrules(username, userid)

    window.mainloop()

# Code
startpage()

window.mainloop()
