# Glade of endpoints

Glade of endpoints is server written on aiohttp and provides endpoint for get requests.

## API

### Group

* **URI:** `/get/group/count/`
* **Method:** `GET`
* **Success Response**
  * **Code:** 200
    * **Content:** `{"count": "<count>"}`, where
      * `<count>` is the count of student
* **Error Responses**
  * **Code:** 404
    * **Content:** None
