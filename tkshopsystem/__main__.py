from tkshopsystem import SupermarketGUI
from tkshopsystem.storage import Storage


if __name__ == "__main__":
    with Storage() as storage:
        app = SupermarketGUI(storage=storage)
        app.mainloop()
