#SONG
#15.July.2019
#Rocket Landing Game!

speed = 0      # speed approaching the moon
fuel = 100     # how much fuel is left
altitude = 100 # altitude above
gravity = -10 # acceleration due to gravity
Mfuel = 20 #Maximum fuel
mfuel = 0 #minimum fuel
Maccel =10 #Maximum acceleration
maccel = -10 #minimum accerleration
acceleration = 0

def show_rocket_status():
    print("altitude: " + str(altitude)+ " / rocket_speed: "+str(speed)+"/fuel: "+ str(fuel))

def Dthruster (thrusters): #DeltaThruster
    old_fuel = fuel
    old_height = altitude
    old_speed = speed

    if (old_fuel - thrusters < 0):
        show_rocket_status()
        print "the vessel is in vertical position "

    elif(thrusters >= mfuel and thrusters <= Mfuel):
        new_fuel = old_fuel - thrusters
        new_acceleration = acceleration +thrusters
        new_position = old_height + speed + acceleration*0.5
        new_speed = speed + acceleration
        return new_fuel, new_acceleration, new_position, new_speed

while(altitude<=0) :
    show_rocket_status()
    while(altitud<=0):
        thrusters = int (raw_input ("Set the thruster's rate(0~20) :"))
        if(thrusters >Mfuel or thrusters< mfuel):
            print"Wrong thrusters input try it again,"
            exit()
        else:
            break
    fuel, acceleration, altitude, speed = Dthruster(thrusters)
    if (altitude <=0 and speed <=3 and speed >=-3):
        show_rocket_status()
        print("Success")
        exit()
    elif(altitude<=0 and speed<3):
        show_rocket_status()
        print "Fail!"
        exit()