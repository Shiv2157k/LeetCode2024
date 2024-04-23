class BrowserHistory1:
    """
    Approach: Using Two Stacks
    T: O(1) -> worstCase O(min(m, n))
    S: O(l * n)
    """
    def __init__(self, homepage: str):
        self._history = []
        self._future = []
        self._current = homepage

    def visit(self, url: str):
        # T: O(1)
        self._history.append(self._current)
        self._future = []
        self._current = url

    def back(self, steps: int) -> str:
        # worstCase T: O(min(m, n))
        while steps > 0 and self._history:
            self._future.append(self._current)
            self._current = self._history.pop()
            steps -= 1
        return self._current

    def forward(self, steps: int) -> str:
        # worstCase T: O(min(m, n))
        while steps > 0 and self._future:
            self._history.append(self._current)
            self._current = self._future.pop()
            steps -= 1
        return self._current
