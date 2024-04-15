

#____________________________________________________________________________
#
#                         SNAKE GAME  PROJECT --4                   
#_____________________________________________________________________________

#Importing libraries
from tkinter import * 
from tkinter import Tk
from random import randint
from PIL import Image , ImageTk
#_______________
# All game sizes
game_width = 300
game_height = 300
slowness = 200
snake_color = "green"
space_size=10
food_size=15
food_color = 'red'
score = 0
keyboard_default = "down"
background="#008B00"
#__________________
class Snake:
    def __init__(self):
        self.body_size = 8
        self.coordinates = [[0, 0] for o in range(self.body_size)]
        self.squares = []
        
        for x, y in self.coordinates:
            square = point_snake.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)
            self.squares.append(square)

class Food:
    def __init__(self):
        x = randint(0, (game_width // space_size) - 1) * space_size
        y = randint(0, (game_height // space_size) - 1) * space_size
        self.coordinates = [x, y]
        point_snake.create_oval(x, y, x + space_size, y + space_size, fill=food_color,tag="food")

def running(snake,food):
    
    x,y=snake.coordinates[0]
    
    if keyboard_default == "up":
        y -= space_size
    elif keyboard_default == "down":
        y += space_size
    elif keyboard_default == "left":
        x -= space_size
    elif keyboard_default == "right":
        x += space_size
    
    snake.coordinates.insert(0, [x, y])
    
    square = point_snake.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)
    snake.squares.insert(0, square)
    
    # Find food in the coordinates
    if x == food.coordinates[0] and y == food.coordinates[1]:
        # Add score
        global score
        score += 1
        label_score.config(text=f"Score: {score}")
        # Delete food
        point_snake.delete("food")
        food=Food()
        
    # No food 
    else:
        del snake.coordinates[-1]
        point_snake.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_game_over(snake):
        game_over()
    
    else:
        root.after(slowness, running,snake,food)  # Call the running function again after a ...
        
# Keyboard event handler
def keyboard_mood(event):
    global keyboard_default
    if event.keysym in ["Up", "Down", "Left", "Right"]:
        keyboard_default = event.keysym.lower()


def check_game_over(snake):
    x , y =snake.coordinates[0]
    
    if x < 0 or x > game_width:
        return True
    if y < 0 or y > game_height:
        return True
    
    for i in snake.coordinates[1:]:
        if x == i[0] and y == i [1]:
            return True
        
    return False  

def game_over():
    point_snake.delete(ALL)
    point_snake.create_text(point_snake.winfo_width() /2 , point_snake.winfo_height()/2,
                            font=("GodOfWar",40),   
                                text="GAME OVER",fill="#8B1A1A")
    
def quit_game():
    root.destroy()


# Window -- root --setup
root = Tk()
root.title("SNAKE GAME")
root.resizable(False, False)
root.configure(bg=background)
root.geometry("500x500")

root.geometry("500x500+{}+{}".format(root.winfo_screenwidth() // 2 -270, root.winfo_screenheight() // 2 - 270))

#icon Edit
img=PhotoImage(file="c:/project_python/Snake game/snake game/snake_2.png")
root.iconphoto(True,img)

#logo 
image = Image.open("c:/project_python/Snake game/snake game/logo.png")
img_resized = image.resize((80, 80))
img_photo = ImageTk.PhotoImage(img_resized)

contact_label = Label(root, image=img_photo, bg=background, width=0)
contact_label.place(x=50, y=33)

#label_snake
try_again = Label(root, text="SNAKE GAME", font=("Snake Game Demo", 45),bg=background)
try_again.place(x=140,y=50)

# point_snake
point_snake = Canvas(root, bg="#080808")
point_snake.grid(row=0, column=0, padx=50, pady=150)
#006400
# label_score
label_score = Label(root, text=f"Score: {score}", font=("Arial", 15), bg=background)
label_score.place(x=190,y=117)

# quit game 
quit_btn= Button(root, text="Quit", command=quit_game, font=("Arial", 13),bd=0)
quit_btn.place(x=200,y=430)

#running keyboard
root.bind("<Left>", keyboard_mood)
root.bind("<Right>", keyboard_mood)
root.bind("<Up>", keyboard_mood)
root.bind("<Down>", keyboard_mood)

#call defines
snake = Snake()
food = Food()
running(snake,food)

root.mainloop()

#Connect Me !

#GitHub : jokernets

#Email : joker.until33@gmail.com




