# SnakeGame 🐍🌟

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<a href="https://github.com/jokernets/snake-game">
<img src="https://github.com/jokernets/snake-game/assets/165279911/2dac646b-5ff8-412e-a3c7-98fe8498f492"></a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>



<p align="center">
  <img src="https://img.shields.io/github/last-commit/jokernets/snake-game">
  <img src="https://img.shields.io/github/contributors/jokernets/snake-game">
  <img src="https://img.shields.io/github/issues/jokernets/snake-game">
  <img src="https://img.shields.io/github/stars/jokernets/snake-game">

</p>


## `Translation 🔗`

  
- [فارسی](https://github.com/jokernets/snake-game/blob/main/Translatin/FA.md)

- [عربية](https://github.com/jokernets/snake-game/blob/main/Translatin/AR.md)




Table of contents ✅✔
=================

<!--ts-->
   * [Installation](#installation)

   * [Anilayes Code📈](#analiys-code-)
     * [PART 1✔](#part-1)
     * [PART 2✔](#part-2)
     * [PART 3✔](#part-3)
     * [PART 4✔](#part-4)
  
   * [Mor Example💯](#more-examples-and-showcase-)
     * [Project Video📺](#video-image-of-the-app-)
    
   * [`CONNECT ME🌐👻`](#connect-me)
<!--te-->













# Installation

## Install the Library with pip:

```python
pip install Tk
pip install Pillow
pip install Random2
pip install String
```

Update existing installation:`pip3 install (YOUR LIBRARY) --upgrade`
(update as often as possible because this library is under active development)


# Analiys Code :


## `PART 1`:
1. **import libraries**:
     - The code starts by importing the required libraries:
  
         - `tkinter`: to create a graphical user interface (GUI).
         - `random': to generate random numbers.
         - `PIL.Image` and `ImageTk`: for working with images.

2. **Game Settings**:
     - The game settings are as follows:
         - `game_width` and `game_height`: dimensions of the game window (300x300).
         - `slowness': the speed of the snake's movement.
         - `snake_color`: Snake color.
         - `space_size' and `food_size': size of snake and food pieces.
         - `food_color`: food color.
         - `score`: initial score.
         - `keyboard_default`: default direction of snake movement.
         - `background`: GUI background color.

3. **window settings**:
     - The main window (`root`) is created using `Tk()`.
     - Window title, size and icon are set.
     - A logo image is loaded and displayed.
     - A canvas (`point_snake`) is created to display game elements.

4. **tags**:
     - Added a label with "SNAKE GAME" text in custom font.
     - A label showing the current score is added.

5. **main loop**:
     - The main event loop (`root.mainloop()`) keeps the GUI running.
     - The game window is placed in the middle of the screen.

6. **Analysis**:
     - The provided code creates a basic GUI of snake game using `tkinter`.
     - However, the actual game logic (snake movement, food production, crash detection, etc.) is missing.
     - To create a functional snake game, additional code must be added to manage snake movement, food production, and accident detection.

```python
#Importing libraries

from tkinter import * 
from tkinter import Tk
from random import randint
from PIL import Image , ImageTk
#________________________
# All game sizes Setting
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
#_______________________

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
 # point_snake
point_snake = Canvas(root, bg="#080808")
point_snake.grid(row=0, column=0, padx=50, pady=150)
#006400

#label_snake
try_again = Label(root, text="SNAKE GAME", font=("Snake Game Demo", 45),bg=background)
try_again.place(x=140,y=50)


# label_score
label_score = Label(root, text=f"Score: {score}", font=("Arial", 15), bg=background)
label_score.place(x=190,y=117)


root.mainloop()

```

<img src="https://github.com/jokernets/snake-game/assets/165279911/e85318d1-420a-4ca4-a04f-ce7f4590235f" width="300" height="300">

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

# Adding Define in project

## `PART 2`:

 1. **Snake class**:
     - In this class, the characteristics of the snake are defined:
         - `body_size`: number of snake parts.
         - `coordinates`: coordinates of snake parts (list of x and y pairs).
         - `squares': a list of snake squares on the game canvas.
     - At first, snake pieces with specified sizes and color are created in the game canvas.

2. **Food class**:
     - In this class, food specifications are defined:
         - The coordinates of the food are placed randomly in the game area.
         - A circle with a certain size and food color is created in the game canvas.

3. **game execution function (running)**:
     - In this function, the movement of the snake and the change of its coordinates are determined based on the direction of the user's movement.
     - If the snake reaches the coordinates of the food, the score will increase and the food will be removed.
     - Otherwise, the last piece of the snake is removed.
     - If the game is over, the function `game_over()` is called.
     - Otherwise, the `running` function will be called again with the specified delay.

4. **calling functions**:
     - At the end, ``Snake()'' and ``Food()'' functions are created and the ``running'' function is called with them.



```python
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
        
#call defines
snake = Snake()
food = Food()
running(snake,food)

```
<img src="https://github.com/jokernets/snake-game/assets/165279911/a2b89aef-2155-464e-95ef-719df1954d3b" width="300" height="300">


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

## `PART 3`:

This code is an **event handler** for keyboard keys. When the user presses a key such as "Up", "Down", "Left" or "Right", the function `keyboard_mood` is called and sets the variable `keyboard_default` to the name of the pressed key.

```python
# Keyboard event handler
def keyboard_mood(event):
    global keyboard_default
    if event.keysym in ["Up", "Down", "Left", "Right"]:
        keyboard_default = event.keysym.lower()

#running keyboard
root.bind("<Left>", keyboard_mood)
root.bind("<Right>", keyboard_mood)
root.bind("<Up>", keyboard_mood)
root.bind("<Down>", keyboard_mood)
```

# GAME OVER 👽

## `PART 4`:

1. `check_game_over(snake)` function:
     - This function receives the coordinates of the snake head.
     - The function returns `True' if the cap's coordinates are outside the game range (`game_width` and `game_height` range).
     - Also, returns `True' if the coordinates of the cap interfere with the coordinates of the snake's body.
     - Otherwise, it returns `False'.

2. `game_over()` function:
     - This function clears all points on the game screen.
     - Then it displays the text "GAME OVER" in the middle of the game screen with the font "GodOfWar" and size 40.

3. `quit_game()` function:
     - This function closes the game window and terminates the program.

The "Quit" button is also used to exit the game
```python

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

#quite game button
quit_btn= Button(root, text="Quit", command=quit_game, font=("Arial", 13),bd=0)
quit_btn.place(x=200,y=430)
```

<img src="https://github.com/jokernets/snake-game/assets/165279911/71c591e6-d3ca-468b-8b15-8479151eaf00" width="300" height="300">


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

## More Examples and Showcase 🎄👑

### Video image of the APP 📺


https://github.com/jokernets/snake-game/assets/165279911/3ffd4a92-cf4c-4144-907a-de6ccc753358



# `CONNECT ME`🌐👻

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammad-fallahnejad-849031293/" height="40" width="60" /></a>



