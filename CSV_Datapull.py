import os
import shutil
import xlsxwriter

#import glob
import re
import xlrd
import csv


if os.path.exists('Z:\Andres Camacho\Test.xlsx'):
       os.remove('Z:\Andres Camacho\Test.xlsx')

workbook = xlsxwriter.Workbook('Z:\Andres Camacho\Test.xlsx')

worksheet1 = workbook.add_worksheet('CW1250_090')
worksheet2 = workbook.add_worksheet('CW1250_088')


header_format = workbook.add_format({'bold': True,'bg_color':'gray','font_color':'white'})


Path1 = r"Z:\Andres Camacho\CW1250_090"
Path2 = r"Z:\Andres Camcaho\CW1250_088"



def dope(path):
    
    global row 
    global col 
    global i
    global rowincsv
    row = 0
    col = 0
    i = 0
    rowincsv = 0
    mylist1 = [None]*46
    mylist2 = [None]*251

    if path == Path1:
        worksheet = worksheet1
        mylist = mylist1
    elif path == Path2:
        worksheet = worksheet2
        mylist = mylist2
    
    names = os.listdir(path)

    #sorting list by name to have chronologically

    for file in names: 
        if (file.endswith(".csv")) and ("PE" not in file) and ("R1" not in file): # avoid csv files D dont want to look at
            
            b =file
            result = re.search('Data_log_(.*).csv',b)
            a = result.group(1)
            #print("/n File number is: ", a)
            mylist[int(a)] = file
        
    names = mylist

    comma = workbook.add_format({'num_format': '#,##0'})
    
    worksheet.set_column('A:Z',30)

    worksheet.write(row,col,'Row', header_format)
    worksheet.write(row,col+1,'CSV Row', header_format)
    worksheet.write(row,col+2,'File Name', header_format)
    worksheet.write(row,col+3,'Time Stamp', header_format)
    worksheet.write(row,col+4,'Value', header_format)
    #worksheet.write(row,col+4,'Path',header_format )


    for file in names: # to debug take away brackets in final
        #if (file.endswith(".csv")) and ("PE" not in file) and ("R1" not in file): 
        
        #print(file)
        
        loc = os.path.join(path,file)
        #print(loc)
        rowincsv = 0            
        mycsv= csv.reader(open(loc))

        for csvrow in mycsv:
            rowincsv = rowincsv+1
            text = csvrow[0]
            
            if ("Actual_Data") in text:
                #print(text)
                output = text.split(';')
                #print(output[2])    
                
                if row == 1000000:
                    row = 0
                    col = 0
                    i = i+1
                    
                    worksheet = workbook.add_worksheet('CW1250_088_'+str(i))
                    worksheet.set_column('A:Z',30)
                    worksheet.write(row,col,'Row', header_format)
                    worksheet.write(row,col+1,'CSV Row', header_format)
                    worksheet.write(row,col+2,'File Name', header_format)
                    worksheet.write(row,col+3,'Time Stamp', header_format)
                    worksheet.write(row,col+4,'Value', header_format)
                    print("\nReached "+str(i)+ " million\n")
                    
                row = row+1
                timestamp = output[1]
                value = output[2]
                worksheet.write(row,0,row)   
                worksheet.write(row,1,rowincsv)                       
                worksheet.write(row,2,file)
                worksheet.write(row,3,timestamp)
                worksheet.write(row,4,int(value))
                #worksheet.write_url(row,4,loc)
                #print("Filename:    ",filename, "\n","Row in CSV:    ",csvrow,"\n","Timestamp:    ",timestamp,"\n","Value:    ",value,"\n","loc:  ",loc,"\n\n")   

            elif ("Actual_X_Data") in text:
                #print(text,"\n")
                output = text.split(';')
                #print(output[2])   
                
                if row == 1000000:
                    row = 0
                    col = 0
                    i = i+1
                    worksheet = workbook.add_worksheet('CW1250_088_'+str(i))
                    worksheet.set_column('A:Z',30)
                    worksheet.write(row,col,'Row', header_format)
                    worksheet.write(row,col+1,'CSV Row', header_format)
                    worksheet.write(row,col+2,'File Name', header_format)
                    worksheet.write(row,col+3,'Time Stamp', header_format)
                    worksheet.write(row,col+4,'Value', header_format)
                    print("\nReached "+str(i)+ " million\n")
                
                row = row+1
                timestamp = output[1]
                value = output[2]
                worksheet.write(row,0,row)   
                worksheet.write(row,1,rowincsv)                       
                worksheet.write(row,2,file)
                worksheet.write(row,3,timestamp)
                worksheet.write(row,4,int(value))
                #worksheet.write_url(row,4,loc)
                #print("Filename:    ",filename, "\n","Row in CSV:    ",csvrow,"\n","Timestamp:    ",timestamp,"\n","Value:    ",value,"\n","loc:  ",loc,"\n\n")   
            
    return  

print("\nWorking on Folder 1...\n")
dope(Path1)
print("\nWorking on Folder 2...\n")
dope(Path2)

workbook.close()
print ("done")
