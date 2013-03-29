from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from games.lfg.models import Person, PersonForm

def index(request):
    people = Person.objects.all()
    param_dictionary = {"people" : people}
    return render_to_response("lfg/index.html",
                                param_dictionary,
                                context_instance=RequestContext(request))

def add_person(request):
    return render_to_response("lfg/add-person.html",
                              { "formset" : PersonForm()},
                              context_instance=RequestContext(request))

def save_person(request):
    try:
        new_person = PersonForm(request.POST)
        if new_person.is_valid():
            new_person.save()
            name = unicode(new_person.cleaned_data['first_name'])
            message = unicode("Person {0:>s} was added successfully!".format(name))
            return render_to_response("lfg/add-person.html", {
                "formset": PersonForm,
                "message": message,
                "status": "success"
            },
            context_instance=RequestContext(request),
            )
        else:
            message = unicode("Invalid form data.")
            return render_to_response("lfg/add-person.html", {
                    "formset": PersonForm,
                    "message": message,
                    "status": "error"
                },
                context_instance=RequestContext(request),
            )
    except ():
        message = unicode("Error adding user.")
        return render_to_response("lfg/add-person.html", {
                "formset": PersonForm,
                "message": message,
                "status": "error"
            },
            context_instance=RequestContext(request),
            )