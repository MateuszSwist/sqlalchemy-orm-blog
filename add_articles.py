from session import session
from models import Author, Article
from faker import Faker


def main():
    author = session.query(Author).get(10)

    # na gorze wyciagamy po id, na dole po username:

    # author = session.query(Author).filter_by(user_name="davidt").one()

    fake = Faker()
    article = Article(
        title=fake.sentence(),
        content=fake.sentence()
    )

    author.articles.append(article)
    session.commit()


if __name__ == '__main__':
    main()
