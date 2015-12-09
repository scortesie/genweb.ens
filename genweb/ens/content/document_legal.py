# -*- coding: utf-8 -*-
from plone.directives import form
from plone.namedfile.field import NamedBlobFile
from zope import schema

from genweb.ens import _


class IDocumentLegal(form.Schema):
    """
    Document legal
    """

    title = schema.TextLine(
        title=_(u"Títol"),
        required=True
    )

    description = schema.Text(
        title=_(u"Descripció"),
        required=False)

    data = schema.Date(
        title=_(u"Data"),
        required=False)

    fitxer = NamedBlobFile(
        title=_(u"Fitxer"),
        description=_(u"Puja un fitxer"),
        required=True)
