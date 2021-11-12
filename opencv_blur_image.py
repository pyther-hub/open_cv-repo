from pygame.locals import *
import cv2
import pickle
import pygame
pygame.init()
all_data = {}


def convert_image_to_table(image_path):
    IO_FILE = open('image_data.dat', 'wb+')
    image = cv2.imread(image_path)
    depth, width = image.shape[:2]
    for x_pos in range(0, width):
        for y_pos in range(0, depth):
            b, g, r = image[y_pos, x_pos]
            all_data[(y_pos, x_pos)] = (r, g, b)
    pickle.dump([all_data, [width, depth]], IO_FILE)
    print('done')


def convert_table_to_image_1(blur_level: int = 1+1):
    blur_level += 1
    image_info = pickle.load(open('image_data.dat', 'rb'))
    data = image_info[0]
    width, depth = image_info[1]
    print('loaded')
    screen = pygame.display.set_mode((width, depth))
    pygame.display.update(screen.fill((255, 255, 255)))
    pygame.display.set_caption(f'{width}X{depth}')
    flag = not True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
        for x_pos in range(0, width, blur_level-1):
            for y_pos in range(0, depth, blur_level-1):
                positions_in_square = list(
                    zip(range(y_pos, y_pos+blur_level-1), range(x_pos, x_pos+blur_level-1)))
                r, b, g = 0, 0, 0
                for pos in positions_in_square:
                    color = data[pos]
                    #print(' '*10, color)
                    r += color[0]
                    b += color[1]
                    g += color[2]
                total_numb = blur_level-1
                if flag:
                    print((int(r/total_numb), int(b/total_numb), int(g / total_numb)))
                    print(len(positions_in_square))
                pygame.draw.rect(screen, (int(r/total_numb), int(b/total_numb), int(g /
                                 total_numb)), (x_pos, y_pos, blur_level, blur_level))
        pygame.display.update()
        flag = False


def convert_table_to_image_2(blur_level: int = 1+1):
    blur_level += 1
    image_info = pickle.load(open('image_data.dat', 'rb'))
    data = image_info[0]
    width, depth = image_info[1]
    print('loaded')
    screen = pygame.display.set_mode((width, depth))
    pygame.display.update(screen.fill((255, 255, 255)))
    pygame.display.set_caption(f'{width}X{depth}')
    flag = not True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
        for x_pos in range(0, width, blur_level-1):
            for y_pos in range(0, depth, blur_level-1):
                r, b, g = 0, 0, 0
                for sq_pos_x in range(y_pos, y_pos+blur_level-1):
                    for sq_pos_y in range(x_pos, x_pos+blur_level-1):
                        color = data[sq_pos_x, sq_pos_y]
                        r += color[0]
                        b += color[1]
                        g += color[2]
                total_numb = (blur_level-1)**2
                if flag:
                    print((int(r/total_numb), int(b/total_numb), int(g / total_numb)))

                pygame.draw.rect(screen, (int(r/total_numb), int(b/total_numb), int(g /
                                 total_numb)), (x_pos, y_pos, blur_level, blur_level))
        pygame.display.update()
        flag = False

convert_table_to_image_2(10)
