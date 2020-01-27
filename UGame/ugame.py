#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Импорт библиотек
from pygame import mixer
from tkinter import *
import time
import threading
import random

#Глобальные переменные
curMI = 1 #Текущий пункт меню
nosRul = 15 #Максимальное количество строк в ПРАВИЛАХ на экране
curRpage = 1 #Номер текущей страницы в ПРАВИЛАХ
maxRlines = 1 #Максимальное количество строк в тексте ПРАВИЛ
textrules = "Hellow" #Текст ПРАВИЛ
maxlevelgold = 0 #Максимальное количество золота на уровне
curlevelgold = 0 #Собранное количество золота на уровне 
fireright = True #Направление огня
curlevel = 1 #Текущий уровень
maxlevel = 33 #Максимальный уровень
curuliki = 0 #Текущие улики
maxuliki = 0 #Максимальные улики
curznanija = 0 #Текущие знания
maxznanija = 0 #Максимальные знания
curadvokat = 0 #Текущие адвокаты
maxadvokat = 0 #Максимальные адвокаты
cursud = 0 #Текущие судьи
maxsud = 0 #Максимальные судьи
curdela = 0 #Текущие дела
maxdela = 0 #Максимальные дела
curpolice = 0 #Текущие полицейские
maxpolice = 0 #Максимальные полицейские

hUp = "q" #Клавиша вверх
hDown = "a" #Клавиша вниз
hLeft = "o" #Клавиша влево
hRight = "p" #Клавиша вправо
hFire = " " #Клавиша ОГОНЬ
hJump = "j" #Клавиша прыжок
#Матрица текущего игрового поля
gfield = [["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"],
    ["S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"]] #Пустой массив игрового поля
px = 1 #Координата Х персонажа
py = 13 #Координата У персонажа
pthread = [] #Массив потоков
pthreadlive = False #Флаг потоки живы
maxthread = 0 #Количество открытых потоков
globalgameover = False #Флаг окончания игры

#Функция движения монстров в потоках
def moveotherpers(xcoord,ycoord,ptype):
    upflag = False
    menlive = True
    mx = xcoord
    my = ycoord
    global canvas
    global bgrd
    global police
    global gfield
    global curpolice
    global px
    global py
    global pthreadlive
    global sud
    global cursud
    global advokat
    global curadvokat
    if ptype == 1:
        #if police
        while menlive == True:
            if pthreadlive == False:
                menlive = False
            if (px == mx) and (py == my):
                mixer.music.load('hdie.ogg')
                mixer.music.play()
                menlive = False
                gameover()
            if upflag == True:
                if (gfield[my-1][mx] == "S") or (gfield[my-1][mx] == "f"):
                    if gfield[my-1][mx] == "f":
                        curpolice = curpolice + 1
                        showstatistic()
                        testlevel()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        mixer.music.load('pdie.ogg')
                        mixer.music.play()
                        menlive = False
                    else:    
                        gfield[my][mx] = "S"
                        time.sleep(0.3)
                        root.update()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        my = my - 1
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=police)
                        if my <= 0:
                            upflag = False
                else:
                    upflag = False
            else:
                if (gfield[my+1][mx] == "S") or (gfield[my+1][mx] == "f"):
                    if gfield[my+1][mx] == "f":
                        curpolice = curpolice + 1
                        showstatistic()
                        testlevel()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        mixer.music.load('pdie.ogg')
                        mixer.music.play()
                        menlive = False
                    else:
                        gfield[my][mx] = "S"
                        time.sleep(0.3)
                        root.update()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        my = my + 1
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=police)
                        if my >= 14:
                            upflag = True
                else:
                    upflag = True
    elif ptype == 2:
        #if sud
        while menlive == True:
            if pthreadlive == False:
                menlive = False
            if (px == mx) and (py == my):
                mixer.music.load('hdie.ogg')
                mixer.music.play()
                menlive = False
                gameover()
            if upflag == True:
                if (gfield[my][mx-1] == "S") or (gfield[my][mx-1] == "f"):
                    if gfield[my][mx-1] == "f":
                        cursud = cursud + 1
                        showstatistic()
                        testlevel()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        mixer.music.load('pdie.ogg')
                        mixer.music.play()
                        menlive = False
                    else:    
                        gfield[my][mx] = "S"
                        time.sleep(0.3)
                        root.update()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        mx = mx - 1
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=sud)
                        if mx <= 0:
                            upflag = False
                else:
                    upflag = False
            else:
                if (gfield[my][mx+1] == "S") or (gfield[my][mx+1] == "f"):
                    if gfield[my][mx+1] == "f":
                        cursud = cursud + 1
                        showstatistic()
                        testlevel()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        mixer.music.load('pdie.ogg')
                        mixer.music.play()
                        menlive = False
                    else:
                        gfield[my][mx] = "S"
                        time.sleep(0.3)
                        root.update()
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                        mx = mx + 1
                        canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=sud)
                        if mx >= 19:
                            upflag = True
                else:
                    upflag = True
    elif ptype == 3:
        #if advokat
        while menlive == True:
            time.sleep(5)
            root.update()
            if pthreadlive == False:
                menlive = False
            if (px == mx) and (py == my):
                mixer.music.load('hdie.ogg')
                mixer.music.play()
                menlive = False
                gameover()
            newx = random.randint(0,19)
            newy = random.randint(0,14)
            if gfield[newy][newx] == "S":
                canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                gfield[my][mx] = "S"
                my = newy
                mx = newx
                gfield[my][mx] = "I"
                canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=advokat)    
            elif gfield[my][mx] == "f":
                curadvokat = curadvokat + 1
                showstatistic()
                testlevel()
                canvas.create_image(80+mx*32,60+my*32, anchor=NW, image=bgrd)
                mixer.music.load('pdie.ogg')
                mixer.music.play()         
            
