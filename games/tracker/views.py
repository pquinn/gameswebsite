# Create your views here.
from games.tracker.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def add_member(request):
    return render_to_response("newmember.html", {
        "formset": PartialMemberForm
        },
        context_instance=RequestContext(request),
    )

@login_required
def save_member(request):
    try:
        new_member = PartialMemberForm(request.POST)
        if new_member.is_valid():
            new_member.save()
            name = unicode(new_member.cleaned_data['tag'])
            message = unicode("Member {0:>s} was added successfully!".format(name))
            return render_to_response("newmember.html", {
                "formset": PartialMemberForm,
                "message": message,
                "status": "success"
            },
            context_instance=RequestContext(request),
            )
        else:
            message = unicode("Invalid form data.")
        return render_to_response("newmember.html", {
                "formset": PartialMemberForm,
                "message": message,
                "status": "error"
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

def leaderboard(request):
    members = Member.objects.all().order_by("-score")
    param_dictionary = {"members": members}
    return render_to_response("leaderboard.html",
                              param_dictionary,
                              context_instance=(RequestContext(request)))