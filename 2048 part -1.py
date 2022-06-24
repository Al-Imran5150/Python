import tkinter as tk
import colors as c
import random


GRID_COLOR = "#a39489"
EMPTY_CELL_COLORS = "#c2b3a9"
SCORE_LABEL_FONT = ("Verdana", 24)
SCORE_FONT = ("Helvetica", 36, "bold")
GAME_OVER_FONT = ("Helvetica", 48, "bold")
GAME_OVER_FONT_COLORS = "#ffffff"
WINNER_BG = "#ffcc00"
LOSER_BG = "#a39489"

cell_colors = {
    2: "#fcefe6",
    4: "#f2e8cb",
    8: "#f5b682",
    16: "#f29446",
    32: "#ff775c",
    64: "#e64c2e",
    128: "#ede291",
    256: "#fce130",
    512: "#ffdb4a",
    1024: "#f0b922",
    2048: "#fad74d",
}

CELL_NUMBER_COLORS = {
    2: "#695c57",
    4: "#695c57",
    8: "#ffffff",
    16: "#ffffff",
    32: "#ffffff",
    64: "#ffffff",
    128: "#ffffff",
    256: "#ffffff",
    512: "#ffffff",
    1024: "#ffffff",
    2048: "#ffffff",
}

CELL_NUMBER_FONTS = {
    2: ("Helvetica", 55, "bold"),
    4: ("Helvetica", 55, "bold"),
    8: ("Helvetica", 55, "bold"),
    16: ("Helvetica", 50, "bold"),
    32: ("Helvetica", 50, "bold"),
    64: ("Helvetica", 50, "bold"),
    128: ("Helvetica", 45, "bold"),
    256: ("Helvetica", 45, "bold"),
    512: ("Helvetica", 45, "bold"),
    1024: ("Helvetica", 40, "bold"),
    2048: ("Helvetica", 40, "bold"),
}


class Game(tk.Frame):
    def __init__(self):
       tk.Frame.__init__(self)
       self.grid()
       self.master.title("2048")

       self.main_grid = tk.Frame(
           self, bg=c.GRID_COLOR, bd=3, width=600
       )
       self.main_grid.grid(pady=(100, 0)) 
       self.MAKE_GUI()

       self.mainloop()


    def MAKE_GUI(self):
        
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

            #make score header
            score_frame = tk.Frame(self)
            score_frame.place(relx=0.5, y=45, anchor="center")
            tk.Label(
                score_frame,
                text="Score",
                font=c.SCORE_LABEL_FONT
            ).grid(row=0)
            self.score_label =tk.Label(score_frame, text="0", font=c.SCORE_FONT)
            self.score_label.grid(row=1)

Game()

    