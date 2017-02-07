import BookManager
import BookCase

def __init__():
    #recuperation des livres et lancement de l'application
    app = BookCase(BookManager.load())
    while not app.exiting:
        app.update()
    BookManager.save(app.save())
