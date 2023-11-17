import j2l.pytactx.agent as pytactx
import getpass

agent = pytactx.Agent(playerId=getpass.getpass("Ref ID: "),
						arena="pyrush",
						username="demo",
						password=input("🔑 password: "),
						server="mqtt.jusdeliens.com",
						verbosity=2)

agent.ruleArena("reset", True)
while True:
	agent.update()
	agent.lookAt((agent.dir + 1) % 4)
	agent.ruleArena("gridColumns",50)
	agent.ruleArena("gridrow",50)
	agent.ruleArena("bgImg","https://i.goopics.net/nqoy0x.png")
	agent.ruleArena("hitImg","https://i.goopics.net/g61y29.png")