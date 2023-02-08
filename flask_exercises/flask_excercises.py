from flask import Flask, request, jsonify
from http import HTTPStatus
from typing import Any, DefaultDict

users = DefaultDict[str, dict]()


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.route("/user/<name>", methods=["GET"])
        def get(name: str) -> Any:
            if name in users.keys():
                response = jsonify({"data": f"My name is {name}"}), HTTPStatus.OK
                return response
            return jsonify(HTTPStatus.NOT_FOUND), HTTPStatus.NOT_FOUND

        @app.route("/user", methods=["POST"])
        def post() -> Any:
            body = request.json
            if "name" not in body.keys():
                response = (
                    jsonify({"errors": {"name": "This field is required"}}),
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )
                return response
            users.update({body["name"]: {}})
            return jsonify({"data": f"User {body.get('name')} is created!"}), HTTPStatus.CREATED

        @app.route("/user/<name>", methods=["PATCH"])
        def patch(name: str) -> Any:
            body = request.json
            new_name = body["name"]
            if name in users.keys():
                users[new_name] = users.pop(name)
                return jsonify({"data": f"My name is {new_name}"}), HTTPStatus.OK
            return jsonify(HTTPStatus.NO_CONTENT)

        @app.route("/user/<name>", methods=["DELETE"])
        def delete(name: str) -> Any:
            if name in users.keys():
                users.pop(name)
            return f"{HTTPStatus.NO_CONTENT}", HTTPStatus.NO_CONTENT
