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
	acciones = request.GET['acciones'][1:-1]
	if acciones is not None: acciones = [elem for elem in acciones.split(',')]

	porcentajes = request.GET['porcentajes'][1:-1]
	if porcentajes is not None: porcentajes = [float(elem) for elem in porcentajes.split(',')]

	colnames = ['fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'volumen', 'openint']

	#data = getDataAccion(colnames, 'CECO2')

	data = [getDataAccion(colnames, str(accion)) for accion in acciones]

	points = [[]]

	for f in range(0, len(data[0].fecha)-1): # cada fecha
		cierre = 0
		
		for j in range(0, len(data)): # cada accion
			cierre = cierre + float(data[j].cierre[f]) * porcentajes[j]

		points[0].append( {
			"fecha": data[0].fecha[f],
			"cierre": round(cierre,2)
		})
	return JsonResponse({"points": points }, status=200)
