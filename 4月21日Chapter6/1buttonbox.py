import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
                           choices = ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " + flavor)
