"""Constants used through the simulation."""

BOUNDS_WIDTH: int = 800
MAX_X: float = BOUNDS_WIDTH / 2
MIN_X: float = -MAX_X
VIEW_WIDTH: int = BOUNDS_WIDTH + 20

BOUNDS_HEIGHT: int = 400
MAX_Y: float = BOUNDS_HEIGHT / 2
MIN_Y: float = -MAX_Y
VIEW_HEIGHT: int = BOUNDS_HEIGHT + 20

CELL_RADIUS: int = 20
CELL_COUNT: int = 50
CELL_SPEED: float = 3.0

IMMUNE: int = -1
VULNERABLE: int = 0
INFECTED: int = 1

INITIAL_INFECTED: int = 2
INITIAL_IMMUNE: int = 0

RECOVERY_PERIOD: int = 180