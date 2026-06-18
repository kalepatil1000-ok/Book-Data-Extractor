import requests

class WebsiteInfoCollection:

    def __init__(self, url):
        self.url = url
        self.response = None

    def get_info(self):
        try:
            self.response = requests.get(self.url, timeout=5)

            print("\n===== WEBSITE INFORMATION =====")
            print(f"URL: {self.response.url}")
            print(f"Status Code: {self.response.status_code}")
            print(f"Encoding: {self.response.encoding}")
            print(f"Content Type: {self.response.headers.get('Content-Type')}")
            print(f"Server: {self.response.headers.get('Server')}")
            print(f"Response Time: {self.response.elapsed.total_seconds()} seconds")

        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def get_page_downloaded(self):
        if self.response.status_code == 200:

            name = input("Enter page name: ")

            with open(f"{name}.html", "w", encoding="utf-8") as f:
                f.write(self.response.text)

            print("Page saved successfully!")
        else:
            print("The page is not valid...!, for downloded!")

url = input("Enter your website url: ")
web = WebsiteInfoCollection(url)
web.get_info()
web.get_page_downloaded()
