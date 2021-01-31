import pygame
import math

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 20)

screen = pygame.display.set_mode((960,960))

pygame.display.set_caption("Tic-Tac-Toe+")

image_x = pygame.image.load('x_image.png')

def the_winner(win):

    if win == 0:
        win_text = "Red Won!"
        text_color = (200, 50, 50)
    elif win == 1:
        win_text = "Blue Won!"
        text_color = (50, 50, 200)

    pygame.mouse.set_visible(True)

    the_winner_state = True

    while the_winner_state:

        mouse = pygame.mouse.get_pos()  # touple

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and 300 < mouse[0] < 700 and 380 < mouse[1] < 420:
                if event.button == 1:
                    menu()

        screen.fill((0, 0, 0))

        text1_pos_x = 960
        text1_pos_y = 960
        display_surface = pygame.display.set_mode((text1_pos_x, text1_pos_y))
        pygame.display.set_caption("Tic-Tac-Toe+")
        font = pygame.font.Font('freesansbold.ttf', 60)
        text1 = font.render(win_text, True, text_color, (0, 0, 0))
        textRect = text1.get_rect()
        textRect.center = (text1_pos_x // 2, 200)

        if 300 < mouse[0] < 700 and 380 < mouse[1] < 420:
            text2_color = (255, 170, 180)
        else:
            text2_color = (200, 200, 200)

        font2 = pygame.font.Font('freesansbold.ttf', 48)
        text2 = font2.render("Back To Menu", True, text2_color, (0, 0, 0))
        textRect2 = text2.get_rect()
        textRect2.center = (text1_pos_x // 2, 400)

        display_surface.blit(text1, textRect)
        display_surface.blit(text2, textRect2)

        pygame.display.update()


def menu():
    pygame.mouse.set_visible(True)

    menu_state = True

    while menu_state:

        mouse = pygame.mouse.get_pos()  # touple

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and 300 < mouse[0] < 700 and 380 < mouse[1] < 420:
                if event.button == 1:
                    menu_state = False
                    game()

        screen.fill((0, 0, 0))

        text1_pos_x = 960
        text1_pos_y = 960
        display_surface = pygame.display.set_mode((text1_pos_x, text1_pos_y))
        pygame.display.set_caption("Tic-Tac-Toe+")
        font = pygame.font.Font('freesansbold.ttf', 60)
        text1 = font.render("Tic-Tac-Toe+", True, (200, 200, 200), (0, 0, 0))
        textRect = text1.get_rect()
        textRect.center = (text1_pos_x // 2, 200)

        if 300 < mouse[0] < 700 and 380 < mouse[1] < 420:
            text2_color = (255, 170, 180)
        else:
            text2_color = (200, 200, 200)

        font2 = pygame.font.Font('freesansbold.ttf', 48)
        text2 = font2.render("Player vs Player", True, text2_color, (0, 0, 0))
        textRect2 = text2.get_rect()
        textRect2.center = (text1_pos_x // 2, 400)

        font3 = pygame.font.Font('freesansbold.ttf', 48)
        text3 = font3.render("Player vs AI", True, (200, 200, 200), (0, 0, 0))
        textRect3 = text3.get_rect()
        textRect3.center = (text1_pos_x // 2, 500)

        display_surface.blit(text1, textRect)
        display_surface.blit(text2, textRect2)
        display_surface.blit(text3, textRect3)

        pygame.display.update()

def game():

    next_player = 0

    running = True
    win = False
    red_win = False
    blue_win = False

    winner = [red_win, blue_win]

    running = True

    for tile in tile_list:
        tile.type = 0

    while running:

        if not win:
            pygame.mouse.set_visible(False)

        pygame.time.delay(1)

        mouse = pygame.mouse.get_pos() #touple

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu()

            if win == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        next_player = click_mouse(mouse, next_player)
                        winner = win_check(next_player)

            if win and event.type == pygame.MOUSEBUTTONDOWN and 300 < mouse[0] < 700 and 380 < mouse[1] < 420:
                if event.button == 1:
                    menu()


        screen.fill((0, 0, 0))

        draw_tiles()

        if not win:
            draw_mouse(mouse, next_player)

        if win == True:

            pygame.mouse.set_visible(True)

            mouse = pygame.mouse.get_pos()

            if winner == 0:
                win_text = "Red Won!"
                text_color = (200, 50, 50)
            elif winner == 1:
                win_text = "Blue Won!"
                text_color = (50, 50, 200)

            text1_pos_x = 960

            font = pygame.font.Font('freesansbold.ttf', 60)
            text1 = font.render(win_text, True, text_color)
            textRect = text1.get_rect()
            textRect.center = (text1_pos_x // 2, 200)
            screen.blit(text1, textRect)

            if 300 < mouse[0] < 700 and 380 < mouse[1] < 420:
                text2_color = (255, 170, 180)
            else:
                text2_color = (200, 200, 200)

            font2 = pygame.font.Font('freesansbold.ttf', 48)
            text2 = font2.render("Back To Menu", True, text2_color)
            textRect2 = text2.get_rect()
            textRect2.center = (text1_pos_x // 2, 400)
            screen.blit(text2, textRect2)

        pygame.display.update()

        if win == True:
            pygame.mouse.set_visible(True)

        if winner != None:
            if winner == 0:
                win = True
            elif winner == 1:
                win = True

class Tiles:

    def __init__(self, type, grid_pos):
        self.type = type
        self.grid_pos = grid_pos


tile_list=[]

for x in range(30):
    for y in range(30):
        tile = Tiles(0, (x, y))

        tile_list.append(tile)


def draw_tiles():

    for tile in tile_list:
        if tile.type == 1:
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(tile.grid_pos[0] * 32 + 1, tile.grid_pos[1] * 32 + 1, 30, 30))
            screen.blit(image_x, (tile.grid_pos[0]*32+1, tile.grid_pos[1]*32+1))
        elif tile.type == 2:
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(tile.grid_pos[0] * 32 + 1, tile.grid_pos[1] * 32 + 1, 30, 30))
            pygame.draw.circle(screen, (50, 50, 200), (tile.grid_pos[0]*32+16, tile.grid_pos[1]*32+16), 15, 4)

        else:
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(tile.grid_pos[0]*32+1, tile.grid_pos[1]*32+1, 30, 30))


def draw_mouse(mouse, next_player):

    color = (0, 0, 0)

    if next_player == 0:
        color = (200, 10, 10)
    if next_player == 1:
        color = (10, 10, 200)
    pygame.draw.rect(screen, color, pygame.Rect(mouse[0]-5, mouse[1]-5, 10, 10))

def click_mouse(mouse, next_player):

    if next_player == 0:
        for tile in tile_list:
            if (math.floor(mouse[0]/32), math.floor(mouse[1]/32)) == tile.grid_pos:
                if tile.type == 0:
                    tile.type = 1
                    return 1
                else:
                    return next_player
    elif next_player == 1:
        for tile in tile_list:
            if (math.floor(mouse[0] / 32), math.floor(mouse[1] / 32)) == tile.grid_pos:
                if tile.type == 0:
                    tile.type = 2
                    return 0
                else:
                    return next_player


def win_check(next_player):
    check_tile_list = []

    if next_player == 1:
        for tile in tile_list:
            if tile.type == 1:
                check_tile_list.append(tile)
        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] + 1:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] + 2:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] - 1:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] - 2:
                                            return 0

        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] - 1 and red1.grid_pos[1] == red2.grid_pos[1]:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] - 2 and red1.grid_pos[1] == red2.grid_pos[1]:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] + 1and red1.grid_pos[1] == red2.grid_pos[1]:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] + 2 and red1.grid_pos[1] == red2.grid_pos[1]:
                                            return 0

        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] - 1 and red1.grid_pos[1] == red2.grid_pos[1] - 1:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] - 2 and red1.grid_pos[1] == red2.grid_pos[1] - 2:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] + 1and red1.grid_pos[1] == red2.grid_pos[1] + 1:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] + 2 and red1.grid_pos[1] == red2.grid_pos[1] + 2:
                                            return 0

        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] - 1 and red1.grid_pos[1] == red2.grid_pos[1] + 1:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] - 2 and red1.grid_pos[1] == red2.grid_pos[1] + 2:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] + 1and red1.grid_pos[1] == red2.grid_pos[1] - 1:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] + 2 and red1.grid_pos[1] == red2.grid_pos[1] - 2:
                                            return 0

    if next_player == 0:
        for tile in tile_list:
            if tile.type == 2:
                check_tile_list.append(tile)
        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] + 1:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] + 2:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] - 1:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] and red1.grid_pos[1] == red2.grid_pos[1] - 2:
                                            return 1

        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] - 1 and red1.grid_pos[1] == red2.grid_pos[1]:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] - 2 and red1.grid_pos[1] == red2.grid_pos[1]:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] + 1and red1.grid_pos[1] == red2.grid_pos[1]:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] + 2 and red1.grid_pos[1] == red2.grid_pos[1]:
                                            return 1

        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] - 1 and red1.grid_pos[1] == red2.grid_pos[1] - 1:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] - 2 and red1.grid_pos[1] == red2.grid_pos[1] - 2:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] + 1and red1.grid_pos[1] == red2.grid_pos[1] + 1:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] + 2 and red1.grid_pos[1] == red2.grid_pos[1] + 2:
                                            return 1

        for red1 in check_tile_list:
            for red2 in check_tile_list:
                if red1.grid_pos[0] == red2.grid_pos[0] - 1 and red1.grid_pos[1] == red2.grid_pos[1] + 1:
                    for red2 in check_tile_list:
                        if red1.grid_pos[0] == red2.grid_pos[0] - 2 and red1.grid_pos[1] == red2.grid_pos[1] + 2:
                            for red2 in check_tile_list:
                                if red1.grid_pos[0] == red2.grid_pos[0] + 1and red1.grid_pos[1] == red2.grid_pos[1] - 1:
                                    for red2 in check_tile_list:
                                        if red1.grid_pos[0] == red2.grid_pos[0] + 2 and red1.grid_pos[1] == red2.grid_pos[1] - 2:
                                            return 1

menu()



