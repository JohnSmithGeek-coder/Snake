class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self):
        """初始化统计信息"""
        self.reset_stats()
        self.game_active = False
        self.music_active = True
        self.first_game = True
        self.space_pause = False
        self.highest_score = 0
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.food_score = 0