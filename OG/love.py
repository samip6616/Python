import turtle
import math
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=900, height=750)
screen.bgcolor("#100018")
screen.title("A Heart Full of Love")
screen.tracer(0)

# Main drawing turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# Heart colors: outer shadow to inner highlight
layers = [
    ("#4a001f", 1.30),
    ("#85002d", 1.18),
    ("#ff003c", 1.05),
    ("#ff3978", 0.88),
    ("#ff8fb8", 0.65),
]

def heart_points(scale):
    points = []
    for i in range(361):
        t = math.radians(i)

        # Mathematical heart curve
        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        points.append((x * scale, y * scale))

    return points

def draw_heart(scale, color):
    points = heart_points(scale)

    pen.penup()
    pen.goto(points[0])
    pen.color(color)
    pen.begin_fill()

    for point in points[1:]:
        pen.goto(point)

    pen.goto(points[0])
    pen.end_fill()

def draw_floating_heart(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.dot(size, color)

def draw_message():
    pen.penup()
    pen.goto(0, -255)
    pen.color("#ffd6e7")
    pen.write(
        "YOU MAKE MY WORLD BEAUTIFUL",
        align="center",
        font=("Arial", 19, "bold")
    )

    pen.goto(0, -290)
    pen.color("#ff80ab")
    pen.write(
        "Love you forever  ♥",
        align="center",
        font=("Arial", 16, "normal")
    )

# Floating particles
particles = []

for _ in range(35):
    particles.append([
        random.randint(-420, 420),
        random.randint(-330, 350),
        random.randint(3, 8),
        random.choice(["#ff3978", "#ff8fb8", "#ffffff"])
    ])

frame = 0

def animate():
    global frame

    pen.clear()

    # Smooth heartbeat pulse
    pulse = 1 + 0.045 * math.sin(frame * 0.16)
    pulse += 0.018 * math.sin(frame * 0.32)

    # Draw layered heart from outside to inside
    for color, layer_scale in layers:
        draw_heart(10 * pulse * layer_scale, color)

    # Animate floating particles
    for particle in particles:
        x, y, size, color = particle

        pen.goto(x, y)
        pen.dot(size, color)

        # Move particles upward
        particle[1] += random.uniform(0.5, 1.8)

        if particle[1] > 370:
            particle[1] = -360
            particle[0] = random.randint(-420, 420)

    draw_message()

    screen.update()
    frame += 1

    # Schedule next animation frame
    screen.ontimer(animate, 30)

# Start animation
animate()
screen.mainloop()