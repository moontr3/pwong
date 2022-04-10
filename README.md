# pwong
Ping-pong 2-player game that written in Python with Pygame (more info about Pygame can be found here: https://www.pygame.org/)

### How to play

- Open file `main.py`, you should see something like this:
```
Welcome to PWong made by moontr3!

Select mode:
[1] Easy
[2] Normal
[3] Hard
[4] Custom

>> _
```

- Type your preferred difficulty *(More information will be displayed in window)*
  - Easy: slow ball and fast players, 3 points to win/lose
  - Normal: average difficulty, 5 points to win/lose
  - Hard: slow players and fast ball, 7 points to win/lose
  - Custom: you can setup speed etc. by yourself

- Another window will appear after selecting difficulty.
*If you selected `Custom` (`4`) mode, you should set up your game and only then window will appear*

- To exit, close the **console** window, **not** a game window.

### Controls
| Key | Binding |
|-----|-----|
| `W` | BLUE (left) player up |
| `S` | BLUE (left) player down |
| `Up` | RED (right) player up |
| `Down` | RED (right) player down |

### Creators & other info
Used libraries:
- Pygame
  - Installation:
    - `$ pip install pygame`
  - Sites:
    - official site: https://www.pygame.org/
    - PyPI: https://pypi.org/project/pygame/

Creators:
- Code:
  - Eugene (https://github.com/jonotyan)
  - moontr3 (me)
- Sprites/design:
  - moontr3 (me)
