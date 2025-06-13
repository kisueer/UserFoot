from flask import Flask, render_template, request
import requests

app = Flask(__name__)

SITES = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Facebook": "https://www.facebook.com/{}",
    "YouTube": "https://www.youtube.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Tumblr": "https://{}.tumblr.com",
    "Flickr": "https://www.flickr.com/people/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "Medium": "https://medium.com/@{}",
    "WordPress": "https://{}.wordpress.com",
    "Blogger": "https://{}.blogspot.com",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    "GitHub Gist": "https://gist.github.com/{}",
    "CodePen": "https://codepen.io/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Telegram": "https://t.me/{}",
    "Xbox": "https://account.xbox.com/en-us/profile?Gamertag={}",
    "eBay": "https://www.ebay.com/usr/{}",
    "PayPal.Me": "https://paypal.me/{}",
    "LeetCode": "https://leetcode.com/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "Codecademy": "https://www.codecademy.com/{}",
    "Codeforces": "https://www.codeforces.com/profile/{}",
    "Replit": "https://replit.com/@{}",
    "Origin (EA)": "https://www.origin.com/us/en-us/profile/user/{}",
    "SourceForge": "https://sourceforge.net/u/{}/",
    
}

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        username = request.form["username"]
        headers = {"User-Agent": "Mozilla/5.0"}
        for site, url_template in SITES.items():
            url = url_template.format(username)
            try:
                res = requests.get(url, headers=headers, timeout=5)
                results[site] = (res.status_code == 200, url)
            except:
                results[site] = (False, url)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