#Функция закрывает все потоки
def closeallthread():
    global pthreadlive
    global maxthread
    global pthread
    pthreadlive = False
    nn = 0
    while nn < maxthread:
        while pthread[nn].is_alive() == True:
            root.update()
        nn = nn +1
    maxthread = 0
    pthread.clear()
    
#Функция окончания игры
def gameover():
    global curlevel
    global gover
    global canvas
    global globalgameover
    globalgameover = True
    root.bind('<Key>', nokey)
    time.sleep(1)
    canvas.create_image(200,60, anchor=NW, image=gover)

#Функция проверяет глобальный конец игры
def testgover():
    global globalgameover
    xflag = True
    while xflag == True:
        if globalgameover == True:
            closeallthread()
            globalgameover = False

#Функция теста уровня на предмет выполнения всех задач уровня, если все исполнено - открываем дверь
def testlevel():
    global maxlevelgold
    global curlevelgold
    global canvas
    global gfield
    global dooro
    global curadvokat
    global maxadvokat
    global curuliki
    global maxuliki
    global curznanija
    global maxznanija
    global cursud
    global maxsud
    global curdela
    global maxdela
    global curpolice
    global maxpolice
    if curlevelgold > maxlevelgold:
        curlevelgold = maxlevelgold
    if curuliki > maxuliki:
        curuliki = maxuliki
    if curznanija > maxznanija:
        curznanija = maxznanija
    if curadvokat > maxadvokat:
        curadvokat = maxadvokat
    if cursud > maxsud:
        cursud = maxsud
    if curdela > maxdela:
        curdela = maxdela
    if curpolice > maxpolice:
        curpolice = maxpolice
    if (maxlevelgold == curlevelgold) and (maxuliki == curuliki) and (maxznanija == curznanija) and (maxadvokat == curadvokat) and (maxsud == cursud) and (maxdela == curdela) and (maxpolice == curpolice):
        n1 = 0
        mixer.music.load('nlev.ogg')
        mixer.music.play()
        while n1 <= 19:
            n2 = 0
            while n2 <=14:
                if gfield[n2][n1] == "C":
                    gfield[n2][n1] = "J"
                    canvas.create_image(80+n1*32,60+n2*32, anchor=NW, image=dooro)
                n2 = n2 + 1
            n1 = n1 + 1

