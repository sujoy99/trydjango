from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm
# Create your views here.
class CourseObjectMixin(object):
    model = Course
    # lookup = 'id'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

class CourseCreateView(View):
    template_name = "courses/course_create.html"
    
    # get method
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)
    
    # post method
    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            'object_list' : self.get_queryset()
        }
        return render(request, self.template_name, context)

class FilterListView(CourseListView):
    queryset = Course.objects.filter(id=1)

class CourseView(CourseObjectMixin, View):
    template_name = "courses/course_detail.html"
    
    def get(self, request, id=None, *args, **kwargs):
        context = {
            'object' : self.get_object()
        }
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
    template_name = "courses/course_update.html"

    # get method
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context = {
                'object' : obj,
                'form' : form
            }
        return render(request, self.template_name, context)
    
    # post method
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context = {
                'object' : obj,
                'form' : form
            }
        return render(request, self.template_name, context)

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html"

    # get method
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context = {
                'object' : obj
            }
        return render(request, self.template_name, context)
    
    # post method
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context = {
                'object' : None
            }
            return redirect('/course/')
        return render(request, self.template_name, context)



# HTTP method
def my_fbv(request, *args, **kwargs):
    return render(request, "about.html", {})