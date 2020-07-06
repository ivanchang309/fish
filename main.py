import pygame

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (100, 75, 255)

fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image, (80, 200))
fish_rect = fish_image.get_rect()
fish_rect.center = (width // 2, height // 2)


def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()

if __name__ == "__main__":
  main()