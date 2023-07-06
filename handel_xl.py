# from openpyxl import Workbook
# import glob
# import os

# def create_excel_file():
#     # Get the desired file name from the user
#     file_name = input("Enter the name for the Excel file: ")

#     # Create a new workbook
#     workbook = Workbook()

#     # Get the active sheet
#     sheet = workbook.active

#     # Update the sheet with some example data
#     sheet['A1'] = 'Hello'
#     sheet['B1'] = 'World!'

#     # Save the workbook with the specified file name
#     workbook.save(file_name + '.xlsx')

#     print(f"Excel file '{file_name}.xlsx' created successfully.")

# # Call the function to create the Excel file
# # create_excel_file() --------------

# def show_existing_excel_files():
#     # Get the current directory
#     current_directory = os.getcwd()

#     # Find all the Excel files in the current directory
#     excel_files = glob.glob(current_directory + "/*.xlsx")

#     # Extract and return the file names
#     file_names = [os.path.basename(file) for file in excel_files]

#     return file_names

# def select_excel_file():
#     # Get the existing Excel file names
#     existing_files = show_existing_excel_files()

#     # Display the names of the existing Excel files
#     print("Existing Excel files:")
#     for index, file_name in enumerate(existing_files):
#         print(f"{index + 1}. {file_name}")

#     # Prompt the user to select a file by index
#     selection = input("Enter the number corresponding to the Excel file: ")

#     try:
#         # Convert the user's selection to an integer
#         selection_index = int(selection) - 1

#         # Check if the selection index is within range
#         if 0 <= selection_index < len(existing_files):
#             # Return the selected file name
#             return existing_files[selection_index]
#         else:
#             print("Invalid selection. Please try again.")
#     except ValueError:
#         print("Invalid input. Please enter a number.")

#     # If an invalid selection was made, return None
#     return None

# # Call the function to get the selected Excel file name
# selected_file = select_excel_file()

# # Check if a file was selected
# if selected_file:
#     print(f"You selected: {selected_file}")
# else:
#     print("No file selected.")

import glob

for name in glob.glob("excel_files/*"):
    print(name)