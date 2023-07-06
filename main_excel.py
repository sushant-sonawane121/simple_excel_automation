# this is the application for creating new excl files, editing existing exel files and many more functions;
from genericpath import isfile
import os
from secrets import choice
import openpyxl


# defination for Creating new Excel File
def create_xls_file():
     
    workbook = openpyxl.Workbook()
    name = input("Enter name of your New File: ")
    fname = name+".xlsx"
    
    file_path = os.path.join('./excel_files',fname)
    workbook.save(file_path)
    

#function for despling all excel file form folder
def display_Excel_Files():
     folder_path = './excel_files'
     files = os.listdir(folder_path)
     list_size = len(files)
     for i in range(0,list_size):
         print(i,files[i])

#function for deleting Excel file
def delete_excel_file():
      folder_path = './excel_files'
      files = os.listdir(folder_path)
      list_size = len(files)
      for i in range(0,list_size):
          print(i,files[i])
          
      no = input("Enter File Number to delete: ")
      fno = int(no)
      fname = files[fno]
     
      fpath = "excel_files/"+fname
      if os.path.isfile(fpath):  
         os.remove(fpath)
         print("File Deleted Successfully")
      else:
            print("file not found")
     



while True:
    
    print("-------------------Main Menu-------------------")
    print("1. Create Excel File")
    print("2. Show All Excel files")
    print("3. Delete Existing Exel File")
    print("4. Edit Existing Excel Files")
    print("5. Exit")
    print("------------------------------------------------")
    
    choice  = input("Enter Your Choice: ")
    if choice == "1":
         create_xls_file()
         print("file created successfully")
    elif choice  == "2":
         display_Excel_Files()
    elif choice == "3":
         delete_excel_file()
    elif choice == "4":
         print("File edited successfully")
    elif choice == "5":
         break
    else:
         print("You Entered Wrong Choise")
         option = input("Do you Want to Choose Again y/n: ")
         if option  == "y":
             continue
         elif option == "n":
             break
         
