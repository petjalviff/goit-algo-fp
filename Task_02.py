import turtle


def draw_pifagor_tree(branch_length, t, angle, level):
    if level == 0:
        return
    else:
        t.forward(branch_length)
        t.right(angle)
        draw_pifagor_tree(0.7 * branch_length, t, angle, level - 1)
        t.left(2 * angle)
        draw_pifagor_tree(0.7 * branch_length, t, angle, level - 1)
        t.right(angle)
        t.backward(branch_length)


def main():
    screen = turtle.Screen()
    screen.bgcolor("skyblue")

    t = turtle.Turtle()
    t.speed(10)
    t.color("blue")
    t.width(3)

    level = int(turtle.textinput("Рівень", "Введіть рівень рекурсії:"))

    t.left(90)
    draw_pifagor_tree(100, t, 45, level)

    screen.exitonclick()


if __name__ == "__main__":
    main()