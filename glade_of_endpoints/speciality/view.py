from aiohttp import web

from aiohttp.web_request import Request

from glade_of_endpoints import helpers


class SpecialityHandler(web.View):
    """Class-based handler for get speciality. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return speciality by group name and faculty. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT DISTINCT speciality.NameSpeciality, speciality.Profile " \
                  "FROM `speciality`, `group_s` WHERE group_s.Name = 'ПАДЖ' " \
                  "and group_s.Faculty = 'географический' and speciality.ID = group_s.IdSpeciality " \
                  "and group_s.IdSpeciality = speciality.ID"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result


class SpecialityProfileHandler(web.View):
    """Class-based handler for get speciality profile. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return speciality by group name and faculty. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT speciality.Profile FROM `speciality`, `group_s`, `qualification` WHERE " \
                  "qualification.NameQualification = 'бакалавр' and group_s.CountSubgroup > 3 and " \
                  "group_s.IdQualification = qualification.ID and qualification.ID = group_s.IdFormEducation " \
                  "and group_s.IdSpeciality = speciality.ID and speciality.ID = group_s.IdSpeciality"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result


class SpecialityNameHandler(web.View):
    """Class-based handler for get speciality name. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return speciality by name of form education and group name. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT speciality.NameSpeciality from `speciality`, `formeducation`, `group_s` WHERE " \
                  "formeducation.NameForm = 'заочное' and group_s.Name = 'ПМ' and " \
                  "formeducation.ID = group_s.IdFormEducation and group_s.IdFormEducation = formeducation.ID and " \
                  "group_s.IdSpeciality = speciality.ID and speciality.ID = group_s.IdSpeciality"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result
