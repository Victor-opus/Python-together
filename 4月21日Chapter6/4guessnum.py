# -*- coding: utf-8 -*-
import random,easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("""你好，我是猜数机器人，接下来我要和你玩猜数游戏！
这个数字是1-99，你将有6次机会，加油，奥利干！！""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("你的猜测是什么呢？")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " 是太小了！")
    elif guess > secret:
        easygui.msgbox(str(guess) + " 是太大了！")
    tries+=1
if guess == secret:
    easygui.msgbox("你真棒，答对了！！")
else:
    easygui.msgbox("没找到也没关系，下次继续。答案是 " + str(secret))
