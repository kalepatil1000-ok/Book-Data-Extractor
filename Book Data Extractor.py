from bs4 import BeautifulSoup
import pandas as pd


class DataFormatting:

    def __init__(self, file):
        self.file = file
        self.soup = None
        self.items = []

    def load_data(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                content = f.read()

            self.soup = BeautifulSoup(content, "html.parser")

        except FileNotFoundError:
            print(f"File not found: {self.file}")

    def extract_data(self):

        if self.soup is None:
            return

        articles = self.soup.find_all(
            "article",
            class_="product_pod"
        )

        for article in articles:

            title = article.find(
                "h3"
            ).find(
                "a"
            )["title"]

            price = article.select_one(
                "p.price_color"
            ).text.replace("£", "")

            rating = article.select_one(
                "p.star-rating"
            )["class"][1]

            self.items.append(
                [title, price, rating]
            )


all_books = []

for i in range(1, 51):

    file_name = f"htmls/page{i}.html"

    data = DataFormatting(file_name)

    data.load_data()
    data.extract_data()

    all_books.extend(data.items)

    print(f"Page {i} processed successfully...")


df = pd.DataFrame(
    all_books,
    columns=[
        "Book Title",
        "Price",
        "Rating"
    ]
)

print("\nTotal Books:", len(df))

df.to_csv(
    "all_books.csv",
    index=False
)

print(
    "\nData saved successfully in all_books.csv"
)