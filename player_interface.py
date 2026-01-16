from abc import ABC, abstractmethod
import random
class Player(ABC):
    def __init__(self):
        self.moves=[]
        self.position=(0,0)
        self.path=[self.position]
    def make_move(self):
        dx,dy=random.choice(self.moves)
        x,y=self.position
        self.position=(x+dx,y+dy)
        self.path.append(self.position)
        return self.position
    @abstractmethod
    def level_up(self):
        pass
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),    # up
            (0, -1),   # down
            (-1, 0),   # left
            (1, 0)     # right
        ]
    def level_up(self):
        self.moves=[
            (0, 1),    # up
            (0, -1),   # down
            (-1, 0),   # left
            (1, 0),    # right
            (1,1),     # 4 diagonals
            (1,-1),
            (-1,1),
            (-1,-1)
        ]
if __name__ == "__main__":
    print("Running basic Pawn tests...\n")

    p = Pawn()

    # Test 1: Initial state
    assert p.position == (0, 0)
    assert p.path == [(0, 0)]
    assert len(p.moves) == 4
    print("✔ Initial state test passed")

    # Test 2: Single-step movement
    old_pos = p.position
    new_pos = p.make_move()

    dx = abs(new_pos[0] - old_pos[0])
    dy = abs(new_pos[1] - old_pos[1])
    assert (dx, dy) in [(1, 0), (0, 1)]
    print("✔ Single-step movement test passed")

    # Test 3: Path tracking
    for _ in range(9):
        p.make_move()

    assert len(p.path) == 11  # 1 initial + 10 moves
    print("✔ Path tracking test passed")

    # Test 4: Level up unlocks diagonals
    p.level_up()
    assert len(p.moves) == 8
    print("✔ Level-up moves test passed")

    # Test 5: Moves after level-up are valid
    for _ in range(20):
        old_pos = p.position
        new_pos = p.make_move()
        dx = abs(new_pos[0] - old_pos[0])
        dy = abs(new_pos[1] - old_pos[1])
        assert (dx, dy) in [(1, 0), (0, 1), (1, 1)]
    print("✔ Post–level-up movement test passed")

    print("\nAll tests passed 🎉")
