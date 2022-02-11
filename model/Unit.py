from typing import Union

from AoE2ScenarioParser.objects.data_objects.unit import Unit


class Unit:
    def __init__(self, unitId, unitName, attack, highestAtk, unitClass, HeroMode, TrainLocationID, tier):
        self.unitId = unitId
        self.unitName = unitName
        self.attack = attack
        self.highestAtk = highestAtk
        self.unitClass = unitClass
        self.HeroMode = HeroMode
        self.TrainLocationID = TrainLocationID
        self.tier = tier

    def getUnit(
            self,
            unit_id: Union[int, None] = None,
            unit_name: Union[int, None] = None,
            attack: Union[int, None] = None,
            highestAtk: Union[int, None] = None,
            unit_class: Union[int, None] = None,
            HeroMode: Union[int, None] = None,
            TrainLocationID: Union[int, None] = None,
            tier: Union[int, None] = None,
    ) -> Unit:
        return self(
            unitId=unit_id,
            unitName=unit_name,
            attack=attack,
            highestAtk=highestAtk,
            unitClass=unit_class,
            HeroMode=HeroMode,
            TrainLocationID=TrainLocationID,
            tier=tier,
        )
    def get_faction_unitid(faction: str):
        '''
        :return: a list of faction unit id based on the passed string "faction"
        check which faction is in a contested zone by checking the amount of p2 flag

        first line: inf 2
        second line: cav 3
        third line: archers 2
        '''
        if faction == "NAR":
            return [
                1, 1663, 1697,
                40, 553, 1228, 1230, 275,
                46, 52, 557, 866, 868
            ]