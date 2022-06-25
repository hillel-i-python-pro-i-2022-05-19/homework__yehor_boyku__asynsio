import concurrent.futures
from typing import Iterator

from settings import CHARACTERS
from init_logging import init_logging
from test import generate, DEFAULT_ALPHABET


def generator_word(length: int = 5, quantity: int = len(CHARACTERS) + 1, conditions: str = CHARACTERS):
    generate(word_length=length, quantity=quantity, alphabet=conditions)
    print(generate)


def calculate_process(quantity) -> Iterator[None]:
    with concurrent.futures.ProcessPoolExecutor() as worker:
        results = worker.map(
            generator_word,
            quantity,
        )
        worker.submit(generator_word, args=(quantity[0],))
    return results


def main():
    alphabet = DEFAULT_ALPHABET
    word_length = 5
    quantity = len(CHARACTERS)
    combinations = list(range(quantity, quantity + 10))
    calculate_process(quantity=combinations)
    print()


if __name__ == "__main__":
    init_logging()
    main()
