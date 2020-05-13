# Main Python file for reviewers

# import relevant libs
import gym
import numpy as np
from keras.models import model_from_json
from support import prepro, summary_of_episodes

# set up the environment
# Frame list collector
frames = []

# code for the two only actions in Pong
UP_ACTION = 2
DOWN_ACTION = 3

# initialization of variables used in the main loop
env = gym.make("Pong-v0")
prev_input = None
rewards = [],[],[]
reward_sum = 0
episode_nb = 0

# beginning of an episode
observation = env.reset()

# import model here
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk.")

# main loop
print("Pong-agent is playing... This will take a minute or two...")
print("...")
print("...")
reward_sum_history = []

# for i in range(STEPS):
while episode_nb < 20:
    # choose action based on model's recommendation
    # preprocess the observation, set input as difference between images
    cur_input = prepro(observation)
    x = cur_input - prev_input if prev_input is not None else np.zeros(80 * 80)
    prev_input = cur_input
    proba = loaded_model.predict(np.expand_dims(x, axis=1).T)
    action = UP_ACTION if np.random.uniform() < proba else DOWN_ACTION

    #run one step
    observation, reward, done, info = env.step(action)
    frames.append(observation) # collecting observation
    # rewards.append(reward)
    reward_sum += reward

    # if episode is over, reset to beginning
    if done:
        observation = env.reset()
        frames.append(observation) # collecting observation
        reward_sum_history.append(reward_sum)

        # increment episode number
        episode_nb += 1

        # Reinitialization
        rewards = [],[],[]
        observation = env.reset()
        reward_sum = 0
        prev_input = None

# print results to command line
summary_of_episodes(reward_sum_history)