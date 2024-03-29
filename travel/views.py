import base64, json, boto3, time, os

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from home.includes.serializer import ExtJsonSerializer
from .models import Place, WorldPlace

def index(request):
  return render(request, 'travel/index.html')

@csrf_exempt
def places(request):
  if request.method == 'GET':
    places = Place.objects.all()
    return HttpResponse(ExtJsonSerializer().serialize(places, 
      fields = ['name', 'icon', 'type', 'address', 
        'latitude', 'longitude', 'plan_date', 'plan_time']))

  elif request.method == 'POST':
    data = json.loads(request.body)
    place = Place(
      name = data['name'], 
      search = data['name'],
      icon = data['icon'],
      type = data['type'],
      address = data['address'],
      latitude = data['latitude'],
      longitude = data['longitude'],
      added_at = timezone.now(),
    )
    place.save()

    return None

@require_http_methods(['GET'])
def world(request):
  return render(request, 'travel/world.html', {
    'places': WorldPlace.objects.all()
  })

@require_http_methods(['POST'])
@csrf_exempt
def location(request):
  basic_auth = request.META['HTTP_AUTHORIZATION'].split()
  username, password = base64.b64decode(basic_auth[1]).split(':')
  user = authenticate(username = username, password = password)
  if user is not None and user.is_active:
    data = json.loads(request.body)
    if data['_type'] == 'location':
      if 'DYNAMODB_REGION' in os.environ:
        client = boto3.client('dynamodb', region_name = os.environ['DYNAMODB_REGION'])
      else:
        client = boto3.client('dynamodb');

      location = {
        'user_id': { 'N': str(user.id) },
        'battery': { 'N': str(data['batt']) },
        'latitude': { 'N': str(data['lat']) },
        'longitude': { 'N': str(data['lon']) },
        'network': { 'S': str(data['conn']) },
        'tracker_id': { 'S': str(data['tid']) },
        'visited_at': { 'N': str(data['tst']) },
      }
      if 'acc' in data:
        location['accuracy'] = { 'N': str(data['acc']) }
      if 'alt' in data:
        location['alt'] = { 'N': str(data['alt']) }
      if 'cog' in data:
        location['heading'] = { 'N': str(data['cog']) }
      if 'desc' in data:
        location['waypoint'] = { 'N': str(data['desc']) }
      if 'event' in data:
        location['event'] = { 'N': str(data['event']) }
      if 'rad' in data:
        location['radius'] = { 'N': str(data['rad']) }
      if 'vac' in data:
        location['altitude_accurancy'] = { 'N': str(data['vac']) }
      if 'vel' in data:
        location['velocity'] = { 'N': str(data['vel']) }
      if 'p' in data:
        location['barometric_pressure'] = { 'N': str(data['p']) }
      if 't' in data:
        location['trigger'] = { 'S': str(data['t']) }


      result = client.put_item(
        TableName = 'locations',
        Item = location
      )
      return HttpResponse(json.dumps({
        'result': result
      }), content_type = 'application/json')

  response = HttpResponse()
  response.status_code = 401
  return response