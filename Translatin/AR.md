
# لعبة الثعبان 🐍🌟

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<a href="https://github.com/jokernets/snake-game">
<img src="1.png"></a>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

## الترجمة 🔗




## جدول المحتويات ✅✔



<!--ts-->

 * [تثبیت](#%D8%AA%D8%AB%D8%A8%D9%8A%D8%AA
)
 * [كود التحليل 📈](#%D9%83%D9%88%D8%AF-%D8%A7%D9%84%D8%AA%D8%AD%D9%84%D9%8A%D9%84-)
   * [الجزء 1✔](#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-1)
   * [الجزء 2✔](#%D8%A7%D9%84%D8%AC%D8%B2%D8%A12
)
   * [الجزء 3✔](#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-3)
   * [الجزء4✔](#%D8%A7%D9%84%D8%AC%D8%B2%D8%A1-4)
  
* [المزيد من الأمثلة💯](#%D8%A7%D9%84%D9%85%D8%B2%D9%8A%D8%AF-%D9%85%D9%86-%D8%A7%D9%84%D8%A3%D9%85%D8%AB%D9%84%D8%A9-%D9%88%D8%A7%D9%84%D8%B9%D8%B1%D8%B6-)
   * [مشروع فيديو📺](#%D8%B5%D9%88%D8%B1%D8%A9-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%84%D9%84%D8%AA%D8%B7%D8%A8%D9%8A%D9%82-)
<!--te-->





# تثبيت

## تثبيت الوحدة مع النقطة:

```python
pip install Tkinter
pip install Pillow
pip install Random2
pip install String
```

### تحديث التثبيت الحالي:`pip3 install (YOUR LIBRARY) --upgrade` (التحديث قدر الإمكان لأن هذه المكتبة قيد التطوير النشط)


# كود التحليل :


## `الجزء 1`:
1. **مكتبات الاستيراد**:
      - يبدأ الكود باستيراد المكتبات المطلوبة:
  
          - `tkinter`: لإنشاء واجهة مستخدم رسومية (GUI).
          - `عشوائي': لتوليد أرقام عشوائية.
          - `PIL.Image` و`ImageTk`: للعمل مع الصور.

2. **إعدادات اللعبة**:
      - إعدادات اللعبة هي كما يلي:
          - `عرض_اللعبة` و `ارتفاع_اللعبة`: أبعاد نافذة اللعبة (300 × 300).
          - "البطء": سرعة حركة الثعبان.
          - `لون_الثعبان`: لون الثعبان.
          - "حجم_المساحة" و"حجم_الطعام": حجم الثعبان وقطع الطعام.
          - `لون_الطعام`: لون طعام.
          - `النتيجة`: النتيجة الأولية.
          - `keyboard_default`: الاتجاه الافتراضي لحركة الثعبان.
          - `الخلفية`: لون خلفية واجهة المستخدم الرسومية.

3. **إعدادات النافذة**:
      - يتم إنشاء النافذة الرئيسية (`الجذر`) باستخدام `Tk()`.
      - تم تعيين عنوان النافذة وحجمها وأيقونتها.
      - يتم تحميل وعرض صورة الشعار.
      - يتم إنشاء لوحة قماشية (`point_snake`) لعرض عناصر اللعبة.

4. **العلامات**:
      - تمت إضافة تسمية بنص "SNAKE GAME" بخط مخصص.
      - تتم إضافة تسمية توضح النتيجة الحالية.

5. **الحلقة الرئيسية**:
      - حلقة الحدث الرئيسية (`root.mainloop()`) تحافظ على تشغيل واجهة المستخدم الرسومية.
      - يتم وضع نافذة اللعبة في منتصف الشاشة.

6. **التحليل**:
      - يقوم الكود المقدم بإنشاء واجهة مستخدم رسومية أساسية للعبة الثعبان باستخدام "tkinter".
      - ومع ذلك، فإن منطق اللعبة الفعلي (حركة الثعبان، وإنتاج الغذاء، واكتشاف الأعطال، وما إلى ذلك) مفقود.
      - لإنشاء لعبة ثعبان وظيفية، يجب إضافة كود إضافي لإدارة حركة الثعبان وإنتاج الغذاء واكتشاف الحوادث.



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

# إضافة تعريف في المشروع

## `الجزء2`:

1. **فئة الثعبان**:
      - تم في هذا الفصل تحديد خصائص الثعبان:
          - `حجم_الجسم`: عدد أجزاء الثعبان.
          - `الإحداثيات`: إحداثيات أجزاء الثعبان (قائمة أزواج x و y).
          - "المربعات": قائمة بمربعات الثعبان على لوحة اللعبة.
      - في البداية، يتم إنشاء قطع الثعبان ذات الأحجام والألوان المحددة في لوحة اللعبة.

2. **فئة الطعام**:
      - يتم في هذا الفصل تحديد المواصفات الغذائية:
          - يتم وضع إحداثيات الطعام بشكل عشوائي في منطقة اللعبة.
          - يتم إنشاء دائرة بحجم معين ولون طعام معين في لوحة اللعبة.

3. ** وظيفة تنفيذ اللعبة (تشغيل) **:
      - في هذه الوظيفة يتم تحديد حركة الثعبان وتغير إحداثياته بناء على اتجاه حركة المستخدم.
      - إذا وصل الثعبان إلى إحداثيات الطعام، فستزيد النتيجة وسيتم إزالة الطعام.
      - وإلا تتم إزالة آخر قطعة من الثعبان.
      - إذا انتهت اللعبة، يتم استدعاء الدالة `game_over()`.
      - وبخلاف ذلك، سيتم استدعاء وظيفة "التشغيل" مرة أخرى مع التأخير المحدد.

4. **وظائف الاتصال**:
      - في النهاية، يتم إنشاء الدالتين ``Snake()'' و``Food()'' ويتم استدعاء الدالة ``running'' معهما.


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

## `الجزء 3`:

هذا الرمز هو **معالج الأحداث** لمفاتيح لوحة المفاتيح. عندما يضغط المستخدم على مفتاح مثل "أعلى" أو "أسفل" أو "يسار" أو "يمين"، يتم استدعاء الوظيفة "keyboard_mood" وتعيين المتغير "keyboard_default" على اسم المفتاح المضغوط.
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


# انتهت اللعبة 👽

## `الجزء 4`:

1. وظيفة `check_game_over(snake)`:
      - تستقبل هذه الوظيفة إحداثيات رأس الثعبان.
      - تقوم الدالة بإرجاع "صحيح" إذا كانت إحداثيات الحد الأقصى خارج نطاق اللعبة (نطاق "عرض_اللعبة" و"ارتفاع_اللعبة").
      - يتم أيضًا إرجاع "صحيح" إذا كانت إحداثيات الغطاء تتداخل مع إحداثيات جسم الثعبان.
      - وإلا فسيتم إرجاع "خطأ".

2. وظيفة `game_over()`:
      - تقوم هذه الوظيفة بمسح جميع النقاط الموجودة على شاشة اللعبة.
      - ثم يعرض النص "GAME OVER" في منتصف شاشة اللعبة بالخط "GodOfWar" وحجمه 40.

3. وظيفة `quit_game()`:
      - تقوم هذه الوظيفة بإغلاق نافذة اللعبة وإنهاء البرنامج.

يتم استخدام زر "إنهاء" أيضًا للخروج من اللعبة

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



# المزيد من الأمثلة والعرض 🎄👑


## صورة فيديو للتطبيق 📺

https://github.com/jokernets/snake-game/assets/165279911/62642493-ac95-4706-b8ee-0c1e108c0047


<a herf="buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>
