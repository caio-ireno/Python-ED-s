class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
    
    def __str__(self):
        return f"({self._name}, {self._score})"


class Score:
    max_entries = 10

    def __init__(self):
        self._entries = []

    def __str__(self):
        return "[" + ", ".join(str(entry) for entry in self._entries) + "]"

    def add(self, entry):
        new_score = entry.get_score()

        if len(self._entries) == self.max_entries:
            if new_score <= self._entries[-1].get_score():
                return
            else:
                self._entries.pop()

        i = len(self._entries)
        while i > 0 and new_score > self._entries[i - 1].get_score():
            i -= 1

        self._entries.insert(i, entry)


# Exemplo de utilização
if __name__ == "__main__":
    score_board = Score()

    score_board.add(GameEntry("Alice", 100))
    score_board.add(GameEntry("Bob", 80))
    score_board.add(GameEntry("Charlie", 120))
    score_board.add(GameEntry("David", 90))
    score_board.add(GameEntry("Eve", 110))

    score_board.add(GameEntry("caio",10000))

    print(score_board)
