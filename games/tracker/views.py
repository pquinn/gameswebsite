# Create your views here.
from games.tracker.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def add_member(request):
    return render_to_response("newmember.html", {
        "formset": PartialMemberForm
        },
        context_instance=RequestContext(request),
    )

def save_member(request):
    try:
        new_member = PartialMemberForm(request.POST)
        if new_member.is_valid():
            new_member.save()
            #todo: figure out how to get name...
            message = unicode("Member was added successfully!")
            return render_to_response("newmember.html", {
                "formset": PartialMemberForm,
                "message": message,
                "status": "success"
            },
            context_instance=RequestContext(request),
            )
    except ():
        message = unicode("Error adding user.")
        return render_to_response("newmember.html", {
                "formset": PartialMemberForm,
                "message": message,
                "status": "error"
            },
            context_instance=RequestContext(request),
            )