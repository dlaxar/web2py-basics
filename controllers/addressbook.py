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
	# weißenböck = badass
	# 
	# request.vars.get('p') => http://..../add.html?p=something
	# wenn p nicht angegeben wird => None
	form = SQLFORM(db.contacts, request.vars.get('p'))

	# diese methode wird 2x aufgerufen
	# 1) um das formular anzuzeigen
	# 2) um das formular zu verarbeiten -> form.process() wird aufgerufen

	if form.process().accepted:
		response.flash = "Your data has been accepted, Master!"
	elif form.errors:
		response.flash = "I'm afraid something went wrong, Master!"
	else:
		response.flash = "You want to add contacts? Sure, Master!"

	return dict(form=form)













