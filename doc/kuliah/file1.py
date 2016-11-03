import shapefile

class File1(object):
	def __init__(self,namafile):
		self.sf = shapefile.Reader(namafile)
	def itungBaris(self):
		rec = self.sf.shapes()
		return len(rec)
