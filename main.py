from tkinter import *
import turtle as trtl
import tkinter as tk


#screen configuration
wn = Tk()
wn.geometry("700x350")
wn.configure(background = "light blue")
wn.title("Register for a swim class")

#experience level list for drop down menu 
experience_level = ["Novice", "Intermediate", "Advanced"]
#age class list for second drop down menu
age_class_list = ["Adult", "Teenage", "Child", "Baby/Toddler" ]

def register_another_swimmer():
    # ask if user wants to register another swimmer
    another_swimmer = tk.messagebox.askyesno(message = "Would you like to register another swimmer?")
    if another_swimmer:
        # reset the code and show first button
        final.destroy()
        show_first_button()
    else:
        # exit the program
        final.destroy()
        lbl_exit_program = tk.Label(wn, text= "Thank you! You may exit the screen", font = 20, background = "light blue")
        lbl_exit_program.pack()
        lbl_exit_program.place(x=200, y=100)


def show_first_button():
  global first_button
  first_button = tk.Button(wn, text="Click to Register", font= 13, width = 25, height = 5, command=first_button_click) 
  first_button.pack()
  first_button.place(x=250, y=100) 
  
def first_button_click():
  global next_button, lbl_last_name, ent_last_name
  first_button.destroy()
  lbl_last_name = tk.Label(wn, text="Enter your last name:", background="light blue")
  lbl_last_name.pack()
  lbl_last_name.place(x=100, y=60)
  ent_last_name = tk.Entry(width=30)
  ent_last_name.pack()
  ent_last_name.place(x=300, y=60)
  next_button = tk.Button(wn, text = "Next", command=next_button_click)
  next_button.pack()
  next_button.place(x=300, y = 100)
  
#initial button 
show_first_button()

#what happens if next button is clicked
def next_button_click():
  global lbl_first_name, lbl_age, lbl_experience, ent_name, ent_age, ent_experience, next_button_2, clicked, swimmer_name, ent_class, lbl_class, clicked2, final
  next_button.destroy()
  lbl_last_name.destroy()
  ent_last_name.destroy()
  lbl_first_name = tk.Label(wn, text = "Enter swimmer's name:", background="light blue") 
  lbl_first_name.pack()
  lbl_first_name.place(x=100, y=60)
  lbl_age = tk.Label(wn, text = "Enter age:", background="light blue") 
  lbl_age.pack()
  lbl_age.place(x=100, y=100)
  lbl_class = tk.Label(wn, text="Class type:", background = "light blue")
  lbl_class.pack()
  lbl_class.place(x=100,y=140)
  lbl_experience = tk.Label(wn, text="Experience level:", background="light blue")
  lbl_experience.pack()
  lbl_experience.place(x=100, y=180)
  #entry area for name and age
  ent_name = tk.Entry(width = 30) 
  ent_name.pack()
  ent_name.place(x = 250, y = 60)
  ent_age = tk.Entry(width = 30) 
  ent_age.pack()
  ent_age.place(x= 250, y= 100)
  #drop down menu for experience level
  clicked = StringVar()
  clicked.set("what is experience level")
  ent_experience = OptionMenu( wn , clicked , *experience_level)
  ent_experience.pack()
  ent_experience.place(x=250, y=180)
  #drop down menu for type of class
  clicked2 = StringVar()
  clicked2.set("Pick an age class:")
  ent_class = OptionMenu(wn, clicked2, *age_class_list)
  ent_class.pack()
  ent_class.place(x=250, y=140)
  #formation of next_2 button
  next_button_2 = tk.Button(wn, text = "Next", command = next_button_2_click)
  next_button_2.pack()
  next_button_2.place(x=300, y = 300)


#function if next button 2 is clicked
def next_button_2_click():
  global final, swimmer_name
  swimmer_name = ent_name.get()
 # for item in experience_level:
  print(clicked.get())
  experience_selected = clicked.get()
  class_selected = clicked2.get()
  next_button_2.destroy()
  lbl_first_name.destroy()
  lbl_age.destroy()
  lbl_experience.destroy()
  ent_name.destroy()
  ent_age.destroy()
  ent_experience.destroy()
  lbl_class.destroy()
  ent_class.destroy()
  #second drop down menu
  print(swimmer_name)
  final = tk.Label(wn, text= "Thank you for registering " +swimmer_name + " for the " + class_selected+ " " +experience_selected+ " class",  background = "light blue", font = 20)
  final.pack()
  final.place(x=110, y=100)

  file = open("database.txt", "r+")
  if swimmer_name in file :
    file.close
  else:    
    file.write("Swimmer name: " + swimmer_name + "--> " + "Class registered: " + class_selected + "\n")
    file.close()
    
  register_another_swimmer()

wn.mainloop()
