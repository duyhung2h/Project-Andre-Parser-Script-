from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.objects.support.new_condition import NewConditionSupport
from AoE2ScenarioParser.objects.support.new_effect import NewEffectSupport

from model.Equipment import Equipment
from model.Weapon import Weapon
from model.EquipmentArea import EquipmentArea
from model.Character import Character
from model.LevelCheckArea import LevelCheckArea
from model.EnemyList import EnemyList
from model.Unit import Unit

# File & Folder setup
scenario_folder = "C:/Users/Admin/Games/Age of Empires 2 DE/76561198148041091/resources/_common/scenario/"

# Source scenario to work with
input_path = scenario_folder + "Tales of Tenebria version 0v9.aoe2scenario"
output_path = scenario_folder + "Tales of Tenebria version 0v9 Parser Result.aoe2scenario"

# declare scenario class
source_scenario = AoE2DEScenario.from_file(input_path)

# declare trigger manager to work with variables and triggers
source_trigger_manager = source_scenario.trigger_manager

# [x1, x2], [y1, y2]
listCharactersEquipmentArea = EquipmentArea.get_equipmentarea()
characterSlotArea = [
    [[449, 451], [466, 468]],
    [[449, 451], [470, 472]],
    [[465, 467], [466, 468]],
    [[465, 467], [470, 472]],
]
characterLevelCheckArea = LevelCheckArea.get_levelcheckarea()
characterLevelQueueArea = LevelCheckArea.get_levelqueuearea()
NewConditionSupport
print(characterLevelCheckArea)
print(listCharactersEquipmentArea[0].weaponArea[0][0])  # x1
print(listCharactersEquipmentArea[0].weaponArea[1][0])  # y1
print(listCharactersEquipmentArea[0].weaponArea[0][1])  # x2
print(listCharactersEquipmentArea[0].weaponArea[1][1])  # y2

# unit_name, unit_id, characterClass, coreUnitId, skill1Icon, skill2Icon, maxRange, projectileId, hp, atk, meleeArmor, pierceArmor, potraitId
listCharacters = Character.get_characters()
listEquipments = []
listEquipments.extend(Equipment.get_equipment())
listEquipments.extend(Weapon.get_weapon())

# remove past triggers
triggerStart = 0
triggerEnd = 0
for triggerId in range(0, len(source_trigger_manager.triggers), 1):
    if source_trigger_manager.triggers[triggerId].name == "ToT - enemies.py Start":
        print(source_trigger_manager.triggers[triggerId].name)
        triggerStart = triggerId
    if source_trigger_manager.triggers[triggerId].name == "ToT - enemies.py End":
        print(source_trigger_manager.triggers[triggerId].name)
        triggerEnd = triggerId
print(triggerStart, triggerEnd)
for triggerId in range(triggerStart - 1, int(triggerEnd), 1):
    source_trigger_manager.remove_trigger(
        trigger_select=TriggerSelect.index(source_trigger_manager.triggers[triggerStart].trigger_id))


# start adding triggers
triggerStart = source_trigger_manager.add_trigger("ToT - enemies.py Start")
triggerSeparator = source_trigger_manager.add_trigger("----StyleOfEncounter---------------")
# Random encounter mechanic:
# Amount of unit spawned will also depends on party size and party level (tier)

# ------------choose different style of encounter--------------
# localArea = 1: Newbie friendly area - only T1 enemies and all enemies distributed balancedly.
# Distance to trigger RE is higher.
# localArea = 2: Normal area - all enemies will spawn, their tier will be according to party's level.
# Distance to trigger RE is medium.
# localArea = 3: Cave - only 1 archer max, no cavs. More wild animals. Distance to trigger RE is lower.
# localArea = 4: Contested area - Strong T2 and T3 units, uniformed faction units, depends on location, no wild animals,
# balanced distribution of infantries, cavs and archers. 1 siege unit maximum. Distance to trigger RE is medium.
# localArea = 5: Bandit infested area - no wild animals, 60% of encounters are ambushes.
# Distance to trigger RE is higher.
# localArea = 10: Nemesis area - only spawn nemesis enemies, nemesis unit will change according to area
# (check area - create P3 nemesis unit in nemesis check area). Distance to trigger RE is lower.


