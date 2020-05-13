import numpy as np

# support function 1 - put in support.py file
# preprocessing used by Karpathy (cf. https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5)
def prepro(I):
    """prepro 210x160x3 uint8 frame into 6400 (80x80) 1D float vector"""
    I = I[35:195] # crop
    I = I[::2,::2,0] # downsample by factor of 2
    I[I == 144] = 0 # erase background (background type 1)
    I[I == 109] = 0 # erase background (background type 2)
    I[I != 0] = 1 # everything else (paddles, ball) just set to 1
    return I.astype(np.float).ravel()

# support function 2
# summary of our game-playing agent's performance
def summary_of_episodes(list):
    wins = 0

    # count the number of wins
    for item in list:
        if item > 0:
            wins += 1
    print(f"Out of {len(list)} episodes, our game-playing agent won {wins} times.")

    # count average number of scores per episode
    print(f"Our game-playing agent scores {21- (-sum(list)/len(list))} points per episode on average.")

    # most points scored in any single game
    print(f"The most points our game-playing agent scored in any episode was {int(21 - (-max(list)))}.")