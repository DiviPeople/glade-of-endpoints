from aiohttp import web

from aiohttp.web_request import Request

from glade_of_endpoints import helpers


class GroupNameHandler(web.View):
    """Class-based handler for get group name. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']
        self._course = None

    async def get(self):
        """Return group name by course and name of qualification. """

        if 'course' in self.request.query:
            self._course = self.request.query['course']
        else:
            return web.StreamResponse(status=400)

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT group_s.name FROM `group_s`, `qualification` WHERE group_s.Course = %s and " \
                  "qualification.NameQualification = 'бакалавр' "
            cursor.execute(sql, str(self._course))
            result = cursor.fetchall()

        return result


class GroupFacultyHandler(web.View):
    """Class-based handler for get faculty name. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return faculty where speciality profile is math. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT group_s.Faculty FROM `group_s`, `speciality` WHERE speciality.Profile = 'математика' " \
                  "and group_s.IdSpeciality = speciality.ID and speciality.ID = group_s.ID"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result


class GroupCountStudentHandler(web.View):
    """Class-based handler for get count of student. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']
        self._count_subgroup = None

    async def get(self):
        """Return count of student where name of form education is full-time
        and by count of subgroup. """

        if 'count_subgroup' in self.request.query:
            self._count_subgroup = self.request.query['count_subgroup']
        else:
            return web.StreamResponse(status=400)

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT group_s.CountStudent from `group_s`, `formeducation` WHERE group_s.CountSubgroup > %s " \
                  "and formeducation.NameForm = 'очное' and group_s.IdFormEducation = formeducation.ID " \
                  "AND formeducation.ID = group_s.IdFormEducation"
            cursor.execute(sql, str(self._count_subgroup))
            result = cursor.fetchall()

        return result


class GroupSubgroupHandler(web.View):
    """Class-based handler for get count subgroup. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']
        self._name_form_education = None

    async def get(self):
        """Return count subgroup by name of form education. """

        if 'name_form_education' in self.request.query:
            self._name_form_education = self.request.query['name_form_education']
        else:
            return web.StreamResponse(status=400)

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT group_s.CountSubgroup from `group_s`, `speciality`, `formeducation` WHERE " \
                  "formeducation.NameForm = %s and speciality.NameSpeciality = 'Математика и механика' " \
                  "and group_s.IdSpeciality = speciality.id and group_s.IdFormEducation = formeducation.ID and " \
                  "speciality.id = group_s.IdSpeciality and formeducation.id = group_s.IdFormEducation"
            cursor.execute(sql, str(self._name_form_education))
            result = cursor.fetchall()

        return result


class GroupCountStudentByFacultyHandler(web.View):
    """Class-based handler for get count subgroup. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return count of students by faculty and with name of form education is full-time. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT group_s.Faculty, SUM(group_s.CountStudent) FROM `group_s`, `formeducation` WHERE " \
                  "formeducation.NameForm = 'очное' and group_s.IdFormEducation = formeducation.ID GROUP BY " \
                  "group_s.Faculty"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result


class CountGroupHandler(web.View):
    """Class-based handler for get count of group. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return count of group by count of students and name of speciality. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "SELECT COUNT(*) AS 'count' FROM `group_s` JOIN `speciality` ON " \
                  "(group_s.IdSpeciality = speciality.ID) WHERE group_s.CountStudent IN (20, 35) and " \
                  "speciality.NameSpeciality = 'Математика и механика'"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result


class GroupUnionHandler(web.View):
    """Class-based handler for get result of union. """

    def __init__(self, request: Request):
        super().__init__(request)

        self._connection = request.app['connection']

    async def get(self):
        """Return result of union query. """

        data = self._sql_query()
        if data:
            return web.json_response(data, dumps=helpers.json_dumbs_ascii)

        return web.StreamResponse(status=404)

    def _sql_query(self):
        """Return the query result to database. """

        with self._connection.cursor() as cursor:
            sql = "(SELECT * FROM `group_s` WHERE group_s.Course > 1) UNION (SELECT * FROM " \
                  "`group_s` WHERE group_s.Name LIKE '%Ж')"
            cursor.execute(sql)
            result = cursor.fetchall()

        return result
