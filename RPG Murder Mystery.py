global Current_Room
global Mirror_Counter
global Banana_Counter
global Couch_Counter
global Item_found
global CorpseFound
global PhoneFound
global Inspected_Max
global Knife_Rack_Checked
global Framed_Picture_Checked
global Entered_Living_Room
global Shattered_Glass
global Spoon_Counter
global BreadFound
global KeyFound


#-------------------------------------------------------------------------------------------------DIFFERENT ENDINGS----------------------------------------------------------

global Couch_Training 
global Spoon_Ending
global Mirror_Ending
global Arrested_Max
global Arrested_Fredrick
global Arrested_Rachel
global Arrested_Jake
global Arrested_Cameron

Couch_Training = False
Spoon_Ending = False
Mirror_Ending = False
Arrested_Max = False
Arrested_Fredrick = False
Arrested_Rachel = False
Arrested_Jake = False
Arrested_Cameron = False

#-------------------------------------------------------------------------------------------------FOR QUESTIONS------------------------------------------------------------------------------------------------------------------

global Q1Max
global Q2Max
global Q3Max

global Q1Rachel
global Q2Rachel
global Q3Rachel

global Q1Jake
global Q2Jake
global Q3Jake
global Q4Jake

global Q1Fredrick
global Q2Fredrick
global Q3Fredrick
global Q1Cameron
global Q2Cameron
global Q3Cameron

Q1Max = False
Q2Max = False
Q3Max = False

Q1Rachel = False
Q2Rachel = False
Q3Rachel = False

Q1Jake = False
Q2Jake = False
Q3Jake = False
Q4Jake = False

Q1Fredrick = False
Q2Fredrick = False
Q3Fredrick = False

Q1Cameron = False
Q2Cameron = False
Q3Cameron = False



