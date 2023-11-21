# Randocise
An application that allows a user to pick a random exercise and narrow down to specific categories if desired.


                                                         ***French Translation Microservice Communication Contract***
1. To request data from the microservice, the user will call the function getFrench(level) with level being the level they want a French word for.
   The microservice must be running and the client-side code must be a part of the user's program code content.
   
   Example: (User wants "level_one_to_five" test_1 = getFrench("level_one_to_five")
   microservice will then return:[French word, tranlsation, wrong translation 1, wrong translation 2] for the variable test1
   
2. The user will receive data from the variable they use to call the getFrench(level) function. From there, the user will have the workable list descibed above.

3. THe UML Diagram is as follows:
![image](https://github.com/Gabes33/Randocise/assets/83144560/59ef6e1c-c74c-4f48-ab16-ee890aa79387)
