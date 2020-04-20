import openpyxl

class Excelop:
    def __init__(self,name,sheetname,open):
        print("this is class of Excel opration")
        if open == 1:
            self.wb = openpyxl.Workbook(name)
        else:
            self.wb = openpyxl.load_workbook(name)
        self.sh = self.wb[sheetname]
        self.filename=name
    #basic function
    def create_sheet(self,sheet_name):
        self.wb.create_sheet(sheet_name)

    def save(self):
        self.wb.save(self.filename)

    def read(self,row,col):
        return self.sh.cell(row = row,column = col).value

    def write(self,row,col,data):
        self.sh.cell(row = row,column = col,value = data)

    def close(self):
        self.wb.close()

    #for ljj iteam
    #查找所有2009的数据项 然后形成  省-行数 的键值对
    def Get_dict(self):
        d={}
        i=1
        rows_data = list(self.sh.rows)
        for rowdata in rows_data[1:]:
            i=i+1
            if rowdata[0].value==2009:
                d[rowdata[2].value]=i
        print(d)
        return d


    def Write_data_save(self,row,col,data):
        self.write(row,col,data)
        self.save()

    def Write_data(self,data,col,row):
        self.write(row,col, data)