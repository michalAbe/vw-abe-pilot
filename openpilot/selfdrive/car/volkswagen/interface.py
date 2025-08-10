# VW interface hook – volanie Abe blinker LC logiky

try:
from openpilot.selfdrive.controls.abe_lane_change import run_blinker_lane_change
except Exception:
def run_blinker_lane_change(*args, **kwargs):
return None

class PlannerStub:
debug_note: str = ""

class VWInterfacePlaceholder:
"""
Placeholder trieda – v skutočnom openpilot VW interface sa toto
zavolá z update loopu. Tu iba demonštrujeme, ako sa LC trigger volá.
"""
def __init__(self):
self._planner = PlannerStub()

def update(self, car_state, model_data):
req = run_blinker_lane_change(car_state, model_data, self._planner)
# TODO: ak req != None -> odovzdať požiadavku do skutočného planneru
return req, self._planner.debug_note
