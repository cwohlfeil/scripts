import ftplib
ftp = ftplib.FTP()
HOST = 'ftp.cse.buffalo.edu'
PORT = 12345
ftp.connect(HOST, PORT)
# list dir
ftp.retrlines('LIST')
# change dir
ftp.cwd('mirror')
ftp.retrlines('LIST')
ftp.quit()


# Download
ftp = ftplib.FTP('ftp.debian.org')
ftp.login()
ftp.cwd('debian')
out = '.\\README'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'README.html', f.write)
ftp.quit()


# Upload
def ftp_upload(ftp_obj, path, ftype='TXT'):
    """ A function for uploading files to an FTP server
    @param ftp_obj: The file transfer protocol object
    @param path: The path to the file to upload 8 """
    if ftype == 'TXT':
        with open(path) as fobj:
            ftp.storlines('STOR ' + path, fobj)
    else:
        with open(path, 'rb') as fobj:
            ftp.storbinary('STOR ' + path, fobj, 1024)

if __name__ == '__main__':
    ftp = ftplib.FTP('host', 'username', 'password')
    ftp.login()

    path = '/path/to/something.txt'
    ftp_upload(ftp, path)

    pdf_path = '/path/to/something.pdf'
    ftp_upload(ftp, pdf_path, ftype='PDF')

    ftp.quit()

