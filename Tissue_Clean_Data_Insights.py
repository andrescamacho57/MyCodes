import os
import shutil
import xlsxwriter

#import glob
import re
import xlrd
import csv
import numpy as np


filepath = r"C:\Users\Andres Camacho\Desktop\Other\PATIENT_LISTS.xlsx"

loc = r"C:\Users\Andres Camacho\Desktop\Desktop\S_P AND TISSUE BIOBANK.xlsx" 



if os.path.exists(filepath):

       os.remove(filepath)



workbook = xlsxwriter.Workbook(filepath)



worksheet1 = workbook.add_worksheet('Tissue(1), Plasma (1-4)')

worksheet2 = workbook.add_worksheet('Tissue(1), Plasma (5-9)')

worksheet3 = workbook.add_worksheet('Tissue(1), Plasma (10+)')

worksheet4 = workbook.add_worksheet('Tissue(+), Plasma (0)')

worksheet5 = workbook.add_worksheet('Tissue(0), Plasma (+)')


worksheet1.set_column('A:Z',30)

worksheet2.set_column('A:Z',30)

worksheet3.set_column('A:Z',30)

worksheet4.set_column('A:Z',30)

worksheet5.set_column('A:Z',30)



header_format = workbook.add_format({'bold': True,'bg_color':'gray','font_color':'white'})



worksheet1.write(0,0,'Patient', header_format)

worksheet1.write(0,1,'Tissue', header_format)

worksheet1.write(0,2,'S/P', header_format)

worksheet1.write(0,3,'Tissue DATES', header_format)

worksheet1.write(0,4,'S/P DATES', header_format)

worksheet1.write(0,5,'Follow up Month', header_format)



worksheet2.write(0,0,'Patient', header_format)

worksheet2.write(0,1,'Tissue', header_format)

worksheet2.write(0,2,'S/P', header_format)

worksheet2.write(0,3,'Tissue DATES', header_format)

worksheet2.write(0,4,'S/P DATES', header_format)

worksheet2.write(0,5,'Follow up Month', header_format)


worksheet3.write(0,0,'Patient', header_format)

worksheet3.write(0,1,'Tissue', header_format)

worksheet3.write(0,2,'S/P', header_format)

worksheet3.write(0,3,'Tissue DATES', header_format)

worksheet3.write(0,4,'S/P DATES', header_format)

worksheet3.write(0,5,'Follow up Month', header_format)


worksheet4.write(0,0,'Patient', header_format)

worksheet4.write(0,1,'Tissue', header_format)

worksheet4.write(0,2,'S/P', header_format)

worksheet4.write(0,3,'Tissue DATES', header_format)

worksheet4.write(0,4,'S/P DATES', header_format)

worksheet4.write(0,5,'Follow up Month', header_format)


worksheet5.write(0,0,'Patient', header_format)

worksheet5.write(0,1,'Tissue', header_format)

worksheet5.write(0,2,'S/P', header_format)

worksheet5.write(0,3,'Tissue DATES', header_format)

worksheet5.write(0,4,'S/P DATES', header_format)

worksheet5.write(0,5,'Follow up Month', header_format)



# To open Workbook 

wb = xlrd.open_workbook(loc) 

sheet = wb.sheet_by_index(0) 

  
# Extracting number of rows 

print("\nRows: ",sheet.nrows) 

print("\n")


#for i in range(sheet.nrows): 

global i
global j
global k
global l
global m

i = 0
j = 0
k = 0
l = 0
m = 0

b = [] 

c = []

Plist = []


for row in range(sheet.nrows):

    b.append(str(sheet.cell_value(row,3)))



for row in range(sheet.nrows):

    c.append(str(sheet.cell_value(row,5)))

x = np.array(b)

Plist = np.unique(x)

# Extracting number of rows 

print("\nRows: ",len(Plist)) 

print(Plist)

y = np.array(c)

U2list = np.unique(y)
U2klist = U2list

print(U2klist)

Type1List = [U2list[1], U2list[2], U2list[4],U2list[6]]

print(Type1List)

Type2List = [U2list[0], U2list[5]]

print(Type2List)

# for row in range(sheet.nrows):

#     if str(sheet.cell_value(row,5)) in U2alist:
#         tissuecount = i = i+1

T1 = []
T2 = []
DateList1 =[]
DateList2 =[]
PD1List = []
PD2List = []

for Patient in Plist:
    Type1Count = 0
    Type2Count = 0
    DateList1 =[] *0
    DateList2 =[] *0
    DateCount = 0

    for row in range(sheet.nrows):
        if Patient == sheet.cell_value(row,3):
            if str(sheet.cell_value(row,5)) in Type1List:
                Type1Count = Type1Count+1
                DateList1.append(sheet.cell_value(row,4))
                
            elif str(sheet.cell_value(row,5)) in Type2List:
                Type2Count = Type2Count +1
                DateList2.append(sheet.cell_value(row,4))

    DateList1 = np.array(DateList1)

    DateList1 = np.unique(DateList1)

    DateList2 = np.array(DateList2)

    DateList2 = np.unique(DateList2) 

    PD1List.append([Patient,len(DateList1)])
    PD2List.append([Patient,len(DateList2)])       

    T1.append(Type1Count)
    T2.append(Type2Count)

    #print("\nPatient:",Patient, "Tissue Count", Type1Count, "Plasma Count", Type2Count,"Unique date Count Tissue", len(DateList1),"Unique date Count Plasma", len(DateList2) )
    
   
    

    if len(DateList1) > 1: 
        if len(DateList2) > 0:
            if len(DateList2) < 5:
                i = i+1
                worksheet1.write(i,0,Patient)

                worksheet1.write(i,1,Type1Count)

                worksheet1.write(i,2,Type2Count)

                worksheet1.write(i,3,len(DateList1))

                worksheet1.write(i,4,len(DateList2))  
    if  len(DateList1) > 1:
        if  len(DateList2) > 4:
            if len(DateList2) <10:
                j = j+1
                worksheet2.write(j,0,Patient)

                worksheet2.write(j,1,Type1Count)

                worksheet2.write(j,2,Type2Count)

                worksheet2.write(j,3,len(DateList1))

                worksheet2.write(j,4,len(DateList2))
    if  len(DateList1) > 1:
        if  len(DateList2) > 9:
            
            k = k+1
            worksheet3.write(k,0,Patient)

            worksheet3.write(k,1,Type1Count)

            worksheet3.write(k,2,Type2Count)

            worksheet3.write(k,3,len(DateList1))

            worksheet3.write(k,4,len(DateList2))

    if  len(DateList1) >0:
        if  len(DateList2) == 0:
            
            l = l+1

            worksheet4.write(l,0,Patient)

            worksheet4.write(l,1,Type1Count)

            worksheet4.write(l,2,Type2Count)

            worksheet4.write(l,3,len(DateList1))

            worksheet4.write(l,4,len(DateList2))

    if  len(DateList2) >0:
        if  len(DateList1) == 0:
            
            m = m+1

            worksheet5.write(m,0,Patient)

            worksheet5.write(m,1,Type1Count)

            worksheet5.write(m,2,Type2Count)

            worksheet5.write(m,3,len(DateList1))

            worksheet5.write(m,4,len(DateList2))


print("\ndone")
workbook.close()