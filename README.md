# Invictus_Capital_Pong_Agent
Repository with code to create a single-player pong-agent using Reinforcement Learning

Please follow the steps below to help you set up the environment in which the pong-agent will play.

1. System requirements
    - Check if your Python environment is already configured by running each of the following lines of code in your terminal/command line:
        
            python3 --version
            pip3 --version
            virtualenv --version

        If these packages are already installed, skip to the next step.
        Otherwise, install Python, the pip package manager, and Virtualenv using the Homebrew package manager.
        Here is the code to do so:
        
            For MacOS:
                /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
                export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
                brew update
                brew install python  # Python 3
                sudo pip3 install -U virtualenv  # system-wide install
                
            For Windows:
                pip3 install -U pip virtualenv

    - Create a virtual environment (optional and recommended) by running the following code in your terminal/command line:
        
        For Ubuntu/MacOS:
            
            virtualenv --system-site-packages -p python3 ./venv
            source ./venv/bin/activate  # sh, bash, ksh, or zsh
            pip install --upgrade pip
            pip list  # show packages installed within the virtual environment
            deactivate  # don't exit until you're done using TensorFlow
        
        For Windows:
            
            virtualenv --system-site-packages -p python3 ./venv
            .\venv\Scripts\activate
            pip install --upgrade pip
            pip list  # show packages installed within the virtual environment
            deactivate  # don't exit until you're done using TensorFlow

    Inside the virtual environment, do the following:

    - Install the TensorFlow pip package
        Through the virtual environment:
        
                pip install --upgrade tensorflow
                python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
        System install:
        
                pip3 install --user --upgrade tensorflow  # install in $HOME
                python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

    - Install the Keras library
    
            pip install keras

    - Install the gym environment pOng-v0
    
            pip install gym
            pip install 'gym[atari]'

    - Install the Numpy library
            
            pip install numpy
    
    - Install Matplotlib
            
            pip install matplotlib

2. Please download the following files and save them in a single folder:
    - python_file_RUN_ME.py # main Python file that needs to be run
    - support.py # support file containing helper functions
    - model.h5 # contains model parameters
    - model.json # contains the model architecture

3. Still inside the virtual environment, CD (change directory) into the directory where the above files are located and run the following
code in your terminal/command line:

    python3 python_file_RUN_ME.py

This lets the pong-agent play 20 episodes (first to 21 points) against the AI player and returns the pong-agent's performance on those 20 episodes. 
This only takes a minute or two to run. 

** Other related files included in this Github repo include:

- pong-agent demo.gif: Visual demonstration of our pong-agent playing against the AI competitor. Only 3000 steps of the       game have been visualized, amounting to a several episodes (first to 21 points). 
  Please open this file and scroll through the frames to see how the agent plays. This visualization does not represent       the pong-agent's performance during the 20 testing episodes.

- Pong Game Notebook.ipynb: This is the Jupyter Notebook in which the pong-agent was created and trained. It also
  includes the code required to visualize the game as the pong-agent plays.

- Pong Game Report: This the the report detailing the work done to create, train and visualize the pong-agent.
