import pygame

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        running = True
        while running:
            running = self.view.handle_events()
            self.model.increment_score()
            self.view.update(self.model.score)
            self.view.clock.tick(30)
        self.view.close()