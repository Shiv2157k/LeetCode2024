

class CompressedStringIterator:

    def __init__(self, compressedString: str):
        self._compressed_str = compressedString
        self._letter = None
        self._letter_counter = 0
        self._next_letter_pointer = 0

    def __move_to_next(self):
        # "L10e2t1C1o1d1e11"
        if self._next_letter_pointer >= len(self._compressed_str):
            raise StopIteration("No more elements to display")
        self._letter = self._compressed_str[self._letter_counter]
        start_pos = curr_pos = self._letter_counter + 1
        while curr_pos < len(self._compressed_str) and self._compressed_str[curr_pos].isdigit():
            curr_pos += 1
        self._letter_counter = int(self._next_letter_pointer[start_pos: curr_pos])
        self._next_letter_pointer = curr_pos

    def next(self):
        if not self.hasNext():
            return ' '
        if self._letter_counter == 0:
            self.__move_to_next()
        self._letter_counter -= 1
        return self._letter

    def hasNext(self):
        return self._next_letter_pointer < len(self._compressed_str) or self._letter_counter > 0