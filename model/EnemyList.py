from GetAllUnitData import GetAllUnitData


class EnemyList:
    unitList = []

    def print_list(unitList):
        for unit in unitList:
            print("unitId: " + str(unit.unitId), "unitName: " + unit.unitName, "unitClass: " + str(unit.unitClass),
                  "tier: " + str(unit.tier), "HeroMode: " + str(unit.HeroMode), "HighestAtk: " + str(unit.highestAtk))

    def filter_list_by_tier(tier: int, list: list):
        unitList = []
        for unit in list:
            if unit.tier == tier:
                unitList.append(unit)
        return unitList
    def get_enemy_archer_list(tier: int):
        unitList = GetAllUnitData.get_archer()
        for unit in unitList:
            highestAtk = {'Class': -1, 'Amount': 0}
            for atk in unit.attack:
                if (atk["Class"] == 3) or (atk["Class"] == 4):
                    if atk["Amount"] > highestAtk["Amount"]:
                        highestAtk = atk
                        unit.highestAtk = atk
            # check attack and classify tier
            if highestAtk["Amount"] > 4 and highestAtk["Class"] == 3:
                unit.tier = 2
            if highestAtk["Amount"] > 6 and highestAtk["Class"] == 3:
                unit.tier = 3
            # exception: elite skirm and imp skirm should be tier 2 and 3
            if unit.unitId == 6:
                unit.tier = 2
            if unit.unitId == 1155:
                unit.tier = 3
        unitListFiltered = EnemyList.filter_list_by_tier(tier=1, list=unitList)
        return unitListFiltered

    def get_enemy_infantry_list(tier: int):
        unitList = GetAllUnitData.get_infantry()
        for unit in unitList:
            highestAtk = {'Class': -1, 'Amount': 0}
            for atk in unit.attack:
                if (atk["Class"] == 3) or (atk["Class"] == 4):
                    if atk["Amount"] > highestAtk["Amount"]:
                        highestAtk = atk
                        unit.highestAtk = atk
            # check attack and classify tier
            if highestAtk["Amount"] > 7 and highestAtk["Class"] == 4:
                unit.tier = 2
            if highestAtk["Amount"] > 11 and highestAtk["Class"] == 4:
                unit.tier = 3
            # exception: pikeman and h.pike, halb should be tier 2 and 3
            if unit.unitId == 358:
                unit.tier = 2
            if unit.unitId == 359 or unit.unitId == 892:
                unit.tier = 3
        unitListFiltered = EnemyList.filter_list_by_tier(tier=tier, list=unitList)
        return unitListFiltered
