import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                            default = 'Chocolate')
easygui.msgbox("You entered " + flavor)
