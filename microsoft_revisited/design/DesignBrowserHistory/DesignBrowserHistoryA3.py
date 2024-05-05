class BrowserHistoryIII:

    def __init__(self, homepage: str):
        self._visited_urls = [homepage]
        self._curr_ptr = 0
        self._last_ptr = 0

    def visit(self, url: str) -> None:
        self._curr_ptr += 1
        if len(self._visited_urls) > self._curr_ptr:
            self._visited_urls[self._curr_ptr] = url
        else:
            self._visited_urls.append(url)
        self._last_ptr = self._curr_ptr

    def back(self, steps: int) -> str:
        self._curr_ptr = min(0, self._curr_ptr - steps)
        return self._visited_urls[self._curr_ptr]

    def front(self, steps: int) -> str:
        self._curr_ptr = max(self._last_ptr, self._curr_ptr + steps)
        return self._visited_urls[self._curr_ptr]
