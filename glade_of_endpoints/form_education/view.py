from aiohttp import web

from aiohttp.web_request import Request

from glade_of_endpoints import helpers


class FormEducationCountStudentHandler(web.View):
    """Class-based handler for get count of course by name of form education. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return group name by course and name of qualification. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT formeducation.NameForm, COUNT(group_s.Course) AS 'count_group' FROM `formeducation` JOIN " \
                  "`group_s` ON(group_s.IdFormEducation = formeducation.ID) GROUP BY group_s.Course"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result
