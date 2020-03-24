import random

class Paddle:
  def __init__(self, canvas, color):
    # main params
    self.canvas = canvas
    self.id = canvas.create_rectangle(0,0,100,10, fill=color)

    # list of start position options
    start_1 = [40, 60, 90, 120, 150, 180, 200]
    random.shuffle(start_1)

    # start position of the paddle
    self.starting_point_x = start_1[0]
    self.canvas.move(self.id, self.starting_point_x, 300)
    self.x = 0
    self.canvas_width = self.canvas.winfo_width()
    self.started = False

    # buttons binding
    self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
    self.canvas.bind_all('<KeyPress-Return>', self.start_game)

  '''
  turn the paddle right
  return: void
  '''
  def turn_right(self, event):
    self.x = 4

  '''
  turn the paddle left
  return: void
  '''
  def turn_left(self, event):
    self.x = -4

  '''
  start game
  return: void
  '''
  def start_game(self, event):
    self.started = True

  '''
  draw the paddle in new place of canvas
  return: void
  '''
  def draw(self):
    self.canvas.move(self.id, self.x, 0)
    pos = self.canvas.coords(self.id)

    if pos[0] <= 0:
      self.x = 0

    elif pos[2] >= self.canvas_width:
      self.x = 0
