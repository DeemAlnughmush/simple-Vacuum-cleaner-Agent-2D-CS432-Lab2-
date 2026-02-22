# Lab 2 – Vacuum Cleaner Agent (2D)

This lab implements a simple reflex vacuum cleaner agent in a 2x2 environment.

## Environment
Rooms:
A  B  
C  D  

Each room can be:
- Dirty (1)
- Clean (0)

The agent follows a fixed path:
Top-left → Top-right → Bottom-right → Bottom-left

## Agent Rules (Simple Reflex)
- If the current room is Dirty → Suck
- If the current room is Clean → Move to next room in path

The agent does not use memory.  
It only reacts based on the current percept (location, status).

## Output Example

See the screenshots below.

![Output](Output1.png)
![Output](Output2.png)


---

