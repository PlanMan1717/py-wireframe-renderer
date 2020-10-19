import turtle
import json

# Delta Y. Use to pan image along Y axis if it does not fit.
dy = -0

# Create Turtle Class
t = turtle.Turtle()

# Load and parse the JSON file.
string_obj = open("./test9.json", 'r')
obj = json.loads(string_obj.read())

# Create Placeholders
vertices = []
lines = []

# Create list of vertices and their positions
for vert in obj["vertices"]:
    vertices.append(vert[0])

# Create list of edges and their delimiting vertices
for line in obj["edges"]:
    lines.append(line[-1])

# Set up turtle
t.speed(0)
t.penup()
t.hideturtle()
t._delay(0)

# More variables for the perspective formula
focalL = 1.5

# Scale factor. Larger --> bigger object
a = 500

# Define functions


def plot(x, y):
    """Place a dot at (X, Y) on the screen."""
    t.goto(x, y + dy)
    t.dot(3)


def plotline(idx1, idx2):
    """Creates a line between two specified vertices."""
    t.goto(x(vertices[idx1][0], vertices[idx1][1]), x(vertices[idx1][2], vertices[idx1][1]) + dy)
    t.pendown()
    t.goto(x(vertices[idx2][0], vertices[idx2][1]), x(vertices[idx2][2], vertices[idx2][1]) + dy)
    t.penup()


def x(x: float, d: float) -> float:
    """
    Perform perspective formula on a number.
    
    out = scaleFactor \u2022 input \u2022 (focalLength \u00f7 | focalLength + 5 - distanceFromCamera|)
    
    Arguments:
    - x : Input
    - d : Distance from camera (usually Y-Coordinate)
    """
    return a * x * (focalL / abs(focalL + 5 - d))


# Controls whether the script should plot vertices before the edges.
# It is not required, but it adds about ~30s to the render time.
# True : Yes
# False : No

shouldPlotVerts = True

# Iterate and plot vertices if allowed

if shouldPlotVerts:
    for vert in vertices:
        plot(x(vert[0], vert[1]), x(vert[2], vert[1]))
else:
    pass

# Iterate and plot lines

for line in lines:
    plotline(line[0], line[1])

# Wait for user to press Enter key, then exit.
input()