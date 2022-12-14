########################################################################################
def robot_start():
    """This is the entry function, do not change"""

    ''' resets everything ..if the input is not "off" then this robot will keep running'''
    Right = [0]
    co = [0,0]
    RobotName = Whats_my_Name()
    Control= Control_Panel(RobotName,co,Right)
    while Control != "off" :
        Control= Control_Panel(RobotName,co,Right)
    else :
        exit
########################################################################################
def Whats_my_Name():
    ''' this take in robot name '''
    RobotName = input("What do you want to name your robot? ")
    print(RobotName+ ": Hello kiddo!")
    return RobotName
#########################################################################################
def Control_Panel(RobotName,co,Right):
    ''' the input that the user puts in will be added to a list and split '''
    inputlist = []
    Control= input(RobotName + ": " +"What must I do next? ").lower()
    inputlist= Control.split()
    ''' what ever the user inputs  will be read and searched through the commands and if it meets the condition
    certain functios will be called'''
    if Control == "help" :
        command_help()
    elif Control == "off"  :
        print(RobotName +": Shutting down..")
        '''
        *if the input requires a movement amount eg..forward 5
            the input list will require 2 items if not itll call the function until 2 is give 
                the list will also require the 2nd item to be an int 
                if not the function will be called until given a int
        '''
    elif  "forward" in Control or "back" in Control or "sprint" in Control :
        if len(inputlist) == 2 :
            AREACHECK = int(inputlist[1])
            try:
                AREACHECK = int(AREACHECK) 
                instruction(Control,inputlist,RobotName,co,Right)
            except:
                Control_Panel(RobotName,co,Right)    
        elif len(inputlist) != 2 :
            Control_Panel(RobotName,co,Right)
    elif "right" in Control or "left" in Control:
        if len(inputlist) == 1:
            instruction(Control,inputlist,RobotName,co,Right)
        else:
            Control_Panel(RobotName,co,Right)
    elif Control != "help" or "off" or "forward" :
        print(RobotName+": Sorry, I did not understand "+ "'"+ Control.capitalize()+ "'.")
    return Control
########################################################################################
                               #####################
                               #####################
                               #####################
########################################################################################
def command_help():
        '''commands that will be displayed if help is the input ''' 
        print("I can understand these commands:")
        print("OFF  - Shut down robot")
        print("HELP - provide information about commands")
        print("Forward - moves robot Forward")
        print("Back - moves robot Back")
        print("Right - moves robot Right")
        print("Left - moves robot Left")
########################################################################################
                               #####################
                               #####################
                               #####################
########################################################################################
def instruction(Control,inputlist,RobotName,co,Right):
    '''
    *depending on input certain functions will be called 
    '''
    dLow = inputlist[0]
    if dLow == "right" : 
        turn_Right_on_x(co,RobotName,Right)    
    elif dLow == "left" :
        turn_Left_on_x(co,RobotName,Right)
    elif dLow == "forward" :     
        noSteps = int(inputlist[1]) 
        move_Forward_on_y(co, noSteps,RobotName,Right) 
    elif dLow == "back" :
        noSteps = int(inputlist[1]) 
        move_Back_on_y(co,noSteps,RobotName,Right)
        '''
        *if the input is sprint 
            itll go into a loop and add the integers to a another list
        '''
    elif dLow == "sprint":
        noSteps = int(inputlist[1]) 
        sprintLen= []
        for i in range(1,noSteps+1):
            sprintLen.append(i)
            # print(sprintLen)
        sprint(co,sprintLen,noSteps,RobotName,Right)
########################################################################################
                               #####################
                               #####################
                               #####################
