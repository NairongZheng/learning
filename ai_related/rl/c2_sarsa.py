import time

import gym
import numpy as np

import gridworld  # 同一个文件夹里


class SarsaAgent(object):
    def __init__(self, n_status, n_act, lr=0.1, gamma=0.9, e_greed=0.1):
        self.n_status = n_status  # 环境数量
        self.n_act = n_act  # 动作数量
        self.lr = lr  # 学习率
        self.gamma = gamma  # 收益衰减率
        self.epsilon = e_greed  # 探索与利用中的探索概率
        self.Q = np.zeros((n_status, n_act))  # 初始化Q表格

    def predict(self, state):
        """
        利用：根据经验得到当前state应该用哪个action
        """
        # return np.argmax(self.Q[state, :]) # 仅会采取第一个最大的下标，采用下面的方法比较科学
        Q_list = self.Q[state, :]
        action = np.random.choice(
            np.flatnonzero(Q_list == Q_list.max())
        )  # 若最大值不止一个，则随机采样
        return action

    def act(self, state):
        """
        根据(1)探索或者(2)利用得到action
        """
        state = check_state(state)
        if np.random.uniform(0, 1) < self.epsilon:  # 探索
            action = np.random.choice(self.n_act)
        else:  # 利用
            action = self.predict(state)
        return action

    def learn(self, state, action, reward, next_state, next_action, done):
        """
        更新Q表格
        """
        state = check_state(state)
        predict_Q = self.Q[state, action]  # 当前Q
        if done:
            target_Q = reward  # 没有下一个状态了
        else:
            target_Q = reward + self.gamma * self.Q[next_state, next_action]
        self.Q[state, action] += self.lr * (target_Q - predict_Q)  # 修正q


def check_state(state):
    """
    版本不一样，state有时候不是int，自己写了个转化
    """
    if isinstance(state, int):
        state = state
    else:
        state = state[1]["prob"]
    return state


# 训练一轮游戏
def train_episode(env, agent, is_render):
    total_reward = 0
    state = env.reset()  # 重置环境
    action = agent.act(state)  # 根据算法选择一个动作

    while True:
        next_state, reward, terminated, truncated, info = env.step(action)  # 与环境进行一个交互
        next_action = agent.act(next_state)  # 探索与利用得到下一个action

        agent.learn(state, action, reward, next_state, next_action, terminated)

        action = next_action
        state = next_state

        total_reward += reward
        if is_render:
            env.render()
        if terminated:
            break

    return total_reward


# 测试一轮游戏
def test_episode(env, agent):
    total_reward = 0
    state = env.reset()

    while True:
        state = check_state(state)
        action = agent.predict(state)
        next_state, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        state = next_state
        env.render()
        time.sleep(0.5)
        if terminated:
            break

    return total_reward


def train(env, episodes=500, lr=0.1, gamma=0.9, e_greed=0.1):
    agent = SarsaAgent(
        n_status=env.observation_space.n,
        n_act=env.action_space.n,
        lr=lr,
        gamma=gamma,
        e_greed=e_greed,
    )

    is_render = False
    for e in range(episodes):  # episodes就是agent走多少次
        ep_reward = train_episode(env, agent, is_render)
        print("Episode %s: reward = %.1f" % (e, ep_reward))

        # 每隔50个episode渲染一下看看效果
        if e % 50 == 0:
            is_render = True
        else:
            is_render = False

    test_reward = test_episode(env, agent)
    print("test reward = %.1f" % (test_reward))


if __name__ == "__main__":
    env = gym.make("CliffWalking-v0")  # 0上, 1右, 2下, 3左
    env = gridworld.CliffWalkingWapper(env)
    train(env)
