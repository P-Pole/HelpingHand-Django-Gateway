from datetime import datetime
from tokenize import generate_tokens
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



def get_charities(request):

    response = requests.get('http://localhost:8002/api/charities/')

    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to retrieve charities data'}, status=500)
    
    charities_data = response.json()

    return JsonResponse(charities_data, safe=False, status=200)

def get_charitiesID(request, pk=None):

    response = requests.get(f'http://localhost:8002/api/charities/{pk}/')

    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to retrieve charities data'}, status=500)
    
    charities_data = response.json()

    return JsonResponse(charities_data, safe=False, status=200)

@csrf_exempt 
def post_transactions(request):

    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        

        charities= body.get('charity_ids')
        amount = body.get('amount')
        subscription = body.get('subscription')
        user_id = body.get('user_id')
        date= datetime.now()
        body["charities"] = ",".join(map(str, charities))

        body["date"] = str(date)
        print(body)
        
        response = requests.post('http://localhost:8001/transactions', json=body)
        if response.status_code == 201:
            return JsonResponse({'success': 'Transaction successful'}, status=201)
        else:
            return JsonResponse({'error': 'Failed to post transaction'}, status=500)
        
    else:
        return JsonResponse({"success":False,'error':'Invalid method'}, status=405)

   

@csrf_exempt        
def login_auth(request):
    if request.method =='POST':

        body_unicode =request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body.get('email')
        password = body.get('password')
        liked_charities = body.get('liked_charities')

        response = requests.get('http://localhost:8002/api/user/')
        users_data = response.json()

        for user_data in users_data:

            if user_data['email'] == email:
                if password==user_data['password']:
                # if check_password(password, user_data['password']):
                    
                    # return JsonResponse({"success":True})
                    user_data.pop('password')
                    return JsonResponse({"success":True, "user": user_data})
                else:
                    return JsonResponse({"success":False,'error': 'Invalid password'}, status=401)
        return JsonResponse({"success":False,'error': 'User not found'}, status=404)
    else:
        return JsonResponse({"success":False,'error':'Invalid method'}, status=405)
            
@api_view(['POST'])
def register_user(request):
    email = request.data.get('email', None)
    
    
    response = requests.get('http://localhost:8002/api/user/')
    users_data = response.json()

    for user_data in users_data:
        if user_data['email'] == email:
            return Response({"error": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

    
    user_data = {
        'email': email,
        'password': request.data.get('password'),
        'first_name': request.data.get('first_name'),
        'last_name': request.data.get('last_name'),
    }

    response = requests.post('http://localhost:8002/api/user/', data=user_data)

    if response.status_code == status.HTTP_201_CREATED:
        return Response({"success": True, "message": "User registered successfully."}, status=status.HTTP_201_CREATED)

    return Response(response.json(), status=response.status_code)

# @csrf_exempt
# def set_like(request, pk=None):
#     if request.method == 'POST':
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         email = body.get('email')
#         new_liked_charity = body.get('likeID')

#         response = requests.get('http://localhost:8002/api/user/')
#         users_data = response.json()
#         user_found = False

#         for user_data in users_data:
#             if user_data['email'] == email:
#                 user_found = True
#                 current_liked_charities = user_data['liked_charities']
#                 if new_liked_charity not in current_liked_charities:
#                     current_liked_charities.append(new_liked_charity)
#                     user_data = {'id': user_data['id'], 'liked_charities': current_liked_charities}
#                     pk = user_data['id']
#                     response = requests.put(f'http://localhost:8002/api/user/{pk}/', data=user_data)
#                     return JsonResponse({"success": True, "liked":True, "updated_liked_charities": current_liked_charities}, status=status.HTTP_200_OK)
                

#         if not user_found:
#             return JsonResponse({"success": False, 'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

#     return JsonResponse({"success": False, 'error': 'Invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)







