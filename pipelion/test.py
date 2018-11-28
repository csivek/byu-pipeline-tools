print("Hello World")

import lion_file_mng_dummy.production_reader as pr

bodies = pr.getBodiesByUser("csivek")
bodies[0].prettyPrint(0)
bodies = pr.getBodies()
for body in bodies:
	body.prettyPrint(0)

histories = pr.getNewHistories("house/interior/testasset")
for hist in histories:
	hist.prettyPrint(0)

#from creation import create_asset
#create_asset("jukebox", "asset")
