# Create your views here.
from games.tracker.models import *
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms

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

@login_required
def add_unlockable(request):
    return render_to_response("tracker/new-unlockable.html", {
        "formset": PartialUnlockableForm
        },
        context_instance=RequestContext(request),
    )

@login_required
def save_unlockable(request):
    try:
        new_unlockable = PartialUnlockableForm(request.POST)
        if new_unlockable.is_valid():
            new_unlockable.save()
            name = unicode(new_unlockable.cleaned_data['name'])
            message = unicode("Unlockable \"{0:>s}\" was added successfully!".format(name))
            return render_to_response("tracker/new-unlockable.html", {
                "formset": PartialUnlockableForm,
                "message": message,
                "status": "success"
            },
            context_instance=RequestContext(request),
            )
        else:
            message = unicode("Invalid form data.")
            return render_to_response("tracker/new-unlockable.html", {
                    "formset": PartialUnlockableForm,
                    "message": message,
                    "status": "error"
                },
                context_instance=RequestContext(request),
            )
    except ():
        message = unicode("Error adding unlockable.")
        return render_to_response("tracker/new-unlockable.html", {
                "formset": PartialUnlockableForm,
                "message": message,
                "status": "error"
            },
            context_instance=RequestContext(request),
            )

def leaderboard(request):
    members = Member.objects.all().order_by("-score")[:25]
    param_dictionary = {"members": members}
    return render_to_response("tracker/leaderboard.html",
                              param_dictionary,
                              context_instance=(RequestContext(request)))

def list_feats(request):
    #feats = Unlockable.objects.filter(type=u'feat')
    #unlockables = Unlockable.objects.filter(is_public=True)
    unlockables = Unlockable.objects.all
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

def mass_achievement_unlock(request):
    if request.method == 'POST':
        formset = MassAchievementUnlockForm(request.POST)
        if formset.is_valid():
            selected_unlockable = formset.cleaned_data['unlockable']
            members = formset.cleaned_data['members']
            for member in members:
                try:
                    new_unlocked = Unlocked(member=member, unlockable=selected_unlockable)
                    new_unlocked.save()
                except:
                    message = unicode("Error saving {0:>s}".format(new_unlocked))
                    return render_to_response("tracker/mass-unlock.html", {
                                "formset": MassAchievementUnlockForm,
                                "message": message,
                                "status": "error"
                                },
                                context_instance=RequestContext(request))
            return HttpResponseRedirect("/tracker/success/")
    else:
        formset = MassAchievementUnlockForm()

    return render(request, "tracker/mass-unlock.html", {
        'formset': formset,
    })

def success(request):
    return render_to_response("tracker/success.html",
                                {"message": "good job",
                                 "status": "success"},
                                context_instance=RequestContext(request))

class MassAchievementUnlockForm(forms.Form):
    unlockable = forms.ModelChoiceField(queryset=Unlockable.objects.all())
    members = forms.ModelMultipleChoiceField(queryset=Member.objects.all())