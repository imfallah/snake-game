
# بازی مار🐍🌟

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

<a href="https://github.com/jokernets/snake-game">
<img src="1.png"></a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>




## ترجمه 🔗
[English](README.md)




فهرست مطالب ✅✔
=================

<!--ts-->
   * [نصب کن ](#%D9%86%D8%B5%D8%A8-%D9%88-%D8%B1%D8%A7%D9%87-%D8%A7%D9%86%D8%AF%D8%A7%D8%B2%DB%8C)

   * [آنالیز کد 📈 ](#%D8%A2%D9%86%D8%A7%D9%84%DB%8C%D8%B2-%DA%A9%D8%AF)
     * [پارت 1✔](#%D9%BE%D8%A7%D8%B1%D8%AA-1)
     * [پارتت 2✔](#%D9%BE%D8%A7%D8%B1%D8%AA-2)
     * [پارت 3✔](#%D9%BE%D8%A7%D8%B1%D8%AA-3)
     * [پارت 4✔](#%D9%BE%D8%A7%D8%B1%D8%AA4)
  
   * [ویترین💯](#%D9%86%D9%85%D9%88%D9%86%D9%87-%D9%87%D8%A7%DB%8C-%D8%A8%DB%8C%D8%B4%D8%AA%D8%B1-%D9%88-%D9%88%DB%8C%D8%AA%D8%B1%DB%8C%D9%86-)
     * [ویدیو از پروژه📺](#%D8%AA%D8%B5%D9%88%DB%8C%D8%B1-%D9%88%DB%8C%D8%AF%DB%8C%D9%88%DB%8C%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-)
<!--te-->

## نصب و راه اندازی
### ماژول را با پیپ نصب کنید:
```python
pip install Tkinter
pip install Pillow
pip install random
```

#### نصب موجود را به روز کنید: pip3 install (کتابخانه شما) -- ارتقاء دهید (تا حد امکان به روز رسانی کنید زیرا این کتابخانه در حال توسعه فعال است)

# آنالیز کد📈📉:

# `پارت 1`:

1. **وارد کردن کتابخانه‌ها**:
    - کد با وارد کردن کتابخانه‌های مورد نیاز آغاز می‌شود:
  
        - `tkinter`: برای ایجاد رابط کاربری گرافیکی (GUI).
        - `random`: برای تولید اعداد تصادفی.
        - `PIL.Image` و `ImageTk`: برای کار با تصاویر.

2. **تنظیمات بازی**:
    - تنظیمات بازی به شرح زیر است:
        - `game_width` و `game_height`: ابعاد پنجره‌ی بازی (300x300).
        - `slowness`: سرعت حرکت مار.
        - `snake_color`: رنگ مار.
        - `space_size` و `food_size`: اندازه‌ی قطعات مار و غذا.
        - `food_color`: رنگ غذا.
        - `score`: امتیاز اولیه.
        - `keyboard_default`: جهت پیش‌فرض حرکت مار.
        - `background`: رنگ پس‌زمینه‌ی GUI.

3. **تنظیمات پنجره**:
    - پنجره‌ی اصلی (`root`) با استفاده از `Tk()` ایجاد می‌شود.
    - عنوان پنجره، اندازه و آیکون تنظیم می‌شوند.
    - یک تصویر لوگو بارگذاری و نمایش داده می‌شود.
    - یک کانواس (`point_snake`) برای نمایش عناصر بازی ایجاد می‌شود.

4. **برچسب‌ها**:
    - یک برچسب با متن "SNAKE GAME" با فونت سفارشی اضافه می‌شود.
    - یک برچسب نمایش امتیاز فعلی اضافه می‌شود.

5. **حلقه‌ی اصلی**:
    - حلقه‌ی رویداد اصلی (`root.mainloop()`) GUI را در حالت اجرا نگه می‌دارد.
    - پنجره‌ی بازی در وسط صفحه‌ی نمایش قرار می‌گیرد.

6. **تحلیل**:
    - کد ارائه شده یک GUI ابتدایی از بازی مار استفاده کننده از `tkinter` را ایجاد می‌کند.
    - با این حال، منطق واقعی بازی (حرکت مار، تولید غذا، تشخیص تصادف و غیره) وجود ندارد.
    - برای ایجاد یک بازی مار کارایی، کد اضافی برای مدیریت حرکت مار، تولید غذا و تشخیص تصادف باید اضافه شود.


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

<img src="https://github.com/jokernets/snake-game/assets/165279911/1928ea5c-26ee-4079-bdb4-34af515072c7" width="300" height="300">

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

# افزودن تابع در پروژه

## `پارت 2`:

1. **کلاس مار (Snake)**:
    - در این کلاس، مشخصات مار تعریف می‌شود:
        - `body_size`: تعداد قطعات مار.
        - `coordinates`: مختصات قطعات مار (لیستی از جفت‌های x و y).
        - `squares`: لیستی از مربع‌های مار در کانواس بازی.
    - در ابتدا، قطعات مار با اندازه‌ها و رنگ مشخص شده، در کانواس بازی ایجاد می‌شوند.

2. **کلاس غذا (Food)**:
    - در این کلاس، مشخصات غذا تعریف می‌شود:
        - مختصات غذا به صورت تصادفی در محدوده‌ی بازی قرار می‌گیرد.
        - یک دایره با اندازه‌ی مشخص و رنگ غذا در کانواس بازی ایجاد می‌شود.

3. **تابع اجرای بازی (running)**:
    - در این تابع، حرکت مار و تغییر مختصات آن بر اساس جهت حرکت کاربر تعیین می‌شود.
    - اگر مار به مختصات غذا برسد، امتیاز افزایش می‌یابد و غذا حذف می‌شود.
    - در غیر این صورت، آخرین قطعه‌ی مار حذف می‌شود.
    - اگر بازی تمام شود، تابع `game_over()` فراخوانی می‌شود.
    - در غیر این صورت، تابع `running` با تاخیر مشخص دوباره فراخوانی می‌شود.

4. **فراخوانی توابع**:
    - در انتها، توابع `Snake()` و `Food()` ایجاد می‌شوند و تابع `running` با آن‌ها فراخوانی می‌شود.




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
<img src="https://github.com/jokernets/snake-game/assets/165279911/4e919e64-8848-4d9c-9ef7-e452135ac6ce" width="300" height="300">

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>



## `پارت 3`:
 این کد یک **event handler** برای کلیدهای کیبورد است. وقتی کاربر کلیدهایی مانند "Up"، "Down"، "Left" یا "Right" را فشار دهد، تابع `keyboard_mood` فراخوانی می‌شود و متغیر `keyboard_default` را با نام کلید فشرده شده تنظیم می‌کند
 
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

# گیم آور بسازیم 👽

## `پارت4`:

1. تابع `check_game_over(snake)`:
    - این تابع مختصات سرپوش مار را دریافت می‌کند.
    - اگر مختصات سرپوش خارج از محدوده‌ی بازی (بازه‌ی `game_width` و `game_height`) قرار گیرد، تابع `True` برمی‌گرداند.
    - همچنین، اگر مختصات سرپوش با مختصات بدن مار تداخل داشته باشد، نیز `True` برمی‌گرداند.
    - در غیر این صورت، `False` برمی‌گرداند.

2. تابع `game_over()`:
    - این تابع تمامی نقاط روی صفحه‌ی بازی را پاک می‌کند.
    - سپس متن "GAME OVER" را در وسط صفحه‌ی بازی با فونت "GodOfWar" و اندازه‌ی 40 نمایش می‌دهد.

3. تابع `quit_game()`:
    - این تابع پنجره‌ی بازی را بسته و برنامه را خاتمه می‌دهد.

دکمه‌ی "Quit" نیز برای خروج از بازی استفاده می شود 

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
<img src="https://github.com/jokernets/snake-game/assets/165279911/f755f6a7-5a1d-4f41-a4eb-b0ebf7921ac5" width="300" height="300">

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

# نمونه های بیشتر و ویترین 🎄👑

## تصویر ویدیویی برنامه 📺
https://github.com/jokernets/snake-game/assets/165279911/62642493-ac95-4706-b8ee-0c1e108c0047


<a herf="buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>





