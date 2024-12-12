from core.grid import Grid
from core.particle import Particle
from core.vector import Vector2D
from core.wave import WaveEquation, WaveSourceEmitter, SIN_WAVE

from services.interference import Interference
from services.helpers import iGridInitHelper


from pyray import *
from math import *
from random import *

FPS: int = 60

SCREEN_WIDTH: int = 1450
SCREEN_HEIGHT: int = 900
WINDOW_MARGIN: int = 25

CELL_WIDTH: int = 12
CELL_HEIGHT: int = 12
CELL_GAP: int = 1

DYNAMIC: bool = True
GRID_WIDTH: int
GRID_HEIGHT: int

if DYNAMIC:
    GRID_WIDTH = (SCREEN_WIDTH - 2 * WINDOW_MARGIN) // (CELL_WIDTH + CELL_GAP)
    GRID_HEIGHT = (SCREEN_HEIGHT - 2 * WINDOW_MARGIN) // (CELL_HEIGHT + CELL_GAP)
else:
    GRID_WIDTH = 100
    GRID_HEIGHT = 100

CENTER: bool = True
if CENTER:
    P_X: int = SCREEN_WIDTH // 2 - (GRID_WIDTH // 2) * (CELL_WIDTH + CELL_GAP)
    P_Y: int = SCREEN_HEIGHT // 2 - (GRID_HEIGHT // 2) * (CELL_WIDTH + CELL_GAP)

# PROTOTYPE_SPECIFIC
PROPGATION_RATE: float = 3  # determines the rate of diffusion

if __name__ == "__main__":
    n = int(input("[Number Of sources] : "))
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Interference of waves")

    # Generate speaker waves
    speakers: list[Wave] = [
        WaveSourceEmitter(
            P = Vector2D(randint(0, GRID_HEIGHT - 1), randint(0, GRID_WIDTH - 1)),
            W = WaveEquation(
                A = randint(15, 30),
                k = 2 * pi / randint(1, 20),
                w = 2 * pi / randint(1, 5),
                q = randint(0, 4),
                t = SIN_WAVE),
            d = 1) for _ in range(n)
    ]

    # SETUP the grid
    grid: Grid[Particle] = iGridInitHelper(GRID_HEIGHT, GRID_WIDTH, speakers)
    

    # Pre-calculate max amplitude and source coordinates
    max_amp: float = sum([wave.W.A for wave in speakers])

    set_target_fps(FPS)
    d_time: float = 1 / FPS
    time: float = 0

    # Pre-compute grid cells for performance
    offset_x = (CELL_WIDTH + CELL_GAP)
    offset_y = (CELL_HEIGHT + CELL_GAP)

    interferenceManager:Interference = Interference(
        grid=grid, sources=speakers
    )
    
    while not window_should_close():
        FPS = get_fps()
        begin_drawing()
        clear_background(BLACK)

        for i, j, particle in interferenceManager:
            if particle is None:
                draw_rectangle(
                    P_X + offset_x * j,
                    P_Y + offset_y * i,
                    CELL_WIDTH,
                    CELL_HEIGHT,
                    (0, 0, 0, 255)
                )
                continue

            x_norm = (particle.d + max_amp) / (2 * max_amp)

            # Color Calculation
            if x_norm <= 0.5:  # Blue to White
                r = int(255 * x_norm * 2)
                g = int(255 * x_norm * 2)
                b = 255
            else:  # White to Red
                r = 255
                g = int(255 * (2 - 2 * x_norm))
                b = int(255 * (2 - 2 * x_norm))

            # Draw particle (if not a speaker position)
            draw_rectangle(
                P_X + offset_x * j,
                P_Y + offset_y * i,
                CELL_WIDTH,
                CELL_HEIGHT,
                (r, g, b, min(255, max(0, int(particle.i*(4/n)))))
            )

        draw_text(str(get_fps()), 5, 5, 10, WHITE)

        end_drawing()

        # Aggregate the wave effect for this particle
        interferenceManager.update(time)
        time += d_time * PROPGATION_RATE

    close_window()