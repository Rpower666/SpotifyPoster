"""
main -

Author: 11761
Date: 2025/1/4
"""
from core.spotify_poster import Poster


# from . import Poster


def main():
    name_tmp = input("请输入歌曲：（格式：偷心 张学友）")
    try:
        name_list = name_tmp.split()
        name = name_list[0]+' - '+name_list[1]
        print(name)
        Poster(name)
    except Exception as e:
        print("错误为：", e)

if __name__ == '__main__':
    main()