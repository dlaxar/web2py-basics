# -*- coding: utf-8 -*-

def index():

	data = None
	# wenn parameter -> zeig nur den kontakt an
	if len(request.args) > 0:
		data = db(db.contacts.id == request.args[0]).select()
	
	# wenn kein parameter -> Liste
	else:
		data = db(db.contacts.id > 0).select()

	return dict(data=data)


# def display_form():
#    form = SQLFORM(db.person)
#    if form.process().accepted:
#        response.flash = 'form accepted'
#    elif form.errors:
#        response.flash = 'form has errors'
#    else:
#        response.flash = 'please fill out the form'
#    return dict(form=form)

def add():
	form = SQLFORM(db.contacts)

	if form.process().accepted:
		response.flash = "Your data has been accepted, Master!"
	elif form.errors:
		response.flash = "I'm afraid something went wrong, Master!"
	else:
		response.flash = "You want to add contacts? Sure, Master!"

	return dict(form=form)














