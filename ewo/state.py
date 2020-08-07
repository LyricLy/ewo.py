from typing import Sequence, Tuple, Optional


class Entity:
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.icon = i

    def __repr__(self):
        return f"Entity({self.x}, {self.y}, {repr(self.icon)})"

    def __str__(self):
        return f"{self.icon} at {self.pos}"

class ViewState:
    def __init__(self, hp: float, str: float, entities: Sequence[Entity], walls: Tuple[Optional[int], Optional[int]]):
        self.entities = entities
        self.hp = hp
        self.str = str
        self.walls = walls

    @classmethod
    def from_payload(cls, payload: dict):
        enemies = []
        wall_x = None
        wall_y = None
        for i, c in enumerate(payload["render"]):
            if c in "#*":
                y, x = divmod(i, 21)
                if wall_x is None and x < 10:
                    wall_x = x - 10
                elif wall_y is None and y < 5:
                    wall_y = y - 5
            elif c != " ":
                y, x = divmod(i, 21)
                enemies.append(Entity(x - 10, y - 5, c))
        return cls(payload["hp"], payload["str"], enemies, (wall_x, wall_y))

    def __repr__(self):
        return f"ViewState({self.hp}, {self.str}, {self.entities})"
