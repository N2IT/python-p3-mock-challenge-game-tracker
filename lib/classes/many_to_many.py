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


class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 < len(new_username) < 16:
            self._name = new_username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

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
            return self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            return self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if hasattr(self, "score"):
            if isinstance(score, int) and 1 < score < 5000:
                self._score = score