import tkinter as tk
from PIL import Image, ImageTk 

# Initialize the main window
root = tk.Tk()
root.title("Pong Game")

# Constants
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20
PADDLE_SPEED = 20
BALL_SPEED_X, BALL_SPEED_Y = 3, 3

# Create the canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Load and set the background image
bg_image = Image.open("background.png")
bg_image = bg_image.resize((WIDTH, HEIGHT), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Load and set the ball image
ball_image = Image.open("custom_ball.png")
ball_image = ball_image.resize((BALL_SIZE, BALL_SIZE), Image.LANCZOS)
ball_photo = ImageTk.PhotoImage(ball_image)
ball = canvas.create_image(WIDTH / 2, HEIGHT / 2, image=ball_photo)

# Create paddles
left_paddle = canvas.create_rectangle(10, HEIGHT / 2 - PADDLE_HEIGHT / 2, 30,
                                       HEIGHT / 2 + PADDLE_HEIGHT / 2, fill="white")
right_paddle = canvas.create_rectangle(WIDTH - 30, HEIGHT / 2 - PADDLE_HEIGHT / 2,
                                        WIDTH - 10, HEIGHT / 2 + PADDLE_HEIGHT / 2, fill="white")

# Score variables
left_score = 0
right_score = 0

# Score display
score_display = canvas.create_text(WIDTH / 2, 20, text=f"{left_score} - {right_score}", fill="white", font=("Arial", 24))

# Initialize movement variables
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
left_paddle_dy = 0
right_paddle_dy = 0

def update_score():
    canvas.itemconfig(score_display, text=f"{left_score} - {right_score}")

def move_paddle():
    canvas.move(left_paddle, 0, left_paddle_dy)
    canvas.move(right_paddle, 0, right_paddle_dy)
    root.after(20, move_paddle)

def move_ball():
    global ball_dx, ball_dy, left_score, right_score

    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.bbox(ball)
    left_paddle_pos = canvas.coords(left_paddle)
    right_paddle_pos = canvas.coords(right_paddle)

    # Ball collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[3] >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_pos[0] <= left_paddle_pos[2] and
            left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[3]):
        ball_dx = -ball_dx
        canvas.move(ball, 5, 0)  # Avoid getting stuck

    elif (ball_pos[2] >= right_paddle_pos[0] and
            right_paddle_pos[1] < ball_pos[3] < right_paddle_pos[3]):
        ball_dx = -ball_dx
        canvas.move(ball, -5, 0)

    # Update score if the ball goes out of bounds
    if ball_pos[0] <= 0:
        right_score += 1
        update_score()
        reset_ball()

    elif ball_pos[2] >= WIDTH:
        left_score += 1
        update_score()
        reset_ball()

    root.after(20, move_ball)

def reset_ball():
    canvas.coords(ball, WIDTH / 2, HEIGHT / 2)
    global ball_dx, ball_dy
    ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

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

# Bind keys to functions
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# Start movement
move_paddle()
move_ball()

# Run the application
root.mainloop()
