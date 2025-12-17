def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_in_front():
        if right_is_clear():
            turn_right()
            move()
        else:
            move()
    elif wall_in_front():
        turn_right()
        if wall_in_front():
            turn_left()
            turn_left()
            if wall_in_front():
                turn_left()
                move()
            else:
                move()
        else:
            move()
            