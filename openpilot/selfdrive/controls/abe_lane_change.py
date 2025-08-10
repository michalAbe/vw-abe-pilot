# Abe Blinkr Lane Change – jednoduchá implementácia
# Sleduje smerovky a spustí požiadavku na zmenu pruhu, keď sú splnené podmienky

from dataclasses import dataclass

@dataclass
class AbeLCConfig:
MIN_SPEED_KPH: int = 30
REQUIRE_TORQUE_CONFIRM: bool = False

def run_blinker_lane_change(car_state, model_data, planner):
"""
car_state: objekt so stavom auta (blinker_left, blinker_right, speed_kph, user_torque_applied)
model_data: objekt s modelovanými údajmi (clear_left, clear_right)
planner: objekt, do ktorého môžeme písať debug poznámku
"""
# rýchlosť auta
speed = float(getattr(car_state, "speed_kph", 0.0))

# ak ideme pomaly, nerobíme lane change
if speed < AbeLCConfig.MIN_SPEED_KPH:
planner.debug_note = "LC: idle (low speed)"
return None

# ak je zapnutá ľavá smerovka
if getattr(car_state, "blinker_left", False):
planner.debug_note = "LC: left"
return {"request": "start", "direction": "left"}

# ak je zapnutá pravá smerovka
if getattr(car_state, "blinker_right", False):
planner.debug_note = "LC: right"
return {"request": "start", "direction": "right"}

# inak nič nerobíme
planner.debug_note = "LC: idle"
return None
