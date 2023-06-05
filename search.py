import requests
import os
import json

from varib import token, finde, link

def get_wall_post(group_name):

    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=100&access_token={token}&v=5.131"
    req = requests.get(url)
    src = req.json()

    if os.path.exists(f"{group_name}"):
        pass
    else:
        os.mkdir(group_name)

    with open(f"{group_name}/{group_name}.json", "w", encoding="utf-8") as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    fresh_posts_id = []

    posts = src['response']['items']

    for fresh_post_id in posts:
        fresh_post_id = fresh_post_id["id"]
        fresh_posts_id.append(fresh_post_id)
        if not os.path.exists(f"{group_name}/exist_posts_{group_name}.txt"):
            pass

        with open(f"{group_name}/exist_posts_{group_name}.txt", "w") as file:
            for item in fresh_posts_id:
                file.write(str(item) + "\n")

    else:
        pass

    return filter_post(group_name)

def filter_post(group_name):
    with open(f"{group_name}/{group_name}.json", 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    items = data["response"]["items"]

    text_post = []
    link_post = []

    for i in items:
        text = i["text"]
        link_id = i["id"]
        owner_id = i["owner_id"]
        text_post.append(text.lower().replace('.', '') )
        link_post.append(f"https://vk.com/{group_name}?w=wall{owner_id}_{link_id}")
        if not os.path.exists(f"{group_name}/exist_posts_{group_name}_text.txt"):
            pass

        with open(f"{group_name}/exist_posts_{group_name}_link.txt", "w", encoding='utf-8') as file:
            for item in link_post:
                file.write(str(item) + "\n")
                if not os.path.exists(f"{group_name}/exist_posts_{group_name}_link.txt"):
                    pass

        with open(f"{group_name}/exist_posts_{group_name}_link.txt", "w", encoding='utf-8') as file:
            for item in link_post:
                file.write(str(item) + "\n")
    for i in range(len(text_post)):
        for j in finde:
            if j in text_post[i]:
                link.append(link_post[i])
    print("done")