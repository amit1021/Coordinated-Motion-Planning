
def test(eb, number_of_steps):
    not_good = 0
    for k in range(eb.n):
        for z in range(eb.n):
            if eb.board_final_state[k][z] != eb.board[k][z] and eb.board_final_state[k][z] > 0:
                not_good += 1

    print("number of not good final: ", not_good)

    print("number_of_steps: ", number_of_steps)
