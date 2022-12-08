from tkinter import *
from math import sqrt
from random import shuffle
HEIGHT = 768
WIDTH = 1366
window = Tk()
colors = ["darkred", "green", "blue", "purple", "pink", "lime"]
health = {
    "ammount" : 3,
    "color": "green"
}
window.title("Bubble Blaster")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
c.pack()
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="red")
ship_id2 = c.create_oval(0, 0, 30, 30, outline="red")
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
ship_spd = 10
score = 0
def move_ship(event):
    if event.keysym == "Up":
        c.move(ship_id, 0, -ship_spd)
        c.move(ship_id2, 0, -ship_spd)
    elif event.keysym == "Down":
        c.move(ship_id, 0, ship_spd)
        c.move(ship_id2, 0, ship_spd)
    elif event.keysym == "Left":
        c.move(ship_id, -ship_spd, 0)
        c.move(ship_id2,  -ship_spd, 0)
    elif event.keysym == "Right":
        c.move(ship_id, ship_spd, 0)
        c.move(ship_id2,  ship_spd, 0)
    elif event.keysym == "P":
        score += 10000
c.bind_all('<Key>', move_ship)
from random import randint
bub_r_b = list()
bub_id_b = list()
bub_r_b = list()
bub_id = list()
bub_r = list()
bub_speed = list()
bub_id_e = list()
bub_r_e = list()
bub_speed_e = list()
min_bub_r = 10
max_bub_r = 30
max_bub_spd = 25
gap = 100
def create_death():
    x = WIDTH + gap
    y = (MID_Y)
    r = randint(300, 350)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="red", fill="gray")
    bub_id_e.append(id1)
    bub_r_e.append(r)
    bub_speed_e.append(randint(6, max_bub_spd))
def create_bubble():
    x = WIDTH + gap
    y = randint(0, HEIGHT)
    r = randint(min_bub_r, max_bub_r)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="white")
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(5, max_bub_spd))
def create_bubble_e():
    x = WIDTH + gap
    y = randint(0, HEIGHT)
    r = randint(min_bub_r, max_bub_r)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="red")
    bub_id_e.append(id1)
    bub_r_e.append(r)
    bub_speed_e.append(randint(6, max_bub_spd))
def create_bubble_r():
    x = WIDTH + gap
    y = randint(0, HEIGHT)
    r = randint(min_bub_r, max_bub_r)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="green",)
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(9, max_bub_spd))
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)
    for i in range(len(bub_id_e)):
        c.move(bub_id_e[i], -bub_speed_e[i], 0)
from time import sleep, time
bub_chance = 30
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y
def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]
def clean():
    for i in range(len(bub_id) -1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -gap:
            del_bubble(i)
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def  collision():
    points = 0
    for bub in range(len(bub_id) -1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points
def collision_b():
    for bub in range(len(bub_id_b) -1, -1, -1):
        if distance(ship_id2, bub_id_b[bub]) < (SHIP_R + bub_r_b[bub]):
            bombClean()
def cleanAll():
    for i in range(len(bub_id) -1, -1, -1):
        x, y = get_coords(bub_id[i])
        del_bubble(i)
def bombClean():
    while True:
        points = 0
        for bub in range(len(bub_id) -1, -1, -1):
            if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
                points += (bub_r[bub] + bub_speed[bub])
                del_bubble(bub)
    return points
def  collision_e():
    for bub in range(len(bub_id_e) -1, -1, -1):
        if distance(ship_id2, bub_id_e[bub]) < (SHIP_R + bub_r_e[bub]):
            window.destroy() 
            import random
            print("You got ", + score, "score")
            jedi = ["Yoda", "Obi-Wan", "Qui Gonn"]
            enemy = ["General Grievious", "Palpatine", "Darth Vader"]
            enemy_1 = random.choice(enemy)
            jedi_1 = random.choice(jedi)
            print("You were killed by ", enemy_1)
            if score >= 1000 and score < 2000:
                if jedi_1 == ("Yoda"):
                    print("Master Yoda: Honored yourself you have, but still much to learn.")
                elif jedi_1 == ("Obi-Wan"):
                    print("Master Kenobi: Very good my young Padawan. Today is your glorious day.")
                elif jedi_1 == ("Qui Gonn"):
                    print("Qui Gonn: You impressed me, padawan. Hope you are always that wise and powerful")
            if score < 1000:
                if enemy_1 == ("General Grievious"):
                    print("General Grievious: You fool! I have mastered the Jedi Arts by Count Dooku! I am your doom. Try to face me again, you do not stand a chance!")
                elif enemy_1 == ("Palpatine"):
                    print("Palpatine: Excellent! I knew you couldn't defeat Palpatine, the supreme Sith Lord! Hope you have better luck suffering the next time.")
                elif enemy_1 == ("Darth Vader"):
                    print("Darth Vader: Your battle skills impress me! Are you trained in the Jedi Arts? Join me and together we will rule the galaxy as friends! Or just play again")
            if score > 2000:
                print("The dark side is a pathway to many abilities, some considered to be unnatural!")
c.create_text(50, 30, text="SCORE", fill="white")
st = c.create_text(50, 50, fill="white")
c.create_text(100, 30, text="TIME", fill="black")
tt = c.create_text(100, 50, fill="white")
c.create_text(250, 700, text="Get the fuel bubbles (green and white) but avoid the bubble droids(red)!)", fill="white")
def show(score):
    c.itemconfig(st, text=str(score))
evil_bub = 50
#MAIN GAME LOOP
while True:
    if randint(1, bub_chance) == 1:
        create_bubble()
    if randint(1, evil_bub) == 1:
        create_bubble_e()
    if randint(1, 100) == 1:
        create_bubble_r()
    if score > 100:
        if randint(1, 1000) == 1:
            create_death()
        if move_bubbles():
            c.create_text(MID_Y, 30, text="Carefull Padawan, Death Star ahead!", fill="white")
        else:
            c.create_text(MID_Y, 30, text="Carefull Padawan, Death Star ahead!", fill="black")
    move_bubbles()
    collision_e()
    collision_b()
    clean()
    score += collision()
    if score >= 400:
        evil_bub = 10
        bub_chance = 30
        if score >= 1000:
            evil_bub = 5
            bub_chance = 45
    show(score)
    window.update()
    shuffle(colors)
    sleep(0.001)
