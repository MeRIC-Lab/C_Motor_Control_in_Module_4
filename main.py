from motorLLC import *
import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


mc = motorLLC()

mc.open()
mc.toruqe_enable()

index = 0
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]         # Goal position

for i in range(1, 6):
#while 1:
#    print("Press any key to continue! (or press ESC to quit!)")
#    if getch() == chr(0x1b):
#        break

    mc.moveto(dxl_goal_position[index])

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0

mc.close()
