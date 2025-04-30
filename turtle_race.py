from turtle import *
import random

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

# Prompt user for their bet
user_gues = screen.textinput(
    title="Make your BET",
    prompt="Which color Turtle will win the race:\n[red, green, blue, yellow, orange, cyan]"
).lower()

# Available turtle colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan']

# Y-positions for turtles
positions = [-100, -65, -30, 0, 30, 65, 100]
turtles = []

# Draw the black vertical finish line
t = Turtle()
t.speed("fastest")
t.penup()
t.goto(0, 0)
t.fd(230)
t.setheading(90)
t.pendown()
t.pensize(50)
t.fd(250)
t.setheading(270)
t.fd(500)

# Write "FINISH" vertically on the finish line
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")

start_x = 230
start_y = 90  # Adjust for alignment

for letter in "FINISH":
    writer.goto(start_x, start_y)
    writer.write(letter, align="center", font=("Arial", 16, "bold"))
    start_y -= 30

# Create turtles and position them at the start
for y in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[y])
    t.penup()
    t.goto(x=-230, y=positions[y])
    turtles.append(t)

# Start the race if user made a bet
if user_gues:
    is_race_on = True

# Turtle race loop
while is_race_on:
    for i in turtles:
        if i.xcor() > 190:  # Check if a turtle has reached the finish line
            is_race_on = False
            win_t = i.pencolor()
            print("\n🏁 The race is over! 🏁")
            print(f"🥇 Winner: {win_t.upper()} turtle")

            if win_t == user_gues:
                print("🎉 Congratulations! You guessed it right!")
            else:
                print(f"❌ Sorry! You lose, You guessed {user_gues.upper()}, but {win_t.upper()} won.")
        rand_dis = random.randint(1, 10)
        i.fd(rand_dis)

# Keep window open until clicked
screen.exitonclick()

