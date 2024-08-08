# ADR_Manager_Application
The ADR Manager is a Python-based GUI application designed to facilitate the management of Architectural Decision Records. It allows users to input, save, and clear ADR details through an intuitive graphical interface.
Features
    1. Title: Input field for the ADR title.
    2. Date: Input field for the date, defaulting to the current date but allowing user modifications.
    3. Status: Input field for the ADR status.
    4. Context: Text area for describing the context of the decision.
    5. Decision: Text area for detailing the decision made.
    6. Consequences: Text area for outlining the consequences of the decision.
    7. Save Button: Saves the entered ADR details to a text file (adrs.txt).

HOW TO RUN:
To run the ADR Manager application, you need to have Python and Tkinter installed on your system. Start by cloning  the source code for the application.ensure all required dependencies are installed by creating a requirements.txt file with the necessary libraries (tkinter, datetime) and running               #tkinter and datetime are the required libraries
pip install -r requirements.txt 
in your terminal.
Once the dependencies are installed, you can execute the script by running 
 <script_name>.py    #file_name
This will launch the ADR Manager GUI, where you can input the title, date, status, context, decision, and consequences of an ADR. After filling in the details, click the "Save ADR" button to save the information to a file. If all fields are correctly filled and the date is in the proper format, a success message will appear, and the form will reset for new entries.
