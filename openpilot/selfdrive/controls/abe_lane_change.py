# Placeholder for Abe's blinker lane-change logic
# TODO: implement signal-driven lane change with safety checks
# Pseudocode outline:
#
# if car_state.blinker_left and safe_to_lane_change_left():
#     plan.lane_change_direction = "left"
#     plan.trigger_lane_change()
# elif car_state.blinker_right and safe_to_lane_change_right():
#     plan.lane_change_direction = "right"
#     plan.trigger_lane_change()
#
# Safety checks (to refine with real code later):
# - minimum speed threshold (e.g., > 30 km/h)
# - lateral/longitudinal acceleration limits
# - blind-spot / adjacent lane occupancy based on model/radar
# - user torque confirmation optional (configurable)

class AbeLaneChangeConfig:
    MIN_SPEED_KPH = 30
    REQUIRE_TORQUE_CONFIRM = False

def should_start_lane_change(cs, model_data):
    # cs: car_state-like object (placeholders)
    if cs.speed_kph < AbeLaneChangeConfig.MIN_SPEED_KPH:
        return False
    # TODO: add checks for adjacent lane safety using model_data
    return True

def run_blinker_lane_change(car_state, model_data, planner):
    # Placeholder only: no real behavior yet
    if car_state.blinker_left and should_start_lane_change(car_state, model_data):
        planner.debug_note = "LC: left (placeholder)"
    elif car_state.blinker_right and should_start_lane_change(car_state, model_data):
        planner.debug_note = "LC: right (placeholder)"
    else:
        planner.debug_note = "LC: idle"
