class Game:
    def __init__(self, title: str):
        if hasattr(self, '_title'):
            raise AttributeError("Title is already set and cannot be modified.")
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if len(title.strip()) == 0:
            raise ValueError("Title must be longer than 0 characters.")
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise AttributeError("Title is already set and cannot be modified.")


    def add_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("Result must be of type Result.")
        self._results.append(result)

    def results(self):
        return self._results

    def players(self):
        return list(set(result.player for result in self._results))
    
    def average_score(player, game):
        scores = [result.score for result in player.results() if result.game == game]
        return sum(scores) / len(scores) if scores else 0


class Player:
    def __init__(self, username: str):
        self.username = username
        self._results = []

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Username must be a string.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Username must be between 2 and 16 characters, inclusive.")
        self._username = value

    def add_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("Result must be of type Result.")
        self._results.append(result)

    def results(self):
        return [result for result in self._results if isinstance(result, Result)]

    def games_played(self):
        return list(set(result.game for result in self._results))

    def played_game(self, game):
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)


class Result:
    def __init__(self, player, game, score: int):
        if hasattr(self, '_score'):
            raise AttributeError("Score is already set and cannot be modified.")
        if not isinstance(player, Player):
            raise TypeError("Player must be of type Player.")
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game.")
        if not isinstance(score, int):
            raise TypeError("Score must be of type int.")
        if not (1 <= score < 5000):
            raise ValueError("Score must be between 1 and 5000, inclusive.")

        self._score = score
        self._player = player
        self._game = game

        player.add_result(self)
        game.add_result(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        raise AttributeError("Score is already set and cannot be modified.")


    @property
    def player(self):
        return self._player
    
    @property
    def game(self):
        return self._game

    

