import ftplib

# Set path
path = '/mirrors/ubuntu-cdimage/releases/22.04/release'
# Set file to get
filename = 'SHA256SUMS'
# Set connection
ftp = ftplib.FTP("ftp.heanet.ie")
# Anon logging
ftp.login()
# Change dir
ftp.cwd(path)
# Get file
ftp.retrbinary("RETR" + filename, open(filename, 'wb').write)
# Exit (cleanly)
ftp.quit()
