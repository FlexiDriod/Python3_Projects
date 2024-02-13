☑ Command-Line To-Do List with Python  

____________________________________________________________________________________________________________________________________________________________________________

➡ Tools:


✔ Python: 

                Versatile programming language used for the project's functionality
                
✔ Dictionaries:

                Data structures storing tasks as key-value pairs (task number -> description & completion status)
                
✔ "rich" library: 

                Adds color and formatting to the command-line interface for visual appeal
___________________________________________________________________________________________________________________________________________________________________________

➡ Steps and Efficiency:


✔ Initialization:

        A ToDoList class is created with an empty dictionary (all_tasks) to store tasks.
        
✔ User interaction:

        A loop presents a colorful menu with numbered options for adding, marking complete, viewing tasks, and exit. User input is validated for valid choices.
        Validate user input based on valid choices (1-4).
        Route user actions based on their choice (add, mark complete, view, or exit).
        
✔ Adding tasks:

        Assign a unique key based on dictionary size, checking if it's already taken and added with their description and initial "incomplete" status.
        Display a confirmation message based on successful addition.
        A confirmation message in blue indicates successful addition.
        
✔ Marking completion:

        User specifies the task number. 
        Check if the task number exists in the dictionary.
        If found, the task's "completed" status is set to True, and a green message confirms the update. 
        If not found, a red message indicates the task number doesn't exist.
        
✔ Viewing tasks:

        Check if there are tasks, in the dictionary (not empty).
        If tasks exist, display a header and iterate over them, showcasing its number, description, and completion status (red for incomplete, yellow for complete).
        If no tasks are present, a red message indicates an empty list.
        
✔ Exit:

        Check if the chosen option is "exit".
        If true, display a message and terminate the program.
        
____________________________________________________________________________________________________________________________________________________________________________
