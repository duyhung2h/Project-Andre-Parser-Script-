import sys
import os
import time
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


'''
File & Folder setup
Copy the file name (click on the line and CTRL + C):

ScenarioParser - RemoveTriggers
Tales of Tenebria version 0v18
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

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# Uncomment this in order to wipe all triggers from the map at start
saved_triggers = source_scenario.trigger_manager.triggers
# target_trigger_manager.variables = []  # Uncomment this in order to wipe all variables from the map at start



print("---------------------------------------")
print("trigger list with their id:")
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    # go for each condition in a trigger
    for effId in range (0, len(source_trigger_manager.triggers[triggerId].effects), 1):
        effect = source_trigger_manager.triggers[triggerId].effects[effId]
        # print(EffectId(value=effect.effect_type))
        # check eff
        if str(EffectId(value=effect.effect_type)).__eq__("EffectId.SEND_CHAT"):
            '''
            check for character death P1
            '''
            print(source_trigger_manager.triggers[triggerId].name + ", ID: "
                  + str(source_trigger_manager.triggers[triggerId].trigger_id))
            print(effect.message)




'''
mark triggers ranging from index "position_start" to "position_end",

to remove triggers designated from position "position_start" to "position_end".
'''
position_start = len(saved_triggers) - 600
position_end = len(saved_triggers) - 0
# len(source_trigger_manager); #or a custom position


# remove triggers
# source_trigger_manager.triggers = saved_triggers[30:position_end]

# Final step: write a modified scenario class to a new scenario file
# source_scenario.write_to_file(output_path)
