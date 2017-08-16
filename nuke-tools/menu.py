import sip
import nuke
import checkout
import publish
import rollback
import nukeAutoComp

menubar = nuke.menu("Nuke")
# Custom Lab Tools
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("byu-pipeline Menu", icon="make me.png")
m.addCommand("Checkout", 'checkout.go()', icon="checkout.xpm")
m.addCommand("Publish", 'publish.go()', icon="publish.xpm")
m.addCommand("Rollback", 'rollback.go()', icon="rollback.xpm")
m.addCommand("Auto Comp", 'nukeAutoComp.go()', icon="")
#Allen was asking about Nuke + Pipeline
