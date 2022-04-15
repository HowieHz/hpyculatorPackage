# from Signal import main_window_signal

name = "hpyculator"

def write(filename,anything,end="\n") -> None:
    filename.write(str(anything)+end)
    filename.flush()

def write_without_flush(filename,anything,end="\n") -> None:
    filename.write(str(anything)+end)

def flush(filename) -> None:
    filename.flush()

def output(self,anything) -> None:
    self.main_window_signal.appendOutPutBox.emit(str(anything))

def outputNotEnd(self,msg:str) -> None:
    self.main_window_signal.appendOutPutBox.emit(msg)

def clearOutput(self) -> None:
    self.main_window_signal.clearOutPutBox.emit()

def setOutput(self, msg:str) -> None:
    self.main_window_signal.setOutPutBox.emit(msg)

def addOne(num:int) -> int:
    return num+1

# def band():
#     main_window_signal.appendOutPutBox.connect(appendOutPut)

#     main_window_signal.setOutPutBox.connect(setOutPut)

#     main_window_signal.clearOutPutBox.connect(clearOutPut)

# def appendOutPut(self, msg:str):
#     self.ui.output_box.appendPlainText(msg)

# def clearOutPut(self):
#     self.ui.output_box.clear()

# def setOutPut(self, msg:str):
#     self.ui.output_box.setPlainText(msg)

# band()