import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

# URL trang chứa các file audio
# BASE_URL = "https://vn.pikbest.com/free-sound-effects/chim.html"
BASE_URL = "https://search.macaulaylibrary.org/catalog?taxonCode=t-11994031&includeChildTaxa=true"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Thư mục lưu audio
SAVE_DIR = "audio_data"
os.makedirs(SAVE_DIR, exist_ok=True)



# Lấy HTML
response = requests.get(BASE_URL, headers=headers)
response.raise_for_status()

print("OK, lấy được HTML")

soup = BeautifulSoup(response.text, "html.parser")

# Tìm tất cả link audio
audio_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    # if href.endswith((".wav", ".mp3", ".ogg")):
    #     audio_links.append(urljoin(BASE_URL, href))
    if href.endswith((".png", ".jpeg")):
        audio_links.append(urljoin(BASE_URL, href))

print(f"Tìm thấy {len(audio_links)} file audio")

# Tải file
for i, audio_url in enumerate(audio_links):
    filename = os.path.join(SAVE_DIR, audio_url.split("/")[-1])
    print(f"[{i+1}/{len(audio_links)}] Đang tải {filename}")

    r = requests.get(audio_url, stream=True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

print("Tải xong toàn bộ audio!")
