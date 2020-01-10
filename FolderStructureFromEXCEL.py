
# Reading an excel file using Python
import xlrd
import os

global Level 
global BeginingOfProcess

parent_dir = []
parent_dir = [None] * 20
parent_dir[0] = r"C:/Users/us5608/OneDrive - NAGases/Desktop/Project 4 _ PSO Review/Drawlists"  # r"C:\Users\Andres Camacho\Desktop\PSO"  
Level = 0
BeginingOfProcess = True

# Give the location of the file
loc = r"C:/Users/us5608/OneDrive - NAGases/Desktop/Project 4 _ PSO Review/Drawlists/Final DrawList Uncollapsed Revised.xlsx" # r"C:\Users\Andres Camacho\Desktop\Final DrawList Uncollapsed.xlsx"
print(os.getcwd())

def FindPDF(row,col):
    global Level
    global BeginingOfProcess
   
    print(sheet.cell_value(row,col), end = '   /   ')
    print(sheet.cell_value(row,col+2))
   
    directory = sheet.cell_value(row, col+2)
   
    if directory == "":
        print("Directory is blank.. row ", row)
    else:
   
        print("Level ", Level, parent_dir [Level])
        if col < Level:
            Level = col
         
        path = os.path.join(parent_dir [col - 1], directory)
        if os.path.isdir(path):
            print("Directory exists ", path)
        else:
            print("Create ", path)
            os.mkdir(path)
            if  BeginingOfProcess:
                Level = 1
                BeginingOfProcess = False
            else:
                Level = Level + 1
            parent_dir [Level] = path  
            print("new level  ", Level, "  ", path)
   
   
    return #dont need anything

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 

# Extracting number of rows
print(sheet.nrows)
print(sheet.ncols)
print("\n")


#for i in range(sheet.nrows):

for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print("\n row ", row, "col ", col, "   ", end = '')
       
#         print(sheet.cell_value(row, col), end = '')
        CellValue = sheet.cell_value(row,col)
        if CellValue != "":
            FindPDF(row,col)
            break
           
#   print("\n")