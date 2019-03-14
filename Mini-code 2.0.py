# A basic test code for the BAFTA YGD entry prototype

# - this code contains:
#  - Both friendly and hostile bullet codes (Working)
#  - Keyboard inputs (Err - "keyboard" module not found)
#  - Boss AI

def FriendlyBulletAppear():
    FriendlyBulletX = PlayerX
    for FriendlyBulletTravel in range(0,100):
        FriendlyBulletX = FriendlyBulletX + 1
        time.sleep(0.5)
        if FriendlyBulletX == EnemyX:
            EnemyHealth = EnemyHealth - 1
            if EnemyHealth == 0:
                EnemyAlive = False      # HIDE ENEMY #
                print("Victory")        # REPLACE THIS WITH AN IMAGE ASSET #

def HostileBulletAppear():
    HostileBulletX = EnemyX
    for HostileBulletTravel in range(0,100):
        HostileBulletX = HostileBulletX - 1
        time.sleep(0.5)
        if HostileBulletX == PlayerX:
            PlayerHealth = PlayerHealth - 1
            if PlayerHealth == 0:
                PlayerAlive = False     # HIDE PLAYER #
                print("Game Over")      # REPLACE THIS WITH AN IMAGE ASSET #


# --KeyboardInput-- #

from keyboard import*
while True:  
    try:
        if keyboard.is_pressed("f"):    # Fires Weapon #
            PlayerShooting = True
            time.sleep(1)
            Player.Shooting = False
            FriendlyBulletAppear()
            
        if keyboard.is_pressed("w"):    # Increases Y axis value #
            PlayerY = PlayerY + 1
            
        if keyboard.is_pressed("a"):    # Decreases X axis value #
            PlayerX = PlayerX - 1
            
        if keyboard.is_pressed("s"):    # Decreases Y axis value #
            PlayerY = PlayerY - 1
            
        if keyboard.is_pressed("d"):    # Increases X axis value #
            PlayerX = PlayerX + 1

        if keyboard.is_pressed("c"):    # Displays control screen #
            print("'W' - Up")           # REPLACE THIS WITH AN IMAGE ASSET #
            print("'A' - Left")
            print("'S' - Down")
            print("'D' - Right")
            print("'C' - Control Screen")
            print("'F' - Fire Weapon")
            
    except:
        print("Err: key not assigned")

# --Backdrop-- #                # GOOD LUCK WITH THIS! XD #

while PlayerAlive == True:
    BackdropNumber = BackdropNumber + 1 #Backdrop cycle
if BackdropNumber == 1:
    print("Backdrop 1")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 2:
    print("Backdrop 2")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 3:
    print("Backdrop 3")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 4:
    print("Backdrop 4")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 5:
    print("Backdrop 5")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 6:
    print("Backdrop 6")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 7:
    print("Backdrop 7")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 8:
    print("Backdrop 8")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 9:
    print("Backdrop 9")         # REPLACE THIS WITH AN IMAGE ASSET #
if BackdropNumber == 10:
    print("Backdrop 10")        # REPLACE THIS WITH AN IMAGE ASSET #

    
# --EnemyAI-- #



from random import*

while EnemyAlive == True:
    print("The enemy is still alive")
    if EnemyHealth < 2:
        SafetyChance = 3
    if EnemyHealth > 1:
        SafetyChance = 10
    if EnemyX > 50:
        Charge = random.randint(0,SafetyChance)
        if Charge == 1:
            for Charging in range(0,EnemyX - 5):
                EnemyX = EnemyX - 1
                if EnemyX < PlayerX + 3:
                    if EnemyX > PlayerX - 3:
                        PlayerHealth = PlayerHealth - 1
                        time.sleep(60)
                        PlayerHealth = PlayerHealth + 1
        Shoot = random.randint(0,SafetyChance)
        if Shoot == 1:
            HostileBulletAppear()
