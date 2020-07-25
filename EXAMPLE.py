import random
import time

name0 = input("Введите ваше имя: ")
name1 = input("Введите имя второго игрока: ")
#name0 = "Илья"
#name1 = "bot"
if name1 == "bot":
    fgr = "@"
else:
    fgr = "*"
abname = False

fp = [[None]*10,
     [None, "·", "o", "·", "o", "·", "o", "·", "o", None],
     [None, "o", "·", "o", "·", "o", "·", "o", "·", None],
     [None, "·", "o", "·", "o", "·", "o", "·", "o", None],
     [None, "·", "·", "·", "·", "·", "·", "·", "·", None],
     [None, "·", "·", "·", "·", "·", "·", "·", "·", None],
     [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
     [None, "·", fgr, "·", fgr, "·", fgr, "·", fgr, None],
     [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
     [None]*10,]
'''
fp = [[None]*10,
     [None, "·", "o", "·", "o", "·", "o", "·", "o", None],
     [None, "o", "·", "o", "·", "o", "·", "o", "·", None],
     [None, "·", "o", "·", ".", "·", ".", "·", "o", None],
     [None, "·", "·", fgr, "·", fgr, "·", "·", "·", None],
     [None, "·", "·", "·", "·", "·", "·", "·", "·", None],
     [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
     [None, "·", fgr, "·", fgr, "·", fgr, "·", fgr, None],
     [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
     [None]*10,]
'''
frag0 = ''
frag1 = ''
last_kill = None
def blit():
    global fp
    global frag0
    global frag1

    board = f"""
    8   {fp[8][1]}  ·  {fp[8][3]}  ·  {fp[8][5]}  ·  {fp[8][7]}  ·
    7   ·  {fp[7][2]}  ·  {fp[7][4]}  ·  {fp[7][6]}  ·  {fp[7][8]}  |{frag1}|
    6   {fp[6][1]}  ·  {fp[6][3]}  ·  {fp[6][5]}  ·  {fp[6][7]}  ·
    5   ·  {fp[5][2]}  ·  {fp[5][4]}  ·  {fp[5][6]}  ·  {fp[5][8]}
    4   {fp[4][1]}  ·  {fp[4][3]}  ·  {fp[4][5]}  ·  {fp[4][7]}  ·
    3   ·  {fp[3][2]}  ·  {fp[3][4]}  ·  {fp[3][6]}  ·  {fp[3][8]}
    2   {fp[2][1]}  ·  {fp[2][3]}  ·  {fp[2][5]}  ·  {fp[2][7]}  ·  |{frag0}|
    1   ·  {fp[1][2]}  ·  {fp[1][4]}  ·  {fp[1][6]}  ·  {fp[1][8]}

        a  b  c  d  e  f  g  h
    """

    return board
print(blit())
def hod_proc(coord_str): #a1 b2
    global fp
    global poss_mov
    global frag0
    global frag1
    global name1
    global name0
    global abname
    global last_kill

    if len(coord_str) == 4:
        coord_str = f"{coord_str[0:2]} {coord_str[2:4]}"

    try:
        int(coord_str[0])
        coord_str = f"{coord_str[1]}{coord_str[0]} {coord_str[4]}{coord_str[3]}"
    except ValueError:
        pass



    transcr = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,
               "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8,}

    try:
        iput = (int(coord_str[1]), transcr[coord_str[0]])
        oput = (int(coord_str[4]), transcr[coord_str[3]])
        last_kill = oput
        print(last_kill)

        
        if abname == False:
            main_fig = "o"
        else:
            main_fig = fgr
        if fp[int(iput[0])][int(iput[1])] == main_fig:
            try:
                if oput in poss_mov[iput]:
                    kill(iput, oput)
                    fp[int(oput[0])][int(oput[1])] = fp[int(iput[0])][int(iput[1])]
                    fp[int(iput[0])][int(iput[1])] = "·"

                    if abname == False:
                        abname = True

                    elif abname == True:
                        abname = False

                else:
                    print("Правилами игры не предусмотрен такой ход.")

            except KeyError:
                print("На заданных координатах фигура отсутствует.")
        else:
            print("Правила игры запрещают трогать чужие фигуры!")
    except IndexError:
        print("Координаты хода заданы неверно.")

    except KeyError:
        print("Координаты хода заданы неверно.")

def aura():
    global poss_mov
    global fp
    time.sleep(1)
    transcr = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
    bot_hod = ''
    b = []
    for key in poss_mov.keys():
        b.append(key) 

    aura_hod = False
    while aura_hod == False: 
        random_poss = random.choice(b) #рандомная позиция фигуры
        if fp[random_poss[0]][random_poss[1]] == fgr:
            if len(poss_mov[random_poss]) > 0:
                random_coord = random.choice(poss_mov[random_poss])
                bot_hod = f"{transcr[random_poss[1]]}{random_poss[0]} {transcr[random_coord[1]]}{random_coord[0]}"
                aura_hod = True
    print("Aura, ваш ход: " + bot_hod)
    return bot_hod

def search():
    for li, line in enumerate(fp):
        for fi, figure in enumerate(line):
            if fp[li][fi] == "o" and abname == False: 
                main = (li, fi)
                poss_mov[main] = []
                if fp[li + 1][fi + 1] == "·":
                    poss_mov[main].append((li + 1, fi + 1))

                if fp[li + 1][fi - 1] == "·":
                    poss_mov[main].append((li + 1, fi - 1))

                if fp[li + 1][fi + 1] == fgr:
                    if fp[li + 2][fi + 2] == "·":
                        poss_mov[main].append((li + 2, fi + 2))
                        hi_hod(main,(li + 2, fi + 2))

                if fp[li + 1][fi - 1] == fgr:
                    if fp[li + 2][fi - 2] == "·":
                        poss_mov[main].append((li + 2, fi - 2))
                        hi_hod(main,(li + 2, fi - 2))

                if fp[li - 1][fi + 1] == fgr:
                    if fp[li - 2][fi + 2] == "·":
                        poss_mov[main].append((li - 2, fi + 2))
                        hi_hod(main,(li - 2, fi + 2))

                if fp[li - 1][fi - 1] == fgr:
                    if fp[li - 2][fi - 2] == "·":
                        poss_mov[main].append((li - 2, fi - 2))
                        hi_hod(main,(li - 2, fi - 2))

            if fp[li][fi] == fgr and abname == True:
                main = (li, fi)
                poss_mov[main] = []
                if fp[li - 1][fi + 1] == "·":
                    poss_mov[main].append((li - 1, fi + 1))

                if fp[li - 1][fi - 1] == "·":
                    poss_mov[main].append((li - 1, fi - 1))

                if fp[li - 1][fi + 1] == "o":
                    if fp[li - 2][fi + 2] == "·":
                        poss_mov[main].append((li - 2, fi + 2))
                        hi_hod(main,(li - 2, fi + 2))

                if fp[li - 1][fi - 1] == "o":
                    if fp[li - 2][fi - 2] == "·":
                        poss_mov[main].append((li - 2, fi - 2))
                        hi_hod(main,(li - 2, fi - 2))

                if fp[li + 1][fi + 1] == "o":
                    if fp[li + 2][fi + 2] == "·":
                        poss_mov[main].append((li + 2, fi + 2))
                        hi_hod(main,(li + 2, fi + 2))

                if fp[li + 1][fi - 1] == "o":
                    if fp[li + 2][fi - 2] == "·":
                        poss_mov[main].append((li + 2, fi - 2))
                        hi_hod(main,(li + 2, fi - 2))


def hi_hod(main_poss, last_poss):
    
    try:
        hi_hod_m[main_poss].sppend(last_poss)
    except:
        hi_hod_m[main_poss] = [last_poss]  

def kill(iput, oput):
    global frag0
    global frag1
    global last_kill

    lo_line = min(oput[0], iput[0])
    hi_line = max(oput[0], iput[0])
    lo_pos = min(oput[1], iput[1])
    hi_pos = max(oput[1], iput[1])

    if hi_line - lo_line == 2:
        fig_frag = fp[lo_line + 1][lo_pos + 1]
        fp[lo_line + 1][lo_pos + 1] = "·"

        if fig_frag == fgr:
            frag0 += fgr

        elif fig_frag == "o":
            frag1 += "o"

def auto_step():
    global abname
    global name0
    global name1
    transcr = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}

    if abname == False:
        name = name0
    else:
        name = name1
    quant = []
    for quantity in hi_hod_m.keys():
        quant.append(quantity)
    
    available_step = "Доступные ходы: "
    
    if len(quant) == 1:
        main_poss = quant[0]
        ipt = transcr[main_poss[1]] + str(main_poss[0])
        opt = transcr[poss_mov[main_poss][0][1]] + str(poss_mov[main_poss][0][0])
        hod = f"{ipt} {opt}"
        print(name + " Ваш ход: " + hod)
        time.sleep(1)

    elif len(quant) > 1:
        for available in quant:
            main_poss = available
            ipt = transcr[main_poss[1]] + str(main_poss[0])
            opt = transcr[poss_mov[main_poss][0][1]] + str(poss_mov[main_poss][0][0])
            available_step += f"{ipt}-{opt}, "
        print(available_step)
        hod = input(name + ", Ваш ход: ")

    else:
        hod = input(name + ", Ваш ход: ")

    return(hod)



gg = True
while gg == True:   

    poss_mov = {}
    hi_hod_m = {}
    search()
    if hi_hod_m != {}:
        poss_mov = hi_hod_m

    if abname == False:
        hod = auto_step()

    elif abname == True:
        if name1 == "bot":
            hod = aura()

        else:
            hod = auto_step()

    if hod == "quit":
        gg = False
    
    for win in fp[1]:
        if win == fgr:
            print(f"Игрок {name0} победил!")
            gg = False 

    for win in fp[8]:
        if win == "o":
            print(f"Игрок {name0} победил!")
            gg = False 
    
    hod_proc(hod)
    print(blit())
    

