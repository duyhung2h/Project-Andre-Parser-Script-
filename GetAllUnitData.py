from enum import Enum
from typing import Union
from model.Unit import Unit
import os
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo

import json

print(os.path)
path = os.path.join(os.path.dirname(__file__), 'unit data converted to json\\aoe2dat\\data', 'units_buildings.json')
with open(
        path) as file:
    data = json.load(file)

    data: dict[str, Union[dict, int, str]]

    unit_data = {}
    unit_data = data["Units"]

    # print(unit_data[0]["Class"])
    enum_variable = []

    for key in range(0, len(unit_data), 1):
        unit_id = unit_data[key]["ID"]
        unit_class = unit_data[key]["Class"]
        unit_name = str.upper(str.replace(unit_data[key]["Name"], " ", "_"))
        # print(unit_data[key])
        HeroMode = -1
        attack = [0, 0]
        if unit_name == "" or unit_id == 94 or unit_id == 436 or unit_id == 438 or unit_id == 138 or unit_id == 639:
            pass
        else:
            try:
                HeroMode = int(unit_data[key]["Creatable"]["HeroMode"])
                print(HeroMode)
            except:
                print("No hero mode!")
            try:
                attack = unit_data[key]["Type50"]["Attacks"]
            except:
                print("No attack!")
            try:
                TrainLocationID = unit_data[key]["TrainLocationID"]
            except:
                print("No train location!")
            enum_variable.append(Unit.getUnit(self=Unit, unit_id=unit_id, unit_class=unit_class, unit_name=unit_name,
                                              HeroMode=HeroMode, attack=attack))


# Run./aoe2dat empires2_x2_p1.dat to get json

# tech_data = data["techs"]
#
# enum_variable2 = []
#
# for key in tech_data.keys():
#     tech_id = key
#     tech_name = str.upper(str.replace(tech_data[key]["name"]," ", "_"))
#     if tech_name == "":
#         pass
#     else:
#         enum_variable2.append([tech_name, [tech_id]])
#         print(f"{tech_name} = ({tech_id})")


unitListGet = []
class GetAllUnitData:
    def get_unit_data():
        # unit_data = []
        for enum in enum_variable:
            print(enum)
        return enum_variable
    def get_archer():
        for enum in enum_variable:
            # get archer class unit
            if enum.unitClass == 0 and enum.HeroMode == 0:
                unitListGet.append(enum)
                enum.tier = 1
        return unitListGet
    def get_infantry():
        for enum in enum_variable:
            # get archer class unit
            if enum.unitClass == 6 and enum.HeroMode == 0:
                unitListGet.append(enum)
                enum.tier = 1
        return unitListGet
