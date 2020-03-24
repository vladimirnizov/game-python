import time
from tkinter import *
from models.ball import Ball
from models.paddle import Paddle
from models.score import Score

# main window of the app
tk = Tk()
tk.title('Game')
tk.resizable(0,0)
# window always in top position
tk.wm_attributes('-topmost', 1)

# main canvas of the game 500X400
canvas = Canvas(tk, width=500, height=400, bg='lightblue')
canvas.pack()

# update the main window with the canvas
tk.update()

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'white')
ball = Ball(canvas, paddle, score, 'yellow')

# while the ball doesn't hit bottom
while not ball.hit_bottom:

  # if game started and paddle can move
  if paddle.started:
    # move the ball
    ball.draw()
    # move the paddle
    paddle.draw()

  # update the main window after drawing
  tk.update_idletasks()
  tk.update()

  # little delay
  time.sleep(0.01)

time.sleep(3)
