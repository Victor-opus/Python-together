import easygui
fahrenheit = easygui.enterbox("Enter the Fahrenheit you want to convert ")
celsius = (int(fahrenheit) - 32) * 5.0 / 9
easygui.msgbox("The celsius is " + str(celsius))
