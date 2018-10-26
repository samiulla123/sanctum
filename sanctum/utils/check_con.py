try:
    import httplib
except:
    import http.client as httplib
URL="www.google.com"
def check_connection(url=URL):
    conn = httplib.HTTPConnection(url, timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

if __name__ == "__main__":
	conn=check_connection()
	if conn:
		print('connection established\n')
	else:
		print('connection not found\n')
