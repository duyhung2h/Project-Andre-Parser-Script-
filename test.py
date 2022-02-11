from model.EnemyList import EnemyList
import sys
from pip import main
# EnemyList.get_enemy_archer_list()
enemyList = EnemyList.get_enemy_infantry_list(tier=1)
EnemyList.print_list(enemyList)
