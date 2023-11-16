import j2l.pytactx.agent as pytactx

agent = pytactx.Agent(playerId=input("👾 id: "),
						arena=input("🎲 arena: "),
						username="demo",
						password=input("🔑 password: "),
						server="mqtt.jusdeliens.com",
						verbosity=2)

actual_state = "recherche"

ennemyX = 0
ennemyY = 0
orientation = 0

def rechercher():
  '''
  Actions effectuées quand le robot est en état recherche:
    Mouvements aléatoires jusqu'à trouver un ennemi
  Transition:
    Si un ennemi est détecté, on passe en mode recherche tout en notant sa position      actuelle
  :ennemyX: Dernière coordonnée X connue de l'ennemi
  :ennemyY: Dernière coordonnée Y connue de l'ennemi
  :actual_state: Etat actuel de la machine à états ("recherche" ou "attaque")
  :orientation: Orientation actuelle du robot (entre 0 et 3)
  :agent.distance: Distance entre le robot et l'ennemi
  :dirX: Valeur du mouvement X choisi par le robot (entre -1 et 1)
  :dirY: Valeur du mouvement Y choisi par le robot (entre -1 et 1)
  '''
  agent.setColor(0, 255, 0)
  global ennemyX
  global ennemyY
  global actual_state
  global orientation
  if agent.distance != 0:
    if orientation == 0:
      ennemyX = agent.x+agent.distance
      ennemyY = agent.y
    if orientation == 1:
      ennemyX = agent.x
      ennemyY = agent.y-agent.distance
    if orientation == 2:
      ennemyX = agent.x-agent.distance
      ennemyY = agent.y
    if orientation == 3:
      ennemyX = agent.x
      ennemyY = agent.y+agent.distance
    actual_state = "attaque"
  for i in range(5):
    agent.move(1,0)
    agent.lookAt(0)
    agent.lookAt(1)
    agent.lookAt(2)
    agent.lookAt(3)
  for i in range(5):
    agent.move(0,-1)
    agent.lookAt(0)
    agent.lookAt(1)
    agent.lookAt(2)
    agent.lookAt(3)
  for i in range(5):
    agent.move(-1,0)
    agent.lookAt(0)
    agent.lookAt(1)
    agent.lookAt(2)
    agent.lookAt(3)
  for i in range(5):
    agent.move(0,1)
    agent.lookAt(0)
    agent.lookAt(1)
    agent.lookAt(2)
    agent.lookAt(3)
  agent.update()

def attaquer():
  '''
  Actions effectuées quand le robot est en état d'attaque:
    Se déplace vers la dernière position ennemie connue et tire sur les ennemis          rencontrés sur la route
  Transition:
    Si quand le robot arrive à la dernière position ennemie et ayant réalisé u 360       il ne trouve personne, il entre en mode recherche
  :ennemyX: Dernière coordonnée X connue de l'ennemi
  :ennemyY: Dernière coordonnée Y connue de l'ennemi
  :actual_state: Etat actuel de la machine à états ("recherche" ou "attaque")
  :ori_to_do: Orientation du robot selon son mouvement
  :agent.distance: Distance entre le robot et l'ennemi
  :x_to_do: Valeur du mouvement X pour atteindre ennemyX
  :y_to_do: Valeur du mouvement Y pour atteindre ennemyY
  '''
  agent.setColor(255,0,0)
  global ennemyX
  global ennemyY
  global actual_state
  while ennemyX != agent.x and ennemyY != agent.y:
    if ennemyX > agent.x:
      x_to_do = 1
      ori_to_do = 0
    if ennemyY > agent.y:
      y_to_do = 1
    if ennemyX < agent.x:
      x_to_do = -1
      ori_to_do = 2
    if ennemyY < agent.y:
      y_to_do = -1
    if ennemyX == agent.x:
      x_to_do = 0
      ori_to_do = 1
    if ennemyY == agent.y:
      y_to_do = 0
    agent.move(x_to_do,y_to_do)
    agent.lookAt(ori_to_do)
    if agent.distance != 0:
      agent.fire(True)
      if orientation == 0:
        ennemyX = agent.x+agent.distance
        ennemyY = agent.y
      if orientation == 1:
        ennemyX = agent.x
        ennemyY = agent.y-agent.distance
      if orientation == 2:
        ennemyX = agent.x-agent.distance
        ennemyY = agent.y
    actual_state = "recherche"
    agent.fire(False)
while True:
  agent.update()
  if actual_state == "recherche":
      rechercher()
  if actual_state== "attaque":
      attaquer()