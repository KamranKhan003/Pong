import pygame
from random import choice


def animation_ball():
    global ball_x, ball_y, player_score, opponent_score, time_score

    ball.x += ball_x
    ball.y += ball_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_y *= -1
    if ball.left <= 0:
        opponent_score += 1
        time_score = pygame.time.get_ticks()
    if ball.right >= screen_width:
        player_score += 1
        time_score = pygame.time.get_ticks()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_x *= -1

def animation_player():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def animation_opponent():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_x, ball_y, time_score

    ball.center = (screen_width/2, screen_height/2)

    current_time = pygame.time.get_ticks()

    if current_time - time_score < 2100:
        ball_x,ball_y = 0,0
    else:
        ball_y = 7 * choice((1,-1))
        ball_x = 7 * choice((1,-1))
        time_score = None

pygame.init()

# Variables
screen_width = 900
screen_height = 600

bg_color = pygame.Color("Gray12")
light_gray = pygame.Color((200,200,200))

ball_x = 7
ball_y = 7

player_speed = 0
opponent_speed = 7

player_score = 0
opponent_score = 0

game_font = pygame.font.Font(None,32)

time_score = True


# Set Width and height of screen
screen = pygame.display.set_mode((screen_width,screen_height))

# Set the caption
pygame.display.set_caption("Pong")

# Clock Object
clock = pygame.time.Clock()


ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(0, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(screen_width-10,screen_height/2 -70, 10,140)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7

            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7

            if event.key == pygame.K_UP:
                player_speed += 7

    
    animation_ball()
    animation_player()
    animation_opponent()

    if time_score:
        ball_restart()

    
    player.y += player_speed

    screen.fill(bg_color)
    pygame.draw.ellipse(screen, light_gray, ball)
    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)
    pygame.draw.aaline(screen, light_gray, (screen_width/2,0), (screen_width/2,screen_height))

    player_surf = game_font.render(f'{player_score}', False, light_gray)
    screen.blit(player_surf, (420,300))

    opponent_surf = game_font.render(f'{opponent_score}', False, light_gray)
    screen.blit(opponent_surf, (470,300))
    

    pygame.display.update()

    
    
    # Set Frame per second
    clock.tick(60)
