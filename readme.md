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
![alt text](https://github.com/LNS98/slam/blob/master/env_map.png?raw=true)
![alt text](https://github.com/LNS98/slam/blob/master/agent_map.png?raw=true)