#Функция опроса клавиатуры при Game over
def nokey(event):
    global curlevel
    if ord(event.char) == 27:
        curlevel = 1
        mainscreen()
        showmenu(1)
        root.bind('<Key>', key)

#Функция опроса клавиатуры в главном меню
def key(event):
    global curMI
    if ord(event.char) == 27:
        mixer.music.stop()
    if ord(event.char) == 32:
        curMI = curMI + 1
    if curMI > 4:
        curMI = 1
    showmenu(curMI)
    if ord(event.char) == 13:
        if curMI == 4:
            mixer.music.stop()
            exitapp()
        if curMI == 2:
            mixer.music.stop()
            aboutscreen()
            root.bind('<Key>', keyabout)
        if curMI == 3:
            mixer.music.stop()
            setscreen()
            root.bind('<Key>', keyset)
        if curMI == 1:
            mixer.music.stop()
            gamescreen()
            root.bind('<Key>', keygame)

#Функция опроса клавиатуры в меню установок
def keyset(event):
    if ord(event.char) == 27:
        mainscreen()
        showmenu(3)
        root.bind('<Key>', key)

#Функция опроса клавиатуры в игре
def keygame(event):
    global px
    global py
    global canvas
    global gfield
    global bgrd
    global pright
    global pleft
    global lineup
    global goldo
    global fireright
    global fireball
    global curlevelgold
    global curlevel
    global maxlevel
    global curadvokat
    global maxadvokat
    global ulika
    global curuliki
    global curdela
    global curznanija
    global win
    global globalgameover
    global yww
    if ord(event.char) == 27:
        closeallthread()
        mainscreen()
        showmenu(1)
        root.bind('<Key>', key)
    elif event.char == "!":
        curlevel = maxlevel - 1
    elif event.char == hRight:
        if (gfield[py][px + 1] == "S") or (gfield[py][px + 1] == "L"):
            if gfield[py][px] == "S":
                canvas.create_image(80+px*32,60+py*32, anchor=NW, image=bgrd)
            elif gfield[py][px] == "L":
                canvas.create_image(80+px*32,60+py*32, anchor=NW, image=lineup)
            px = px + 1
            canvas.create_image(80+px*32,60+py*32, anchor=NW, image=pright)
            fireright = True
        elif (gfield[py][px+1]) == "G":
            mixer.music.load('coin.ogg')
            mixer.music.play()
            canvas.create_image(80+(px+1)*32,60+py*32, anchor=NW, image=goldo)
            gfield[py][px+1] = "O"
            curlevelgold = curlevelgold + 1
            showstatistic()
            testlevel()
        elif (gfield[py][px+1]) == "E":
            mixer.music.load('coin.ogg')
            mixer.music.play()
            canvas.create_image(80+(px+1)*32,60+py*32, anchor=NW, image=bgrd)
            gfield[py][px+1] = "S"
            curznanija = curznanija + 1
            showstatistic()
            testlevel()
        elif (gfield[py][px+1]) == "Z":
            mixer.music.load('coin.ogg')
            mixer.music.play()
            canvas.create_image(80+(px+1)*32,60+py*32, anchor=NW, image=ulika)
        elif (gfield[py][px+1]) == "J":
            curlevel = curlevel + 1
            closeallthread()
            if curlevel <= maxlevel:
                gamescreen()
            else:
                curlevel = 1
                globalgameover = True
                root.bind('<Key>', nokey)
                canvas.create_image(190,20, anchor=NW, image=win)
                canvas.create_image(105,300, anchor=NW, image=yww)
                mixer.music.load('yw.ogg')
                mixer.music.play()
    elif event.char == hLeft:
        if (gfield[py][px - 1] == "S") or (gfield[py][px - 1] == "L"):
            if gfield[py][px] == "S":
                canvas.create_image(80+px*32,60+py*32, anchor=NW, image=bgrd)
            elif gfield[py][px] == "L":
                canvas.create_image(80+px*32,60+py*32, anchor=NW, image=lineup)
            px = px - 1
            canvas.create_image(80+px*32,60+py*32, anchor=NW, image=pleft)
            fireright = False
        elif (gfield[py][px-1]) == "G":
            mixer.music.load('coin.ogg')
            mixer.music.play()
            canvas.create_image(80+(px-1)*32,60+py*32, anchor=NW, image=goldo)
            gfield[py][px-1] = "O"
            curlevelgold = curlevelgold + 1
            showstatistic()
            testlevel()
        elif (gfield[py][px-1]) == "E":
            mixer.music.load('coin.ogg')
            mixer.music.play()
            canvas.create_image(80+(px-1)*32,60+py*32, anchor=NW, image=bgrd)
            gfield[py][px-1] = "S"
            curznanija = curznanija + 1
            showstatistic()
            testlevel()
        elif (gfield[py][px-1]) == "Z":
            mixer.music.load('coin.ogg')
            mixer.music.play()
            canvas.create_image(80+(px-1)*32,60+py*32, anchor=NW, image=ulika)
        elif (gfield[py][px-1]) == "J":
            curlevel = curlevel + 1
            closeallthread()
            if curlevel <= maxlevel:
                gamescreen()
            else:
                curlevel = 1
                globalgameover = True
                root.bind('<Key>', nokey)
                canvas.create_image(190,20, anchor=NW, image=win)
                canvas.create_image(105,300, anchor=NW, image=yww)
                mixer.music.load('yw.ogg')
                mixer.music.play()
    elif event.char == hUp:
        if gfield[py][px] == "L":
            canvas.create_image(80+px*32,60+py*32, anchor=NW, image=lineup)
            py = py - 1
            canvas.create_image(80+px*32,60+py*32, anchor=NW, image=pleft)    
    elif event.char == hDown:
        if ((gfield[py][px] == "L") or (gfield[py][px] == "S")) and (gfield[py+1][px] == "L"):
            if gfield[py][px] == "S":
                canvas.create_image(80+px*32,60+py*32, anchor=NW, image=bgrd)
            elif gfield[py][px] == "L":
                canvas.create_image(80+px*32,60+py*32, anchor=NW, image=lineup)
            py = py + 1
            canvas.create_image(80+px*32,60+py*32, anchor=NW, image=pleft)
    elif event.char == hFire:
        if fireright == True:
            nn=px + 1
            mixer.music.load('fireball.ogg')
            mixer.music.play()
            while nn <= 19:
                if (gfield[py][nn] == "S") or (gfield[py][nn] == "f"):
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=fireball)
                    root.update()
                    time.sleep(0.2)
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    gfield[py][nn] = "S"
                elif gfield[py][nn] == "O":
                    gfield[py][nn] = "S"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 19
                elif gfield[py][nn] == "Z":
                    gfield[py][nn] = "S"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 19
                    curuliki = curuliki + 1
                    showstatistic()
                    testlevel()
                elif gfield[py][nn] == "V":
                    gfield[py][nn] = "S"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 19
                elif gfield[py][nn] == "A":
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 19
                elif gfield[py][nn] == "H":
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 19
                elif gfield[py][nn] == "I":
                    curadvokat = curadvokat + 1
                    if curadvokat > maxadvokat:
                        curadvokat = maxadvokat
                    showstatistic()
                    testlevel()
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 19
                else:
                    nn = 19
                nn = nn + 1
        else:
            nn=px - 1
            mixer.music.load('fireball.ogg')
            mixer.music.play()
            while nn > 0:
                if (gfield[py][nn] == "S") or (gfield[py][nn] == "f"):
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=fireball)
                    root.update()
                    time.sleep(0.2)
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    gfield[py][nn] = "S"
                elif gfield[py][nn] == "O":
                    gfield[py][nn] = "S"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 0
                elif gfield[py][nn] == "Z":
                    gfield[py][nn] = "S"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 0
                    curuliki = curuliki + 1
                    showstatistic()
                    testlevel()
                elif gfield[py][nn] == "V":
                    gfield[py][nn] = "S"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 0
                elif gfield[py][nn] == "A":
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 0
                elif gfield[py][nn] == "A":
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 0
                elif gfield[py][nn] == "I":
                    curadvokat = curadvokat + 1
                    if curadvokat > maxadvokat:
                        curadvokat = maxadvokat
                    showstatistic()
                    testlevel()
                    gfield[py][nn] = "f"
                    canvas.create_image(80+nn*32,60+py*32, anchor=NW, image=bgrd) 
                    nn = 0
                else:
                    nn = 0
                nn = nn - 1
    elif event.char == hJump:
        nn = 0
        while (nn <= 2) and ((gfield[py-nn-1][px] == "S") or (gfield[py-nn-1][px] == "Y")):
            if gfield[py-nn-1][px] == "S":
                canvas.create_image(80+px*32,60+(py-nn)*32, anchor=NW, image=bgrd)
                canvas.create_image(80+px*32,60+(py-nn-1)*32, anchor=NW, image=pright)
                root.update()
                time.sleep(0.2)
                canvas.create_image(80+px*32,60+(py-nn-1)*32, anchor=NW, image=pright)
            elif gfield[py-nn-1][px] == "Y":
                mixer.music.load('gulp.ogg')
                mixer.music.play()
                gfield[py-nn-1][px] = "S"
                canvas.create_image(80+px*32,60+(py-nn)*32, anchor=NW, image=bgrd)
                canvas.create_image(80+px*32,60+(py-nn-1)*32, anchor=NW, image=pright)
                root.update()
                time.sleep(0.2)
                canvas.create_image(80+px*32,60+(py-nn-1)*32, anchor=NW, image=pright)
                curdela = curdela + 1
                showstatistic()
                testlevel()
            nn = nn + 1
        while nn >= 0:
            if gfield[py-nn+1][px] == "S":
                canvas.create_image(80+px*32,60+(py-nn+1)*32, anchor=NW, image=pright)
                canvas.create_image(80+px*32,60+(py-nn)*32, anchor=NW, image=bgrd)
                root.update()
                time.sleep(0.2)
                canvas.create_image(80+px*32,60+(py-nn)*32, anchor=NW, image=bgrd)
            nn = nn - 1

