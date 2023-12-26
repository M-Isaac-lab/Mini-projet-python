from model.model import GameModel
from view.view import GameView
from controller.controller import GameController

if __name__ == "__main__":
    model = GameModel()
    view = GameView()
    controller = GameController(model, view)
    controller.run()