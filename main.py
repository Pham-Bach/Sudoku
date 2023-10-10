import pygame


pygame.init()

screen = pygame.display.set_mode((750, 800))

pygame.display.set_caption("Sodoku")

font = pygame.font.SysFont(None, 80)

number_grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
	[6, 0, 0, 0, 7, 5, 0, 0, 9],
	[0, 0, 0, 6, 0, 1, 0, 7, 8],
	[0, 0, 7, 0, 4, 0, 2, 6, 0],
	[0, 0, 1, 0, 5, 0, 9, 3, 0],
	[9, 0, 4, 0, 6, 0, 0, 0, 5],
	[0, 7, 0, 3, 0, 0, 0, 1, 2],
	[1, 2, 0, 0, 0, 7, 4, 0, 0],
	[0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Mảng mới random_number_grid = [[0 for i in range(9)] for j in range(9)]

'''
# Lặp qua mảng ban đầu
for row in range(9):
    for col in range(9):
        # Chọn một vị trí ngẫu nhiên trong mảng mới
        random_row = random.randint(0, 8)
        random_col = random.randint(0, 8)

        # Đặt giá trị của mảng ban đầu vào vị trí ngẫu nhiên đó
        random_number_grid[random_row][random_col] = number_grid[row][col]
'''
def draw_bg():
    #background color
    screen.fill((255, 255, 255))

    #
    pygame.draw.rect(screen, pygame.Color("black"), pygame.Rect(15, 15, 720, 720), 10) #

    #
    i = 1
    while (i * 80) < 720: #720 / 9 = 80, i * 80 = x coordinate, margin = 15, y = 15, line width = 5
        line_width = 5 if i % 3 > 0 else 10
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2((i * 80) + 15, 15), pygame.Vector2((i * 80) + 15, 735), line_width)
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(15, (i * 80) + 15), pygame.Vector2(735, (i * 80) + 15), line_width)
        i += 1

def draw_num():
    row = 0
    offset = 35
    while row < 9:
        col = 0
        while col < 9:
            #output = random_number_grid[row][col]
            output = number_grid[row][col]
            #print(str(output))
            n_text = font.render(str(output), True, pygame.Color("black"))
            screen.blit(n_text, pygame.Vector2((col * 80) + offset + 3, (row * 80) + offset - 3))
            col += 1
        row +=1

x = 0
y = 0
dif = 720/9
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_bg()

    draw_num()

    pygame.display.update()
