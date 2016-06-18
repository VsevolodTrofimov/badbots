# Data API:
2 API's by now: vision and game

## In each API
commands - AI puts what need to be done there

state - Modules put data they processed (ex. world state for game API or objects for vision)


## Syntax:

### data.game.commands.get()
  **returns** all game commands(actions) that were added **since last call**

  ...

  if none returns empty array

### data.game.commands.add()
**adds** all game state(ammo/hp/etc) and adds timestamp

### data.game.vision.get()

  **returns** all vision data that were added **since last call**

  ...

  if none returns empty array

### data.game.vision.add()
  **adds** vision data that will be than requested by AI
