import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                                   bg="lightblue", fg="black",
                                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def on_button_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.current_player:
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col]["fg"] = "red" if self.current_player == "X" else "blue"
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for row in range(3):
            if all(self.buttons[row][col]["text"] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.buttons[row][col]["text"] == player for row in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == player for i in range(3)) or \
           all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
                self.buttons[row][col]["fg"] = "black"
        self.current_player = "X"

if _name_ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