########################################################################################
def move_Forward_on_y(co,noSteps,RobotName,Right):
    
    if noSteps > 200 : #if the amount of steps are more than 200 then an error message will be displayed 
            co[1]+= 0
            co[0]-= 0
            print(RobotName +": Sorry, I cannot go outside my safe zone.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").")
    elif -200 < co[1] <= 200 and -100 < co[0] < 100   :
        
        if Right[0] == 0  : #right has its own function ..so the value of right will depending what value of the coordinates are called
            co[1] +=noSteps
            print(" > "+RobotName +" moved forward by " + str(noSteps)+ " steps.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
        elif Right[0] == 1  :
            co[0] += noSteps 
            print(" > "+RobotName +" moved forward by " + str(noSteps)+ " steps.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
        elif Right[0] == 2 :
            co[1] -= noSteps 
            print(" > "+RobotName +" moved forward by " + str(noSteps)+ " steps.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
        elif Right[0] == 3 :
            if noSteps > 100 : 
                co[0] -= 0
                print(RobotName +": Sorry, I cannot go outside my safe zone.")
                print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").")
            else:    
                co[0] -= noSteps 
                print(" > "+RobotName +" moved forward by " + str(noSteps)+ " steps.")
                print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
    return co[0],co[1]
########################################################################################
                                    # #########################    
                                    # #########################
                                    # #########################
########################################################################################
def move_Back_on_y(co, noSteps,RobotName,Right):
    if co[1] >= 200 :#if the amount of steps are more than 200 then an error message will be displayed 
        co[1] -= noSteps
        print(RobotName +" :Sorry, I cannot go outside my safe zone.")
        print("   > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").")
    elif -200 < co[1] <= 200 and -100 < co[0] < 100   :

        if Right[0] == 0:   #right has its own function ..so the value of right will depending what value of the coordinates are called
            co[1] -=noSteps
            print(" > "+RobotName +" moved back by " + str(noSteps)+ " steps.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
        elif Right[0] == 1:
            co[0] -= noSteps 
            print(" > "+RobotName +" moved back by " + str(noSteps)+ " steps.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
        elif Right[0] == 2:
            co[1] -= noSteps 
            print(" > "+RobotName +" moved back by " + str(noSteps)+ " steps.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
        elif Right[0] == 3:
            co[0] += noSteps 
            print(" > "+RobotName +" moved back by " + str(noSteps)+ " steps.")
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
        
    return co[0],co[1]
########################################################################################
                               #####################
                               #####################
########################################################################################
def turn_Right_on_x(co,RobotName,Right):
    Right[0] += 1 #every time this function is called the right var will inc
    print(" > " +RobotName + " turned right.")
    print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
    if Right[0] == 4 :#once it reaches 4 itll reset because then it wouldve turned in a circle
        Right[0] = 0
    return Right
                               #####################
def turn_Left_on_x(co,RobotName,Right):
    # Right[0] += 3
    for i in range(3):#creates a loop for right cause 3 rights makes a left 
        Right[0] += 1
        if Right[0] == 4 :#once it reaches 4 itll reset because then it wouldve turned in a circle
            Right[0] = 0
    print(" > " +RobotName + " turned left.")
    print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").") 
    return Right   
#########################################################################################
                               #####################
                               #####################
                               #####################
#########################################################################################
def sprint(co,sprintLen,noSteps,RobotName,Right):
    '''
    *if any of the coordinates are over these amounts nothing will function 
    and error msg. will be shown
    '''
    if -200 < co[1] <= 200 and -100 < co[0] < 100   :
        if len(sprintLen)== 0:
            print(" > "+RobotName +" now at position (" +str(co[0]) +"," + str(co[1])+").")
            return co[1]
        if len(sprintLen) > 0 :
            '''
            *for the sprint func. the list will decrement after every item that has been  added it will be removed
            until the list is empty
            *each step will be removed and the LENGTH of the list will be shown 
            '''
            if Right[0] == 0 :
                co[1] +=sprintLen[0]
                print(" > "+RobotName +" moved forward by "+str(len(sprintLen))+ " steps.")
                sprintLen.remove(sprintLen[0]) 
                return sprint(co,sprintLen,noSteps,RobotName,Right)

            elif Right[0] == 1 :
                co[0] += sprintLen[0] 
                print(" > "+RobotName +" moved forward by "+str(len(sprintLen))+ " steps.")
                sprintLen.remove(sprintLen[0])
                return sprint(co,sprintLen,noSteps,RobotName,Right)

            elif Right[0] == 2 :
                co[1] -= sprintLen[0]
                print(" > "+RobotName +" moved forward by "+str(len(sprintLen))+ " steps.")
                sprintLen.remove(sprintLen[0])
                return sprint(co,sprintLen,noSteps,RobotName,Right)

            elif Right[0] == 3:
                co[0] -= sprintLen[0]
                print(" > "+RobotName +" moved forward by "+str(len(sprintLen))+ " steps.")
                sprintLen.remove(sprintLen[0])
                return sprint(co,sprintLen,noSteps,RobotName,Right)  

    else :#if the robot gives and error message itll minus the input and the movement of that input will be null
        co[1] -=noSteps
        print("> "+RobotName+" Sorry, I cannot go outside my safe zone.")
        return Control_Panel(RobotName,co,Right)
#########################################################################################
if __name__ == "__main__":
    robot_start()
#########################################################################################
