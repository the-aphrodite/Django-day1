from django.shortcuts import render, redirect, get_object_or_404

from trainee.models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all()  # Fetch all trainees
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})


def add_trainee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        # Create and save new trainee
        Trainee.objects.create(name=name, age=age, email=email)

        return redirect('trainee_list')  # Redirect back to trainee list

    return render(request, 'trainee/add_trainee.html')

def update_trainee(request, pk):  # Ensure 'pk' is used, not 'id'
    trainee = get_object_or_404(Trainee, pk=pk)  # pk should match the URL pattern

    if request.method == "POST":
        trainee.name = request.POST.get('name')
        trainee.age = request.POST.get('age')
        trainee.email = request.POST.get('email')
        trainee.save()
        return redirect('trainee_list')

    return render(request, 'trainee/update_trainee.html', {'trainee': trainee})

# Delete Trainee
def delete_trainee(request, pk):  # Use 'pk' instead of 'id'
    trainee = get_object_or_404(Trainee, pk=pk)
    trainee.delete()
    return redirect('trainee_list')  # Redirect back to the trainee list
