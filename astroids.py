from circleshape import CircleShape
from constants import LINE_WIDTH


class Astroid(CircleShape):
    def __init__(self, x, y, radius):
        super.__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (x, y), radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position = self.position + self.velocity * dt
        
    


