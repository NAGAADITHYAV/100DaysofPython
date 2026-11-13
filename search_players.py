import requests
import csv
import time

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQwMjFjZDgyLWRmNDUtNDExMy1iOWUzLTJkMTdkNzBjMmYzZSIsImlhdCI6MTc5Mjk5MTQ5Nywic3ViIjoiZGV2ZWxvcGVyL2Y1ZGJjNTNlLTM2YjctNDU0Ny04OGEyLWZhMjY4ODQ2N2JiNSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjk5LjYuMjQ3LjQzIl0sInR5cGUiOiJjbGllbnQifV19.-428mZTWYww_saAv6iXYqrqpNn2Vt37KcdmUrjl0xujHn1rINGlrVRoY8tuzwhpUxJaFZqtzY6_QhulKQE5BKQ"
START_TAG = "PYLCLQ2YP"
COUNT = 500

CHARS = "0289CGJLPQRUYV"
BASE = len(CHARS)

def tag_to_num(tag):
    n = 0
    for c in tag.replace("#", ""):
        n = n * BASE + CHARS.index(c)
    return n

def num_to_tag(n, length):
    s = ""
    while n:
        s = CHARS[n % BASE] + s
        n //= BASE
    return "#" + s.rjust(length, CHARS[0])

headers = {"Authorization": f"Bearer {API_KEY}"}
start = tag_to_num(START_TAG)
players = []

for i in range(1, COUNT + 1):
    tag = num_to_tag(start + i, len(START_TAG))

    url = f"https://api.clashofclans.com/v1/players/%23{tag[1:]}"

    try:
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            p = r.json()
            players.append({
                "tag": p["tag"],
                "name": p["name"],
                "town_hall": p["townHallLevel"],
                "trophies": p.get("trophies", 0),
                "clan": p.get("clan", {}).get("name", "")
            })
            print("FOUND:", p["tag"], p["name"])

        elif r.status_code == 404:
            print("Not found:", tag)

        elif r.status_code == 429:
            print("Rate limited. Stopping.")
            break

        else:
            print("API error:", r.status_code, r.text[:200])
            if r.status_code in (400, 403):
                break

    except requests.RequestException as e:
        print("Request failed:", e)
        break

    time.sleep(0.3)

with open("players.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f, fieldnames=["tag", "name", "town_hall", "trophies", "clan"]
    )
    writer.writeheader()
    writer.writerows(players)

print(f"Found {len(players)} players.")