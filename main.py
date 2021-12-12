import SysInfo
import FTPServer
import FileManager

def main():
    fileName = "info.txt"
    fileManager = FileManager.FileManager()
    ftp = FTPServer.FTPServer()

    data = SysInfo.SystemInfoRetreiver().getSystemInfoData()
    fileManager.writeDataToFile(fileName, data)
    ftp.uploadFile(fileName)
    fileManager.readDataToFile(fileName)

