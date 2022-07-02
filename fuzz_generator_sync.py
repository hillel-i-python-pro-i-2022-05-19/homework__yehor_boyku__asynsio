import concurrent.futures
import logging
from concurrent import futures
from typing import Iterator

from settings import CHARACTERS
from init_logging import init_logging
from fuzz_generator import generate, DEFAULT_ALPHABET


# def generator_word(length: int = 5, quantity: int = len(CHARACTERS) + 1, conditions: str = CHARACTERS):
def generator_word(length: int = 5, quantity: int = 15, conditions: str = 'abcdefgh'):
    result = list(generate(word_length=length, quantity=quantity, alphabet=conditions))
    logging.info(result)
    return result


def calculate_process(quantity: list[int]) -> list[str]:
    with concurrent.futures.ProcessPoolExecutor() as worker:
        results = worker.map(
            generator_word,
            quantity,
        )
        worker.submit(generator_word, args=(quantity[0],))
        items = [future.result() for future in concurrent.futures.as_completed(results)]
    return items


def main():
    alphabet = DEFAULT_ALPHABET
    word_length = 5
    quantity = len(CHARACTERS)
    # combinations = list(range(1, quantity + 1))
    combinations = list(range(1, 4))
    calculate_process(quantity=combinations)
    # calculate_thread(quantity=combinations)
    print()


if __name__ == "__main__":
    init_logging()
    main()
