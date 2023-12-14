# PyRush API
In this README, you'll know PowerUps and weapons and their matching commands.
## What can you do in the map
In the map of the game, you can do all the following acts with your bot :
- Move all around the map
- Shoot with your weapon
- Kill ennemies
- Score a point if you step in the ennemies's spawn zone
- Get killed -> respawn in your spawn zone
- Use powers ups -> if you do 3 kills
- Change your weapon -> if you grab a piece
## List of weapons, their specs and their commands
#### SMG mode
The basic weapon. Shoots faster than lasergun and can be reloaded.  
- 5sec reloading time  
- Command -> smg_mode()
### When you interact with a piece
#### Sniper mode
It explains itself:  
- 50% of drop chance  
- 2sec cooldown  
- use 5 ammo  
- one shot every ennemy  
Command -> sniper_mode()
### Rocket mode
Basically a big gun that shoots explosive rockets:  
- 50% of drop chance  
- 5sec cooldown  
- use 20 ammo  
- deals area  damage (when the shot touch a wall or someone it drop a bomb which explode instantly)  
- Command - > rocket_mode()
## List of PowerUps, their specs and their commands
### Reloading
- 30% drop chance  
- Reloads 30% of your active weapon ammo  
- Command -> refuelAmmo()
### Shield
- 10% drop chance  
- Cancel all received damage during 3sec  
- Command -> shield()
### Heal
- 50% drop chance  
- Gives you 50% of your lost HP  
- Command -> heal()
### Invisibility
- 10% drop chance
- Makes you invisible for you ennemy during 2sec  
- Command -> invisibility()
