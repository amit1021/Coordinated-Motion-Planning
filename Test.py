
def test(eb, number_of_steps):
    not_good = 0
    for k in range(eb.n):
        for z in range(eb.n):
            if eb.board_final_state[k][z] != eb.board[k][z] and eb.board_final_state[k][z] > 0:
                not_good += 1
                print("robot final place", k, " ", z, " ", eb.board_final_state[k][z])
                print("robot board", k, " ", z, " ", eb.board[k][z])

    print("number of not good final: ", not_good)
    # print(
    #     "   0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29")
    # for i in range(eb.n):
    #     print(i, eb.board[i])


    print("number_of_steps: ", number_of_steps)