#------------------------------------------------------------------------------------------STARTING SETTINGS------------------------------------------------------------------------------------------------------------------------
KeyFound = False
Spoon_Counter = 0
Shattered_Glass = 0
Entered_Living_Room = False
PhoneFound = False
CorpseFound = False
Item_found = False
Inspected_Max = False
Current_Room = 'Hall'
Mirror_Counter = 0
Banana_Counter = 0
Couch_Counter = 0
Framed_Picture_Counter = 0
Knife_Rack_Checked = False
Framed_Picture_Checked = False
BreadFound = False
locations = {
    #______________________________________________________________________________BELOW HERE IS THE HALL SCRIPT______________________________________________________________________________________________________________________




    
              "Hall" :{
                'Shoe Cabinet': "There are shoes in there.... what did you expect?",
                'Key Rack': 'There are no keys on the Key Rack',
                'Framed Picture': ['It is a picture of 3 Men and 2 Women at the beach.','In the picture there is Jake, Fredrick, Cameron, Magdalena and Rachel. \n The beach seems to be mostly empty except from a man with brown hair walking away from the group.'],
                'Party Invitations': 'Why are there some still leftover?',
                'Coat': "There are stains along the sleeves of a black coat with a fur covered hood, \n  it is too difficult to distinguish its origin",
                
                'North':'Kitchen',
                'West':'Dining Room',
                'South':'Front Door',
                'East':'Living Room',
                },







              
    #__________________________________________________________________________BELOW HERE IS THE FRONT DOOR SCRIPT____________________________________________________________________________________________________________________






                "Front Door":{
                    "Nothing": "There is nothing to inspect",
                    "More_Nothing" : "There is a whole lot of nothing there",
                    "Even_More_Nothing" : "There is an overwhelming amount of nothing",

                    
                    'North': 'Hall',
                    'East': 'You cannot go in that direction',
                    'West': 'You cannot go in that direction',
                    'South': ["You decided that this wasn't worth your time, you went home","Runaway Ending"]
                      },



#________________________________________________________________________________BELOW HERE IS THE KITCHEN SCRIPT_____________________________________________________________________________________________________________________





                  
              "Kitchen":{
                'Shattered_Glass':['This seems to be a shattered pint glass, it appears that there was no liquid in it though when it was broken.','There seems a bit of blood on a piece of the glass, maybe it was thrown?'],       
                'Knife_Rack': "One of the knives are missing. Was it lost or was it a weapon?",
                'Mirror':['Its a mirror, you see yourself in the reflection. You are quite the handsome chap!','You decide to arm yourself and challenge the man in the mirror to a game of finger guns. \n 3 \n 2 \n 1 \n You crack the gun and point it at the mirror and fire.... you lost. Somehow.','You stare into the reflection with a loving gaze, you indulge yourself by blowing yourself a kiss <3','You decide to make peace and not war.\n You walk towards the mirror, you get so close that your breathe creates condensation on the window','After applying chapsticks and puckering up your lips, you smooch your reflection. \n The suspects walk into the kitchen. \n There is a strong tension in the room so you stop.','You return for more, you are such a sloppy kisser that you hear the sounds of pure disgust.','You carry on making out with your reflection then you receive a phone call. \n In graphic detail, your superiors state what the an anonymous spectator have reported.\n You have been let off the assignment and been fired. \n On your way out of the crime scene, you blow one last kiss to the mirror', 'Mirror Ending'],
                'Sink': 'It appears bloody.',
                'Bananas':['It is a regular bunch of yellow bananas.','As you stare at the bananas, you start to feel strange.','You start to think that the bananas are witnesses','You begin to interrogate the bunch of bananas','After playing good cop/bad cop with the bananas, you begin to feel welcoming with the bunch.','You start to channel your inner banana.',"You start feel even more strange, you are beginning to change! \n Not just mentally but physically too. \n You are now a banana...... don't question it too much","Banana Ending"],
                'North': 'Conservatory',
                'West': 'Pantry',
                'South' : 'Hall',
                'East': 'Garden',
        
                  },


                  


#_____________________________________________________________BELOW HERE IS THE DINING ROOM SCRIPT________________________________________________________________________________________________________________________________



                  
              "Dining Room":{
                    'Candle': 'This is a lit scented candlestick, it smells like fresh lavender. In my opinion it really lightens up the room. I would rate it 10 out of 10',
                    'Spoon':["This is a spoon.",'Yes....it is very interesting''SOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO interesting....','IT IS A SPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON',"SPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON","SPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON",'Due to how interesting the spoon is, you forgot your purpose and just went home shouting SPOON',"Spoon Ending"],
                    'Phone':"You see the text messages of each of the suspects with the recently diseased. \n The messages between the victim and Rachel didn't end well. Maybe we I should interrogate her?",
                    'North': 'Pantry',
                    'West': 'You cannot go that direction',
                    'South': 'You cannot go that direction',
                    'East': 'Hall',
                  },





#_____________________________________________________________BELOW HERE IS THE PANTRY SCRIPT____________________________________________________________________________________________________________________________________




                  
              "Pantry":{
                  'Bread': 'The smell of bread fills your nose and reminds you of the old bakery.There is some bite marks in it. \n Although the room is dark and can make out a bloodstained item nearby it. ',
                  'Carrots':'They are carrots. You nibble on them hoping that they improve your vision.',
                  'Meat':"It is rotten. Meat doesn't last long in pantries.....You start to question the intelligence of the suspects.",
                  '???????':'You grab the item and realise that it is a knife. You shine a light on it and there seems to be some brown cloth on the weird handle of it.',



                  'North' : 'Storage Room',
                  'West': 'You cannot go that direction',
                  'South': 'Dining Room',
                  'East': 'Kitchen',
                  },




#_______________________________________________________________BELOW HERE IS THE CONSERVATORY SCRIPT____________________________________________________________________________________________________________________________



                  
              "Conservatory":{
                  'Plant':"It is a fake plant in a real pot. It doesn't have a purpose.",
                  'Couch':["You examine the couch, there is no stains or cuts on it.","After further examine, you realise that it is just like the couch your parent's had when you were a child.","You lay down on the couch contemplating your current perdicament.","Your eye lids begin to fall.","You begin to feel more relaxed.","You fell asleep, you had the best sleep of your life. \n You awaken hours later, no one is in the house and the body is gone. \n Whoever committed the crime managed to get away. \n You decide to go back up to sleep due to the comfiness of the couch.",'Sleepy Head Ending'],
                  'Table': 'This seems like a nice table. It seems like there is a lonesome cuppa on there. \n',


                  'North': 'You cannot go that direction',
                  'West': 'Storage Room',
                  'South' : 'Kitchen',
                  'East': 'Porch',
                  },





#_______________________________________________________________BELOW HERE IS THE STORAGE ROOM SCRIPT____________________________________________________________________________________________________________________________





                  
              "Storage Room":{
                  'Spider': 'You see a spider in the dark corner of the room, it appears to be plotting. You are very intimidated by it and decide that you should leave the connive its evil scheme by itself.',
                  'Boxes': 'The room is filled with boxes, there are too many to sort through and you cannot move investigate much of the room.',


                  'North': 'You cannot go that direction',
                  'West': 'You cannot go that direction',
                  'South': 'You cannot go that direction',
                  'East': 'Conservatory',
                  },
                





#__________________________________________________________________BELOW HERE IS THE PORCH SCRIPT________________________________________________________________________________________________________________________________





                  
              "Porch":{
                  'Plant': 'It is a real plant in a fake pot.',
                  'Key': "It is a small key with the word pantry on it",
                  'Sunglasses':'You put on the sun glasses , you instantly feel 100x cooler.... \n SAdly you cannot see anything due to it being night time.',


                  'North' : 'You cannot go that direction',
                  'West': 'Conservatory',
                  'South': 'Garden',
                  'East': 'You cannot go that direction',
                  },








#______________________________________________________________________BELOW HERE IS THE GARDEN SCRIPT__________________________________________________________________________________________________________________________




                  

              "Garden":{
                  'Plants': 'There appears to be a series of fake plants in fake dirt next to real flowers in real dirt.',
                  'Rake':'You accidentally step onto the rake whilst investigating it. \n You fall down in agony.',
                  'Footsteps':'There are sunken footsteps in the dirt leading to the pond, maybe it is a lead',
                  'Corpse':['Pockets : They are empty',"Head : There is a dent with heavy bruising and some blood across the left side of the victim's skull. \n There appears to be some glass in there.","Chest : A visible stab wound on the victim's lower torso, the weapon wasn't left in the body.","Hands : There is a ring on the left hand of the victim. The knuckles are swollen, cut and badly bruised."],

                  'North': 'Porch',
                  'West': 'Kitchen',
                  'South': 'Living Room',
                  'East': 'You cannot go that direction',
                  },





#________________________________________________________________________BELOW HERE IS THE LIVING ROOM SCRIPT___________________________________________________________________________________________________________________




                  
              "Living Room":{
                  'Jake':['The body was found by Cameron on the porch.'," I was smoking a cigarette with Max then I went to get a drink from the kitchen.","What knife? There are plenty of knives in there, I am sure it is just misplaced thats all.","I think it was Cameron who did it. \n Cameron used to date Magdalena but they broke up a year or two ago at the beach. \n Apparently she didn't want to get married to Cameron back then so she broke up with him because of how awkward it was. \n Recently she became engaged to Fredick, Cameron's best friend, I reckon that Cameron just got so angry at Magdalena due to it that he snapped and choked her."],
                  'Fredrick':["Jake found the body in the garden, he rushed in with tears in his eyes and made everyone go with him. I couldn't move... when I heard the screams and cries I knew he was telling the truth. All I could do was call the police.","Cameron and I were talking about the good old times back when we were both kids. \n I was about to tell him about the recent news of my engagement when Jake came in..... my dear Magdalena. We were meant to be getting married next year. \n This was the reason we held this party. It was to reveal the engagement...","I couldn't bring myself to see her body.... I just. My dear Magdalena. You deserved so much better than this.","I don't know who would do this but if/when you find them, give that person hell and make sure they spend their life regretting what they did."],
                  "Max":["Jake found the body out in the garden, I didn't know her well but seeing her body... it made me feel sorry for her and Fredrick.","I was smoking out the front with Jake but he had to go to the toilet or something. I wasn't listening much.","I am the new one to the group, I have only been hanging with this lot for a few weeks or so. I met Jake at a bar when I was serving drinks. \n I bet he wanted me to be the bartender for this party."," I am not sure, I dont know these people that well. \n I know Cameron and Jake fell out during the beginning of the party."],
                  'Cameron':["I am not sure who found the body, I was busy sorting out something in the pantry.","I was in the pantry, there was some food in there and I was hungry so I ate some bread. I rushed out when I heard someone crying.","I still loved her. I used to date Magdalena a while ago, she meant the world to me. It was heartbreaking when she rejected me. \n When I saw the ring on her finger today, I just broke down. Fredrick isn't a good guy, I wouldn't trust him if I was you.","The only people I can think of that could of done this is Fredrick or Rachel."],
                  'Rachel':["I found the body on the porch, I thought it would be best if she laid in her favourite place, her garden. She was so pleased and proud of it","I was in the Kitchen, there was some dishes needed to be done and I was talking to Cameron. He wanted the key for the pantry, it was in the kitchen so I gave it to him.","I didn't look at Cameron, he disgusts me. He let himself go after the break up between him and Magdalena. He isn't the man he used to be.","Jake asked if he could help cutting up some food so I handed him some food and told him to get some food from the pantry. Maybe he left the knife in there by accident.","Magdalena and I go way back. We met back in college and have been best friends since. We had a fight recently though, I don't even remember what it was about. \n I just hope she didn't hate me when she passed away."],
                  'North': 'Garden',
                  'West': 'Hall',
                  'South': 'You cannot go that direction',
                  'East': ' You cannot go that direction',
                  }
              }








