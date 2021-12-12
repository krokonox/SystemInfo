import ftplib

class FTPServer:
    HOSTNAME = "ftp.dlptest.com"
    SERNAME = "dlpuser"
    PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"

    def uploadFile(self, filename):
        ftp_server = ftplib.FTP(self.HOSTNAME, self.USERNAME, self.PASSWORD)
        ftp_server.encoding = "utf-8"

        with open(filename, "wb") as file:
            # Command for Downloading the file "RETR filename"
            ftp_server.retrbinary(f"RETR {filename}", file.write)
  
            # Get list of files
            ftp_server.dir()
  
            # Display the content of downloaded file
            file= open(filename, "r")
            print('File Content:', file.read())
            ftp_server.quit()