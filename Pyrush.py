# L'ARME DE BASE


# Mitraillette
def smg_mode(self):
	"""tire dans le meme principe que agent.Fire mais plus vite et permet de recharger. La recharge prend 5 sec
 hitFire(10)
	rangeFire(30)
	spreadFire(0)
	ammo(100)
	dtFire(50)
 """
	pass


# LES POWER-UPS


# Après avoir fait 3 kills
def refuelAmmo(self):
	"""Recharge toutes les munitions de l'arme.
 Taux de drop : 30%
 """
	pass


def shield(self):
	"""Bouclier qui contre toutes les balles pendant 3sec
Taux de drop : 10%
 """
	pass


def heal(self):
	"""Redonne la moitié de la vie perdue
 Taux de drop : 50%
 """
	pass


def invisibility(self):
	"""Rend le détenteur invisible pendant 2sec
 Taux de drop : 10%
 """
	pass


# Après avoir rammassé une pièce
def sniper_mode(self):
	"""effectue un tir qui ulitise 5 munitions permettant de tuer en une balle mais tire en 2sec d'intervalle
 Taux de drop : 50%
 hitFire(100)
 rangeFire(0)
 spreadFire(0)
 ammo(5)
 dtFire(2000)
 """
	pass


def rocket_mode(self):
	"""tire en utilisant 20 munitions et a l'impact pose une bombe qui explose instantanément. Cadence de tir de 5 secondes d'intervale
 Taux de drop : 50%
 hitFire(50)
 rangeFire(0)
 ammo(40)
 ownerFire(20)
 PAS ENCORE FONCTIONNEL
 """
	pass
