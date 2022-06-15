import concurrent.futures
from itertools import combinations_with_replacement, product
from typing import Iterator

from settings import CHARACTERS
from init_logging import init_logging


def generator_word(length: int = 5, conditions: str = CHARACTERS):
    for i in product(conditions, repeat=length):
        print(''.join(i))


def calculate_process(quantity) -> Iterator[None]:
    with concurrent.futures.ProcessPoolExecutor() as worker:
        results = worker.map(
            generator_word,
            quantity,
        )
        worker.submit(generator_word, args=(quantity[0],))
    return results


def main():
    start = 5
    quantity = list(range(start))
    calculate_process(quantity=quantity)
    print()


if __name__ == "__main__":
    init_logging()
    main()
