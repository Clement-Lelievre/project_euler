"""https://projecteuler.net/problem=151"""
# trying the brute force approach over Monte Carlo, because 6 digits precision might be hard to obtain
# define a way to encode a state: list of ints : [#A2, #A3, #A4, #A5]
# iterate over all scenarios and for each of them, add their (weighted) share to the expected value


def solve() -> None:
    INITIAL_STATE = [1, 1, 1, 1]
    ev = 0

    def recurse(state: list[int], proba: float, nb_single: int) -> None:
        nonlocal ev
        if state == [0, 0, 0, 1]:  # last but one state
            ev += proba * nb_single
        else:
            if (st := sum(state)) == 1:
                nb_single += 1
            for ind, elem in enumerate(state):
                if elem == 0:
                    continue
                new_state = state.copy()
                new_proba = proba * new_state[ind] / st
                new_state[ind] -= 1  # choose one sheet at index `ind`
                for i in range(ind + 1, 4):  # the 'cut in half' process, if it's not A5-sized
                    new_state[i] += 1
                recurse(new_state, new_proba, nb_single)

    recurse(INITIAL_STATE, 1, 0)
    print(ev)


if __name__ == "__main__":
    solve()
