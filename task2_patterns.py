ESC = "\x1b"
CSI = f"{ESC}["
RESET = f"{CSI}0m"


def block(rgb=(0, 0, 0), width=2):
    r, g, b = rgb
    return f"\033[48;2;{r};{g};{b}m" + (" " * width) + RESET

def print_romb(x, y, cx, cy, r, thickness=2):
    md = abs(x - cx) + abs(y - cy)
    return (r - thickness) < md <= r

def draw(nx=25, ny=13, pixel_w=2, pixel_h=1, color_on=(0, 0, 0), color_off=(255, 255, 255)):
    cy = ny // 2
    r = 5
    thickness = 2
    cx1 = 6
    cx2 = cx1 + 2 * r

    on_px  = block(color_on,  pixel_w)
    off_px = block(color_off, pixel_w)

    for y in range(ny):
        line = []
        for x in range(nx):
            on = (
                print_romb(x, y, cx1, cy, r, thickness) or
                print_romb(x, y, cx2, cy, r, thickness)
            )
            line.append(on_px if on else off_px)
        row = "".join(line)
        for _ in range(pixel_h):
            print(row)

if __name__ == "__main__":
    draw(nx=25, ny=13, pixel_w=2, pixel_h=1, color_on=(0, 0, 0), color_off=(255, 255, 255) )
