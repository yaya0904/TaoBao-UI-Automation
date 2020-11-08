# coding=utf-8
__author__ = "jewelry_zhu"
import xlrd
import xlwt
import os

class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        #get titles
        self.row = self.table.row_values(0)

        #get rows number
        self.rowNum = self.table.nrows

        #get columns number
        self.colNum = self.table.ncols

        #the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def write(self, titleName, value):
        self.openExcel()

        columnNum = self.getColNum(titleName)

        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet(self.name, cell_overwrite_ok=True)

        for x in range(self.rowNum):
            row = self.table.row_values(x)
            for i in range(self.colNum):
                sheet.write(x, i, row[i])

        if self.hasNext():
            sheet.write(self.curRowNo, columnNum, value)
            self.curRowNo += 1

        os.remove(self.path)
        book.save(self.path)

    def getColNum(self, titleName):
        titleColNum = -1

        try:
            for i in range(len(self.row)):
                if self.row[i] == titleName:
                    titleColNum = i
                    break
                else:
                    continue
        except Exception as ex:
            print(ex)

        return titleColNum



