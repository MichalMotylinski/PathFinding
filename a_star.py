

"""class PathFindWindow(Frame):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.master.title("Path Finding")
        self.master.minsize(1400, 725)

        #grid_canvas = Canvas(self.master, width=800, height=700, bg="blue")
        #grid_canvas.grid(row=0, column=1)


        # example values
        for x in range(50):
            for y in range(20):
                btn = Button()
                btn.grid(column=x, row=y, sticky=N + S + E + W)"""


"""grid_size_btn = Button(self.master, text="Create grid")
grid_size_btn.pack()
grid_size_btn.place(x=900, y=50)

grid_elements_num = Text(self.master, height=1, width=20)
grid_elements_num.pack()
grid_elements_num.place(x=980, y=54)"""

"""def main():

    root = Tk()
    app = PathFindWindow()
    root.mainloop()


if __name__ == '__main__':
    main()
"""

def reconstruct_path(came_from, current):
    total_path = current

def a_star(start, goal, h):
    came_from = []

