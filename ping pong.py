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

ball_image= Image.open("custom_ball.png")
ball_image = ball_image.resize((ball_size, ball_size), Image.LANCZOS)
ball_photo=ImageTk.PhotoImage(ball_image)
ball=canvas.create_image(Width/2, Height/2, image=ball_photo)

left_paddle= canvas.create_rectangle(10, Height/2-PaddleHeight/2, 30, Height/2 + PaddleHeight/2, fill='White')
right_paddle= canvas.create_rectangle(Width-30, Height/2 - PaddleHeight/2, Width-10, Height/2 + PaddleHeight/2, fill="white")

ball_dx, ball_dy = ball_x, ball_y
left_paddle_dy=0
right_paddle_dy=0

def movePaddle():
    canvas.move(left_paddle, 0, left_paddle_dy)
    canvas.move(right_paddle, 0, right_paddle_dy)
    root.after(20, movePaddle)


root.mainloop()
