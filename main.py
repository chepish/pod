from varib import group_names, link, search_done
from search import get_wall_post
from telegram import start_message


def main():
    # поиск нужных сылок
    for gm in group_names:
        get_wall_post(gm)
    else: search_done = True


    

if __name__ == "__main__":
    main()
