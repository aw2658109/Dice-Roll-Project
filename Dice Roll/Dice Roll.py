import tkinter as tk
import random
root=tk.Tk()
root.geometry("700x450")
root.title("Roll Dice")

label=tk.Label(root,text="",font=("times",260))

def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button=tk.Button(root,text="let's roll....",width=40,height=5,font=10,bg="white",bd=2,command=roll)
button.pack(padx=10,pady=10)


root.mainloop()