#_________________________________________________________________________________BELOW HERE IS THE ARRESTING AND INSPECTION OF CHARACTERS DIALOGUE-----------------------------------------------------------------------------

              
Character = {
        "Max":"He is a man in his 20's, he is rather scrawny and doesn't look like a violent character. \n He has yellow stains around his fingers, he must be a smoker. /n He is wearing an Nike t-shirt and shoes along with jeans and standing quite far away from the others.",
        "Rachel" : "She seems to be around late teens to earlier 20's, she appears to be physically distraught. On her hand there is a cut, was it caused by a fight?",
        "Cameron" : "He is rather large and jugding from his build, I don't doubt that he could kill someone. \n There is tattoos up his right arm, some of it is covered by his blue shirt. \n His face displays shock.",
        "Fredrick" : "Just like Cameron, his build could easily allow him to win fights. He appears to be in around 20 but I cannot judge fully due to him crying into his hands.",
        "Jake": "He appears to be a scrappy chap. There appears to be a scar on forearm. He is around 20 and doesn't seem like he wants to talk. \n Maybe he is scared. \n Maybe he is hiding something",

        "Arrest Jake":["So what if I killed her, she deserved it! She only toyed with me.","Arrested Jake"],
        "Arrest Max":["WHAT?!?!? WHAT DO YOU MEAN? I didn't do this. I couldn't..","Arrested Max"],
        "Arrest Rachel":["I AM HER BEST FRIEND, SHE WAS LIKE MY SISTER!!! I would never do that. You got to believe me. I know we fought but I wouldn't kill her...","Arrested Rachel"],
        "Arrest Fredrick":["Why....... she meant the world to me. Now she is gone, I have nothing left.","Arrested Fredrick"],
        "Arrest Cameron":["This is just wrong, I loved her. I wanted to get back with her. I wouldn't kill her. I didn't kill her.","Arrested Cameron"],
         }

