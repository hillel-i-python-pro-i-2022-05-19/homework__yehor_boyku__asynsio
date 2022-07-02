from string import ascii_lowercase, digits
from typing import Final, TypeAlias, Iterable

from init_logging import init_logging

T_ALPHABET: TypeAlias = str
T_WORD: TypeAlias = str

T_INDEX_OF_CHARACTER: TypeAlias = int

DEFAULT_ALPHABET: Final[T_ALPHABET] = ascii_lowercase + digits


def generate(word_length: int, quantity: int, alphabet: T_ALPHABET) -> Iterable[T_WORD]:
    min_index_of_character_in_alphabet: Final[T_INDEX_OF_CHARACTER] = 0
    max_index_of_character_in_alphabet: Final[T_INDEX_OF_CHARACTER] = len(alphabet) - 1

    word_as_list_of_indexes: list[T_INDEX_OF_CHARACTER] = [min_index_of_character_in_alphabet] * word_length

    current_position: int = len(word_as_list_of_indexes) - 1
    previous_position: int = current_position
    last_position: int = word_length - 1

    count = 0
    while count < quantity:
        if current_position == previous_position == last_position:
            if word_as_list_of_indexes[current_position] <= max_index_of_character_in_alphabet:
                yield ''.join([alphabet[index] for index in word_as_list_of_indexes])
                word_as_list_of_indexes[current_position] += 1
            else:
                word_as_list_of_indexes[current_position] = min_index_of_character_in_alphabet
                previous_position = current_position
                current_position -= 1
        elif current_position >= 0:
            if word_as_list_of_indexes[current_position] < max_index_of_character_in_alphabet:
                word_as_list_of_indexes[current_position] += 1
                current_position = previous_position
            else:
                word_as_list_of_indexes[current_position] = min_index_of_character_in_alphabet
                current_position -= 1
        else:
            break


def main():
    alphabet = DEFAULT_ALPHABET
    word_length = 5
    combinations = len(alphabet) ** 4
    with open("r_of_generator.txt", "w") as file:
        for word in generate(word_length=word_length, quantity=combinations + 1, alphabet=alphabet):
            print(word)
            file.write(word + "\n")


if __name__ == '__main__':
    init_logging()
    main()