#Функция опроса клавиатуры в правилах
def keyabout(event):
    global curRpage
    global nosRul
    global maxRlines
    if ord(event.char) == 27:
        mainscreen()
        showmenu(2)
        root.bind('<Key>', key)
    if ord(event.char) == 32:
        curRpage = curRpage + 1
        if (curRpage * nosRul) > (maxRlines + nosRul - 1):
            curRpage = 1
        printabout()

#Функция завершения работы программы
def exitapp():
    global root
    root.destroy()

#Функция отображения меню главного экрана
def showmenu(item):
    global canvas
    global imgBGame
    global imgRule
    global imgSet
    global imgExt
    global imgBGames
    global imgRules
    global imgSets
    global imgExts
    canvas.create_image(160,310, anchor=NW, image=imgBGame)  
    canvas.create_image(160,335, anchor=NW, image=imgRule)
    canvas.create_image(160,360, anchor=NW, image=imgSet)
    canvas.create_image(160,385, anchor=NW, image=imgExt)
    if item == 1:
        canvas.create_image(160,310, anchor=NW, image=imgBGames)
    if item == 2:
        canvas.create_image(160,335, anchor=NW, image=imgRules)
    if item == 3:
        canvas.create_image(160,360, anchor=NW, image=imgSets)
    if item == 4:
        canvas.create_image(160,385, anchor=NW, image=imgExts)

