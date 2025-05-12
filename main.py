from ssh_module import connect_ssh

hostname=input("ENTER IP ADDRESS TO CONNECT:")
port=input("ENTER PORT NUMBER:")
username=input("ENTER USERNAME:")
password=input("ENTER PASSWORD:")

connect_ssh(hostname,port,username,password)