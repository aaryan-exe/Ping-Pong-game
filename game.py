import tkinter as tk
from PIL import Image, ImageTk  # Ensure Pillow is installed (pip install pillow)

# Initialize the game window
root = tk.Tk()
root.title("Pong Game")

# Define game settings
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 100
PADDLE_SPEED = 20
BALL_SPEED_X, BALL_SPEED_Y = 3, 3

# Set up the canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Load and set custom background image
bg_image = Image.open("background.png")  # Replace with your background image file
bg_image = bg_image.resize((WIDTH, HEIGHT), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Load custom ball image
ball_image = Image.open("custom_ball.png")  # Replace with your ball image file
ball_image = ball_image.resize((BALL_SIZE, BALL_SIZE), Image.LANCZOS)
ball_photo = ImageTk.PhotoImage(ball_image)
ball = canvas.create_image(WIDTH / 2, HEIGHT / 2, image=ball_photo)

# Create paddles
left_paddle = canvas.create_rectangle(10, HEIGHT/2 - PADDLE_HEIGHT/2, 30, HEIGHT/2 + PADDLE_HEIGHT/2, fill="white")
right_paddle = canvas.create_rectangle(WIDTH - 30, HEIGHT/2 - PADDLE_HEIGHT/2, WIDTH - 10, HEIGHT/2 + PADDLE_HEIGHT/2, fill="white")

# Initialize variables
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
left_paddle_dy = 0
right_paddle_dy = 0

# Move paddles
def move_paddle():
    canvas.move(left_paddle, 0, left_paddle_dy)
    canvas.move(right_paddle, 0, right_paddle_dy)
    root.after(20, move_paddle)

# Move ball and detect collisions
def move_ball():
    global ball_dx, ball_dy
    
    # Move ball
    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.bbox(ball)
    left_paddle_pos = canvas.coords(left_paddle)
    right_paddle_pos = canvas.coords(right_paddle)
    
    # Ball collision with top and bottom
    if ball_pos[1] <= 0 or ball_pos[3] >= HEIGHT:
        ball_dy = -ball_dy
    
    # Ball collision with left paddle
    if (ball_pos[0] <= left_paddle_pos[2] and 
        left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[3]):
        ball_dx = -ball_dx
        canvas.move(ball, 5, 0)  # Move ball slightly to the right
    
    # Ball collision with right paddle
    elif (ball_pos[2] >= right_paddle_pos[0] and 
          right_paddle_pos[1] < ball_pos[3] < right_paddle_pos[3]):
        ball_dx = -ball_dx
        canvas.move(ball, -5, 0)  # Move ball slightly to the left

    # Reset ball if it goes out of bounds
    if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
        canvas.coords(ball, WIDTH/2, HEIGHT/2)
        ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
    
    root.after(20, move_ball)

# Control paddles with key presses
def key_press(event):
    global left_paddle_dy, right_paddle_dy
    if event.keysym == 'w':
        left_paddle_dy = -PADDLE_SPEED
    elif event.keysym == 's':
        left_paddle_dy = PADDLE_SPEED
    elif event.keysym == 'Up':
        right_paddle_dy = -PADDLE_SPEED
    elif event.keysym == 'Down':
        right_paddle_dy = PADDLE_SPEED

def key_release(event):
    global left_paddle_dy, right_paddle_dy
    if event.keysym in ('w', 's'):
        left_paddle_dy = 0
    elif event.keysym in ('Up', 'Down'):
        right_paddle_dy = 0

# Bind keys to paddle movement
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# Start moving paddles and ball
move_paddle()
move_ball()

# Run the main loop
root.mainloop()
