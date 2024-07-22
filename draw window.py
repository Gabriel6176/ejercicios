import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Window and Door Designer")

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.selected_tool = "window"
        self.width_entry = tk.Entry(self.master, width=10)
        self.width_entry.pack(side=tk.LEFT)
        self.width_entry.insert(0, "100")
        
        self.height_entry = tk.Entry(self.master, width=10)
        self.height_entry.pack(side=tk.LEFT)
        self.height_entry.insert(0, "150")

        self.create_tools()

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def create_tools(self):
        self.window_button = tk.Button(self.master, text="Window", command=lambda: self.set_tool("window"))
        self.window_button.pack(side=tk.LEFT)

        self.door_button = tk.Button(self.master, text="Door", command=lambda: self.set_tool("door"))
        self.door_button.pack(side=tk.LEFT)

    def set_tool(self, tool):
        self.selected_tool = tool

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        
        if self.selected_tool == "window":
            self.canvas.create_rectangle(self.start_x, self.start_y, 
                                         self.start_x + width, self.start_y + height, 
                                         outline="black", width=2)
        elif self.selected_tool == "door":
            self.canvas.create_rectangle(self.start_x, self.start_y, 
                                         self.start_x + width, self.start_y + height, 
                                         outline="brown", width=2)

    def end_draw(self, event):
        pass

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()