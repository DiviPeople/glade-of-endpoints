import logging

import pymysql.cursors
from aiohttp import web

from glade_of_endpoints import config
from glade_of_endpoints.view import AllHandler
from glade_of_endpoints.group.view import (
    GroupNameHandler,
    GroupFacultyHandler,
    GroupCountStudentHandler,
    GroupSubgroupHandler,
    GroupCountStudentByFacultyHandler,
    CountGroupHandler,
    GroupUnionHandler,
)
from glade_of_endpoints.speciality.view import (
    SpecialityHandler,
    SpecialityProfileHandler,
    SpecialityNameHandler,
)
from glade_of_endpoints.form_education.view import FormEducationCountStudentHandler

logging.basicConfig(filename=config.LOG_PATH, level=logging.INFO)

routes = web.RouteTableDef()

connection = pymysql.connect(host=config.DB_HOST,
                             user=config.DB_USER,
                             password=config.DB_PASSWORD,
                             db=config.DB_NAME,
                             charset=config.DB_CHARSET,
                             cursorclass=pymysql.cursors.DictCursor)


async def main():
    """The main entry point. """

    app = web.Application(middlewares=[web.normalize_path_middleware()])
    app['connection'] = connection

    app.router.add_get('/get/all/', AllHandler)

    app.router.add_get('/get/group/count/', CountGroupHandler)
    app.router.add_get('/get/group/name/', GroupNameHandler)
    app.router.add_get('/get/group/faculty/', GroupFacultyHandler)
    app.router.add_get('/get/group/count-students/', GroupCountStudentHandler)
    app.router.add_get('/get/group/count-students-by-faculty/', GroupCountStudentByFacultyHandler)
    app.router.add_get('/get/group/count-subgroup/', GroupSubgroupHandler)
    app.router.add_get('/get/group/union/', GroupUnionHandler)

    app.router.add_get('/get/speciality/', SpecialityHandler)
    app.router.add_get('/get/speciality/profile/', SpecialityProfileHandler)
    app.router.add_get('/get/speciality/name/', SpecialityNameHandler)
    app.router.add_get('/get/form_education/count-student/', FormEducationCountStudentHandler)

    return app

if __name__ == '__main__':
    web.run_app(main(), host=config.HOST, port=config.PORT)
    connection.close()
