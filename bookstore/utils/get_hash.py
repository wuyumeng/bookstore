from hashlib import sha1
def get_hash(str):
	"""用来加密明文密码"""
	sh = sha1()
	sh.update(str.encode("utf-8"))
	return sh.hexdigest()