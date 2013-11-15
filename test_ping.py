import httplib, urllib 
import subprocess 
import time
#205 server web
#208 monitor
#86 PC windows
#202 rele
#211 sonda analogica
lista_ip_dispositivi_OK = [208,211] 
lista_ip_dispositivi_ERR = []
while True:
	for ping in lista_ip_dispositivi_OK:
		print lista_ip_dispositivi_OK
		print lista_ip_dispositivi_ERR
		
		if (ping in lista_ip_dispositivi_ERR) == False:
			address = "192.168.0." + str(ping)
			res = subprocess.call(['ping', '-c', '1', address])
			if res == 0:
				print "ping to", address, "OK "
				#conn = httplib.HTTPSConnection("api.pushover.net:443")
				#conn.request("POST", "/1/messages.json",urllib.urlencode({"token": "abdf67yAvRcQufveo2nGkwKNi6xTHb","user": "u2v1vYFWvmGGNGN3Ffnn9NnCW1Y3xN","message": "hello world",}), { "Content-type": "application/x-www-form-urlencoded" })
				#conn.getresponse()
			elif res == 2:
				print "no response from", address
				conn = httplib.HTTPSConnection("api.pushover.net:443")
				conn.request("POST", "/1/messages.json",urllib.urlencode({"token": "abdf67yAvRcQufveo2nGkwKNi6xTHb","user": "u2v1vYFWvmGGNGN3Ffnn9NnCW1Y3xN","message": "errore da %s" % address,"title": "Sonda non raggiungibile"}), { "Content-type": "application/x-www-form-urlencoded" })
				conn.getresponse()
				lista_ip_dispositivi_ERR.append(ping)
			else:
				print "ping to", address, "failed!"
				conn = httplib.HTTPSConnection("api.pushover.net:443")
				conn.request("POST", "/1/messages.json",urllib.urlencode({"token": "abdf67yAvRcQufveo2nGkwKNi6xTHb","user": "u2v1vYFWvmGGNGN3Ffnn9NnCW1Y3xN","message": "errore da %s" % address,"title": "Sonda non raggiungibile"}), { "Content-type": "application/x-www-form-urlencoded" })
				conn.getresponse()
				lista_ip_dispositivi_ERR.append(ping)
		else:
			address = "192.168.0." + str(ping)
			res = subprocess.call(['ping', '-c', '1', address])
			if res == 0:
				print "ping to", address, "OK "
				conn = httplib.HTTPSConnection("api.pushover.net:443")
				conn.request("POST", "/1/messages.json",urllib.urlencode({"token": "abdf67yAvRcQufveo2nGkwKNi6xTHb","user": "u2v1vYFWvmGGNGN3Ffnn9NnCW1Y3xN","message": "sonda %s ora risulta raggiungibile" % address,"title": "Sonda ripristinata"}), { "Content-type": "application/x-www-form-urlencoded" })
				conn.getresponse()
				lista_ip_dispositivi_ERR.remove(ping)
			elif res == 2:
				print "no response from", address
				#conn = httplib.HTTPSConnection("api.pushover.net:443")
				#conn.request("POST", "/1/messages.json",urllib.urlencode({"token": "abdf67yAvRcQufveo2nGkwKNi6xTHb","user": "u2v1vYFWvmGGNGN3Ffnn9NnCW1Y3xN","message": "errore da %s" % address,"title": "Sonda non raggiungibile"}), { "Content-ty$
				#conn.getresponse()
			else:
				print "ping to", address, "failed!"
				#conn = httplib.HTTPSConnection("api.pushover.net:443")
				#conn.request("POST", "/1/messages.json",urllib.urlencode({"token": "abdf67yAvRcQufveo2nGkwKNi6xTHb","user": "u2v1vYFWvmGGNGN3Ffnn9NnCW1Y3xN","message": "errore da %s" % address,"title": "Sonda non raggiungibile"}), { "Content-ty$
				#conn.getresponse()

	time.sleep(60)
