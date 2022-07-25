import colors

ASCII = "¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;\"^:,'.` "
# reverse the string
ASCII = ASCII[::-1]
N_ASCII = len(ASCII)

def convert_value(x):
    return ASCII[int(x/256*N_ASCII)]

if __name__ == '__main__':
    # create a grid of gradient
    grid = ""
    for i in range(255):
        _ = convert_value(i) * 80
        grid += _ + "\n"
    print(grid)
