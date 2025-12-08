def doPost(request, session):
	import system.util

	# Decode the raw byte array
	raw = ''.join([chr(x) for x in request['data']])

	# Log for debugging (optional)
	system.util.getLogger("WEBDEV").info("Raw POST body: " + raw)

	try:
		data = system.util.jsonDecode(raw)
	except:
		return {'json': {'error': 'Invalid JSON body'}}

	# Get the statement if present
	statement = data.get("statement", "No statement received")

	return {'json': {'message': statement}}