import tkinter as tk
#import share_price_info as kio_file

#Creating the parent window
root = tk.Tk()
f = tk.Frame(root)

#Title for window
root.title("My first GUI")

#Size of the window - min and max
root.maxsize(550, 650)
root.minsize(250, 250)

#Setting a fixed size of window on opening
root.geometry("500x500")

#Setting the background colour
root.configure(background="white")

title = tk.Label(root, text="Platform", fg="black", font="Helvetica 20 bold", bg="grey")
title.grid(row=0, columnspan=3)

#Logo for top
topimg = tk.PhotoImage(file="stock_market.gif")
stock_img = tk.Label(root, image=topimg, bg="black")
stock_img.grid(row=1, columnspan=3)

#Entry to type which share you want to find info for
search = tk.Entry(root)
search.grid(row=2, column=1, sticky="W")

#Function to print out what has been searched for in the Entry bar
def search_bar():
    print(search.get())
    kio_file.share_price()
    #if search.get() == "kio":
        #use the information from the share info script
        #kio_file.share_price()

#Search button
tk.Button(root, text="Search", command=search_bar) .grid(row=3, column=1, sticky="W")

#Button when pressed closes program.
exit_btn = tk.Button(root, text="Exit Platform", bg="black", fg="white", width=20, height=2, command=root.destroy)
exit_btn.grid(row=4, column=2, sticky="E")   


#Label that prints the share info when the "KIO info" button is clicked
currentPrice = tk.StringVar(root, "Click for share info")
currentMovement = tk.StringVar(root, "Click for share info")

def setValues():
    price = kio_file.kio_price
    print(price)
    currentPrice.set(price)
    movement = kio_file.share_movement
    print(movement)
    currentMovement.set(movement)

#When button is clicked, the function as part of the "command" widget in the button code will run and the "textvariable" here
#which is linked to it will also be activated.
kio_printout = tk.Label(root, textvariable=currentPrice, bg='black', fg="white", width=40, height=3)
kio_printout.grid(row=4, column=1, padx=5, pady=5)

kio_printout = tk.Label(root, textvariable=currentMovement, bg='black', fg="white", width=40, height=3)
kio_printout.grid(row=5, column=1, padx=5, pady=5)

#When push the button the share details print out
kio = tk.Button(root, text="KIO info", bg="black", fg="white", width=30, height=2, command=setValues)
kio.grid(row=4, column=0, sticky="W", padx=5, pady=5)


print(root.grid_size())

#Run the program
root.mainloop()