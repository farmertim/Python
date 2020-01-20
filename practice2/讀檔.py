class readfile:
    def __init__(self,name):
        self.filename=name
        print(self.filename)
        self.file=None
    def openfile(self):
        self.file=open(self.filename,mode="r",encoding="utf-8")
        #print(self.file)
        #mode="r" r唯讀模式 w寫入模式(複寫) a 寫入模式(續寫)
    def readfile(self):
        return self.file.read() #開啟檔案(檔案物件.read())
fi=readfile("data.txt")
fi.openfile()
print(fi.readfile())
