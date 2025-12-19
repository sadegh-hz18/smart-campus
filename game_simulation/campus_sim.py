import pygame
import sys
import os

# مسیر پوشه current برای import
sys.path.append(os.path.dirname(__file__))

from student import Student

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Campus Simulation")

student = Student(50, 200, 5)
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        student.x += student.speed
    if keys[pygame.K_LEFT]:
        student.x -= student.speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (student.x, student.y), 15)
    pygame.display.update()

pygame.quit()