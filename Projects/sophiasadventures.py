# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
# TODO - set your background
# TODO - set the starting value for your variable
b1= create_sprite ("sophiascastle",150,150)
s1= create_sprite("sophia321",100,100)
s2= create_sprite ("purplegem2",random.randint(-500,500),random.randint(-250,250))
# Section 3: Controls
# TODO - define your controls
# TODO - pick keys for each control
def move_up():
	b1.setheading(90)
	b1.forward(10)
	s2.setheading(90)
	s2.forward(10)
   	 
def move_down():
	b1.setheading(270)
	b1.forward(10)
	s2.setheading(270)
	s2.forward(10)
    
def move_left():
	b1.setheading(180)
	b1.forward(10)
	s2.setheading(180)
	s2.forward(10)
    

def move_right():    
	b1.setheading(0)
	b1.forward(10)
	s2.setheading(0)
	s2.forward(10)
window.onkeypress(move_up, "s")
window.onkeypress(move_down,"w")
window.onkeypress(move_left,"d")
window.onkeypress(move_right,"a")

# Section 4: Game Loop
window.listen()
timer = 0
points = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions
	if get_distance(s1,s2)<50:
		points+=1
		s2.goto(random.randint(-500,500),random.randint(-250,250))





	window.update()

	if points>= 5:
		break
	

print("Game Over")
