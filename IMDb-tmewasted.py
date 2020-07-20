'''
Lets see how much time is spend in watching TV series.
List of TV series watched till date in an ARRAY.
Loop get the seasons -> episode count -> runtime of each episode -> summation of all the episodes.
'''
# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')



from imdb import IMDb
from pprint import pprint
import json
# create an instance of the IMDb class
ia = IMDb()
final_time = list()
finaltime = 0

webseries = ['0903747','0411008','0455275','0108778','0098904','0285403','6468322']
for webserie in webseries:
	movie = ia.get_movie(webserie, info=['episodes'])      # Band of Brothers
	pprint(movie)
	for k,v in movie.items():
		if isinstance(v,dict):
			for kk,vv in v.items():
				for kkk,vvv in vv.items():
					pprint(vvv.movieID)
					# pprint(vvv.myTitle)
					movie1 = ia.get_movie(vvv.movieID)
					pprint(movie1)
					for k,v in movie1.items():
						if k == 'runtimes':
							print(k,v)
							final_time.append(v)
							finaltime += int(v[0])

		pprint(v)


pprint(final_time)
pprint(finaltime)
pprint('time wasted in minutes --> ' + str(finaltime))
print('hey')
