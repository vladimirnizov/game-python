import random

class Ball:
  def __init__(self, canvas, paddle, score, color):
    # main parameters
    self.canvas = canvas
    self.paddle = paddle
    self.score = score

    # create a ball figure
    self.id = self.canvas.create_oval(10,10,25,25, fill = color)
    # start position
    self.canvas.move(self.id, 245, 100)

    # list of possible directions
    starts = [-2, -1, 1, 2]
    random.shuffle(starts)

    # choose the start direction to move
    self.x = starts[0]
    self.y = -2

    #canvas size
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()

    self.hit_bottom = False

  '''
  this function will decide what to do when touching the platform
  params: pos - list of 4 coords
  return: Boolean
  '''
  def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)

    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
      if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
        self.score.hit()
        return True

      return False

  '''
  draw the ball in new place on canvas
  return: void
  '''
  def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)

    if pos[1] <= 0:
      self.y = 2

    if pos[3] >= self.canvas_height:
      self.hit_bottom = True
      self.canvas.create_text(250, 120, text='game over', font=('Courier', 24), fill='red')

    if self.hit_paddle(pos):
      self.y = -2

    if pos[0] <= 0:
      self.x = 2

    if pos[2] >= self.canvas_width:
      self.x = -2
