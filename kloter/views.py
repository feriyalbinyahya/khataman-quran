from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import NumberKloter
from .models import Person
from .forms import PersonForm

def index(request):
    response = {}
    number = len(NumberKloter.objects.all())
    response['kloter_number'] = str(number)
    return render(request, 'dashboard.html', response)

def list_kloter(request):
    response = {}
    number = NumberKloter.objects.all()
    response['kloter_number2'] = number
    return render(request, 'listkloter.html', response)

def addkloter(request):
    new_kloter = NumberKloter(kloter_number=len(NumberKloter.objects.all())+1, ronde=1)
    new_kloter.save()
    return HttpResponseRedirect('/kloter/')

def render_kloter(request, kloter):
    response = {}
    persons = Person.objects.filter(nomer_kloter__iexact=kloter)
    jumlah_selesai = 0
    for i in persons:
        if i.selesai:
            jumlah_selesai = jumlah_selesai + 1

    response['selesai'] = jumlah_selesai
    list_number = [i for i in range(1, len(persons)+1)]
    periode = NumberKloter.objects.get(kloter_number=kloter)
    response['persons'] = persons
    response['list_number'] = list_number
    response['periode'] = periode

    return render(request, 'kloter.html', response)

def new_juz(request, kloter):
    periode = NumberKloter.objects.get(kloter_number=kloter)
    periode.ronde = periode.ronde + 1
    periode.save()
    persons = Person.objects.filter(nomer_kloter__iexact=int(kloter))
    temp_name = ""
    if len(persons) > 2:
        temp_name = persons[0].name
        persons[0].name = persons[len(persons)-1].name
        persons[0].save()
        for i in range(len(persons)-1):
            temp = persons[i+1].name
            persons[i+1].name = temp_name
            persons[i+1].save()
            temp_name = temp

    for i in persons:
        i.selesai = False
        i.save()

            
    

    return HttpResponseRedirect('/' + str(kloter))

def formperson(request):
    response = {}
    response['person_form'] = PersonForm
    return render(request, 'formtambah.html', response)

def addperson(request):
    response = {}
    form = PersonForm(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['name'] = request.POST['name']
        response['no_juz'] = int(request.POST['no_juz'])
        response['nomer_kloter'] = int(request.POST['nomer_kloter'])
        response['telepon'] = request.POST['telepon']
        periode = NumberKloter.objects.get(kloter_number=response['nomer_kloter'])
        person = Person(name=response['name'], no_juz=response['no_juz'], nomer_kloter=response['nomer_kloter'], ronde=periode.ronde, telepon=response['telepon'])
        person.save()
        return HttpResponseRedirect('/' + str(response['nomer_kloter']))
    else:
        return HttpResponseRedirect('/')

def deleteperson(request, id):
    response={}
    person = Person.objects.get(id = id)
    kloter = person.nomer_kloter
    person.delete()
    return HttpResponseRedirect('/' + str(kloter))

def resetjuz(request, kloter):
    persons = Person.objects.filter(nomer_kloter__iexact=int(kloter))
    list_number = [i for i in range(1, len(persons)+1)]
    for i in range(len(persons)):
        t = persons[i]
        t.no_juz = list_number[i]
        t.save()
    return HttpResponseRedirect('/' + str(kloter))

def resetputaran(request, kloter):
    putaran = NumberKloter.objects.filter(kloter_number__iexact=int(kloter))
    t = putaran[0]
    t.ronde = 1
    t.save()

    return HttpResponseRedirect('/' + str(kloter))

def selesai(request, id):
    person = Person.objects.get(id = id)
    kloter = person.nomer_kloter
    person.selesai = True
    person.save()
    return HttpResponseRedirect('/' + str(kloter))

def belumselesai(request, id):
    person = Person.objects.get(id = id)
    kloter = person.nomer_kloter
    person.selesai = False
    person.save()
    return HttpResponseRedirect('/' + str(kloter))
