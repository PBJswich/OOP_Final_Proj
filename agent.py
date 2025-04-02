import torch
import random 
import numpy as np
from collections import deque
# from game import cards 
max_memory = 100_000
batch_size = 1000
LR = 0.001

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # random
        self.gamma = 0 
        self.memory = deque(maxlen = max_memory)

    def get_state(self, game):
        pass

    def remeber(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self):
        pass

    def get_action(self, state):
        pass
def train():
    pass

if __name__ == '__main__':
    train()