import random
class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.agent_pos = (0, 0)
        self.wumpus_pos = (random.randint(1, size-1), random.randint(1, size-1))
        self.gold_pos = (random.randint(1, size-1), random.randint(1, size-1))
        self.pits = [(random.randint(1, size-1), random.randint(1, size-1)) for _ in range(2)]
        self.alive = True
        self.has_gold = False
    def get_percepts(self, pos):
        x, y = pos
        percepts = []
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]: # Check adjacent cells for breeze (pit nearby)
            adj_x, adj_y = x + dx, y + dy
            if (adj_x, adj_y) in self.pits:
                percepts.append("Breeze")
                break
        if abs(x - self.wumpus_pos[0]) + abs(y - self.wumpus_pos[1]) == 1: # Check for stench (wumpus nearby)
            percepts.append("Stench") # Check for glitter (gold here)
        if pos == self.gold_pos:
            percepts.append("Glitter")
        return percepts
    def move_agent(self, direction):
        x, y = self.agent_pos
        moves = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
        dx, dy = moves.get(direction, (0, 0))
        new_pos = (x + dx, y + dy)
        if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
            self.agent_pos = new_pos
            if new_pos == self.wumpus_pos or new_pos in self.pits:
                self.alive = False
            elif new_pos == self.gold_pos:
                self.has_gold = True
if __name__ == "__main__":
    world = WumpusWorld()
    print(f"Wumpus at: {world.wumpus_pos}, Gold at: {world.gold_pos}, Pits at: {world.pits}")
    for move in ["right", "up", "right", "down"]:
        if world.alive:
            world.move_agent(move)
            percepts = world.get_percepts(world.agent_pos)
            print(f"Move {move} to {world.agent_pos}: {percepts}")
            if not world.alive:
                print("Agent died!")
            elif world.has_gold:
                print("Gold found!")