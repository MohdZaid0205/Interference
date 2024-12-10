from core.vector import Vector2D  # Assuming this is already implemented
from core.wave import WaveEquation, WaveSourceEmitter, COS_WAVE, SIN_WAVE
from math import sin, cos

# Test for WaveEquation Displacement method
def test_wave_equation_displacement_sin_wave():
    wave = WaveEquation(A=1.0, k=2.0, w=3.0, q=0.0, t=SIN_WAVE)
    displacement = wave.displacement(x=1.0, t=1.0)
    expected_displacement = 1.0 * sin(3.0 * 1.0 - 2.0 * 1.0 + 0.0)  # sin(1)
    assert abs(displacement - expected_displacement) < 1e-6, f"Expected displacement {expected_displacement}, got {displacement}"

def test_wave_equation_displacement_cos_wave():
    wave = WaveEquation(A=1.0, k=2.0, w=3.0, q=0.0, t=COS_WAVE)
    displacement = wave.displacement(x=1.0, t=1.0)
    expected_displacement = 1.0 * cos(3.0 * 1.0 - 2.0 * 1.0 + 0.0)  # cos(1)
    assert abs(displacement - expected_displacement) < 1e-6, f"Expected displacement {expected_displacement}, got {displacement}"

def test_wave_equation_intensity():
    wave = WaveEquation(A=2.0, k=2.0, w=3.0, q=0.0, t=SIN_WAVE)
    intensity = wave.intensity(x=5.0)
    expected_intensity = (2.0 ** 2) / 5.0  # (A^2) / x
    assert abs(intensity - expected_intensity) < 1e-6, f"Expected intensity {expected_intensity}, got {intensity}"

# Test for WaveSourceEmitter calculateDisplacement method
def test_wave_source_emitter_calculate_displacement():
    wave = WaveEquation(A=1.0, k=2.0, w=3.0, q=0.0, t=SIN_WAVE)
    emitter = WaveSourceEmitter(P=Vector2D(0.0, 0.0), W=wave, d=2.0)
    target_position = Vector2D(3.0, 4.0)
    displacement = emitter.calculateDisplacement(at=target_position, t=1.0)

    # Distance from emitter to target position (Pythagoras theorem)
    distance = Vector2D.distance(Vector2D(0.0, 0.0), target_position)
    
    # Expected displacement calculation
    expected_displacement = wave.displacement(x=distance, t=1.0)
    assert abs(displacement - expected_displacement) < 1e-6, f"Expected displacement {expected_displacement}, got {displacement}"

# Test for WaveSourceEmitter calculateIntensity method
def test_wave_source_emitter_calculate_intensity():
    wave = WaveEquation(A=2.0, k=1.0, w=3.0, q=0.0, t=COS_WAVE)
    emitter = WaveSourceEmitter(P=Vector2D(0.0, 0.0), W=wave, d=2.0)
    target_position = Vector2D(1.0, 1.0)  # Distance sqrt(1^2 + 1^2) = sqrt(2)
    
    # Calculate intensity
    intensity = emitter.calculateIntensity(at=target_position)
    
    # Expected intensity
    distance = Vector2D.distance(Vector2D(0.0, 0.0), target_position)
    expected_intensity = wave.intensity(x=distance) / emitter.d
    assert abs(intensity - expected_intensity) < 1e-6, f"Expected intensity {expected_intensity}, got {intensity}"

# Test WaveSourceEmitter with a non-zero intensity falloff
def test_wave_source_emitter_intensity_falloff():
    wave = WaveEquation(A=1.0, k=2.0, w=3.0, q=0.0, t=SIN_WAVE)
    emitter = WaveSourceEmitter(P=Vector2D(0.0, 0.0), W=wave, d=4.0)  # Increased intensity falloff
    target_position = Vector2D(2.0, 0.0)  # 2 units away from the emitter
    
    # Calculate intensity with falloff
    intensity = emitter.calculateIntensity(at=target_position)
    
    # Expected intensity considering falloff (distance = 2)
    distance = Vector2D.distance(Vector2D(0.0, 0.0), target_position)
    expected_intensity = wave.intensity(x=distance) / 4.0
    assert abs(intensity - expected_intensity) < 1e-6, f"Expected intensity {expected_intensity}, got {intensity}"

# Test Vector2D distance method (assumed to be implemented)
def test_vector2d_distance():
    v1 = Vector2D(0.0, 0.0)
    v2 = Vector2D(3.0, 4.0)
    distance = Vector2D.distance(v1, v2)
    expected_distance = 5.0  # sqrt(3^2 + 4^2)
    assert abs(distance - expected_distance) < 1e-6, f"Expected distance {expected_distance}, got {distance}"
