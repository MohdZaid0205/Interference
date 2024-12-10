from core.vector import Vector2D
from core.particle import Particle

# Test for Particle initialization
def test_particle_initialization():
    position = Vector2D(3, 4)
    displacement = 5.0
    intensity = 10.0

    # Create a Particle object
    particle = Particle(P=position, d=displacement, i=intensity)

    # Assert that the attributes are correctly assigned
    assert particle.P == position, f"Expected position {position}, got {particle.P}"
    assert particle.d == displacement, f"Expected displacement {displacement}, got {particle.d}"
    assert particle.i == intensity, f"Expected intensity {intensity}, got {particle.i}"

# Test for Particle with default values
def test_particle_default_values():
    position = Vector2D(0, 0)
    displacement = 0.0
    intensity = 0.0

    # Create a Particle object with default values
    particle = Particle(P=position, d=displacement, i=intensity)

    # Assert default values
    assert particle.P == position, f"Expected position {position}, got {particle.P}"
    assert particle.d == displacement, f"Expected displacement {displacement}, got {particle.d}"
    assert particle.i == intensity, f"Expected intensity {intensity}, got {particle.i}"

# Test for modifying particle's properties
def test_particle_modification():
    position = Vector2D(1, 1)
    displacement = 2.5
    intensity = 5.0

    # Create a Particle object
    particle = Particle(P=position, d=displacement, i=intensity)

    # Modify particle's attributes
    new_position = Vector2D(3, 3)
    new_displacement = 10.0
    new_intensity = 20.0
    particle.P = new_position
    particle.d = new_displacement
    particle.i = new_intensity

    # Assert modified values
    assert particle.P == new_position, f"Expected position {new_position}, got {particle.P}"
    assert particle.d == new_displacement, f"Expected displacement {new_displacement}, got {particle.d}"
    assert particle.i == new_intensity, f"Expected intensity {new_intensity}, got {particle.i}"

# Test for equality of two particles
def test_particle_equality():
    position1 = Vector2D(0, 0)
    position2 = Vector2D(0, 0)
    displacement = 5.0
    intensity = 10.0

    # Create two identical Particle objects
    particle1 = Particle(P=position1, d=displacement, i=intensity)
    particle2 = Particle(P=position2, d=displacement, i=intensity)

    # Assert both particles are equal
    assert particle1 == particle2, f"Expected particles to be equal, but they are not"

# Test for comparison of different particles
def test_particle_inequality():
    position1 = Vector2D(0, 0)
    position2 = Vector2D(1, 1)
    displacement = 5.0
    intensity = 10.0

    # Create two different Particle objects
    particle1 = Particle(P=position1, d=displacement, i=intensity)
    particle2 = Particle(P=position2, d=displacement, i=intensity)

    # Assert both particles are not equal
    assert particle1 != particle2, f"Expected particles to be different, but they are not"
