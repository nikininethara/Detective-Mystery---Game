print("Welcome, Detective.")
print("A valuable diamond has disappeared from the city museum")
print("The diamond was displayed in a locked glass case")
print("The museum was closed when the diamond disappeared")
print("You have been called to investigate")
print("You arrive at the museum")
print("The front doors are open")

evidence= []
while True:
    print("Inside, you see three areas:")
    print("1. Exhibition Room")
    print("2. Security Room")
    print("3. Storage Room")
    print("4. Check Evidence Notebook")
    print("5. Review Investigation")
    print("6. Investigate Suspects")
    print("7. Analyze the Evidence")
    print("8. Make Final Accusation")

    choice1 = "1"
    choice2 = "2"
    choice3 = "3"
    choice44 = "4"
    choice45 = "5"
    choice46 = "6"
    choice47 = "7"
    choice48 = "8"

    choice_0 = input("Where do you want to investigate?   ")

    if choice_0 == choice1:
        print("You enter the Exhibition Room")
        print("The diamond was displayed here")
        print("The room is quiet")
        print("You walk toward the place where the diamond was displayed")
        print("You see an empty glass display case")
        print("The case is still locked")

        print("You notice three things that may be important:")
        print("1. The glass display case")
        print("2. Security seal")
        print("3. The floor around the display case")
        print("4. Leave the Exhibition Room")

        choice4 = "1"
        choice5 = "2"
        choice6 = "3"
        choice7 = "4"

        choice_1 = input("What do you want to investigate?   ")

        if choice_1 == choice4:
            print("You examine the glass display case")
            print("The glass is not broken")
            print("The lock is still intact")
            print("There are no obvious signs that the case was forced open")
            print("Something about this seems strange")
            if "The glass display case is still locked" not in evidence:
                evidence.append("The glass display case is still locked")

        elif choice_1 == choice5:
            print("You examine the security seal")
            print("The seal has been broken")
            print("There is a small mark on the broken piece")
            print("It looks like part of a number")
            if "The security seal was broken and had a number mark" not in evidence:
                evidence.append("The security seal was broken and had a number mark")

        elif choice_1 == choice6:
            print("You examine the floor around the display case")
            print("You notice a small muddy footprint")
            print("It leads away from the display case toward the hallway")
            print("The footprint is too small to identify the person")
            if "A small muddy footprint was found near the display case" not in evidence:
                evidence.append("A small muddy footprint was found near the display case")

        elif choice_1 == choice7:
            print("You leave the Exhibition Room")

    elif choice_0 == choice2:
        print("You enter the Security Room")
        print("Several security monitors are still running")
        print("A security desk is covered with papers")

        print("You see:")
        print("1. Security cameras")
        print("2. Security log")
        print("3. Security desk")
        print("4. Leave the Security Room")

        choice8 = "1"
        choice9 = "2"
        choice10 = "3"
        choice11 = "4"

        choice_2 = input("What do you want to investigate?  ")

        if choice_2 == choice8:
            print("You check the security cameras")
            print("The camera facing the Exhibition Room stopped recording at 10:15 PM")
            print("The other cameras continued working")
            print("You notice that the camera cable has been disconnected")
            if "The Exhibiton Room camera cable was disconnected" not in evidence:
                evidence.append("The Exhibiton Room camera cable was disconnected")

        elif choice_2 == choice9:
            print("You examine the security log")
            print("The last recorded entries are:")
            print("9:40 PM - Security Guard entered the Exhibition Room")
            print("9:55 PM - Museum Cleaner entered the hallway")
            print("10:05 PM - Curator entered the Exhibition Room")
            print("10:15 PM - Exhibition Room camera stopped recording")
            if "The security log shows the guard, cleaner and curator entered before the camera" not in evidence:
                evidence.append("The security log shows the guard, cleaner and curator entered before the camera")

        elif choice_2 == choice10:
            print("You search the security desk")
            print("You find a handwritten note")
            print("The note says:")
            print("The spare security-card was returned at 10:20 PM")
            if "The spare security-card was returned at 10:20 PM" not in evidence:
                evidence.append("The spare security-card was returned at 10:20 PM")

            print("You find another security record")
            print("The record shows the security access codes assigned to staff")
            print("The number on the broken security seal matches the Curator's security access code.")
            if "The number on the broken security seal matches the Curator's security access code." not in evidence:
                evidence.append("The number on the broken security seal matches the Curator's security access code.")
            
        elif choice_2 == choice11:
            print("You leave the Security Room")

    elif choice_0 == choice3:
        print("You enter the Storage Room")
        print("The room is crowded with boxes and old museum equipment")

        print("You look around and see:")
        print("1. A cleaning cart")
        print("2. A locked cabinet")
        print("3. Several storage boxes")
        print("4. Leave the Storage Room")

        choice12 = "1"
        choice13 = "2"
        choice14 = "3"
        choice15 = "4"

        choice_3 = input("What do you want to investigate?  ")

        if choice_3 == choice12:
            print("You examine the cleaning cart")
            print("There are several cleaning supplies inside")
            print("You notice a small piece of blue fabric caught on the side of the cart")
            if "A piece of blue fabric was found on the cleaning cart" not in evidence:
                evidence.append("A piece of blue fabric was found on the cleaning cart")

        elif choice_3 == choice13:
            print("You examine the locked cabinet")
            print("The cabinet has a small keyhole")
            print("You cannot open it yet")
            print("You notice a label on the cabinet:") 
            print("'Security Equipment'")
            if "The locked cabinet is labelled 'Security Equipment'" not in evidence:
                evidence.append("The locked cabinet is labelled 'Security Equipment'")

        elif choice_3 == choice14:
            print("You search the storage boxes")
            print("Most of them contain old museum supplies")
            print("One box is different.")
            print("Inside, you find an empty security-card holder.")
            print("There is a name written on the holder:")
            print("'Security Department'")
            if "An empty security-card holder marked 'Security Department' was found" not in evidence:
                evidence.append("An empty security-card holder marked 'Security Department' was found")

        elif choice_3 == choice15:
            print("You leave the Storage Room")
    
    elif choice_0 == choice44:
        print("Evidence Notebook")
        print(evidence)

    elif choice_0 == choice45:
        print("You review the evidence you have collected")
        length = len(evidence)
        if length < 3:
            print("You don't have enough evidence yet. Continue investigating")
        else:
            print("You have collected enough evidence to begin connecting the clues")

    elif choice_0 == choice46:
        length = len(evidence)
        if length < 3:
            print("You don't have enough evidence yet. Continue investigating")
            print("Collect at least 3 pieces of evidence first")
        else:
            print("You have collected enough evidence to begin connecting the clues")
            print("There are 3 people who could have stolen the diamond")
            print("The 3 suspects are: ")
            print("1. Security Guard")
            print("2. Museum Cleaner")
            print("3. Curator")

            choice51 = "1"
            choice52 = "2"
            choice53 = "3"
            choice_5 = input("Who do you want to investigate first? ")

            if choice_5 == choice51:
                print("The Security Guard entered the Exhibiton Room at 9:40 PM")
                print("The Exhibiton Room camera stopped recording at 10:15 PM")
                print("The spare security-card was returned at 10:20 PM")
            elif choice_5 == choice52:
                print("The Museum Cleaner entered the hallway at 9:55 PM")
                print("A piece of blue fabric was found on the cleaning cart")
                print("A muddy footprint was found near the display case")
            elif choice_5 == choice53:
                print("The Curator entered the Exhibition Room at 10:05 PM")
                print("The Curator was inside shortly before the camera stopped recording")
                print("The security seal was found broken")

    elif choice_0 == choice47:
        length = len(evidence)
        if length < 3:
            print("You don't have enough evidence yet. Continue investigating")
            print("Collect at least 3 pieces of evidence first")
        else:
            print("You have collected enough evidence to begin connecting the clues")
            print("Who had access to the Exhibiton Room?")
            print("1. Security Guard")
            print("2. Museum Cleaner")
            print("3. Curator")

            choice61 = "1"
            choice62 = "2"
            choice63 = "3"
            analysis_choice1 = input("Enter your choice:  ")
            if analysis_choice1 == choice61:
                print("Incorrect!")
            elif analysis_choice1 == choice62:
                print("Incorrect!")
            elif analysis_choice1 == choice63:
                print("Correct!")
                print("The Curator had access to the Exhibiton Room because the Curator entered the room at 10:05 PM")
            else:
                print("Invalid choice!")

            print("Who could have been near the security camera?")
            print("1. Security Guard")
            print("2. Museum Cleaner")
            print("3. Curator")

            choice71 = "1"
            choice72 = "2"
            choice73 = "3"
            analysis_choice2 = input("Enter your choice:  ")
            if analysis_choice2 == choice71:
                print("Correct!")
                print("The Security Guard could have been near the security camera becuase the guard was responsible for museum security")
            elif analysis_choice2 == choice72:
                print("Incorrect!")
            elif analysis_choice2 == choice73:
                print("Incorrect!")
            else:
                print("Invalid choice!")

            print("Who is connected to the blue fabric / muddy footprint? ")
            print("1. Security Guard")
            print("2. Museum Cleaner")
            print("3. Curator")

            choice81 = "1"
            choice82 = "2"
            choice83 = "3"
            analysis_choice3 = input("Enter your choice:  ")
            if analysis_choice3 == choice81:
                print("Incorrect!")
            elif analysis_choice3 == choice82:
                print("Correct!")
                print("The Museum Cleaner is connected to the blue fabric because the fabric was found on the cleaning cart")
                print("The muddy footprint could also be connected to the cleaner becuase the cleaner works around the museum")
            elif analysis_choice3 == choice83:
                print("Incorrect!")
            else:
                print("Invalid choice!")

    elif choice_0 ==choice48:
        length = len(evidence)
        if length < 3:
            print("You do not have enough evidence to make a final accusation.")
            print("Continue investigating before making your final decision")
        else:
             print("You have reviewed the evidence. Who do you accuse of stealing the diamond")
             print("1. Security Guard")
             print("2. Museum Cleaner")
             print("3. Curator")

             choice91 = "1"
             choice92 = "2"
             choice93 = "3"
             accusation = input("Enter your decision:  ")

             if accusation == choice91:
                 print("Your accusation is incorrect :[ ")
             elif accusation == choice92:
                 print("Your accusation is incorrect :[ ")
             elif accusation == choice93:
                 if analysis_choice1 == choice63 and analysis_choice2 == choice71 and analysis_choice3 == choice82:
                     print("Your accusation is correct!!! :) ")
                     print("Becuase all the 3 people had some connection to the crime, but the one who has the strongest combination of evidence is the Curator.")
                     print("The Curator is connected to the Exhibiton Room and the security-seal number/accesscode.")
                     print("Congratulations, Detective! You solved the case.")
                     print("The investigation is complete")
                 else:
                     print("Your accusation is not fully supported by your analysis")
                     print("Review the evidence and analyze the clues again.")
                 break

    else:
        print("That's not a valid area")