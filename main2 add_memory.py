from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk


root = Tk()
# root.geometry('500x300')
root.title('ASK DOC!')



# im=Image.open("doctor.jpg")
# im = im.resize((323,327),Image.ANTIALIAS)
# img=ImageTk.PhotoImage(im)
# doc_pic = Label(root, image=img )
photo = PhotoImage(file="doctor.png")
doc_pic = Label(root, image=photo)
doc_pic.pack()
def show_memory_test():
    function_selection_window.withdraw()

    memory_window = Toplevel(root)
    v_content = StringVar()
    v_content.set('Here shows the content \nyou need to memorize!')

    menubar = Menu(memory_window)
    lang_var = StringVar()
    lang_var.set('6')
    difficulty_menu = Menu(menubar, tearoff=False)
    difficulty_menu.add_radiobutton(label="6", variable=lang_var,value='6')
    difficulty_menu.add_radiobutton(label="7.635", variable=lang_var,value='7.635')
    difficulty_menu.add_radiobutton(label="8", variable=lang_var,value='8')
    difficulty_menu.add_radiobutton(label="9.7", variable=lang_var, value='9.7')
    difficulty_menu.add_radiobutton(label="19", variable=lang_var, value='19')
    difficulty_menu.add_radiobutton(label="29.8", variable=lang_var, value='29.8')
    difficulty_menu.add_radiobutton(label="48", variable=lang_var, value='48')
    difficulty_menu.add_radiobutton(label="UltimateChallenge", variable=lang_var, value='UltimateChallenge')


    menubar.add_cascade(label="diffuculty", menu=difficulty_menu)
    memory_window.config(menu=menubar)
    def fit_str_to_label(string):
        pre_content = list(string)
        final_content = ''
        count = 0
        while True:
            if count + 20 >= len(pre_content):
                final_content += ''.join(pre_content[count:len(pre_content)])
                break
            else:
                final_content += ''.join(pre_content[count:count + 18])
                final_content += '\n'
                count += 18
        return final_content
    def create_content():
        import random
        nonlocal lang_var
        difficulitie = lang_var.get()
        print(difficulitie)
        if difficulitie == "6":  # these shou have buttons
            char2 = chr(random.randint(33, 126))  # in acsii, only 33 to 126 are useable chararacters
            char1 = chr(random.randint(33, 126))
            array = [char1, char1, char1, char2, char2, char2]
            random.shuffle(array)
            # print("".join(array))
        elif difficulitie == "7.635":
            char2 = chr(random.randint(33, 126))
            char1 = chr(random.randint(33, 126))
            array = [char1, char1, char1, char2, char2, char2, char2, char2]
            random.shuffle(array)
            # print("".join(array))
        elif difficulitie == "8":
            char2 = chr(random.randint(33, 126))
            char1 = chr(random.randint(33, 126))
            array = [char1, char1, char1, char1, char2, char2, char2, char2]
            random.shuffle(array)
            # print("".join(array))
        elif difficulitie == "9.7":
            char2 = chr(random.randint(33, 126))
            char1 = chr(random.randint(33, 126))
            array = [char1, char1, char1, char1, char2, char2, char2, char2, char2, char2]
            random.shuffle(array)
            # print("".join(array))
        elif difficulitie == "19":
            char2 = chr(random.randint(33, 126))
            char3 = chr(random.randint(33, 126))
            char1 = chr(random.randint(33, 126))
            array = [char1, char1, char1, char1, char2, char2, char2, char2, char3, char3, char3, char3]
            random.shuffle(array)
            # print("".join(array))
        elif difficulitie == "29.8":
            char2 = chr(random.randint(33, 126))
            char3 = chr(random.randint(33, 126))
            char4 = chr(random.randint(33, 126))
            char1 = chr(random.randint(33, 126))
            array = [char1, char1, char1, char1, char2, char2, char2, char2, char3, char3, char3, char3, char4, char4,
                     char4, char4]
            random.shuffle(array)
            # print("".join(array))
        elif difficulitie == "48":
            char2 = chr(random.randint(33, 126))
            char3 = chr(random.randint(33, 126))
            char4 = chr(random.randint(33, 126))
            char1 = chr(random.randint(33, 126))
            char5 = chr(random.randint(33, 126))
            char6 = chr(random.randint(33, 126))
            char8 = chr(random.randint(33, 126))
            char7 = chr(random.randint(33, 126))
            array = [char1, char1, char2, char2, char3, char3, char3, char4, char4, char5, char5, char6, char6, char7,
                     char7, char8, char8]
            random.shuffle(array)
            # print("".join(array))
        elif difficulitie == "UltimateChallenge":
            array = []
            for i in range(100):
                array.append(chr(random.randint(33, 126)))
            random.shuffle(array)
            # print("".join(array))
        else:
            array=[]
        # for ch in array:
        #     print(ord(ch),end=' ')
        # print()
        question = "".join(array)
        return question
    content = ''
    def show_content():
        nonlocal content
        content = create_content()
        final_content = fit_str_to_label(content)

        # for c in range(0,len(pre_content),10):
        #     final_content += ''.join(pre_content[c:c+10 if c+10<len(pre_content) else len(pre_content)-1])+'\n'
        v_content.set(final_content)
        write_zone['state'] = DISABLED
        show_content_button['state'] = DISABLED
        submit_button['state'] = DISABLED

        if lang_var.get() == 'UltimateChallenge':
            count_time.set('60')
        else:
            count_time.set('15')
        while count_time.get() != '0':
            import time
            time_left = int(count_time.get())
            time_left -= 1
            count_time.set(str(time_left))
            time.sleep(1)
            memory_window.update()
        v_content.set('Please write what you have seen')
        show_content_button['text'] = 'Restart'
        write_zone['state'] = NORMAL
        show_content_button['state'] = NORMAL
        submit_button['state'] = NORMAL

    def submit():
        written = write_zone.get()
        write_zone.delete(0,END)
        if written == content:
            v_content.set('Congratulations! You have passed the test!')
        else:
            v_content.set(fit_str_to_label('Sorry! Your answer is not correct. The answer is '+content))
    def return_menu_from_memory_window():
        memory_window.destroy()
        function_selection_window.update()
        function_selection_window.deiconify()
    word_zone = Label(memory_window, font=('Calibri',20), textvariable=v_content)
    show_content_button = Button(memory_window, text='start test', command=show_content, font=('Calibri',15), width=18)
    write_zone = Entry(memory_window,font=('Calibri',20), justify=CENTER)
    submit_button = Button(memory_window, text='submit', command=submit, font=('Calibri',15),width=18)
    count_time = StringVar()
    count_time.set('Here counts the time down')
    count_down = Label(memory_window, textvariable=count_time, font=('Calibri',20))
    return_to_menu_button = Button(memory_window, text='return to menu', command=return_menu_from_memory_window, font=('Calibri', 15), width=18)
    submit_button['state'] = DISABLED
    word_zone.pack()
    write_zone.pack()
    show_content_button.pack()
    submit_button.pack()
    return_to_menu_button.pack()
    count_down.pack()
    memory_window.mainloop()

