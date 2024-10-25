# checke
# save and load system stuff

# Importing
import customtkinter as ctk

# Initial Window
window = ctk.CTk()

# Fonts
titlefont = ctk.CTkFont(family = "Helvetica", size = 40)
entryfont = ctk.CTkFont(family = "Source Sans Pro", size = 20)
rulesfont = ctk.CTkFont(family = "Source Sans Pro", size = 24)
buttonfont = ctk.CTkFont(family = "Source Sans Pro", size = 30)

# Functions
def name(text, label, mode):
    if mode == 'New Game':
        if text:
            gamepage(username = text[:12])
        else:
            label.configure(text = 'This field is required!\nMax: 12 Characters', text_color='red')            
    elif mode == 'Load Game':
        if text:
            gamepage(userid = text)
        else:
            label.configure(text = 'This field is required!\nUserID to load game', text_color='red')

def modechange(mode):
    if mode == 'New Game':
        length.focus_set()
        namefield.configure(placeholder_text = 'Enter your name...')
        length.configure(text = '\nMax: 12 Characters', text_color='white')
    if mode == 'Load Game':
        length.focus_set()
        namefield.configure(placeholder_text = 'Enter your UserID...')
        length.configure(text = '\nUserID to load game', text_color='white')

# checke
# test all codes after this
def addrules(condition, n):
    if condition:
        if n-1 in completed or n in rules_displayed:
            c = rulesflist[n-1].cget("fg_color")
            if c == 'black':
                rulesflist[n-1].configure(fg_color = '#34eb37')
            if n+1 not in rules_displayed:
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
    satisfied.configure(text = 'Rules satisfied: '+str(len(completed)-1)+'/50')

def checkrules():
    if len(completed) < 50:
        pw = passwordfield.get("1.0", "end-1c")
        addrules("1" in pw, 1)
        addrules("2" in pw, 2)
        addrules("3" in pw, 3)
        addrules("4" in pw, 4)
        addrules("5" in pw, 5)
        addrules("6" in pw, 6)
        addrules("9" in pw, 9)
        window.after(500, checkrules)
    else:
        gameover()

def rulelabel(n):
    rulesf = ctk.CTkFrame(rules, fg_color = 'black')
    rulesf.grid(row = n-1, pady = 5, padx = 10)
    rulesflist.append(rulesf)
    rulelab = ctk.CTkLabel(rulesf, text = 'Rule '+str(n)+'\n'+rules_list[n-1], wraplength = 180, padx = 10, pady = 20, fg_color = '#360c6e', font = rulesfont, corner_radius = 5)
    rulelab.grid(row = 0, pady = 3, padx = 3)
    # checke
    #   remove this part
    #   scroll to the new rule
    #rulelab = ctk.CTkLabel(rules, text = 'Rule '+str(n)+'\n'+rules_list[n-1], wraplength = 180, padx = 10, pady = 20, fg_color = '#360c6e', font = rulesfont, corner_radius = 5)
    #rulelab.grid(row = n-1, pady = 5, padx = 10)

# checke
# game over function
def gameover():
    pass

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

    dropdown = ctk.CTkOptionMenu(nameframe, values = ['New Game', 'Load Game'], font = ctk.CTkFont(family = "Source Sans Pro", size = 30), dropdown_font = entryfont, width = 250, height = 50, fg_color = 'black', button_color = 'black', button_hover_color = 'black', dropdown_fg_color = '#2C0A4A', dropdown_text_color = '#E0E0E0', dropdown_hover_color = '#1f0636', anchor = 'center', command = modechange)
    dropdown.grid(row = 0, padx = 20, pady = 20)

    namefield = ctk.CTkEntry(nameframe, border_width = 3, border_color = '#1b1b1c', font = entryfont, text_color = 'black', fg_color = 'white', placeholder_text = 'Enter your name...', width = 200)
    namefield.grid(row = 1, padx = 20, pady = 10)

    length = ctk.CTkLabel(nameframe, text = '\nMax: 12 Characters', text_color = 'white')
    length.grid(row = 2)

    enter = ctk.CTkButton(nameframe, text = 'Start', fg_color = '#360c6e', hover_color = '#230647', border_width = 2, border_color = 'black', font = buttonfont, command = lambda: name(namefield.get(), length, dropdown.get()))
    enter.grid(row = 3, padx = 20, pady = 20)

    warning = ctk.CTkLabel(window, font = ctk.CTkFont('Helvetica', 16), text = 'This game is supposed to be very hard and challenging.\nTry your best to not rage while playing this game.')
    warning.grid(row = 2, padx = 20, pady = 20)

def gamepage(username = None, userid = None):
    global window, passwordfield, rules, rules_list, satisfied, completed, notcompleted, rules_displayed, rulesflist

    window.destroy()

    window = ctk.CTk()

    ctk.set_appearance_mode('dark')

    window.title('Password Game: Apocalypse')
    window.iconbitmap('icon.ico')
    window.resizable(width=False, height=False)

    window.configure(fg_color = '#4B0082')

    completed = {0}
    notcompleted = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}
    rules_displayed = [1]
    rulesflist = []

    rules_file = open('rules.txt', 'r')
    rules_text = rules_file.read()
    rules_list = rules_text.split('\n')

    # Left
    rules = ctk.CTkScrollableFrame(window, label_text = 'Rules', label_fg_color = '#360c6e', label_font = ctk.CTkFont(family = "Source Sans Pro", size = 22), label_text_color = 'white', height = 300, width = 240, fg_color = '#6e078c', corner_radius = 5, border_width = 3, border_color = 'black', scrollbar_button_color = 'black', scrollbar_button_hover_color = 'black')
    rules.grid(row = 0, column= 0, padx = 20, pady = 20)

    rulelabel(1)

    rules.grid_columnconfigure(0, weight=1)

    # Right
    rightframe = ctk.CTkFrame(window, fg_color = '#6e078c', border_width = 3, border_color = 'black')
    rightframe.grid(row = 0, column = 1, padx = 20, pady = 20)

    statsframe = ctk.CTkFrame(rightframe, fg_color = '#360c6e', border_width = 2, border_color = 'black')
    statsframe.grid(row = 0, padx = 20, pady = 20)

    name = ctk.CTkLabel(statsframe, text = username, font = titlefont)
    name.grid(row = 0, pady = 20, padx = 20)

    satisfied = ctk.CTkLabel(statsframe, text = 'Rules satisfied: '+str(len(completed))+'/50', font = entryfont)
    satisfied.grid(row = 1, padx = 20)

    uid = ctk.CTkLabel(statsframe, text = 'UserID: ', font = entryfont)
    uid.grid(row = 2, padx = 20)

    saved = ctk.CTkLabel(statsframe, text = '')
    saved.grid(row = 3, padx = 20)

    passwordfield = ctk.CTkTextbox(rightframe, fg_color = '#210447', border_width = 2, border_color = 'black', height = 100, width = 200, font = entryfont, scrollbar_button_color = 'black', scrollbar_button_hover_color = 'black')
    passwordfield.grid(row = 1, padx = 20)

    save = ctk.CTkButton(rightframe, text = 'Save Game', fg_color = '#360c6e', hover_color = '#230647', border_width = 3, border_color = 'black', font = buttonfont)
    save.grid(row = 2, padx = 20, pady = 20)

    rules_file.close()

    checkrules()

    window.mainloop()

# Code
startpage()

window.mainloop()
