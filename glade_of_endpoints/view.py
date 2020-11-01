from aiohttp import web

from aiohttp.web_request import Request

from glade_of_endpoints import helpers


class AllHandler(web.View):
    """Class-based handler for get all from database. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return all from database. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT * FROM `group_s` JOIN `formeducation` ON (group_s.IdFormEducation = formeducation.id) " \
                  "JOIN `speciality` ON (group_s.IdSpeciality = speciality.ID) JOIN `qualification` " \
                  "ON (group_s.IdQualification = qualification.ID)"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result
