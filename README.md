# simple-space-game
It's my first game, so please have mercy.:) I'd like to know what can I improve in terms of:

- the structure of the code
- the performance (currently around 25fps on my machine)
- the design pattern I could potentially use here
- the overall file split and names (I'm sure my_functions, my_classes and my_constants aren't the industry standard)

Bugs and flaws:
- LEVEL UP BUG: pause the game and wait till fraction of the second before next level up, unpause, the level goes up, pause again, etc
- change lists iteration to group iteration when drawing sprites etc.

Bad design practices:
- from <moduleName> import * (can cause trouble, and considered a bad practice)
- cluttered functions that perhaps could be simpler, and some of them could be class methods

TODO:
- implement more modes and make it a list. then access by "if item not in modes execute ..code".
- ability to shoot enemies
- smoke from the exhaust while accelerating


Game controls:
General:

- M                               - mute the music
- P                               - pause the game
- TAB                             - toggle tests

Player 1:                       Player 2:
arrow UP                        w               - move up
arrow DOWN                      s               - move down
arrow LEFT                      a               - move left
arrow RIGHT                     d               - move right  

_________________________________________________________________________

