from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.datasets.units import *
from AoE2ScenarioParser.datasets.buildings import *
from AoE2ScenarioParser.datasets.heroes import *
from AoE2ScenarioParser.datasets.other import *
from AoE2ScenarioParser.datasets.projectiles import *
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.data_objects.condition import Condition
from AoE2ScenarioParser.objects.data_objects.effect import Effect
from AoE2ScenarioParser.objects.support.new_condition import NewConditionSupport
from AoE2ScenarioParser.objects.support.new_effect import NewEffectSupport
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

'''
File & Folder setup
Copy the file name (click on the line and CTRL + C):

ScenarioParser - ModifyAllUnits
Tales of Tenebria version 0v20v6
testGAIAunit
'''

input_scenario_nanme = input(
    'Please enter the scenario name (spare the .aoe2scenario extension): ')
try:
    scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"
    source_scenario = AoE2DEScenario.from_file(
        scenario_folder + input_scenario_nanme + ".aoe2scenario")
except FileNotFoundError:
    scenario_folder = resource_path("")
    print("\ncannot find main scenario folder. redirect to base dir: " + scenario_folder)

# Source scenario to work with
input_path = scenario_folder + input_scenario_nanme + ".aoe2scenario"
# Transfer scenario to extract triggers into
output_path = scenario_folder + input_scenario_nanme + \
              " Parser Result" + ".aoe2scenario"

''''''

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# target_trigger_manager.triggers = []  # Uncomment this in order to wipe all triggers from the map at start
# target_trigger_manager.variables = []  # Uncomment this in order to wipe all variables from the map at start

print("--------Variables-------------------------------")
unit_manager = source_scenario.unit_manager
for unit in unit_manager.units[0]:
    # print(unit)
    if unit.unit_const == 415:
        print(str(unit.reference_id) + " x: " + str(unit.x) + " y: " + str(unit.y))
        unit.unit_const = 809
variables = source_scenario.trigger_manager.variables
for variableNum in range(0, len(variables), 1):
    print("ID: " + str(variables[variableNum].variable_id) + " - " + variables[variableNum].name)
print("---------------------------------------")
# for a_localArea in range(0, len(UnitInfo), 1):
# print(UnitInfo[a_localArea].ID)
print("---------------------------------------")
print("trigger list with their id:")
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    print(source_trigger_manager.triggers[triggerId].name + ", ID: "
          + str(source_trigger_manager.triggers[triggerId].trigger_id))


# put triggers ranging from index position_start to position_end, to position position_transfer in the target file
test_position_start = 0
test_position_end = 0
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    if source_trigger_manager.triggers[triggerId].name == "------------------testStartCheckShit":
        print(source_trigger_manager.triggers[triggerId].name)
        test_position_start = source_trigger_manager.triggers[triggerId].trigger_id + 1
        test_position_end = test_position_start + 4

