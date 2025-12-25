import random
import threading
import time
import os

plansza = [[0 for _ in range(9)] for _ in range(9)]
japko = [0,0]
gracz = [[5,6],[5,5],[5,4]]
graczStrona = [0,1]
stronyLiczby = [[-1,0],[1,0],[0,-1],[0,1]]
stronyChar = ['w','s','a','d']
inputZ = 'd'
czyGraTrwa = True
czyZbieranieInputu = True

def inputCollector():
    global inputZ
    while czyZbieranieInputu:
        inputZ = input()
        for i in range(4):
            if (stronyChar[i] == inputZ):
                graczStrona[0] = stronyLiczby[i][0]
                graczStrona[1] = stronyLiczby[i][1]

def consoleClear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def atStart():
    for y in range(9):
        for x in range(9):
            plansza[y][x] = '.'
    gracz = [[5,5],[5,4]]
    graczStrona = [0,-1]
    japko = [0,0]
    inputZ = 'd'
    czyGraTrwa = True
def wartosciNaTablice():
    for y in range(9):
        for x in range(9):
            plansza[y][x] = '.'
    plansza[japko[0]][japko[1]] = '*'
    for i in range(len(gracz)):
        plansza[gracz[i][0]  ][gracz[i][1]] = 'o'
def wypisywanie():
    for y in range(9):
        for x in range(9):
            print(plansza[y][x],end='')
        print('\n',end='')
def japkoZnalezione():
    if gracz[0][0] == japko[0]:
        if gracz[0][1] == japko[1]:
            return False
    return True
def noweMiejsceJapko():
    wolneMiejsca = [[0,0]]
    for y in range(9):
        for x in range(9):
            if [y,x] not in gracz:
                wolneMiejsca.append([y,x])

    wolneMiejsca.pop(0)
    losowyMango67 = random.randint(0,len(wolneMiejsca))
    japko[0] = wolneMiejsca[losowyMango67][0]
    japko[1] = wolneMiejsca[losowyMango67][1]
def workingGame():
    while czyGraTrwa:
        wartosciNaTablice()
        wypisywanie()
        time.sleep(1)
        consoleClear()

        if japkoZnalezione():
            gracz.pop()
        else:
            noweMiejsceJapko()
            
        if gracz[0][0]+graczStrona[0] < 0 or gracz[0][1]+graczStrona[1] < 0 or gracz[0][0]+graczStrona[0] > 8 or gracz[0][1]+graczStrona[1] > 8:
            break
        if [gracz[0][0]+ graczStrona[0],gracz[0][1] + graczStrona[1]] in gracz:
            break
        gracz.insert(0, [gracz[0][0]+ graczStrona[0],gracz[0][1] + graczStrona[1]])
    

def main():
    consoleClear()
    gra = threading.Thread(target=workingGame)
    zbieranieInputu = threading.Thread(target=inputCollector,daemon=True)
    atStart()
    gra.start()
    zbieranieInputu.start()
    gra.join()
    print("Koniec gry!")
    czyZbieranieInputu = False
    os._exit(0)
    
main()