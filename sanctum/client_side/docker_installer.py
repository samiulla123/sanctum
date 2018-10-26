import os
import subprocess

class Docker:
    def package(self):
        os.system('sudo apt-get install apt-transport-https ca-certificates curl software-properties-common')
        os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
        os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
        Docker.update(self)

    def update(self):
        os.system('sudo apt-get update')
        Docker.doc_install(self)

    def doc_install(self):
        os.system('sudo apt-cache policy docker-ce')
        os.system('apt-cache search docker-ce')
        cmd = "sudo apt-get install -y docker-ce"
        value = subprocess.call(cmd, shell=True)
        if value==100:
            os.system('apt-get install -y docker')
        else:
            os.system('sudo apt-get install -y docker-ce')
        os.system('sudo systemctl status docker')
        Docker.load(self)


    def doc(self):
        cmd="sudo docker --version"
        value = subprocess.call(cmd, shell=True)
        print(value, type(value))
        if value != 0:
            Docker.package(self)
        else:
            print("Already installed docker file")
            Docker.load(self)

    def load(self):
        print("done")
        cmd = "sudo docker-compose --version"
        value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
        print(value, type(value))
        if value != 0:
            cmd="mkdir /usr/local/bin/docker-compose"
            value=subprocess.call(cmd, shell=True)
            os.system('sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose')
            os.system('sudo chmod +x /usr/local/bin/docker-compose')
            os.system('sudo docker-compose --version')

        else:
            print("Already docker-compose is installed")
            Docker.OpenSsh(self)
        # os.system('docker load -i')
       # os.system('docker load -i python_container.tar')

    def OpenSsh(self):
        os.system('sudo apt install -y openssh-server')
        os.system('')
        cmd = "sudo systemctl status ssh"
        value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
        print(value, type(value))
        if value!=0:
            os.system('sudo systemctl start ssh')

class Docker_Compose:
    def Run(self):
        os.system('sudo docker ps -a')
        print("Enter container_ID to start container(Press 0 if container is not exists)")
        con=input()
        if con == '0':
            Docker_Compose.Val(self)
        else:
            os.system('clear')
            os.system('sudo docker start '+con)
            os.system('sudo docker exec -it '+con+' bash')
    def Val(self):
        os.system('sudo docker pull 10.10.1.79:5000/client_files')
        os.system('sudo docker images')
        print("Enter docker REPOSITORY name you want to run")
        repo = input()
        os.system('clear')
        os.system('sudo docker run -it '+repo+' bash')


class Copy:
    def create(self):
        os.system('sudo mkdir -p /etc/docker/certs.d/10.10.1.79\:5000 ')
        os.system('sudo scp domain.crt /etc/docker/certs.d/10.10.1.79\:5000')

class Commit:
    def commit1(self):
        print("print do you want to commit changes(Y/N)")
        val=input()
        if val == 'Y' or val == 'y':
            os.system('sudo docker images')
            print("Enter images name")
            dname=input()
            os.system('sudo docker ps -a')
            print("Enter container id ")
            cname=input()
            print("Enter new image name")
            name=input()
            os.system('sudo docker commit '+cname+' '+dname+'/'+name)
            os.system('sudo docker images')
            print("Docker image commited successfully")
        if val == 'N' or val == 'n':
            print()
obj=Docker()
obj.doc()
ob=Copy()
ob.create()
obj1=Docker_Compose()
obj1.Run()
obj3=Commit()
obj3.commit1()