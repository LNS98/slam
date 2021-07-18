# SLAM from Scratch
*Basic implemtation of [SLAM](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping) from scratch,
mostly for learning (and fun).*

At this point, the agent can sense from the enviornment and create a map based
on what it has sensed.

## Files
    - `env.py` holds `Env` class responsible for dealing
      with the environemnt. And `Display` class responsible for some plotting
      with cv2.
    - `agent.py` holds `Agent` class responsible for moving and creating map of
      env based on what it senses.
    - `sensors.py` hold (for now) `LaserSensor`, a model sensor for a Lidar like
      sensor that is what actually tries to see what is in the env.

## Example
*Display of agent in environment map*
<img width="1147" alt="env_map" src="https://user-images.githubusercontent.com/40740001/126078394-470ef7a5-1c6f-46e2-8570-eaf21ef3dad5.png">
*Display of the agent's in map of the environment*
<img width="1067" alt="agent_map" src="https://user-images.githubusercontent.com/40740001/126078397-ba3dc737-2f3b-4286-90ba-c8ae3cc5b13e.png">
