from django.shortcuts import render
from to.models import task

# Create your views here.
def asr(request):
    if request.method== 'POST':
        index=request.POST['index']
        task1=request.POST['task1']
        t= task(index=index, task1=task1)
        t.save()




    p=task.objects.all()

    return render(request,'todo.html',{"s":p})
