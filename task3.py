#EPL season
def epl():
    win=3
    draw=1
    wins=int(input('How many wins for your team so far '))
    draws=int(input('How many draws for your team so far '))
    losees=int(input('How many losses for your team so far '))
    points=(wins*win)+(draws*draw)
    print(f"your team has {points} points")
epl()    
