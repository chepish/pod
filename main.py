from varib import group_names, link
from search import get_wall_post
from telegram import *

def main():

    # поиск нужных сылок
    for gm in group_names:
        get_wall_post(gm)

    

if __name__ == "__main__":
    main()