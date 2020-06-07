# ROS Cheatsheet

This is a cheat sheet prepared and used by myself.

## ROSTOPIC
A tool for displaying debug information about ROS topics, including publishers, subscribers, publishing rate, and messages.

Commands:
rostopic **Method** to do **Description**
```
Method          Description
__________________________________
bw
echo
hz
list
pub
type
find            find topics by type
```

## Turtlesim (for testing)

starts roscore  
`$ roscore`  
  
run turtlesim  
`$ rosrun turtlesim turtlesim_node`  
  
using arrow keys to move turtle   
`rosrun turtlesim turtle_teleop_key`  

## Catkin

## Bashrc

The `~/.bashrc` is kind of like a configuration file that runs whenever each terminal is open.  
Sometimes, the bashrc may not update when you add stuff to it. In that case, just "refresh" it!  
We "refresh" by using the source command : `source ~/.bashrc`  