def show_BMI_test():
    showinfo('Warning','Sorry, this is currently under construction',parent=function_selection_window)

def show_fat_test():
    function_selection_window.withdraw()
    fat_test_window = Toplevel(root)
    v_gender = StringVar()
    def change_variable_label():
        if v_gender.get() == 'Male':
            variable_label1['text'] = 'Input abdomen circumference:'
            variable_label2.grid_forget()
            variable_entry2.grid_forget()
        else:
            variable_label1['text'] = 'Input waist circumference:'
            variable_label2.grid(row=4, column=0)
            variable_entry2.grid(row=4, column=1, padx=10)
    def calc():
        #Err checking
        err_flag = False
        if v_height.get().isdigit():
            height = int(v_height.get())
            print(height)
        else:
            v_height.set('Height must be positive integer!')
            err_flag = True

        if v_neck.get().isdigit():
            neck = int(v_neck.get())
            print(neck)
        else:
            v_neck.set('Neck circumference must be positive integer!')
            err_flag = True

        if v_variable1.get().isdigit():
            variable1 = int(v_variable1.get())
            print(variable1)
        else:
            v_variable1.set('This must be positive integer!')
            err_flag = True

        if v_gender.get() == 'Female':
            if v_variable2.get().isdigit():
                variable2 = int(v_variable2.get())
                print(variable2)
            else:
                print(v_gender.get())
                v_variable2.set('This must be positive integer!')
                err_flag = True

        if err_flag:
            return

        if v_gender.get()=='Male':
            abdomen = variable1
            m1=86.01
            m2=70.041
            m3=36.76
            import math as m
            if abdomen - neck <= 0:
                showwarning('Warning', 'Abdomen circumference must be bigger than neck', parent=fat_test_window)
                return
            a=m.log10(abdomen - neck)
            b=m.log10(height)
            fat=m1 * a - m2 * b + m3
        else:
            waist = variable1
            hip = variable2
            f1=163.205
            f2=97.684
            f3=78.387
            import math as m
            if waist + hip - neck <= 0:
                showwarning('Warning','This is not a normal person!',parent=fat_test_window)
                return
            c=m.log10(waist + hip - neck)
            d=m.log10(height)
            fat=f1 * c -f2 * d - f3
    def return_menu_from_fat_window():
        fat_test_window.destroy()
        function_selection_window.update()
        function_selection_window.deiconify()
    r1=Radiobutton(fat_test_window, text="Male", variable=v_gender, value='Male', command=change_variable_label, font=('Calibri',18))
    r1.grid(row=0, column=0)
    r1.select()
    r2=Radiobutton(fat_test_window, text="Female", variable=v_gender, value='Female', command=change_variable_label, font=('Calibri',18))
    r2.grid(row=0, column=1)

    v_height = StringVar()
    v_neck = StringVar()
    v_variable1 = StringVar()
    v_variable2 = StringVar()

    height_label = Label(fat_test_window, text='Input height:',font=('Calibri',18))
    height_label.grid(row=1, column=0)
    height_entry = Entry(fat_test_window, textvariable=v_height, width=35,font=('Calibri',18))
    height_entry.grid(row=1, column=1, padx=10)
    neck_label = Label(fat_test_window, text='Input neck circumference:',font=('Calibri',18))
    neck_label.grid(row=2, column=0)
    neck_entry = Entry(fat_test_window, textvariable=v_neck, width=35,font=('Calibri',18))
    neck_entry.grid(row=2, column=1, padx=10)

    variable_label1 = Label(fat_test_window, text='Input abdomen circumference:',font=('Calibri',18))
    variable_label1.grid(row=3, column=0)
    variable_entry1 = Entry(fat_test_window, textvariable=v_variable1, width=35,font=('Calibri',18))
    variable_entry1.grid(row=3, column=1, padx=10)

    variable_label2 = Label(fat_test_window, text='Input hip circumference:',font=('Calibri',18))
    variable_entry2 = Entry(fat_test_window, textvariable=v_variable2, width=35,font=('Calibri',18))

    submit_button = Button(fat_test_window, text='Submit', command=calc, width=15,font=('Calibri',18))
    submit_button.grid(row=5, columnspan=2)

    to_main_button = Button(fat_test_window, text='Return To Menu', command=return_menu_from_fat_window, width=15,font=('Calibri',18))
    to_main_button.grid(row=6, columnspan=2)

    fat_test_window.mainloop()