# check localArea
for a_localArea in range(1, 11, 1):
    # Base chance:
    # monk and priest only spawn in tier 2 +
    # siege: tier 2+, spawn along with amount of spearman according to type of siege. Only spawn in contested area.
    # after killing spearman siege turn into p0, and get damaged over time.
    chanceInf = 25
    chanceArch = 25
    chanceCav = 25
    chanceMonk = 15
    chanceWild = 10

    # ambush: volleys of projectile will be fired upon the party, and after that enemies will appear.
    # Will have at least 3-4 archers in the team.
    chanceAmbush = 15

    # MINIBOSS: A strong unit/hero that has a_localArea low chance to appear, unit pool is according to tier
    # (like tier 1 miniboss are champion, knight,... spawn in slot 2.)
    # They are also accompanied with fixed proportion of enemy units, (ex: 4 identical inf and archer)
    # minibossRanged: Fire volley of projectiles from far away, once finished spawn enemies.
    # minibossMelee: Spawn boss first, then the boss will call their minions in seconds later
    #
    # Different ratio of unit type on enemy encounters results in different combat tactics
    # (high ratio of archers will result in melee units guarding them defensively, etc...)
    #
    # Boss or strong enemies can have 1 nemesis and 1 status skill, depending on type.
    # Their main ability will be random, taken from Nemesis skills
    #
    #
    # --------------Extra status skill (one of the following):-----------------
    # Melee Boss
    # Bash: melee boss can stun their enemy after a_localArea period of time
    # Counter: melee boss can reflect damage based on chance
    # Taunt: melee boss can taunt enemies (disable targeting for other units, enable targeting for themself)
    # Enrage: melee boss can go berserk (boost atk speed and movement speed)
    # Warcry: melee boss can temporary
    # ...
    #
    # Ranged Boss:
    # Sharpshoot: ranged boss can charge and sharpshoot an enemy for increased damage, and weaken an enemy,
    # reducing their atk and movement speed.
    # Poison shot: Hitting targets will poison them for a_localArea certain amount of time.
    # Focus fire: Ranged boss can temporary increasing their range, atk speed and accuracy,
    # and all projectiles will travel faster.
    # ...

    chanceMinibossMelee = 10
    chanceMinibossRanged = 10
    encounterMessage1 = ""
    encounterMessage2 = ""
    distanceRE = 50
    if a_localArea == 1:
        distanceRE = 50
        encounterMessage1 = "<YELLOW>!!Random encounter: Friendly wilderness!!"
    # check enemy tier
    for b_enemyTier in range(1, 3, 1):
        # check party size to queue up random encounter units
        for c_partySize in range(1, 5, 1):
            flagId = 599 + b_enemyTier
            if a_localArea == 1:
                flagId = 600
            if b_enemyTier == 1:
                encounterMessage1 = "\n Enemy tier: " + str(b_enemyTier)
                encounterMessage2 = "<RED>A group of " + str(c_partySize) + " ruffians ambushed your party!"

            triggerCheckFlagSpawnEnemies = source_trigger_manager.add_trigger(
                "A" + str(a_localArea) + "-StartRE-" + str(c_partySize) + "mem",
                looping=True, enabled=True)
            # if spawn flag area for p2 has no p2 flag
            triggerCheckFlagSpawnEnemies.new_condition.own_fewer_objects(object_group=ObjectClass.FLAG, source_player=2,
                                                                         area_x1=88, area_x2=90, area_y1=467,
                                                                         area_y2=469, quantity=0)
            # check party size
            triggerCheckFlagSpawnEnemies.new_condition.own_fewer_objects(object_group=ObjectClass.FLAG, source_player=0,
                                                                         area_x1=100, area_x2=102, area_y1=477,
                                                                         area_y2=479, quantity=c_partySize)
            triggerCheckFlagSpawnEnemies.new_condition.objects_in_area(object_group=ObjectClass.FLAG, source_player=0,
                                                                       area_x1=100, area_x2=102, area_y1=477,
                                                                       area_y2=479, quantity=c_partySize)
            # RE_DistanceTravelled
            triggerCheckFlagSpawnEnemies.new_condition.variable_value(quantity=distanceRE,
                                                                      comparison=Comparison.LARGER, variable=13)
            # RE_inDangerousArea
            triggerCheckFlagSpawnEnemies.new_condition.variable_value(quantity=1,
                                                                      comparison=Comparison.EQUAL, variable=17)
            # localArea
            triggerCheckFlagSpawnEnemies.new_condition.variable_value(quantity=a_localArea,
                                                                      comparison=Comparison.EQUAL, variable=18)
            # RE_CurrentlyBattling
            triggerCheckFlagSpawnEnemies.new_condition.variable_value(quantity=1,
                                                                      comparison=Comparison.EQUAL, variable=19,
                                                                      inverted=True)
            # change RE_CurrentlyBattling to 1
            triggerCheckFlagSpawnEnemies.new_effect.change_variable(quantity=1,
                                                                    operation=Operation.SET, variable=19)
            # change RE_DistanceTravelled to 0
            triggerCheckFlagSpawnEnemies.new_effect.change_variable(quantity=0,
                                                                    operation=Operation.SET, variable=13)
            # change musicProgression to 0
            triggerCheckFlagSpawnEnemies.new_effect.change_variable(quantity=0,
                                                                    operation=Operation.SET, variable=24)
            # disable P2 spawner to not be targetted and change shooter to P3
            triggerCheckFlagSpawnEnemies.new_effect.disable_unit_targeting(selected_object_ids=146508, source_player=2)
            triggerCheckFlagSpawnEnemies.new_effect.change_ownership(source_player=4, target_player=3,
                                                                     object_list_unit_id=436)
            # add queue flag
            triggerCheckFlagSpawnEnemies.new_effect.remove_object(object_group=ObjectClass.FLAG, source_player=2,
                                                                  area_x1=88, area_x2=90, area_y1=467,
                                                                  area_y2=469)
            for d in range(0, c_partySize, 1):
                triggerCheckFlagSpawnEnemies.new_effect.create_object(object_list_unit_id=flagId,
                                                                      source_player=2,
                                                                      location_x=89, location_y=468)
                triggerCheckFlagSpawnEnemies.new_effect.create_object(object_list_unit_id=flagId,
                                                                      source_player=2,
                                                                      location_x=89, location_y=468)
            triggerCheckFlagSpawnEnemies.new_effect.display_instructions()
    # check if all enemies are killed
    triggerDetectAllEnemiesKilled = source_trigger_manager.add_trigger("P2AllKilledArea" + str(a_localArea))

