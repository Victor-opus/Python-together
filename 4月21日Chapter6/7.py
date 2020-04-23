#coding:utf-8
import easygui

name = easygui.enterbox("Enter your name")
room = easygui.enterbox("Enter your room num")
street = easygui.enterbox("Enter your street")
region = easygui.enterbox("Enter your  region")

whole_address = name + '\n' + room + '\n' +street + '\n' + region
easygui.msgbox(whole_address)
