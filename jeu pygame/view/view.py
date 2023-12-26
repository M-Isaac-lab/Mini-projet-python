import pygame

class GameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Jeu Pygame MVC")
        self.clock = pygame.time.Clock()

    def update(self, score):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        self.screen.blit(text, (100, 100))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def close(self):
        pygame.quit()   