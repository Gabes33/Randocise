import time
import emoji
import random


class Display:

    def __init__(self):

        print("""   
    ###############################
    WELCOME TO THE RANDOCISE APP!
    ##############################""")

        #time.sleep(2)

        print("""  
    ###############################
            MAIN SCREEN
    ##############################""")

    def get_input(self, min, max):

        user_inp = int(input("Enter here: "))
        while user_inp < int(min) or user_inp > int(max):
            print("Please enter a valid number")
            user_inp = int(input("Enter here: "))

        return user_inp

    def main_page(self):
        main_string_1 = """
        choose and option below to get started!
        Just enter a number on the keyboard and press enter"""

        main_string_2 = """
                 1. Enter
                 2. Exit
                 3. Help
                 4. Random"""

        print(main_string_1.center(20))
        print(main_string_2.center(20))

    def main_screen_help(self):
        print("""
                Main Screen Help
                1. Enter - This starts the application
                2. Exit - This closes the application entirely
                3. Random - Picks a random exercise with any difficulty/category""")


    def exercise_difficulty(self):
        # Citation for the following lines of code to retrieve emoji files:
        # Date: 11/6/2023
        # Copied from:
        # Source URL: https://www.geeksforgeeks.org/python-program-to-print-emojis/

        print("""
        Let's get an exercise in!
        Choose an exercise difficulty, or choose a random one:""")
        print("""
        1. Easy \U0001F600
        2. Challenging \U0001F605
        3. Intermediate \U0001F610
        4. Difficult \U0001F61D
        5. Advanced \U0001F62C
        6. Random
        7. Help
        8. Back""")

    def exercise_difficulty_help(self):
        print("""
        Exercise Difficulty Explanations""")
        print("""
        1. Easy - For people who may have never exercised before, or
                  are looking to try basic exercises
                  
        2. Challenging - For beginners who want to push themselves
                         a little bit more
        
        3. Intermediate - For people who may have been exposed to many
                          typical exercises
        
        4. Difficult - For people who want to push themselves outside of
                       their comfort zone
        
        5. Advanced - For experts looking to push their outer limits
        
        6. Random - Choose a random difficulty!
        
        7. Back - Return to main screen
        """)

    def category(self, level, difficulty):
        print(f"""
        Level {level}: {difficulty}
        Please pick a category or choose random!""")

        print("""
        1. Arms/Shoulders
        2. Abs
        3. Back/Chest
        4. Legs/Glutes
        5. Cardio
        6. Random
        7. Help
        8. Back """)

    def category_help(self):
        print("""
        Category Help and Muscles Targeted""")
        print("""
        1. Arms/Shoulders - biceps, triceps, and deltoids
        2. Abs - abdominal muscles and obliques
        3. Back/Chest - pectoralis, trapezius, latissimus dorsi
        4. Legs/Glutes - quadriceps, hamstrings, gluteus
        5. Cadio - heart, lungs, and circulatory system
        6. Random - a random exercise is chosen for you
        7. Back - choose a new difficulty""")

    def nav_main(self):
        self.main_page()
        main_input = self.get_input(1, 4)
        enter_app = False
        while enter_app is False:
            if main_input == 1:
                enter_app = True
                self.nav_exer_diff()
            if main_input == 2:
                print("""
                        Are you sure you want to exit?"
                        1. Yes
                        2. No""")
                exit_check = program_display.get_input(1, 2)
                if exit_check == 1:
                    print("Thank you for visiting!")
                    main_input = 0
                elif exit_check == 2:
                    self.main_page()
                    main_input = program_display.get_input(1, 4)
            elif main_input == 3:
                program_display.main_screen_help()
                help_input = self.get_input(1, 3)
                if help_input == 1:
                    main_input = 1
                    self.nav_exer_diff()
                    enter_app = True
                elif help_input == 2:
                    main_input = 2
                elif help_input == 3:
                    main_input = 4
            elif main_input == 4:
                enter_app = True
                print("""This will randomize a unique exercise""")

    def nav_exer_diff(self):
        self.exercise_difficulty()
        exer_level = self.get_input(1, 8)
        return_screen = False
        while return_screen is False:
            if exer_level == 1:
                self.category(1, "Easy")
                cat_num = self.get_input(1, 8)
                if cat_num == 1:
                    print("random exercise gets picked")
                    print("placeholder for easy arms/shoulders")
                    return_screen = True
                elif cat_num == 2:
                    print("random exercise gets picked")
                    print("placeholder for easy abs")
                    return_screen = True
                elif cat_num == 3:
                    print("random exercise gets picked")
                    print("placeholder for easy back/chest")
                    return_screen = True
                elif cat_num == 4:
                    print("random exercise gets picked")
                    print("placeholder for easy legs/glutes")
                    return_screen = True
                elif cat_num == 5:
                    print("random exercise gets picked")
                    print("placeholder for easy cardio")
                    return_screen = True
                elif cat_num == 6:
                    print("random exercise with random category gets picked")
                    return_screen = True
                elif cat_num == 7:
                    self.category_help()
                    help_cat_num = self.get_input(1, 7)
                    if help_cat_num == 1 or 2 or 3 or 4 or 5 or 6:
                        print("random exercise with potential random category is picked")
                        return_screen = True
                    if help_cat_num == 7:
                        self.exercise_difficulty()
                        exer_level = self.get_input(1, 8)
                elif cat_num == 8:
                    self.exercise_difficulty()
                    exer_level = self.get_input(1, 8)
            elif exer_level == 2:
                self.category(2, "Challenging")
                cat_num = self.get_input(1, 8)
                if cat_num == 1:
                    print("random exercise gets picked")
                    print("placeholder for challenging arms/shoulders")
                    return_screen = True
                elif cat_num == 2:
                    print("random exercise gets picked")
                    print("placeholder for challenging abs")
                    return_screen = True
                elif cat_num == 3:
                    print("random exercise gets picked")
                    print("placeholder for challenging back/chest")
                    return_screen = True
                elif cat_num == 4:
                    print("random exercise gets picked")
                    print("placeholder for challenging legs/glutes")
                    return_screen = True
                elif cat_num == 5:
                    print("random exercise gets picked")
                    print("placeholder for challenging cardio")
                    return_screen = True
                elif cat_num == 6:
                    print("random exercise with random category gets picked")
                    return_screen = True
                elif cat_num == 7:
                    program_display.category_help()
                    help_cat_num = program_display.get_input(1, 7)
                    if help_cat_num == 1 or 2 or 3 or 4 or 5 or 6:
                        print("random exercise with potential random category is picked")
                        return_screen = True
                    if help_cat_num == 7:
                        self.exercise_difficulty()
                        exer_level = self.get_input(1, 8)
                elif cat_num == 8:
                    self.exercise_difficulty()
                    exer_level = self.get_input(1, 8)
            elif exer_level == 3:
                self.category(3, "Intermediate")
                cat_num = self.get_input(1, 8)
                if cat_num == 1:
                    print("random exercise gets picked")
                    print("placeholder for intermediate arms/shoulders")
                    return_screen = True
                elif cat_num == 2:
                    print("random exercise gets picked")
                    print("placeholder for intermediate abs")
                    return_screen = True
                elif cat_num == 3:
                    print("random exercise gets picked")
                    print("placeholder for intermediate back/chest")
                    return_screen = True
                elif cat_num == 4:
                    print("random exercise gets picked")
                    print("placeholder for intermediate legs/glutes")
                    return_screen = True
                elif cat_num == 5:
                    print("random exercise gets picked")
                    print("placeholder for intermediate cardio")
                    return_screen = True
                elif cat_num == 6:
                    print("random exercise with random category gets picked")
                    return_screen = True
                elif cat_num == 7:
                    self.category_help()
                    help_cat_num = self.get_input(1, 7)
                    if help_cat_num == 1 or 2 or 3 or 4 or 5 or 6:
                        print("random exercise with potential random category is picked")
                        return_screen = True
                    if help_cat_num == 7:
                        self.exercise_difficulty()
                        exer_level = self.get_input(1, 8)
                elif cat_num == 8:
                    self.exercise_difficulty()
                    exer_level = self.get_input(1, 8)
            elif exer_level == 4:
                self.category(4, "Difficult")
                cat_num = self.get_input(1, 8)
                if cat_num == 1:
                    print("random exercise gets picked")
                    print("placeholder for difficult arms/shoulders")
                    return_screen = True
                elif cat_num == 2:
                    print("random exercise gets picked")
                    print("placeholder for difficult abs")
                    return_screen = True
                elif cat_num == 3:
                    print("random exercise gets picked")
                    print("placeholder for difficult back/chest")
                    return_screen = True
                elif cat_num == 4:
                    print("random exercise gets picked")
                    print("placeholder for difficult legs/glutes")
                    return_screen = True
                elif cat_num == 5:
                    print("random exercise gets picked")
                    print("placeholder for difficult cardio")
                    return_screen = True
                elif cat_num == 6:
                    print("random exercise with random category gets picked")
                    return_screen = True
                elif cat_num == 7:
                    self.category_help()
                    help_cat_num = self.get_input(1, 7)
                    if help_cat_num == 1 or 2 or 3 or 4 or 5 or 6:
                        print("random exercise with potential random category is picked")
                        return_screen = True
                    if help_cat_num == 7:
                        self.exercise_difficulty()
                        exer_level = self.get_input(1, 8)
                elif cat_num == 8:
                    self.exercise_difficulty()
                    exer_level = self.get_input(1, 8)
            elif exer_level == 5:
                self.category(5, "Advanced")
                cat_num = self.get_input(1, 8)
                if cat_num == 1:
                    print("random exercise gets picked")
                    print("placeholder for easy arms/shoulders")
                    return_screen = True
                elif cat_num == 2:
                    print("random exercise gets picked")
                    print("placeholder for easy abs")
                    return_screen = True
                elif cat_num == 3:
                    print("random exercise gets picked")
                    print("placeholder for easy back/chest")
                    return_screen = True
                elif cat_num == 4:
                    print("random exercise gets picked")
                    print("placeholder for easy legs/glutes")
                    return_screen = True
                elif cat_num == 5:
                    print("random exercise gets picked")
                    print("placeholder for easy cardio")
                    return_screen = True
                elif cat_num == 6:
                    print("random exercise with random category gets picked")
                    return_screen = True
                elif cat_num == 7:
                    self.category_help()
                    help_cat_num = self.get_input(1, 7)
                    if help_cat_num == 1 or 2 or 3 or 4 or 5 or 6:
                        print("random exercise with potential random category is picked")
                        return_screen = True
                    if help_cat_num == 7:
                        self.exercise_difficulty()
                        exer_level = self.get_input(1, 8)
                elif cat_num == 8:
                    self.exercise_difficulty()
                    exer_level = self.get_input(1, 8)
            elif exer_level == 6:
                exer_level = random.randint(1, 5)
            elif exer_level == 7:
                self.exercise_difficulty_help()
                exer_help_level = self.get_input(1, 7)
                if exer_help_level == 1:
                    exer_level = 1
                elif exer_help_level == 2:
                    exer_level = 2
                elif exer_help_level == 3:
                    exer_level = 3
                elif exer_help_level == 4:
                    exer_level = 4
                elif exer_help_level == 5:
                    exer_level = 5
                elif exer_help_level == 6:
                    exer_level = random.randint(1, 5)
                elif exer_help_level == 7:
                    exer_level = 8
            elif exer_level == 8:
                return_screen = True
                self.nav_main()



if __name__ == "__main__":
    program_display = Display()
    #time.sleep(4)
    program_display.nav_main()

