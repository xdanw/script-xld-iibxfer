list_iibDeployableSpecs = repository.search("iib.BarFileSpec");
list_udmDeployedApps = repository.search("udm.DeployedApplication");
list_iibDeployedInstances = repository.search("iib.BarFile");
# Notes:
# list_udmDeployedApps are records of deployed app versions. NO key/value data only has an array of IDs in .deployeds.
# list_iibDeployableSpecs are artifacts, will have key values
# Use this to dump all stored iibBarFiles (including those not yet deployed)
# list_iibDeployedInstances are deployed artifact and also will have key values
# Use this to dump iibBarFiles (only ones that were sent to a server)

print "Found these deployed iib.BarFile items: " + str(list_iibDeployedInstances) + "\r\n";

for deployedId in list_iibDeployedInstances:
   # Debug...
   # print "Dumping: " + str(deployedId) + "...\r\n"
   iibCiObject = repository.read(deployedId);
   iibName = iibCiObject.name;
   iibPreProp = iibCiObject.values["preProperties"];
   iibPostProp = iibCiObject.values["postProperties"];

   newDICT1 = factory.configurationItem("Environments/Dictionaries/IIB_" + iibName + "_preProperties", "udm.Dictionary", {"entries": iibPreProp});
   newDICT2 = factory.configurationItem("Environments/Dictionaries/IIB_" + iibName + "_postProperties", "udm.Dictionary", {"entries": iibPostProp});

   repository.create(newDICT1);
   repository.create(newDICT2);
