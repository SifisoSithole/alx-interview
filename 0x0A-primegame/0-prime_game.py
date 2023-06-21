#!/usr/bin/python3
"""
Prime game
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        if n == 1:
            return "Ben"

        numbers = set(range(2, n + 1))
        player = "Maria"

        while True:
            prime = None
            for num in numbers:
                if is_prime(num):
                    prime = num
                    break

            if prime is None:
                return player

            numbers.difference_update(range(prime, n + 1, prime))

            player = "Ben" if player == "Maria" else "Maria"

    winners = [play_game(n) for n in nums]

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
