import tkinter as tk
import deckalgorithm

durak = tk.Tk()

durak.title("Durak")
durak.geometry("640x580")
durak.configure( bg="#E6E6E6", cursor="star")

top_frame = tk.Frame(durak, bg="#E6E6E6")
top_frame.pack(pady=2)

opponent_label = tk.Label(top_frame, text="Opponents deck", font=("Comfortaa", 14), fg='black', bg='white', relief="groove")
opponent_label.pack()

opponent_card_frame = tk.Frame(durak, bg="#E6E6E6")
opponent_card_frame.pack(pady=15)

opponent_card1 = tk.Label(opponent_card_frame, text = deckalgorithm.opponent[0], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
opponent_card2 = tk.Label(opponent_card_frame, text = deckalgorithm.opponent[1], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
opponent_card3 = tk.Label(opponent_card_frame, text = deckalgorithm.opponent[2], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
opponent_card4 = tk.Label(opponent_card_frame, text = deckalgorithm.opponent[3], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
opponent_card5 = tk.Label(opponent_card_frame, text = deckalgorithm.opponent[4], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
opponent_card6 = tk.Label(opponent_card_frame, text = deckalgorithm.opponent[5], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")

opponent_card1.pack(side="left", padx=10)
opponent_card2.pack(side="left", padx=10)
opponent_card3.pack(side="left", padx=10)
opponent_card4.pack(side="left", padx=10)
opponent_card5.pack(side="left", padx=10)
opponent_card6.pack(side="left", padx=10)

bottom_frame = tk.Frame(durak, bg="#E6E6E6")
bottom_frame.pack(pady=2)

player_label = tk.Label(bottom_frame, text="Your deck", font=("Comfortaa", 14), fg='black', bg='white', relief="groove")
player_label.pack()

player_card_frame = tk.Frame(durak, bg="#E6E6E6")
player_card_frame.pack(pady=15)

player_card1 = tk.Label(player_card_frame, text = deckalgorithm.player[0], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
player_card2 = tk.Label(player_card_frame, text = deckalgorithm.player[1], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
player_card3 = tk.Label(player_card_frame, text = deckalgorithm.player[2], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
player_card4 = tk.Label(player_card_frame, text = deckalgorithm.player[3], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
player_card5 = tk.Label(player_card_frame, text = deckalgorithm.player[4], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")
player_card6 = tk.Label(player_card_frame, text = deckalgorithm.player[5], 
                 font=("Comfortaa", 12), fg='black', bg='white', relief="raised")

player_card1.pack(side="left", padx=10)
player_card2.pack(side="left", padx=10)
player_card3.pack(side="left", padx=10)
player_card4.pack(side="left", padx=10)
player_card5.pack(side="left", padx=10)
player_card6.pack(side="left", padx=10)

durak.mainloop()