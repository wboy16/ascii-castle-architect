def draw_spires():
    print("""
   /\\      /\\
  /  \\    /  \\
 | [] |  | [] |""")


def draw_wall_section():
    print("|" + "=" * 14 + "|")
    print("| [ ]     [ ]  |")


def draw_gate():
    print("|" + "=" * 14 + "|")
    print("|    | || |    |")
    print("|    | || |    |")


def castle_arch():
    draw_spires()
    for i in range(3):
        draw_wall_section()
    draw_gate()


castle_arch()
