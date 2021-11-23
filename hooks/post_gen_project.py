import sys
import subprocess

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
        

def env_automator():
    subprocess.call(['conda','env', 'create','--file','enviroment.yml'])

def main():
    option_g = input("Do you want to initialize git? [y/n]: ")
    if option_g not in ['y', 'n']:
        sys.exit(1)
    elif option_g == 'y':
        git_init()
    else:
        print(f'{SUCCESS} All ready to go!')

if __name__ == '__main__':
    main()