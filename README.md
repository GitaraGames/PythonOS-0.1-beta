# PythonOS-0.1-beta
Python OS version 0.1 (BETA)

Данный проект представляет собой не настоящую
операционную систему, предназначенную для
работы с файлами типа TXT. А другие
функции типа воспроизведения аудио файл,
подсчёт примера на калькуляторе и т.д.
появяться в новых версиях системы.

#__НАСТРОЙКИ СИСТЕМЫ__#
Чтобы настроить систему под себя, надо
зайти в папку ```system```, а далее
в файл ```settings.init```.
В нём Вы можете указать настройки
системы типа язык, размеры экрана,
цвета интерфейса.

```
self.color = "dark blue"
self.desktop_color = "dark blue"
self.buttons_color = "light blue"
self.buttons_text_color = "black"
self.width = 700
self.height = 400
self.language = "en/en" # (en/en) or (ru/ru)
```

#___ДЛЯ РАЗРАБОТЧИКА___#
Чтобы создать своё приложение, необходимо
в папке PythonOS рядом с файлом main.py
создать новую папку название которой будет
названием вашего приложения (имя на английском).
В этой папке создайте файл ```__init__.py```, в
нём напишите:

```
import main
from tkinter import *

app = main.App()
window = app.window()
text = Label(window, text="Hello World!")
text.place(x=0, y=50)
window.configure(width=200, height=200)
```

Данный код поможет Вам создать своё приложение.
Далее в папке ```menu``` зайдите в файл ```__init__.py```
И вставьте в конец следующий код:
```
button_test = Button(window, text="Test App", command=lambda:exec(open("Test App/__init__.py", "r").read()))
button_test.pack()
```
Вместо ```Test App``` везде укажите название 
своего приложения, первый случай:
```text="Test App"``` - это имя приложения
в меню системы, второе: ```open("Test App/__init__.py", "r")``` - 
это имя папки в которой лежит Ваше приложение.
После запустите систему, откройте меню и
Вы увидите своё приложение.
