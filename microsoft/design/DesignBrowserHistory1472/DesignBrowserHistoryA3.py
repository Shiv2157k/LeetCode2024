from typing import List


class DesignBrowserHistory:

    def __init__(self, homepage: str):
        self.visitedURLs = [homepage]
        self.currURL = 0
        self.lastURL = 0

    def visit(self, url: str) -> None:
        self.currURL += 1
        if len(self.visitedURLs) > self.currURL:
            self.visitedURLs[self.currURL] = url
        else:
            self.visitedURLs.append(url)
        self.lastURL = self.currURL

    def back(self, steps: int) -> str:
        self.currURL = max(0, self.currURL - steps)
        return self.visitedURLs[self.currURL]

    def forward(self, steps: int) -> str:
        self.currURL = min(self.lastURL, self.currURL + steps)
        return self.visitedURLs[self.currURL]
