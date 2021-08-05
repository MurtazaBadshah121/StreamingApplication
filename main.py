import tkinter as tk

window = tk.Tk()
window.title("Welcome!")
#window.geometry("400x300")



welcomelabel = tk.Label(text="Welcome to Streamify app!")
choicelabel = tk.Label(text="Please log in or create a new account")


btLogin = tk.Button(text="Log in")
btRegister = tk.Button(text="Register")


welcomelabel.grid(row=0, column=0)
choicelabel.grid(row=1, column=0)
btLogin.grid(row=2, column=0)
btRegister.grid(row=3, column=0)

#welcomelabel.pack()
#choicelabel.pack()
#btLogin.pack()
#btRegister.pack()
#frame_a.pack()
#frame_b.pack()

window.mainloop()

#if __name__ == '__main__':
     #   window()