def show_function_selection():
    print(language_selection.get(ACTIVE))

    language_selection_window.withdraw()
    global function_selection_window
    function_selection_window = Toplevel(root)

    function_label = Label(function_selection_window, text='Please select one of the functions', font=('Calibri',20))
    function_label.pack()
    BMI_button = Button(function_selection_window, text='Get BMI', command=show_BMI_test, font=('Calibri',20))
    BMI_button.pack(fill=X)
    fat_button = Button(function_selection_window, text='Get body fat rate', command=show_fat_test, font=('Calibri',20))
    fat_button.pack(fill=X)
    memory_button = Button(function_selection_window, text='Get memory challenge', command=show_memory_test, font=('Calibri',20))
    memory_button.pack(fill=X)
    function_selection_window.mainloop()
def show_language_selection():
    root.withdraw()
    global language_selection_window, language_selection
    language_selection_window = Toplevel(root)

    instruction = Label(language_selection_window, text='Please select language', font=('Calibri',20))
    instruction.pack()
    language_selection = Listbox(language_selection_window, font=('Calibri',15))
    language_selection.pack()

    # 往列表里添加数据
    for item in ["English", "中文", "español"]:
        language_selection.insert(END, item)
    language_selection.select_set(0)

    button_next_language = Button(language_selection_window, font=('Calibri',15), text='continue', command=show_function_selection)
    button_next_language.pack()

    language_selection_window.mainloop()
button_next_root = Button(root, text='Continue', command=show_language_selection, font=('Calibri',15))
button_next_root.pack()

if __name__ == '__main__':
    root.mainloop()