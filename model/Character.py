class Character:
    """
    This is a_localArea Character class


    A character can have different attributes, such as unit_id, unit_name (their true name displayed in the scenario)

    characterClass indicates which class a_localArea character is, which will affect on their gear restriction.

    There are 4 character classes at the moment: warrior, rogue, ranger and soulweaver.

    They can also have different panel areas, according to their position on the list."""


    def __init__(self, unitName, unitId, characterClass, coreUnitId, skill1Icon, skill2Icon, maxRange, projectileId, hp,
                 atk, meleeArmor, pierceArmor, potraitId):
        self.unitName = unitName
        self.unitId = unitId
        self.characterClass = characterClass
        self.coreUnitId = coreUnitId
        self.skill1Icon = skill1Icon
        self.skill2Icon = skill2Icon
        self.maxRange = maxRange
        self.projectileId = projectileId
        self.hp = hp
        self.atk = atk
        self.meleeArmor = meleeArmor
        self.pierceArmor = pierceArmor
        self.potraitId = potraitId


    def get_characters():
        return [
            Character('Charles', 439, "warrior", 136167, 281, 276, 0, 187, 50, 3, 3, 1, 162),
            Character('Coline', 1066, "rogue", 136180, 277, 278, 0, 187, 30, 5, 2, 1, 216),
            Character('Nemunas', 1069, "ranger", 169037, 279, 277, 4, 511, 30, 5, 0, 3, 314),
            Character('Dominiel', 430, "soulweaver", 136179, 276, 280, 3, 369, 40, 4, 1, 3, 52),
            Character('Corvus', 1683, "warrior", 168727, 281, 276, 0, 187, 40, 4, 3, 1, 368),
        ]