#___________________________________________________________________________BELOW HERE ARE THE FUNCTION FOR THE MOVEMENT BETWEEN ROOMS________________________________________________________________________________________________________________________



def Moving():
    global Current_Room
    global KeyFound
    print("Here are your options of were to go:")
    for PrimaryKey, SubKey in locations.items():
        if PrimaryKey == Current_Room:
            print(" 1 : To the north :" , SubKey["North"])
            print(" 2 : To the east :" , SubKey["East"])
            print(" 3 : To the south :" , SubKey["South"])
            print(" 4 : To the west :" , SubKey["West"])
    ans = input(" Which way will you go? \n :")
    done = True
    while done == True:
        Valid_Choice = False
        while Valid_Choice == False:
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            ans = input("That is not a valid input, please input one of the option. \n 1 : North \n 2 : East \n 3: South \n 4 : West \n :")
                            Valid_Choice = False
                        else:
                            direction = 'West'
                            Valid_Choice = True
                    else:
                        direction = 'South'
                        Valid_Choice = True
                else:
                    direction = 'East'
                    Valid_Choice = True
            else:
                direction = 'North'
                Valid_Choice = True
        for MainKey , SubKey in locations.items():
            if MainKey == Current_Room:
                New = SubKey[direction]
                print(New)
                if New == 'You cannot go in that direction':
                    ans = input("Please input one of the option. \n 1 : North \n 2 : East \n 3 : South \n 4 : West \n :")
                    done = True
                else:
                    if New == "Pantry":
                        if KeyFound == True:
                            done = False
                        else:
                            print('You cannot go in that direction')
                            ans = input("Please input one of the option. \n 1 : North \n 2 : East \n 3 : South \n 4 : West \n :")
                            done = True
                    else:
                        done = False
    Current_Room = New
    Menu()


#------------------------------------------------------------------------------------ THE CODE THAT ALLOWS YOU TO INSPECT PEOPLE--------------------------------------------------------------------------------------------------




def Inspect(PersonID):
    ans = PersonID
    Valid_Choice = False
    while Valid_Choice == False:
        if ans != '1':
            if ans != '2':
                if ans != '3':
                    if ans != '4':
                        if ans != '5':
                            ans = input("That is not a valid input, please input one of the option. \n 1 : Max  \n 2 : Rachel \n 3 : Cameron \n 4 : Fredrick \n 5 : Jake \n :")
                            Valid_Choice = False
                        else:
                            person = 'Jake'
                            Valid_Choice = True
                    else:
                        person = 'Fredrick'
                        Valid_Choice = True
                else:
                    person = 'Cameron'
                    Valid_Choice = True
            else:
                person = 'Rachel'
                Valid_Choice = True
        else:
            person = 'Max'
            Valid_Choice = True
    print(Character[person])
                

#----------------------------------------------------------------------------------ARRESTING THE CHARACTERS CODE-------------------------------------------------------------------------------------------------------------------


def Arrest():
    ans = input("Who are you going to arrest?  \n 1 : Max  \n 2 : Rachel \n 3 : Cameron \n 4 : Fredrick \n 5 : Jake \n :")
    Suspect = "Arrest"
    Valid_Choice = False
    while Valid_Choice == False:
        if ans != '1':
            if ans != '2':
                if ans != '3':
                    if ans != '4':
                        if ans != '5':
                            ans = input("That is not a valid input, please input one of the option. \n 1 : Max  \n 2 : Rachel \n 3 : Cameron \n 4 : Fredrick \n 5 : Jake \n :")
                            Valid_Choice = False
                        else:
                            person = 'Jake'
                            Valid_Choice = True
                            Arrested_Jake = True
                    else:
                        person = 'Fredrick'
                        Valid_Choice = True
                        Arrested_Fredrick = True
                else:
                    person = 'Cameron'
                    Valid_Choice = True
                    Arrested_Cameron = True
            else:
                person = 'Rachel'
                Valid_Choice = True
                Arrested_Rachel = True
        else:
            person = 'Max'
            Valid_Choice = True
            Arrested_Max = True

            
    Suspect = Suspect + ' ' + person
    array = Character[Suspect]
    print(' ' + array[0])
    Ending()


#-----------------------------------------------------------------------------INTERROGATING A PERSON CODE------------------------------------------------------------------------------------------------------------------------

