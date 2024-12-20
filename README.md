<<<<<<< HEAD
The program "restaurant.py" outputs the console UI for a Restaurant Management System™, which lets the server take orders.
It's made up of many functions with lots of different features that I will describe in the following paragraphs.

Setup() This function asks for input necessary for setup (in this case the number of tables the restaurant has).

    This function is very easily customizable, if the restaurant happens to need more setup 
    variables. It doesn't let a server accidentally input table 400/ will let them know when
    they input a number greater (& below 0 ) than the number of tables the restaurant has.


Main() is the mother function that welcoms the user and prints the necessary commands to set up 
the system before actual use by calling the setup() function when "!setup" is input.
     
    Elif when "!order" is input, it calls the take_order() function.
    
    Elif when "!exit" is input, it breaks the program. 
    
    For breaking inside the take_order() function the user has to input "quit".
    
    It doesn't carry any parameters.

class Order: 
This class is mainly there to define the structure of the order object. It includes the param 
meal_index for the index of each item on the imported menu, that works like an index, and the 
table another class that I explain down below in its own docstring. Both params are defined as
integers.

    The class includes four methods: 
    1. __init__
    2. __str__
    3. create_invoice
    4. add_special_request

class Table:
Initializes the table class. Saves a number, and is used inside the order function.

The take_order function does the actual work:
This function lets the user take an order as the name suggests.
    It guides the user through a bunch of questions:
    
    1. What table is the order for?
    2. Prints the entire menu with corresponding keys.
    3. Asks for the key of the order.
    4. Returns the order summary and asks if the customer has any special requests.
    Keeps asking for special requests until 'done' is input.
    5. Asks if that's all.
    6. Calculates the total and prints summary. Asks if the user wants to edit something.
    7. Prints final invoice. Saves it in the .txt file.
    
       
    It uses both classes and the create_invoice() function.

To use this program, a Python interpreter version 3.10 or newer must be installed, along with the libraries and support programs included in the standard installation from [www.python.org](http://www.python.org).

To start the program, launch `restaurant.py` in the manner appropriate for your operating system, either from the interpreter shell or within an IDE, such as IDLE.

For further information regarding documentation or the user manual, see the analysis.

The current implementation allows for this functionality, but there are potential improvements. One suggestion is to always provide the ability to overwrite everything (e.g., a special request could increase the price by one euro since ingredients might be replaced, and it's generally important to allow everything in such a program to be overwritten when necessary). Additionally, it could be possible to include a feature to request tips and calculate percentages for them.

At present, no bugs are known.
=======
I deserve a job for this masterpiece.
>>>>>>> b8dbbcba90ba33f0bf2420b416fe92fe9b21de58
