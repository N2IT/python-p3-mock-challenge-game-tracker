class Game:

    def __init__(self, title="" ):
        self._title = title
        
        # add player to game
        self._players = []

        # add results to Game
        self._results = []
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            if isinstance(title, str) and len(title) > 0:
                self._title = title

    def results(self):
        return [ result for result in Result.all if result.game == self ]
            
    def players(self):
        players_list = []
        for result in Result.all:
            if result.game == self:
                if result.player in players_list:
                    None
                else: 
                    players_list.append(result.player)
        return players_list

    def average_score(self, player):
        all_scores = []
        for result in Result.all:
            if result.player == player:
                all_scores.append(result.score)
        score_sum = sum(all_scores)
        score_number = len(all_scores)
        return score_sum / score_number
                
                


    def __repr__(self):
        return f"Game: {self.title}"

class Player:

    all = []

    def __init__(self, username):
        self._username = username

        # add games to players
        self._games = []

        # add results to players
        self._results = []

        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 < len(username) < 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return [ game for game in Result.all if game.player == self ]

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

    def __repr__(self):
        return f"Player: {self.username}"

class Result:
    
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score
        Result.all.append(self)

        # construct result object as SSOT
        # populating lists within Player class
        self.player._games.append(self.game)
        self.player._results.append(self)

        # populating lists within Game class
        self.game._players.append(self.player)
        self.game._results.append(self)

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

    def __repr__(self):
        return f"{self.player}\n{self.game}\nScore: {self.score}"