from django.shortcuts import render, redirect, get_object_or_404

from course.models import Course

def course_list(request):
    courses = Course.objects.all()  # Fetch all courses
    return render(request, 'course/course_list.html', {'courses': courses})


def add_course(request):
    if request.method == "POST":
        title = request.POST.get('title')
        duration = request.POST.get('duration')

        # Create and save new course
        Course.objects.create(title=title, duration=duration)

        return redirect('course_list')  # Redirect back to course list

    return render(request, 'course/add_course.html')

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        course.title = request.POST.get('title')
        course.duration = request.POST.get('duration')
        course.save()
        return redirect('course_list')

    return render(request, 'course/update_course.html', {'course': course})

# Delete Course
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course_list')
