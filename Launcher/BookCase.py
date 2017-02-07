import BookManager


class BookCase():
    """
    App initialization, loading content and configuration
    """

    def __init__(self):
        self.load()
        self.exiting = False


    def run(self):
        yield

    def update(self):
        yield

    def exit(self):
        self.save()
        self.exiting = True
        return

    def save(self):
        BookManager.save(self.books)
        return

    def load(self):
        self.books = BookManager.load()
        return