#Функция отображения фона экрана
def bgscreen():
    global canvas
    global imgBackGround
    global imgColonna
    global imgLTConer
    canvas.create_image(0,0, anchor=NW, image=imgBackGround)
    canvas.create_image(735,0, anchor=NW, image=imgColonna)
    canvas.create_image(0,0, anchor=NW, image=imgColonna)
    canvas.create_image(0,0, anchor=NW, image=imgLTConer)

#Функция отображения главного экрана
def mainscreen():
    global canvas
    global imgTitle
    bgscreen()
    canvas.create_image(100,70, anchor=NW, image=imgTitle)
    canvas.create_text(400,570,fill = "white", font = "Times 20 italic bold", text = "Space - перемещение, Enter - выбор.")
    canvas.update
    mixer.init()
    mixer.music.load('mmm.ogg')
    mixer.music.play()

#Функция отображения экрана правил
def aboutscreen():
    global canvas
    global imgHolst
    bgscreen()
    canvas.create_image(77,35, anchor=NW, image=imgHolst)
    canvas.create_text(400,570,fill="white",font="Times 20 italic bold",text="Space - листать, Esc - основное меню.")
    canvas.update
    showabouttext()

#Функция загрузки правил из файла
def showabouttext():
    global canvas
    global textrules
    global maxRlines
    f = open('rules.txt', 'r')
    textrules = f.readlines()
    maxRlines = len(textrules)
    f.close()
    printabout()
    
