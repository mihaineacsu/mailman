# Copyright (C) 2006-2015 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <http://www.gnu.org/licenses/>.

"""Model for languages."""

__all__ = [
    'Language',
    ]


from mailman.database.model import Model
from mailman.interfaces.languages import ILanguage
from sqlalchemy import Column, Integer, Unicode
from zope.interface import implementer



@implementer(ILanguage)
class Language(Model):
    """See `ILanguage`."""

    __tablename__ = 'language'

    id = Column(Integer, primary_key=True)
    code = Column(Unicode)