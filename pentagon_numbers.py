"""https://projecteuler.net/problem=44"""

# I first analyzed with pen and paper and thought I could use some clever formula to optimize but did not quite find it
# from what I saw in the thread after solving, not many solvers found a smart way


def pentagon_numbers(n: int) -> list[int]:
    return [k * (3 * k - 1) / 2 for k in range(1, n + 1)]


def search(first_nb_pentagonals: int) -> int | None:
    pentagonals = pentagon_numbers(first_nb_pentagonals)
    pentagonals = pentagonals[
        len(pentagonals) // 10 :
    ]  # optim: no need to include the first 10% elements since they were done at previous iteration
    pentagonals_set = set(pentagonals)
    diff = 1
    while diff < len(pentagonals):
        for i in range(len(pentagonals) - diff):
            if (
                delta := pentagonals[i + diff] - pentagonals[i]
            ) in pentagonals_set and pentagonals[i + diff] + pentagonals[
                i
            ] in pentagonals_set:
                return delta  # it must be the solution since I iterate over sorted pentagonals and the diff P(n+1)-P(n) = 3n+1 is growing
        diff += 1

def solve() -> None:
    power = 2
    while (res := search(10**power)) is None:
        power += 1
    print(res)


if __name__ == "__main__":
    assert pentagon_numbers(10) == [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    solve()  # my solution works but for it to be sound, ie the global minimum, I'd need to prove that it can't happen that there is a better solution (ie lower delta) further up the pentagonals
    # for example, assume I find P(k+i) - P(k) as solution, with diff i between the indices. Maybe there is later in the pentagonals a diff less than i, say j, AND such that
    # P(m+j) - P(m) < P(k+i) - P(k)
