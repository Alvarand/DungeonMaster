import random

#здесь хранятся глобальные переменные

amount = 0
player = {'level': 1, 'type': random.randint(1,4), 'i':0, 'j':0, 'hp':6, 'arm':0} #конфигурация игрока
enemy = {'lvl':1,'i':0, 'j':0, 'hp':2} #конфигурация мобов

#словарь текстур
dictEnv = {	0: 'srcBMP/env',
				1: 'srcBMP/env',
				2: 'srcBMP/player/'+str(player['type'])+'.bmp',
				3: 'srcBMP/env/light/ladder.bmp',
				4: 'srcBMP/env/light/chest.bmp',
				5: 'srcBMP/env/light/mob.png'
			}