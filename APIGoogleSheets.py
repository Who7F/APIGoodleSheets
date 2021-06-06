#Python(3.5.2)
#This work with google sheets. Read and write.
#You will need to add APIs to your google sheet and download credentials for this code to read
#You also need to share goodle sheep with email with in the Key
#gspread and oauth2clinet will need to be installed 
#This class only has two usable methods. PrintCell, ChangeCell
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GSReader:

    def __init__(self, GoogleKey, SpreadSheets):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.GoogleKey = GoogleKey #The credentials
        self.SpreadSheets = SpreadSheets

    
    def OpenSheets(self, WorkSheet): #Only to be called by the class
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.GoogleKey, self.scope)
        client = gspread.authorize(creds)
        
        return client.open(self.SpreadSheets).worksheet(WorkSheet)

    def PrintCell(self, WorkSheet, ColumnCell, RowCell):
        sheet = self.OpenSheets(WorkSheet)
        return sheet.cell(ColumnCell, RowCell).value

    def ChangeCell(self, WorkSheet, ColumnCell, RowCell, NewVal):
        sheet = self.OpenSheets(WorkSheet)
        sheet.update_cell(ColumnCell, RowCell, NewVal) 
        return sheet.cell(ColumnCell, RowCell).value

    def PrintCell2(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.GoogleKey, self.scope)
        client = gspread.authorize(creds)
        sheet = client.open('GSR').sheet1
        

def main(): #following code should be used for testing, and is inactive when this module is imported
    SpreadSheets = 'Place Holder' #Place Holder.  Sheet name
    KeyFile = 'Place Holder' #Place Holder.  Json file name
    f = GSReader(KeyFile, SpreadSheets) #Makes an instance of the class
    
    WorkSheet = 'Sheet1' #Name of the work sheet you want to use
    ColumnCell = 1  
    RowCell = 1
    MyText = 'Place Holder'
    
    print (f.PrintCell(WorkSheet,ColumnCell,RowCell)) 
    print ('New Cell Val =', (f.ChangeCell(WorkSheet,ColumnCell,RowCell, MyText)))
    
    print('done')

if __name__=='__main__':
    main()
