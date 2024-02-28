class Game:

    all = []

    def __init__(self, title=""):
        self._title = title
        Game.all.append(self)
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            if isinstance(title, str) and len(title) > 0:
                self._title = title

    def results(self):
        return [ result for result in Result.all if result.game == self]

    def players(self):
        pass

    def average_score(self, player):
        pass

    def __str__(self):
        return f"Game: {self.title}"

class Player:

    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 < len(username) < 16:
            self._username = username

    def results(self):
        if isinstance(result, Result):
            [result for result in Results.all if resresult.player == self]

    def games_played(self):
        if isinstance(game, Game):
            return 

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

    def __str__(self):
        return f"Player: {self.username}"

class Result:
    
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if hasattr(self, "score"):
            if isinstance(score, int) and 1 < score < 5000:
                self._score = score

    def __str__(self):
        return f"{self.player}\n{self.game}\nScore: {self.score}"