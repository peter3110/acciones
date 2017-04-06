from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, JsonResponse, HttpResponse

import json
import pandas

def getDataAccion(colnames, accion):
	if (accion == 'AGRO'):
		return pandas.read_csv('backend/data/hist_AGRO20170404.csv', names=colnames, header=0)
	if (accion == 'CECO2'):
		return pandas.read_csv('backend/data/hist_CECO220170404.csv', names=colnames, header=0)
	if (accion == 'ALUA'):
		return pandas.read_csv('backend/data/hist_ALUA20170404.csv', names=colnames, header=0)
	return []

@csrf_exempt
def getData(request):
	colnames = ['fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'volumen', 'openint']

	data = getDataAccion(colnames, 'CECO2')
	points = [[]]
	for i in range(0, len(data.fecha)-1):
		points[0].append({
			"fecha": data.fecha[i],
			"cierre": float(data.cierre[i])
		})
	return JsonResponse({ "points": points }, status=200)
