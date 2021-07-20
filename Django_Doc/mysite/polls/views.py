from datetime import timezone
from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.http import  HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import  reverse
from .models import Question,Choice
from django.views import  generic
from django.utils import timezone
# function based View
#def index(request):
 #   return HttpResponse("Hello World; You are at poll index")

#def detail(request, question_id):
 #   question=get_object_or_404(Question,pk=question_id)
  #  return render(request,'polls/detail.html',{'question':question})
    

#def results(request,question_id):
 ##  return render(request,'polls/results.html',{'question':question})
    

def vote (request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
         return render(request,'polls/detail.html',{'question':question,'error_message':"you didn't select a choice"})
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,) ))

#def index(request):
 #   latest_question_list=Question.objects.order_by('-pub_date')[:5]
  #  template =loader.get_template('polls/index.html')
   # context={
    #    'latest_question_list':latest_question_list,
    #}
#    return HttpResponse(template.render(context,request))



# class based view

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        ## return laste 5 published question
        #return Question.objects.order_by('-pub_date')[:5]
        """
            Return the last five published questions (not including those set to be
            published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

