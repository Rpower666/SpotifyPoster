"""
spotify_poster -

Author: 11761
Date: 2025/1/4
"""
import os
import dotenv
from BeatPrints import lyrics, poster, spotify

def Poster(name):
    # 加载 .env 文件
    dotenv.load_dotenv(".env")

    # 获取 Spotify 凭据
    CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not CLIENT_ID or not CLIENT_SECRET:
        print("未找到 CLIENT_ID 或 CLIENT_SECRET，请确保 .env 文件正确设置。")
        return

    save_img = os.path.join(os.getcwd(), 'img')
    # 初始化组件
    ly = lyrics.Lyrics()
    ps = poster.Poster(save_img)  # 图片保存路径
    sp = spotify.Spotify(CLIENT_ID, CLIENT_SECRET)

    try:
        # 搜索曲目
        search = sp.get_track(name, limit=1)
        if not search:
            print("未找到曲目，请检查关键词是否正确。")
            return

        # 获取曲目元数据和歌词
        metadata = search[0]
        track_lyrics = ly.get_lyrics(metadata)
        highlighted_lyrics = ly.select_lines(track_lyrics, "5-9")

        # 生成曲目海报
        ps.track(metadata, highlighted_lyrics)
        print("海报生成成功！")
    except Exception as e:
        print("处理出错:", str(e))


if __name__ == "__main__":
    name = "偷心 - 张学友"

    Poster(name)