def Interrogate(PersonID):
    global Q1Max
    global Q2Max
    global Q3Max

    global Q1Rachel
    global Q2Rachel
    global Q3Rachel

    global Q1Jake
    global Q2Jake
    global Q3Jake
    global Q4Jake

    global Q1Fredrick
    global Q2Fredrick
    global Q3Fredrick
    global Q1Cameron
    global Q2Cameron
    global Q3Cameron

    global PhoneFound
    global Ending
    global Inspected_Max
    global Knife_Rack_Checked
    global Framed_Picture_Checked
    global locations
    
    ans = PersonID
    Valid_Choice = False
    while Valid_Choice == False:
        if ans != '1':
            if ans != '2':
                if ans != '3':
                    if ans != '4':
                        if ans != '5':
                            ans = input("That is not a valid input, please input one of the option. \n 1 : Max  \n 2 : Rachel \n 3 : Cameron \n 4 : Fredrick \n 5 : Jake \n :")
                            Valid_Choice = False
                        else:
                            person = 'Jake'
                            Valid_Choice = True
                    else:
                        person = 'Fredrick'
                        Valid_Choice = True
                else:
                    person = 'Cameron'
                    Valid_Choice = True
            else:
                person = 'Rachel'
                Valid_Choice = True
        else:
            person = 'Max'
            Valid_Choice = True
    for MainKey , SubKey in locations.items():
        if MainKey == "Living Room":
            Script = SubKey[person]
    done = False       
        
    while done != True:
        print(" 1 : Where was the body found? \n 2 : What were you doing and where were you when the body was found?")
        if person != "Jake":
            if person != "Fredrick":
                if person != "Cameron":
                    if person != "Rachel":
                        if Inspected_Max == True:
                            print(" 3 : Why are you standing so far way from everyone?")
                        else:
                            print(" 3 : ??????????????????????????????????????")
                    else:
                        if (Knife_Rack_Checked == True and Q2Rachel == True):
                            print(" 3 : What happened to the knife?")
                        else:
                            print(" 3 : ??????????????????????????????????????")
                else:
                    if  (Framed_Picture_Checked == True and Q4Jake == True):
                        print(" 3 : What were your feelings towards Magdalena?")
                    else:
                        print(" 3 : ?????????????????????????????????????????")
            else:
                print(" 3 : How did you react when you saw her?")
        else:
            if (Knife_Rack_Checked == True and(Q4Rachel == True and Q2Max == True)):
                print(" 3 : What happened to the knife?")
            else:
                print(" 3 : ??????????????????????????????????????")
        print(" 4 : Who do you think did it?")
        if person != "Rachel":
            print('\n')
        else:
            if Q1Rachel != True:
                print(" 5 : ?????????????????????????????????")
                print('\n')
            else:
                print(" 5 : How do you know Magdalena?")
                print('\n')

        
        print(" 0 : To exit")
        question = input(":")
        print('\n')
        if question != '1':
            if question != '2':
                if question != '3':
                    if question != '4':
                        if (question != '5'):
                            if question == '0':
                                done = False
                                LivingRoom()
                            else:
                                print("That is an Invalid input, please put one of the valid options.")
                                print('\n')
                                done = False
                        else:
                            if person == 'Rachel':
                                if (Q1Rachel == True and PhoneFound == True):
                                    print(Script[4] + '\n')
                                else:
                                    print("You don't know what to say, you begin to think of a different question.")
                            else:
                                print("That is an Invalid input, please put one of the valid options.")
                                done = False
                            print('\n')
                    else:
                        print(Script[3] + '\n')
                        if person == "Rachel":
                            Q4Rachel = True       



                else:
                    
                    if person =="Max":
                        if Inspected_Max == True:
                            print(Script[2] + '\n')
                            Q3Max = True
                        else:
                            print("You fail to formulate a question. You just stare at Max, he begins to feel uncomfortable and you begin to feel awkward. In order to break this feeling, you begin to think of a different question.")
                        print('\n')

                    if person == "Cameron":
                        if  (Framed_Picture_Checked == True and Q4Jake == True):
                            print(Script[2] + '\n')
                            Q3Cameron = True
                        else:
                            print("You just fondle your chin whilst trying to think of a question , you come up with nothing. Cameron begins to question your skills as a detective. You begin to think of another question to ask.")
                    print('\n')
                            
                    if person == "Fredrick":
                        print(Script[2] + '\n')
                        print('\n')


                        
                    if person == "Rachel":
                        if (Knife_Rack_Checked == True and Q2Rachel == True):
                            print(Script[2] + '\n')
                            Q3Rachel = True
                        else:
                            print("You just begin to ponder about this situation but you cannot create a question. Rachel seems to traumatise to care about this. You begin to think of another question ask her.")
                        print('\n')
                        
                            
                    if person == "Jake":
                        if (Knife_Rack_Checked == True and(Q4Rachel == True and Q2Max == True)):
                            print(Script[2] + '\n')
                        else:
                            print("Jake looks at you as you try and ask a question, you become intimidated and turn around due to you not knowing what to ask. You begin to think of a different question to ask him.")
                        print('\n')



                        
            else:
                if person =="Max":
                    print(Script[1] + '\n')
                    Q2Max = True
                if person =="Rachel":
                    print(Script[1] + '\n')
                    Q2Rachel = True
                if person =="Jake":
                    print(Script[1] + '\n')
                    Q2Jake = True
                if person =="Fredrick":
                    print(Script[1] + '\n')
                    Q2Fredrick = True
                if person =="Cameron":
                    print(Script[1] + '\n')
                    Q2Cameron = True
        else:
            if person =="Max":
                print(Script[0] + '\n' )
                Q1Max = True
            if person =="Rachel":
                print(Script[0] + '\n' )
                Q1Rachel = True
            if person =="Jake":
                print(Script[0] + '\n' )
                Q1Jake = True
            if person =="Fredrick":
                print(Script[0] + '\n' )
                Q1Fredrick = True
            if person =="Cameron":
                print(Script[0] + '\n' )
                Q1Cameron = True
        done = False
            
                        
                    
                                































