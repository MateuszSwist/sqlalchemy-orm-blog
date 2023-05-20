from faker import Faker
from models import Base, Author, Article, Hashtag


def generate_authors(session):
    fake = Faker()
    return [
        Author(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            author_id=fake.author_id(min=1, max=50),
        )
        for _ in range(count)
    ]
def main():
    pass


if __name__ == "__main__":
    main()