#Функция вывода на экран текста правил
def printabout():
    global canvas
    global nosRul
    global curRpage
    global textrules
    global maxRlines
    global imgHolst
    canvas.create_image(77,35, anchor=NW, image=imgHolst)
    nn=0
    while nn <= nosRul-1:
        nos = (curRpage - 1) * nosRul + nn
        nn = nn + 1
        if nos <= (maxRlines-1):
            canvas.create_text(400,130+nn*23,fill="darkblue",font="Times 18 italic bold",text=textrules[nos])
            canvas.update
            
#Функция отображения экрана установок
def setscreen():
    global canvas
    global imgHolst2
    global hUp
    global hDown
    global hLeft
    global hRight
    global hFire
    global hJump
    bgscreen()
    canvas.create_image(100,100, anchor=NW, image=imgHolst2)
    canvas.create_text(400,190,fill="black",font="Times 20 italic bold",text="Клавиши управления")
    canvas.create_text(400,570,fill="white",font="Times 20 italic bold",text="Esc - основное меню.")
    ckey = hUp
    if ckey == " ":
        ckey = "Space"
    canvas.create_text(400,275,fill="white",font="Times 20 italic bold",text="Вверх - "+ckey)
    ckey = hDown
    if ckey == " ":
        ckey = "Space"
    canvas.create_text(400,300,fill="white",font="Times 20 italic bold",text="Вниз - "+ckey)
    ckey = hLeft
    if ckey == " ":
        ckey = "Space"
    canvas.create_text(400,325,fill="white",font="Times 20 italic bold",text="Влево - "+ckey)
    ckey = hRight
    if ckey == " ":
        ckey = "Space"
    canvas.create_text(400,350,fill="white",font="Times 20 italic bold",text="Вправо - "+ckey)
    ckey = hFire
    if ckey == " ":
        ckey = "Space"
    canvas.create_text(400,375,fill="white",font="Times 20 italic bold",text="Огонь - "+ckey)
    ckey = hJump
    if ckey == " ":
        ckey = "Space"
    canvas.create_text(400,400,fill="white",font="Times 20 italic bold",text="Прыжок - "+ckey)
    canvas.update

