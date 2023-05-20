from session import Session
from models import Author


def main():
    session = Session()

# zwykły druk:

    # for author in session.query(Author):
    #     print(author.first_name)

# druk z obcym kluczem:

    for author in session.query(Author):
        for article in author.articles:
            print(author, article)


if __name__ == '__main__':
    main()
