Escape Room Puzzle Game

Overview

Escape Room is a 2D puzzle game built with Pygame where you navigate through a dangerous room filled with traps and enemies. Your goal is to solve the lever puzzle and reach the exit door.
Game Features

Puzzle Mechanics: Activate levers in the correct sequence to unlock the exit door
Combat System: Fight enemies that attempt to disrupt your progress
Agent AI: Watch an AI-controlled agent attempt to solve the puzzle alongside you
Obstacles: Avoid deadly moving saw blades that patrol the map
Multiple Solutions: The lever combination changes each playthrough for replayability

Controls

WASD: Move player character
E: Interact with levers
SPACE: Attack enemies

Game Objects
Player
The player character can move around the room, interact with levers, and attack enemies. The player has 100 health points and can take damage from saws and enemy attacks.
Levers
Four levers are positioned around the room. Each lever has two states (on/off), and you must set them to match the hidden solution pattern to unlock the exit door.
Enemy
An enemy character patrols the room, attempting to:

Attack the player or agent
Deactivate any activated levers
Avoid hazards like saw blades

Agent AI
An AI-controlled character that:

Automatically tries to solve the lever puzzle
Navigates around hazards
Can fight enemies
Will attempt to reach the exit once all levers are correctly set

Saw Blades
Three deadly saw blades move along fixed paths in the room. They deal significant damage on contact to the player, agent, and enemy.
Exit Door
Initially locked, the door will unlock once all levers are set to the correct pattern. Interact with the unlocked door to proceed to the next area.
Technical Architecture
The game is built using a component-based entity system where:

Each game object is an Entity
Behavior is defined by Components attached to entities
Components handle specific functionality (physics, combat, AI, etc.)

Key components include:

Physics: Handles collisions and movement
Combat: Manages health, damage, and attacks
PathFinding: Calculates optimal paths for AI movement
PuzzleSystem: Tracks lever states and checks the solution

Puzzle Mechanics
The puzzle solution is randomly generated at the start of each game. Players must:

Find the correct combination of lever states (ON/OFF)
Avoid or defeat the enemy who tries to reset the levers
Reach the exit door once unlocked

Installation & Running

Ensure Python and Pygame are installed:

pip install pygame

Run the game:

python game.py
Developer Notes

The agent AI uses A* pathfinding to navigate the map
Enemy behavior balances between attacking players and disrupting lever states
Combat uses a simple damage and cooldown system
Saw paths are defined as line segments that saws move along

Credits

Built with Pygame
Pixel art assets included in the content directory
