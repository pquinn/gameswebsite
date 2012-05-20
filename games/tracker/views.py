# Create your views here.
from games.tracker.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

#not sure why a request context is required here...
@login_required
def add_member(request):
    return render_to_response("tracker/new-member.html", {
        "formset": PartialMemberForm
        },
        context_instance=RequestContext(request),
    )

#change return to HttpResponseRedirect
@login_required
def save_member(request):
    try:
        new_member = PartialMemberForm(request.POST)
        if new_member.is_valid():
            new_member.save()
            name = unicode(new_member.cleaned_data['tag'])
            message = unicode("Member {0:>s} was added successfully!".format(name))
            return render_to_response("tracker/new-member.html", {
                "formset": PartialMemberForm,
                "message": message,
                "status": "success"
            },
            context_instance=RequestContext(request),
            )
        else:
            message = unicode("Invalid form data.")
            return render_to_response("tracker/new-member.html", {
                    "formset": PartialMemberForm,
                    "message": message,
                    "status": "error"
                },
                context_instance=RequestContext(request),
            )
    except ():
        message = unicode("Error adding user.")
        return render_to_response("tracker/new-member.html", {
                "formset": PartialMemberForm,
                "message": message,
                "status": "error"
            },
            context_instance=RequestContext(request),
            )

def leaderboard(request):
    members = Member.objects.all().order_by("-score")
    param_dictionary = {"members": members}
    return render_to_response("tracker/leaderboard.html",
                              param_dictionary,
                              context_instance=(RequestContext(request)))

def list_feats(request):
    #feats = Unlockable.objects.filter(type=u'feat')
    unlockables = Unlockable.objects.all()
    param_dictionary = {"unlockables": unlockables}
    return render_to_response("tracker/unlockable-list.html",
                              param_dictionary,
                              context_instance=(RequestContext(request)))

def unlockable_detail(request, unlockable_id):
    unlockable = get_object_or_404(Unlockable, pk=unlockable_id)
    param_dictionary = {"unlockable": unlockable}
    return render_to_response("tracker/unlockable-detail.html",
                                param_dictionary,
                                context_instance=(RequestContext(request)))