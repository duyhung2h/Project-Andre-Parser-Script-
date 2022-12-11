from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.conditions import ConditionId
import time

# test value
condition_id = ConditionId(value=10)
print(condition_id)

# File & Folder setup
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
scenario_name = "Tales of Tenebria version 0v17 unbloated"
input_path = scenario_folder + scenario_name + ".aoe2scenario"
output_path = scenario_folder + scenario_name + " unbloated" + ".aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

print("--------Variables-------------------------------")
unit_manager = source_scenario.unit_manager
variables = source_scenario.trigger_manager.variables
for variableNum in range(0, len(variables), 1):
    print("ID: " + str(variables[variableNum].variable_id) + " - " + variables[variableNum].name)
print("---------------------------------------")
print("trigger list with their id:")
# for unitId in range(0, len(source_trigger_manager.triggers), 1):
#     print(source_trigger_manager.triggers[unitId].name + ", ID: "
#           + str(source_trigger_manager.triggers[unitId].trigger_id))
# go for each triggers
bloated_trigger_list = []
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    # mark if trigger is loop
    is_loop = source_trigger_manager.triggers[triggerId].looping
    no_timer_con = True
    # go for each condition in a trigger
    for conId in range (0, len(source_trigger_manager.triggers[triggerId].conditions), 1):
        # mark if theres a timer con
        if ConditionId(value=source_trigger_manager.triggers[triggerId].conditions[conId].condition_type) == 'ConditionId.TIMER':
            no_timer_con = False
    # time.sleep(1)
    if is_loop and no_timer_con is True:
        print(source_trigger_manager.triggers[triggerId].name + ", ID: "
              + str(source_trigger_manager.triggers[triggerId].trigger_id))
        bloated_trigger_list.append(source_trigger_manager.triggers[triggerId])
        source_trigger_manager.triggers[triggerId].new_condition.timer(timer=10)
print(len(bloated_trigger_list))
print("unbloating... ")

# source_scenario.write_to_file(output_path)

