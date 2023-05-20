from session import session
from models import Hashtag, Article


def main():
    hashtags = session.query(Hashtag).get(1)
    print(f"Article with #{hashtags.name}")
    for article in hashtags.articles:
        print(article.title)

    print('-' * 20)
    for article in session.query(Article):
        print(article.title)
        for hashtag in article.hashtags:
            print(f"{hashtags.name}")


if __name__ == '__main__':
    main()
