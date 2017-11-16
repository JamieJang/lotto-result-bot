from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ResultNumber

def keyboard(request):
	return JsonResponse({
		'type':'text',
	})

def get_result_num(r):
	try:
		result = ResultNumber.objects.get(rounds=r)
		return result
	except:
		return False
	

@csrf_exempt
def answer(request):
	json_str = ((request.body).decode('utf-8'))
	received_json_data = json.loads(json_str)
	rounds = received_json_data['content']
	result = get_result_num(rounds)
	if result:
		return JsonResponse({
			'message':{
				'text': rounds + '회차 당첨번호입니다.\n\n' + get_result_num(rounds)
			},
		})
	else:
		return JsonResponse({
			'message':{
				'text': rounds + '회차는 아직 추첨 전입니다.'
			},
		})
