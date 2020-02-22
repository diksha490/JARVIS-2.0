import tkinter as tk

master=tk.Tk()
master.title("Welcome Human ! ")

search_button = tk.Button(master, text="Search",command=lambda: search_text(tentry))
search_button.grid(row=0,column=0)
master.mainloop()
