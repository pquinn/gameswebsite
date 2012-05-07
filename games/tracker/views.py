# Create your views here.
from games.tracker.models import *
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext

def add_member(request):
#    #MemberFormSet = modelformset_factory(Member)
#    if request.method == 'POST':
#        #formset = MemberFormSet(request.POST, request.FILES)
#        if formset.is_valid():
#            formset.save()
#    else:
#        formset = MemberFormSet()
    return render_to_response("newmember.html", {
        "formset": MemberForm
        },
        context_instance=RequestContext(request),
    )