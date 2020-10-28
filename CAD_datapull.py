import os
import shutil
import xlsxwriter

if os.path.exists('test.xlsx'):
       os.remove('test.xlsx')

workbook = xlsxwriter.Workbook('test.xlsx')

worksheet = workbook.add_worksheet('FoodDraw')

header_format = workbook.add_format({'bold': True,'bg_color':'gray','font_color':'white'})

# Add a bold format to use to highlight cells.
#bold = workbook.add_format({'bold': True})



# Add a number format for cells with money.
comma = workbook.add_format({'num_format': '#,##0'})

CurrentPath = r"Z:\FoodDraw"
#Z:\FoodDraw
#Z:\FoodDraw\Shaun\Spiral

row = 0
col = 0

worksheet.write(row,col,'Row', header_format)
worksheet.write(row,col+1,'Path', header_format)

worksheet.write(row,col+2,'Number Of Local Files', header_format)
worksheet.write(row,col+3,'Number Of Folders', header_format)
worksheet.write(row,col+4,'Local Folder Size (Bytes)',header_format )

worksheet.write(row,col+5,'Total Number of Files', header_format)
worksheet.write(row,col+6,'Total Number of Sub-Folders', header_format)

worksheet.write(row,col+7,'Total Folder Size (Bytes)', header_format)
worksheet.write(row,col+8,'Total Folder Size (KB)', header_format)
worksheet.write(row,col+9,'Total Folder Size (MB)', header_format)
worksheet.write(row,col+10,'Total Folder Size (GB)', header_format)

worksheet.write(row,col+11,'Number of Local Cad Files', header_format)
worksheet.write(row,col+12,'Total Number of Cad Files', header_format)

worksheet.write(row,col+13,'Total Cad Size (Bytes)', header_format)
worksheet.write(row,col+14,'Total Cad Size (KB)', header_format)
worksheet.write(row,col+15,'Total Cad Size (MB)', header_format)
worksheet.write(row,col+16,'Total Cad Size (GB)', header_format)

# Cad Files in Subfolder, Total Number of Cad Files,Total Cad Size

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
    CadSize = 0
    TotalCadSize = 0
    CadNumFiles = 0
    SubCadNumFiles = 0
    TotCadNumFiles = 0
    
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
            
            #file = str(file)
            # ipt, iam, stp, dwg, sldprt, sldasm
            if file.lower().endswith(('.sldprt','ipt', 'iam', 'stp', 'dwg', 'sldprt', 'sldasm')):
                CadSize = os.path.getsize(filepath)
                CadNumFiles = CadNumFiles + 1
                TotalCadSize = TotalCadSize + CadSize

        else:
            
            if os.path.isdir(filepath):
                print('\n',file, 'File Folder')
                size, Number, Dir, CadNum, Cad = FolderProperties(filepath)
                print('Number of files in Subfolder', Number)
                NumberOfFilesInSubFolder = NumberOfFilesInSubFolder + Number 
                SubCadNumFiles = SubCadNumFiles + CadNum
#                 print('Folder Size:',filepath, size)
#                 #if size > 1024:
#                  #   print(size/1024,'KB')
                SubFolderSize = SubFolderSize + size
                TotalFolderSize = TotalFolderSize + size
                NumberOfDir = NumberOfDir +1
                TotNumDir = TotNumDir + Dir+1
                TotalCadSize = TotalCadSize + Cad
    
    TotNumFiles = NumberOfFiles + NumberOfFilesInSubFolder 
    TotCadNumFiles = CadNumFiles + SubCadNumFiles
    
    
    print('\nFile Path:',path,'\nTotal Folder Size:', TotalFolderSize,'\nTotal Cad Size:',TotalCadSize, '\nCad Files in Subfolder',SubCadNumFiles, '\nTotal Number of Cad Files', TotCadNumFiles, '\nNumber of Files:', NumberOfFiles, '\nTotal Number of Files:', TotNumFiles,'\nNumber of Sub Folders',NumberOfDir,'\nTotal Number of folders', TotNumDir)
     
        
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
            
    worksheet.write(row,col+11,CadNumFiles, comma)   #Cad Files in Subfolder
    worksheet.write(row,col+12,TotCadNumFiles, comma)     #Total Number of Cad Files
    worksheet.write(row,col+13,TotalCadSize, comma) #Total Cad Size
    
    if TotalCadSize >= 1024:
            worksheet.write(row,col+14,TotalCadSize/1024,comma) #KB
        
    if TotalCadSize >= 1048576:
            worksheet.write(row,col+15,TotalCadSize/1048576,comma) #MB
        
    if TotalCadSize >= 1073741824:
            worksheet.write(row,col+16,TotalCadSize/1073741824,comma) #GB
    

   
    return TotalFolderSize, TotNumFiles, TotNumDir, TotCadNumFiles, TotalCadSize;



a,b,c,d,e = FolderProperties(CurrentPath)


workbook.close()