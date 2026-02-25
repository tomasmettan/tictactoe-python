import tkinter as tk
from tkinter import messagebox

player = 'X'
game_over = False

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

def on_button_click(row, col):
    global player, game_over
    if not game_over and buttons[row][col]['text'] == '':
        buttons[row][col]['text'] = player
        if check_winner():
            messagebox.showinfo("Fin del Juego", f"Jugador {player} Gana!")
            game_over = True
        elif all(buttons[i][j]['text'] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Fin del Juego", "Empate!")
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'

def reset_game():
    global player, game_over
    player = 'X'
    game_over = False
    for r in range(3):
        for c in range(3):
            buttons[r][c]['text'] = ''

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x450")
root.configure(bg="#0C3F50")

frame = tk.Frame(root, bg="#0C3F50")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

buttons = [[tk.Button(frame, text='', font=('Arial', 24), width=5, height=2,
                      command=lambda r=r, c=c: on_button_click(r, c))
            for c in range(3)] for r in range(3)]

for r in range(3):
    for c in range(3):
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

reset_button = tk.Button(root, text='Reiniciar', font=('Arial', 14), command=lambda: reset_game())
reset_button.pack(pady=20)

root.mainloop()