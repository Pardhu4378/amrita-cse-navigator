import re

with open('c:/Users/pardh/OneDrive/Desktop/AmritaCSENavigator/data.py', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_videos(match):
    url_match = re.search(r'"Python":\s*\{\s*"English":\s*"(.*?)"', match.group(0))
    if url_match:
        url = url_match.group(1)
        return f'"video_url": "{url}",'
    return match.group(0)

new_content = re.sub(r'"videos":\s*\{[^{}]*\{[^{}]*\}[^{}]*\{[^{}]*\}[^{}]*\{[^{}]*\}[^{}]*\},?', replace_videos, content)

new_content = re.sub(
    r'DEFAULT_VIDEO = \{.*?\}',
    'DEFAULT_VIDEO_URL = "https://www.youtube.com/embed/rfscVS0vtbw"',
    new_content, flags=re.DOTALL
)

new_content = new_content.replace(
    '"videos": DEFAULT_VIDEO,',
    '"video_url": DEFAULT_VIDEO_URL,'
)

with open('c:/Users/pardh/OneDrive/Desktop/AmritaCSENavigator/data.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('data.py transformed!')
