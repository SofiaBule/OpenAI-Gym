import gym

# Create environment
env = gym.make('CartPole-v1')

# Run an episode
observation = env.reset()
done = False
while not done:
    env.render()
    action = env.action_space.sample()  # Random action
    observation, reward, done, info = env.step(action)

# Close the environment
env.close()
