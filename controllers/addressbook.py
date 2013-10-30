# -*- coding: utf-8 -*-

def index():

	#             where       select (nix = *)
	return dict(data=db(db.contacts.id > 0).select())