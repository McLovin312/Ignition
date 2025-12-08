def handleTimerEvent():
	from java.net import InetAddress
	
	logger = system.util.getLogger("DeviceMonitor")
	
	targetIp = "10.10.60.128"
	
	def isReachable(ip):
	    try:
	        return InetAddress.getByName(ip).isReachable(2000)
	    except Exception as e:
	        logger.warn("Ping failed for {}: {}".format(ip, str(e)))
	        return False
	
	# Check if device is online
	if not isReachable(targetIp):
	    sessions = system.perspective.getSessionInfo(projectFilter="McLovin")
	    
	    for session in sessions:
	        try:
	            system.perspective.closeSession(session['id'])
	            logger.info("Closed session: {}".format(session['id']))
	        except Exception as e:
	            logger.error("Error closing session {}: {}".format(session['id'], str(e)))
	
	print("finished")