#-----------------------------------------------------------------------------ROOM FUNCTIONS-------------------------------------------------------------------------------------------------------------------------------------
def LivingRoom():
    val = print(" You are in the Living Room")
    done = False
    while done != True:
        val = input("What will you do? \n 1 : Interrogate the Suspects  \n 2 : Inspect the Suspects \n 3 : Arrest a Suspect \n 4 : Move to a different Room \n : ")
        if val != '1':
            if val != '2':
                if val != '3':
                    if val != '4':
                        print("That is not a valid input, please try again.")
                    else:
                        done = True
                        Moving()
                else:
                    done = True
                    Arrest()
            else:
                done = True
                PersonID = input("Who will you Interrogate?  \n 1 : Max  \n 2 : Rachel \n 3 : Cameron \n 4 : Fredrick \n 5 : Jake \n :")
                Inspect(PersonID)
        else:
            done = True
            PersonID = input("Who will you Interrogate?  \n 1 : Max  \n 2 : Rachel \n 3 : Cameron \n 4 : Fredrick \n 5 : Jake \n :")
            Interrogate(PersonID)

    

#----------------------------------------------------------------------------INVESTIGATE ITEMS-------------------------------------------------------------------

def Investigate():
    global Current_Room
    global Mirror_Counter
    global Banana_Counter
    global Couch_Counter
    global Pantry_Door_Unlocked
    global Item_found
    global CorpseFound
    global PhoneFound
    global Ending
    global Inspected_Max
    global Knife_Rack_Checked
    global Framed_Picture_Checked
    global Entered_Living_Room
    global Shattered_Glass
    global Spoon_Counter
    global BreadFound
    global KeyFound
    
    if Current_Room == 'Hall':
        
        done = False
        while done != True:
            ans = input("The are few items that stick out here, what will you investigate? \n 1 : Coat \n 2 : Shoe Cabinet \n 3 : Party Invitations \n 4 : Key Rack \n 5 : Framed Picture \n 6 : Back Off \n :") 
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            if ans != '5':
                                if ans != '6':
                                    print("That is not a valid input, please try again.")
                                else:
                                    done = True
                                    Menu()
                            else:
                                val = "Framed Picture"
                        else:
                            val = "Key Rack"
    
                    else:
                        val = "Party Invitations"                  

                else:
                    val = "Shoe Cabinet"
            else:
                val = "Coat"
            
            for MainKey,Subkey in locations.items():
                if MainKey == 'Hall':
                    outcome = Subkey[val]
            if val == "Framed Picture":
                if Entered_Living_Room == True:
                    print(outcome[1])
                    Framed_Picture_Checked = True
                else:
                    print(outcome[0])
            else:
                print(outcome)


                    
    if Current_Room == 'Front Door':
        done = False
        while done != True:
            ans = input("There doesn't seem to be much here, what do you want to look? \n 1 : Nothing \n 2 : More Nothing \n 3 : Even More Nothing \n 4 : Exit \n :")
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            print("That is not a valid input, please try again.")
                        else:
                            done = True
                            Menu()
                    else:
                        val = "Even_More_Nothing"
                else:
                    val = "More_Nothing"
            else:
                val = "Nothing"
        for MainKey,Subkey in locations.items():
            if MainKey == 'Front Door':
                outcome = Subkey[val]
        print(outcome)


        

    if Current_Room == 'Kitchen':
        done = False
        while done != True:
            ans = input("There are a lot of sharp objects in here, what do you want to look? \n 1 : Shattered Glass \n 2 : Knife Rack \n 3 : Mirror \n 4 : Sink \n 5 : Bananas \n 6 : Exit \n :")
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            if ans != '5':
                                if ans != '6':
                                    print("That is not a valid input, please try again.")
                                else:
                                    done = True
                                    Menu()
                            else:
                                val = "Bananas"
                        else:
                            val = "Sink"
                    else:
                        val = "Mirror"
                else:
                    val = "Knife_Rack"
                    Knife_Rack_Checked = True
            else:
                val = "Shattered_Glass"
        
        for MainKey,Subkey in locations.items():
            if MainKey == 'Kitchen':
                outcome = Subkey[val]
                
        if val != "Bananas":
            if val != "Mirror":
                if val != "Shattered_Glass":
                    print(outcome)
                else:
                    if Shattered_Glass == 2:
                        Shattered_Glass = 0
                        print(outcome[Shattered_Glass])
                        Shattered_Glass += 1
                        Ending()
                    else:
                        print(outcome[Shattered_Glass])
                        Shattered_Glass += 1
            else:
                if Mirror_Counter == 6:
                    print(outcome[Mirror_Counter])
                    Mirror_Counter += 1
                    print("You have achieved the " + outcome[Mirror_Counter])
                    Ending()
                else:
                    print(outcome[Mirror_Counter])
                    Mirror_Counter += 1
        else:
            if Banana_Counter == 6:
                print(outcome[Banana_Counter])
                Banana_Counter += 1
                print("You have achieved the " + Banana_Counter)
                Ending()
            else:
                print(outcome[Banana_Counter])
                Banana_Counter += 1

        
    if Current_Room == 'Dining Room':
        done = False
        while done != True:
            ans = input("The layout of the room has three items that stand out, what do you want to look? \n 1 : Candle \n 2 : Spoon \n 3 : Phone \n 4 : Exit \n :")
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            print("That is not a valid input, please try again.")
                        else:
                            done = True
                            Menu()
                    else:
                        val = "Phone"
                        PhoneFound = True
                else:
                    val = "Spoon"
            else:
                val = "Candle"
        for MainKey,Subkey in locations.items():
            if MainKey == 'Dining Room':
                outcome = Subkey[val]
        if val != "Spoon":
            print(outcome)
        else:
            if "Spoon" == 6:
                print(outcome[Banana_Counter])
                Banana_Counter += 1
                print("You have achieved the " + outcome[Banana_Counter])
                Ending()
            else:
                print(outcome[Banana_Counter])
                Banana_Counter += 1
                

    if Current_Room == 'Pantry':
        done = False
        while done != True:
            print("The are few items that stick out here, what will you investigate? \n 1 : Bread \n 2 : Carrots \n 3 : Meat")
            if BreadFound == True:
                ans = input(" 4 : ??????? \n 5 : Exit \n :")
            else:
                ans = input(" 4 : Exit \n :") 
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            if ans != '5':
                                print("That is not a valid input, please try again.")
                            else:
                                if BreadFound == False:
                                    print("That is not a valid input, please try again.")
                                else:
                                    done = True
                                    Menu()
                        else:
                            if BreadFound == True:
                                val = "???????"
                                Item_Found = True
                            else:
                                done = True
                                Menu()
                    else:
                        val = "Meat"                  
                else:
                    val = "Carrots"
            else:
                val = "Bread"
                BreadFound = True
            for MainKey,Subkey in locations.items():
                if MainKey == 'Pantry':
                    outcome = Subkey[val]
            print(outcome)


    if Current_Room == 'Conservatory':
        done = False
        while done != True:
            ans = input("This area seems rather relaxing but dull, what do you want to look at? \n 1 : Plant \n 2 : Couch \n 3 : Table \n 4 : Exit \n :")
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            print("That is not a valid input, please try again.")
                        else:
                            done = True
                            Menu()
                    else:
                        val = "Plant"
                else:
                    val = "Couch"
            else:
                val = "Table"
        for MainKey,Subkey in locations.items():
            if MainKey == 'Conservatory':
                outcome = Subkey[val]
        if val == "Couch":
            if Couch_Counter == 5:
                print(outcome[Couch_Counter])
                Couch_Counter += 1
                print("You have achieved the " + outcome[Couch_Counter])
                Ending()
            else:
                print(outcome[Couch_Counter])
                Couch_Counter += 1
        else:
            print(outcome)
                



    if Current_Room == 'Storage Room':
        done = False
        while done != True:
            ans = input("This place is rather dark and cramped, what do you want to look at? \n 1 : Spider \n 2 : Boxes \n 3 : Exit \n :")
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        print("That is not a valid input, please try again.")
                    else:
                        done = True
                        Menu()
                else:
                    val = "Boxes"
            else:
                val = "Spider"
            for PrimaryKey, SubKey in locations.items():
                if PrimaryKey == "Storage Room":
                    outcome = SubKey[val]
            print(outcome)
        

    if Current_Room == 'Porch':
        done = False
        while done != True:
            ans = input("This porch is rather bare, what do you want to look at? \n 1 : Plant \n 2 : Key \n 3 : Sunglasses \n 4 : Exit \n :")
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            print("That is not a valid input, please try again.")
                        else:
                            done = True
                            Menu()
                    else:
                        val = "Sunglasses"
                else:
                    val = "Key"
                    KeyFound = True
            else:
                val = "Plant"
        for MainKey,Subkey in locations.items():
            if MainKey == 'Porch':
                outcome = Subkey[val]
        print(outcome)


    if Current_Room == 'Garden':
        done = False
        while done != True:
            print("This garden looks just like any other except from one thing, what will you investigate? \n 1 : Plants \n 2 : Rake \n 3 : Footsteps \n 4 : Corpse \n 5 : Exit")
            if ans != '1':
                if ans != '2':
                    if ans != '3':
                        if ans != '4':
                            if ans != '5':
                                print("That is not a valid input, please try again.")
                            else:
                                done = True
                                Menu()
                        else:
                           val = "Corpse"
                    else:
                        val = "Footsteps"                  
                else:
                    val = "Rake"
            else:
                val = "Plants"
            for MainKey,Subkey in locations.items():
                if MainKey == 'Garden':
                    outcome = Subkey[val]
            if val == 'Corpse':
                search = False
                while search != True: 
                    part = input("What part of the corpse are you going to be Investigating? \n 1 : Pockets \n 2 : Head \n 3 : Chest \n 4 : Hands \n  5 : Exit")
                    if part != '1':
                        if part != '2':
                            if part != '3':
                                if part != '4':
                                    if part != '5':
                                        print("That is not a valid input, please try again")
                                    else:
                                        search = True
                                else:
                                    print(outcome[3])
                            else:
                                print(outcome[2])
                        else:
                            print(outcome[1])
                    else:
                        print(outcome[0])
                    


    if Current_Room == 'Living Room':
        print("There is no items to Investigate here.")
        Menu()

