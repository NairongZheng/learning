# rl强化学习
[参考链接](https://www.bilibili.com/video/BV1Gq4y1v7Bs)

[代码链接](https://github.com/rexrex9/reinforcement_torch_pfrl/tree/main)

0. gridworld.py：渲染用的
1. gym了解
2. SARSA
3. Q-learning
4. DQN
5. 经验回放
6. 固定Q目标


## 公式
1. 时序差分TD：$V(S_t){\leftarrow}V(S_t)+\alpha[R_{t+1}+{\gamma}V(S_{t+1})-V(S_t)]$
2. SARSA：$Q(S_t,A_t){\leftarrow}Q(S_t,A_T)+\alpha[R_{t+1}+{\gamma}Q(S_{t+1},A_{t+1})-Q(S_t,A_t)]$
3. Q-learning：$Q(S_t,A_t){\leftarrow}Q(S_t,A_T)+\alpha[R_{t+1}+{\gamma}{\max}(Q(S_{t+1},:))-Q(S_t,A_t)]$