from app.ui.menu import run_menu
from database.db import Base, engine

Base.metadata.create_all(engine)


def main():
    run_menu()


if __name__ == "__main__":
    main()
