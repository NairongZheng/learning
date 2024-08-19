import gym
import random
import gridworld


def test1():
    """
    CliffWalking-v0
    """
    # env = gym.make("CliffWalking-v0")
    env = gym.make("CliffWalking-v0", render_mode="human")
    # env = gridworld.CliffWalkingWapper(env)

    state = env.reset()
    while True:
        # action = random.randint(0,3)
        action = env.action_space.sample()  # 这个等于上面的，因为就是上下左右
        state, reward, terminated, truncated, info = env.step(action)

        env.render()  # 渲染一帧动画
        if terminated:
            break


def test2():
    """
    CartPole-v1
    """
    # env = gym.make("CartPole-v1")
    env = gym.make("CartPole-v1", render_mode="human")

    state = env.reset()
    while True:
        action = env.action_space.sample()
        state, reward, terminated, truncated, info = env.step(action)

        env.render()  # 渲染一帧动画
        # if terminated:
        #     break


def main():
    # test1()  # 测试CliffWalking-v0
    test2()   # 测试CartPole-v1
    pass


if __name__ == "__main__":
    main()
