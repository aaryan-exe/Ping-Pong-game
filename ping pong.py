import tkinter as tk
from PIL import Image, ImageTk
root=tk.Tk()
root.title=("Ping Pong game by Aryan Patil")

Width, Height = 600, 400
ball_size= 20
PaddleWidth,PaddleHeight=20, 100
paddle_speed = 20
ball_x, ball_y = 3,3
root.maxsize(Width, Height)

canvas=tk.Canvas(root, width=Width, height=Height)
canvas.pack()

bg_image=Image.open("Background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

root.mainloop()


# left_paddle = canvas.create_rectangle(10, HEIGHT/2 - PADDLE_HEIGHT/2, 30, HEIGHT/2 + PADDLE_HEIGHT/2, fill="white")
# right_paddle = canvas.create_rectangle(WIDTH - 30, HEIGHT/2 - PADDLE_HEIGHT/2, WIDTH - 10, HEIGHT/2 + PADDLE_HEIGHT/2, fill="white")
