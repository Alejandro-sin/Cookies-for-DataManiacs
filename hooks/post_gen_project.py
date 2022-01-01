import sys
import subprocess
import time




SUCCESS = "\x1b[33m"

def git_init():
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add','*'])
    subprocess.call(['git', 'commit', "-m","First commit"])
    print(f'{SUCCESS} Do you like to connect with github repo? [y/n]')
    connecting_option = input("> ")
    if connecting_option not in ['y', 'n']:
        print("You must to do manually")

    elif connecting_option == 'y':
        r = input("url_repo >")
        branch = input("What is the name of the branch to connect with? [main/master]")
        subprocess.call(['git', 'remote', 'add', 'origin', r])
        subprocess.call(['git', 'pull', 'origin', branch])
        subprocess.call(['git', 'push', 'origin', branch])
        print(f'{SUCCESS} All ready to go!')
    elif connecting_option == 'n':
        print(f'{SUCCESS} All ready to go!')
     


def idle_automator():
    option = input("Do you want yo open on VS Code? [y/n]")
    if option == 'y':subprocess.call(['code',' .'])


def env_automator():
    #subprocess.call(['conda', 'env','create','--file','environment.yml'])
    subprocess.call(['python', '-m', 'venv','env'])
    subprocess.call(['.\\env\\Script\\activate', '-m', 'venv','env'])
    subprocess.call(['pip', 'install', 'requirements.txt'])
    print("********  Environment created Success  ********")

def main():
    env_automator()
    time.sleep(2)
    idle_automator()
    a = input("Do you want initalize your repository? [y/n]")
    if a == "y": git_init()
    else : print("Your project: {{cookiecutter.project_slug}} are ready to go!")




if __name__ == '__main__':
    main()