def Ending():
    global Couch_Training 
    global Spoon_Ending
    global Mirror_Ending
    global Arrested_Max
    global Arrested_Fredrick
    global Arrested_Rachel
    global Arrested_Jake
    global Arrested_Cameron
    
    if Mirror_Ending != True:
        if Spoon_Ending != True:
            if Couch_Training != True:
                if Arrested_Max != True:
                    if Arrested_Fredrick != True:
                        if Arrested_Rachel != True:
                            if Arrested_Cameron != True:
                                print("You stare at Jake with shock, everybody is flabbergasted at him. The atmosphere begins so tense that you can barely put on the handcuffs. \n As you walk him to the car you hear crying accompanied with cursing that was aim at Jake")
                                print("You bring him to the station, he seems to be lifeless and cold. \n You throw him into a cell whilst showing the confession to your superior. \n You are told that you have done a good job and that you may take the rest of the night off to recover from this traumatising experience.")
                                print(" You have gotten the Arrested Jake Ending")
                                
                            else:
                                print(' You put the handcuffs onto Cameron as they plead for you not to do this. \n Cameron tries to convince you that you have arrested the wrong person although you just think they are talking tripe. \n When you get to the station you put the suspect into a Cell to wait for questioning.')
                                print(" A few moments later, your superior tells you that there is another case for you to solve. It is another murder..... at the same house.")
                        else:
                            print(' You put the handcuffs onto Rachel as they plead for you not to do this. \n Rachel tries to convince you that you have arrested the wrong person although you just think they are talking tripe. \n When you get to the station you put the suspect into a Cell to wait for questioning.')
                            print(" A few moments later, your superior tells you that there is another case for you to solve. It is another murder..... at the same house.")
                    else:
                        print(' You put the handcuffs onto Fredrick as they plead for you not to do this. \n Fredrick tries to convince you that you have arrested the wrong person although you just think they are talking tripe. \n When you get to the station you put the suspect into a Cell to wait for questioning.')
                        print(" A few moments later, your superior tells you that there is another case for you to solve. It is another murder..... at the same house.")
                                
                else:
                    print(' You put the handcuffs onto Max as they plead for you not to do this. \n Max tries to convince you that you have arrested the wrong person although you just think they are talking tripe. \n When you get to the station you put the suspect into a Cell to wait for questioning.')
                    print(" A few moments later, your superior tells you that there is another case for you to solve. It is another murder..... at the same house.")
            else:
                print("Congratulations you have achieved a secret ending!")
        else:
           print("Congratulations you have achieved a secret ending!")
    else:
        print("Congratulations you have achieved a secret ending!")

        
    print("Please try to get another ending, you can get of a total of 8 different Endings!")





def Start():
    print(" You are a detective in a rural small village where normally nothing happens. \n The biggest crime that has been committed since you joined the force was when there was a robbery at the post office. \n Today however, you got called to a house around 11 o'clock at night")
    print(" When you are travelling to the house, you begin to wonder why would this happen. \n Why would someone would commit murder? \n This is the first time you ever had to deal with a murder case. You are alone, no one is there to help you. \n Only you can solve this case...")
    print(" When you arrive at the house, you see that the house is just like every other house in the area. \n The house has a red exterior paint with a grey slate tile roof. \n The front lawn is cut pristinely cut and the walkway to the door has no dirt upon it except from two burnt out ciggarrette butts.")
    print(" As you enter you begin to think of what you should do.")
    Menu()



          
def Menu():
    global Current_Room
    print("You are in the" , Current_Room)
    done = False
    while done != True:
        ans = input(" \n What will you do? \n 1 : Move to another room \n 2 : Investigate \n :")
        if ans != '1':
            if ans != '2':
                print("That is not a valid input. Please try again")
            else:
                done = True
                Investigate()
        else:
            done = True
            Moving()
            
    



Start()    
