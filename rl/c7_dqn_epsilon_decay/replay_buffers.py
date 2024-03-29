import random
import collections
from torch import FloatTensor
import numpy as np


class ReplayBuffer(object):
    def __init__(self, max_size, num_steps=1):
        self.buffer = collections.deque(maxlen=max_size)
        self.num_steps = num_steps

    def append(self, exp):
        self.buffer.append(exp)

    def sample(self, batch_size):
        mini_batch = random.sample(self.buffer, batch_size)
        obs_batch, action_batch, reward_batch, next_obs_batch, done_batch = zip(
            *mini_batch
        )
        obs_batch = FloatTensor([np.array(i) for i in obs_batch])
        # obs_batch = FloatTensor(obs_batch)
        action_batch = FloatTensor(action_batch)
        reward_batch = FloatTensor(reward_batch)
        # next_obs_batch = FloatTensor(next_obs_batch)
        next_obs_batch = FloatTensor([np.array(i) for i in next_obs_batch])
        done_batch = FloatTensor(done_batch)
        return obs_batch, action_batch, reward_batch, next_obs_batch, done_batch

    def __len__(self):
        return len(self.buffer)


if __name__ == "__main__":
    a = collections.deque(maxlen=3)
    print(a)
    a.append((1, 1))
    a.append((2, 2))
    a.append((3, 3))
    a.append((4, 4))
    print(a)
    state, action = zip(*a)
    print(state, action)
