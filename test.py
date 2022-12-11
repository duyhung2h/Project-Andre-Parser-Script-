from model.EnemyList import EnemyList
import sys, os
from pip import main
# EnemyList.get_enemy_archer_list()
enemyList = EnemyList.get_enemy_infantry_list(tier=1)
EnemyList.print_list(enemyList)
for item in enemyList[:5]+enemyList[7:]:
    print(item.unitId)
EnemyList.print_list(enemyList[1:4])