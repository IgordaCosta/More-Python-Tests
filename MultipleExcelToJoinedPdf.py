import JoinPdfs
import MultipleExcelToMultiplePdfs



Folderlocation="C:\\Users\\IgorDC\\Documents\\AutoFormFillerFiles\\"

nameOfNewFile="NewFileJoined"
desiredFileType="testFile"


MultipleExcelToMultiplePdfs.MultipleExcelToMultiplePdfs(Folderlocation=Folderlocation,desiredFileType=desiredFileType)


JoinPdfs.JoinPdfs(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType)







