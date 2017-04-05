from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, JsonResponse, HttpResponse

import json
import pandas

def getDataAccion(colnames, accion):
	if (accion == 'AGRO'):
		return pandas.read_csv('backend/data/hist_AGRO20170404.csv', names=colnames)
	if (accion == 'CECO2'):
		return pandas.read_csv('backend/data/hist_CECO220170404.csv', names=colnames)
	if (accion == 'ALUA'):
		return pandas.read_csv('backend/data/hist_ALUA20170404.csv', names=colnames)
	return []

@csrf_exempt
def getData(request):
	colnames = ['fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'volumen', 'openint']

	data = getDataAccion(colnames, 'CECO2')
	
	answer = {
		"fecha": data.fecha.tolist(),
		"cierre": data.cierre.tolist(),
	}
	return JsonResponse(answer, status=200)
