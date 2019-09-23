import os
batch_file = open('cloner.bat','w')
with open("./repo-SHAs.txt", "r") as fr:
    for line in fr:
        cmd1 = line.split()
        clone_cmd = 'git clone https://github.com/'+cmd1[0]+' ./Repos/'+cmd1[0]
        print(clone_cmd)
        batch_file.write(clone_cmd+'\n')
        #os.system(clone_cmd)
        checkout_cmd = 'git -C ./Repos/'+cmd1[0]+' reset --hard '+cmd1[1]
        print(checkout_cmd)
        batch_file.write(checkout_cmd+'\n')
        #os.system(checkout_cmd)
batch_file.close()
