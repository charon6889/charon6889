import paramiko

def connect_ssh(hostname,port,username,password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    
    try:
        client.connect(hostname=hostname,port=port,username=username,password=password)
        print("CONNECTED SUCCESSFULY TO:",hostname)    
        while True:
            cmd = input(f"{username}@{hostname}$ ")
            if cmd.lower() in ['exit', 'quit']:
                print("Connection closed.")
                break

            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                print(output)
            if error:
                print(f"{error}")

        client.close()

    except Exception as e:
     print("Connection failed:", str(e))
        