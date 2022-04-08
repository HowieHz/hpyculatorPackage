import wx

def write(filename,anything,end="\n") -> None:
    filename.write(str(anything)+end)
    filename.flush()

def write_without_flush(filename,anything,end="\n") -> None:
    filename.write(str(anything)+end)

def flush(filename) -> None:
    filename.flush()

def output(self,anything,end="\n") -> None:
    wx.CallAfter(self.outPutToOutPut,self,str(anything)+end)

def outPutToOutPut(self,msg:str) -> None:
    self.output.AppendText(msg)

def clearOutPut(self) -> None:
    self.output.Clear()

def setOutPut(self, msg:str) -> None:
    self.output.SetValue(msg)

def addOne(num:int) -> int:
    return num+1