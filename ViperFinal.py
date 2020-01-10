import os
import shutil
import xlsxwriter

if os.path.exists('test.xlsx'):
       os.remove('test.xlsx')

workbook = xlsxwriter.Workbook('test.xlsx')

worksheet = workbook.add_worksheet('Viper')

header_format = workbook.add_format({'bold': True,'bg_color':'gray','font_color':'white'})

# Add a bold format to use to highlight cells.
#bold = workbook.add_format({'bold': True})



# Add a number format for cells with money.
comma = workbook.add_format({'num_format': '#,##0'})

CurrentPath = r"C:\Users\us5608\OneDrive - NAGases\Desktop"


row = 0
col = 0

worksheet.write(row,col,'Row', header_format)
worksheet.write(row,col+1,'Path', header_format)

worksheet.write(row,col+2,'Number Of Local Files', header_format)
worksheet.write(row,col+3,'Number Of Local Sub-Folders', header_format)
worksheet.write(row,col+4,'Local Sub-Folder Size (Bytes)',header_format )

worksheet.write(row,col+5,'Total Number of Files', header_format)
worksheet.write(row,col+6,'Total Number of Sub-Folders', header_format)
worksheet.write(row,col+7,'Total Folder Size (Bytes)', header_format)


def FolderProperties(path):
    
    global row 
    global col
    
    names = os.listdir(path)
    
    NumberOfFiles = 0
    TotalFolderSize = 0
    NumberOfDir = 0
    NumberOfFilesInSubFolder = 0
    SubFolderSize = 0
    TotNumFiles = 0
    TotNumDir = 0
    Dir = 0

    for file in (names): 
    
        filepath = os.path.join(path, file)
        #print(filepath) 
    
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            #print(file, 'File Size:',size)
           # if size > 1024:
                   #print(size/1024,'KB')
    
            NumberOfFiles = NumberOfFiles + 1
            TotalFolderSize = TotalFolderSize + size

        else:
            
            if os.path.isdir(filepath):
                print('\n',file, 'File Folder')
                size, Number, Dir = FolderProperties(filepath)
                print('Number of files in Subfolder', Number)
                NumberOfFilesInSubFolder = NumberOfFilesInSubFolder + Number 
                
#                 print('Folder Size:',filepath, size)
#                 #if size > 1024:
#                  #   print(size/1024,'KB')
                SubFolderSize = SubFolderSize + size
                TotalFolderSize = TotalFolderSize + size
                NumberOfDir = NumberOfDir +1
                TotNumDir = TotNumDir + Dir+1
    
    TotNumFiles = NumberOfFiles + NumberOfFilesInSubFolder  
    
    
    print('\nFile Path:',path,'\nTotal Folder Size:', TotalFolderSize, '\nNumber of Files:', NumberOfFiles, '\nTotal Number of Files:', TotNumFiles,'\nNumber of Sub Folders',NumberOfDir,'\nTotal Number of folders', TotNumDir)
     
        
    row = row + 1
    
    worksheet.write(row,col,row)
    worksheet.write_url(row,col+1,path)
    
    worksheet.write(row,col+2,NumberOfFiles, comma)   #Local
    worksheet.write(row,col+3,NumberOfDir, comma)     #Local 
    worksheet.write(row,col+4,SubFolderSize, comma) #Local
    
    worksheet.write(row,col+5,TotNumFiles, comma)   #Total
    worksheet.write(row,col+6,TotNumDir, comma)     #Total
    worksheet.write(row,col+7,TotalFolderSize, comma) #Total
    
    if TotalFolderSize >= 1024:
        worksheet.write(row,col+8,TotalFolderSize/1024,comma) #KB
        
    if TotalFolderSize >= 1048576:
        worksheet.write(row,col+9,TotalFolderSize/1048576,comma) #MB
        
    if TotalFolderSize >= 1073741824:
        worksheet.write(row,col+10,TotalFolderSize/1073741824,comma) #GB
#     worksheet.write(row,col+7,'Total Folder Size (KB)', comma)
    
#       if TotalFolderSize >= 1024:
#          worksheet.write(row,col+4,TotalFolderSize/1024,comma) #KB
   
    return TotalFolderSize, TotNumFiles, TotNumDir;



a,b,c = FolderProperties(CurrentPath)


workbook.close()