#Функция отображения текущей статистики
def showstatistic():
    global canvas
    global curlevel
    global maxlevel
    global curlevelgold
    global maxlevelgold
    global curuliki
    global maxuliki
    global curznanija
    global maxznanija
    global curadvokat
    global maxadvokat
    global cursud
    global maxsud
    global curdela
    global maxdela
    global curpolice
    global maxpolice
    global info
    canvas.create_image(80,545, anchor=NW, image=info)
    canvas.create_text(170,560,fill="black",font="Times 14 italic bold",text=str(curlevel)+" / "+str(maxlevel))
    canvas.create_text(170,581,fill="black",font="Times 14 italic bold",text=str(curlevelgold)+" / "+str(maxlevelgold))
    canvas.create_text(300,560,fill="black",font="Times 14 italic bold",text=str(curuliki)+" / "+str(maxuliki))
    canvas.create_text(300,581,fill="black",font="Times 14 italic bold",text=str(curznanija)+" / "+str(maxznanija))
    canvas.create_text(440,560,fill="black",font="Times 14 italic bold",text=str(curadvokat)+" / "+str(maxadvokat))
    canvas.create_text(440,581,fill="black",font="Times 14 italic bold",text=str(cursud)+" / "+str(maxsud))
    canvas.create_text(590,560,fill="black",font="Times 14 italic bold",text=str(curdela)+" / "+str(maxdela))
    canvas.create_text(590,581,fill="black",font="Times 14 italic bold",text=str(curpolice)+" / "+str(maxpolice))

#Функция игрового экрана
def gamescreen():
    global canvas
    global info
    global curlevel
    global curuliki
    global maxuliki
    global curznanija
    global maxznanija
    global curadvokat
    global maxadvokat
    global cursud
    global maxsud
    global curdela
    global maxdela
    global curpolice
    global maxpolice
    global curlevelgold
    global maxlevelgold
    bgscreen()
    curlevelgold = 0
    maxlevelgold = 0
    curuliki = 0
    maxuliki = 0
    curznanija = 0
    maxznanija = 0
    curadvokat = 0
    maxadvokat = 0
    cursud = 0
    maxsud = 0
    curdela = 0
    maxdela = 0
    curpolice = 0
    maxpolice = 0
    showgamescr(curlevel)
    canvas.create_image(80,545, anchor=NW, image=info)
    showstatistic()

#Функция загрузки и отображения игрового экрана с заданным уровнем
def showgamescr(level):
    global canvas
    global wall1
    global wall2
    global wall3
    global wall4
    global bgrd
    global dooro
    global doorc
    global goldc
    global goldo
    global maxlevelgold
    global curlevelgold
    global lineup
    global gfield
    global pright
    global px
    global py
    global pleft
    global police
    global maxpolice
    global maxthread
    global pthread
    global pthreadlive
    global sud
    global maxsud
    global advokat
    global maxadvokat
    global ulika
    global maxuliki
    global dela
    global maxdela
    global znan
    global maxznanija
    fname = "level"
    if level < 10:
        fname = fname + "0"
    fname = fname + str(level) + ".map"
    f = open(fname, 'r')
    textmap = f.readlines()
    f.close()
    sline = 0
    while sline <= 14:
        linetext = textmap[sline]
        col = 0
        while col <= 19:
            gfield[sline][col] = linetext[col]
            if linetext[col] == "W":
                #print wall 4
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=wall4)
            elif linetext[col] == "V":
                #print wall 3
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=wall3)
            elif linetext[col] == "S":
                #print space
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
            elif linetext[col] == "B":
                #print wall 2
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=wall2)
            elif linetext[col] == "M":
                #print wall 1
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=wall1)
            elif linetext[col] == "D":
                #print door open
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=dooro)
            elif linetext[col] == "C":
                #print door close
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=doorc)
            elif linetext[col] == "O":
                #print gold open
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=goldo)
            elif linetext[col] == "E":
                #print znanija
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=znan)
                maxznanija = maxznanija + 1
            elif linetext[col] == "G":
                #print gold close
                maxlevelgold = maxlevelgold + 1
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=goldc)
            elif linetext[col] == "Y":
                #print dela
                maxdela = maxdela + 1
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=dela)
            elif linetext[col] == "Z":
                #print uliki hiden
                maxuliki = maxuliki + 1
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
            elif linetext[col] == "L":
                #print lineup
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=lineup)
            elif linetext[col] == "P":
                #print first position of person right
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=pright)
                px = col
                py = sline
                gfield[sline][col] = "S"
            elif linetext[col] == "R":
                #print first position of person left
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=pleft)
                px = col
                py = sline
                gfield[sline][col] = "S"
            elif linetext[col] == "A":
                #print police
                gfield[sline][col] = "A"
                maxpolice = maxpolice + 1
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=police)
                pthread.append(threading.Thread(target=moveotherpers, args=(col,sline,1,)))
                maxthread = maxthread + 1
                pthreadlive = True
                pthread[maxthread-1].daemon = True
                pthread[maxthread-1].start()
            elif linetext[col] == "H":
                #print sud
                gfield[sline][col] = "H"
                maxsud = maxsud + 1
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=sud)
                pthread.append(threading.Thread(target=moveotherpers, args=(col,sline,2,)))
                maxthread = maxthread + 1
                pthreadlive = True
                pthread[maxthread-1].daemon = True
                pthread[maxthread-1].start()    
            elif linetext[col] == "I":
                #print advokat
                gfield[sline][col] = "I"
                maxadvokat = maxadvokat + 1
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=bgrd)
                canvas.create_image(80+col*32,60+sline*32, anchor=NW, image=advokat)
                pthread.append(threading.Thread(target=moveotherpers, args=(col,sline,3,)))
                maxthread = maxthread + 1
                pthreadlive = True
                pthread[maxthread-1].daemon = True
                pthread[maxthread-1].start()       
            col = col + 1
        sline = sline + 1
    canvas.update
    