# working with triggers
testTriggers = source_trigger_manager.triggers[test_position_start:test_position_end]
try:
    print(testTriggers[0].trigger_id)

    print(testTriggers[0].conditions[1].object_type)
    print("Charles id: " + str(testTriggers[0].conditions[0].unit_object))
    print(testTriggers[0].conditions[1].object_type)
    print(testTriggers[0].conditions[1].object_list)
    print(testTriggers[0].conditions[1].quantity)
    print(testTriggers[0].effects[1].trigger_id)
    print("Clarissa id: " + str(testTriggers[3].conditions[0].unit_object))
    print("Coline id: " + str(testTriggers[3].conditions[1].unit_object))
    print("Dominiel id: " + str(testTriggers[3].conditions[2].unit_object))
    print("Corvus id: " + str(testTriggers[3].conditions[3].unit_object))
    print("Nemunas id: " + str(testTriggers[3].conditions[4].unit_object))

    print("condition 1 object state: " + str(testTriggers[0].conditions[1].object_state))

    print("area x1 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_x1))
    print("area x2 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_x2))
    print("area y1 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_y1))
    print("area y2 condition 0 trigger 1: " + str(testTriggers[0].conditions[0].area_y2))

    print("tele x effect 0 trigger 1: " + str(testTriggers[0].effects[0].location_x))
    print("tele y effect 0 trigger 1: " + str(testTriggers[0].effects[0].location_y))

    print("tele x effect 2 trigger 1: " + str(testTriggers[0].effects[2].location_x))
    print("tele y effect 2 trigger 1: " + str(testTriggers[0].effects[2].location_y))

    print("tele x effect 3 trigger 1: " + str(testTriggers[0].effects[3].location_x))
    print("tele y effect 3 trigger 1: " + str(testTriggers[0].effects[3].location_y))

    print("tele x effect 4 trigger 1: " + str(testTriggers[0].effects[4].location_x))
    print("tele y effect 4 trigger 1: " + str(testTriggers[0].effects[4].location_y))

    print("area x1 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_x1))
    print("area x2 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_x2))
    print("area y1 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_y1))
    print("area y2 effect 6 trigger 1: " + str(testTriggers[0].effects[6].area_y2))

    print("tele x effect 6 trigger 1: " + str(testTriggers[0].effects[6].location_x))
    print("tele y effect 6 trigger 1: " + str(testTriggers[0].effects[6].location_y))

    print("modify attribute object attribute id (hitpoints): " + str(testTriggers[3].effects[0].object_attributes))
    print("modify attribute object attribute id (movement speed): " + str(testTriggers[3].effects[1].object_attributes))
    print("modify attribute object attribute id (attack): " + str(testTriggers[3].effects[2].object_attributes))
    print("modify attribute object attribute id (armor): " + str(testTriggers[3].effects[3].object_attributes))
    print("modify attribute object attribute id (shown attack): " + str(testTriggers[3].effects[4].object_attributes))
    print("modify attribute object attribute id (shown range): " + str(testTriggers[3].effects[5].object_attributes))
    print("modify attribute object attribute id (shown melee armor): " + str(testTriggers[3].effects[6].object_attributes))
    print("modify attribute object attribute id (shown pierce armor): " + str(testTriggers[3].effects[7].object_attributes))
    print("modify attribute object attribute id (attack reload time): " + str(testTriggers[3].effects[8].object_attributes))
    print("modify attribute object attribute id (building icon override): " + str(
        testTriggers[3].effects[9].object_attributes))
    print("modify attribute object attribute id (garrison capacity): " + str(testTriggers[3].effects[10].object_attributes))
    print("modify attribute object attribute id (line of sight): " + str(testTriggers[3].effects[11].object_attributes))
    print("modify attribute object attribute id (unit size x): " + str(testTriggers[3].effects[12].object_attributes))
    print("modify attribute object attribute id (unit size y): " + str(testTriggers[3].effects[13].object_attributes))
    print("modify attribute object attribute id (max range): " + str(testTriggers[3].effects[14].object_attributes))

    print("Equipment spawn point X: " + str(testTriggers[3].effects[15].location_x))
    print("Equipment spawn point Y: " + str(testTriggers[3].effects[15].location_y))

    print("modify attribute operation (set): " + str(testTriggers[3].effects[0].operation))
    print("modify attribute operation (add): " + str(testTriggers[3].effects[1].operation))
    print("modify attribute operation (subtract): " + str(testTriggers[3].effects[2].operation))
    print("modify attribute operation (multiply): " + str(testTriggers[3].effects[3].operation))
    print("modify attribute operation (divide): " + str(testTriggers[3].effects[4].operation))

    print("area x1 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_x1))
    print("area x2 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_x2))
    print("area y1 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_y1))
    print("area y2 character menu trigger 4: " + str(testTriggers[3].conditions[5].area_y2))

    print("area inside equipment inventory trigger 4: x1=" + str(testTriggers[3].conditions[6].area_x1) +
          " x2=" + str(testTriggers[3].conditions[6].area_x2) +
          " y1=" + str(testTriggers[3].conditions[6].area_y1) +
          " y2=" + str(testTriggers[3].conditions[6].area_y2))
    print("area check character death trigger 4: x1=" + str(testTriggers[3].conditions[7].area_x1) +
          " x2=" + str(testTriggers[3].conditions[7].area_x2) +
          " y1=" + str(testTriggers[3].conditions[7].area_y1) +
          " y2=" + str(testTriggers[3].conditions[7].area_y2))
    print("area check core character control board trigger 4: x1=" + str(testTriggers[3].conditions[8].area_x1) +
          " x2=" + str(testTriggers[3].conditions[8].area_x2) +
          " y1=" + str(testTriggers[3].conditions[8].area_y1) +
          " y2=" + str(testTriggers[3].conditions[8].area_y2))
    print("area unequipment trigger 4: x1=" + str(testTriggers[3].conditions[9].area_x1) +
          " x2=" + str(testTriggers[3].conditions[9].area_x2) +
          " y1=" + str(testTriggers[3].conditions[9].area_y1) +
          " y2=" + str(testTriggers[3].conditions[9].area_y2))
    print("area character level trigger 4: x1=" + str(testTriggers[3].conditions[10].area_x1) +
          " x2=" + str(testTriggers[3].conditions[10].area_x2) +
          " y1=" + str(testTriggers[3].conditions[10].area_y1) +
          " y2=" + str(testTriggers[3].conditions[10].area_y2))
    print("area character level queue trigger 4: x1=" + str(testTriggers[3].conditions[11].area_x1) +
          " x2=" + str(testTriggers[3].conditions[11].area_x2) +
          " y1=" + str(testTriggers[3].conditions[11].area_y1) +
          " y2=" + str(testTriggers[3].conditions[11].area_y2))
    print("area enemy spawn: x1=" + str(testTriggers[3].conditions[12].area_x1) +
          " x2=" + str(testTriggers[3].conditions[12].area_x2) +
          " y1=" + str(testTriggers[3].conditions[12].area_y1) +
          " y2=" + str(testTriggers[3].conditions[12].area_y2))
    print("area enemy check loot: x1=" + str(testTriggers[3].conditions[13].area_x1) +
          " x2=" + str(testTriggers[3].conditions[13].area_x2) +
          " y1=" + str(testTriggers[3].conditions[13].area_y1) +
          " y2=" + str(testTriggers[3].conditions[13].area_y2))
    print("area flag amount of enemy spawn: x1=" + str(testTriggers[3].conditions[14].area_x1) +
          " x2=" + str(testTriggers[3].conditions[14].area_x2) +
          " y1=" + str(testTriggers[3].conditions[14].area_y1) +
          " y2=" + str(testTriggers[3].conditions[14].area_y2))
    print("area check party size flag0: x1=" + str(testTriggers[3].conditions[15].area_x1) +
          " x2=" + str(testTriggers[3].conditions[15].area_x2) +
          " y1=" + str(testTriggers[3].conditions[15].area_y1) +
          " y2=" + str(testTriggers[3].conditions[15].area_y2))
    print("check spawner P2 436 unitId: id=" + str(testTriggers[3].conditions[16].unit_object))
    print("area check p2 flag turn into enemies (infantry): x1=" + str(testTriggers[3].conditions[17].area_x1) +
          " x2=" + str(testTriggers[3].conditions[17].area_x2) +
          " y1=" + str(testTriggers[3].conditions[17].area_y1) +
          " y2=" + str(testTriggers[3].conditions[17].area_y2))
    print("area check type of enemy faction: x1=" + str(testTriggers[3].conditions[18].area_x1) +
          " x2=" + str(testTriggers[3].conditions[18].area_x2) +
          " y1=" + str(testTriggers[3].conditions[18].area_y1) +
          " y2=" + str(testTriggers[3].conditions[18].area_y2))
except:
    print("This is not the ToT map!")

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)