# check enemy tier per local area
for a_enemyTier in range(1, 3, 1):
    # create infantry enemies
    triggerSeparator = source_trigger_manager.add_trigger("---CreateINF-------------", enabled=False)
    listEnemy = EnemyList.get_enemy_infantry_list(a_enemyTier)
    for b_unitId in range(0, len(listEnemy), 1):
        triggerTurnFlagIntoEnemies = source_trigger_manager.add_trigger(
            "ChkFlgTurnToINF_" + listEnemy[b_unitId].unitName,
            enabled=True, looping=True)
        #for a list of separate faction unit
        # get naran faction units
        listFaction = ["NAR"]
        for c_factionId in range (0, len(listFaction), 1):
            listFactionUnits = Unit.get_faction_unitid(faction="NAR")
            for d_factionUnitId in range (0, len(listFactionUnits), 1):
                if listEnemy[b_unitId].unitId == listFactionUnits[d_factionUnitId]:
                    triggerTurnFlagIntoEnemies.new_condition.objects_in_area(area_x1=89, area_x2=89,
                                                                             area_y1=460, area_y2=460,
                                                                             quantity=1 + c_factionId, source_player=2,
                                                                             object_list=600)

triggerEnd = source_trigger_manager.add_trigger("ToT - enemies.py End")

# Final step: write a_localArea modified scenario class to a_localArea new scenario file
source_scenario.write_to_file(output_path)