#Начальные установки расширения игрового экрана
swidth = 800
sheigth = 600

#Задание начальных значений основного окна программы
root = Tk()
root.wm_title("Ugame by Sergey Barsukov")
root.iconbitmap(r"ugame.ico")
canvas = Canvas(root, width=swidth, height=sheigth)
x = (root.winfo_screenwidth() - swidth) / 2
y = (root.winfo_screenheight() - sheigth) / 2
root.wm_geometry("+%d+%d" % (x, y))
canvas.pack()

#Занрузка текстур графики
imgBackGround = PhotoImage(file="bg.png")
imgColonna = PhotoImage(file="colonna.png")
imgLTConer = PhotoImage(file="tlc.png")
imgTitle = PhotoImage(file="title.png")
imgBGame = PhotoImage(file="bgame.png")
imgRule = PhotoImage(file="rule.png")
imgSet = PhotoImage(file="setting.png") 
imgExt = PhotoImage(file="exit.png")
imgBGames = PhotoImage(file="bgames.png")
imgRules = PhotoImage(file="rules.png")
imgSets = PhotoImage(file="settings.png") 
imgExts = PhotoImage(file="exits.png")
imgHolst = PhotoImage(file="holst.png")
imgHolst2 = PhotoImage(file="holst2.png")
wall1 = PhotoImage(file="wl1.png")
wall2 = PhotoImage(file="wl2.png")
wall3 = PhotoImage(file="wl3.png")
wall4 = PhotoImage(file="wl4.png")
bgrd = PhotoImage(file="boxbg.png")
dooro = PhotoImage(file="dooro.png")
doorc = PhotoImage(file="doorc.png")
goldc = PhotoImage(file="chc.png")
goldo = PhotoImage(file="cho.png")
lineup = PhotoImage(file="lup.png")
pleft = PhotoImage(file="pleft.png")
pright = PhotoImage(file="pright.png")
fireball = PhotoImage(file="fireball.png")
info = PhotoImage(file="info.png")
police = PhotoImage(file="police.png")
gover = PhotoImage(file="gover.png")
sud = PhotoImage(file="sud.png")
advokat = PhotoImage(file="advokat.png")
ulika = PhotoImage(file="ulika.png")
dela = PhotoImage(file="dela.png")
znan = PhotoImage(file="znan.png")
win = PhotoImage(file="win.png")
yww = PhotoImage(file="yww.png")

#Запуск программы
mainscreen()
showmenu(1)
gthread = threading.Thread(target=testgover, args=())
gthread.daemon = True
gthread.start()
root.bind('<Key>', key)
root.mainloop()