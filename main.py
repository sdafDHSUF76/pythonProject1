import json
import random
from datetime import datetime
from typing import Optional

import uvicorn
from fastapi import FastAPI, Query

from schema_create_users import User
from schema_create_users import UserResponse as UserCreateResponse
from schema_get_users import UserResponse

app = FastAPI()


def _get_json(file_name: str) -> list[dict] | dict:
    """Получаем данные из json."""
    with open(file_name) as file:
        data: list[dict] | dict = json.load(file)
    return data


def _calculate_total_pages(total_users: int, per_page: int) -> int:
    """Вычисляем общее количество страниц."""
    return (total_users + per_page - 1) // per_page


def _get_start_and_end_index(page: int, per_page: int) -> (int, int):
    """Вычисляем начальный и конечный индекс для извлечения данные.

    По указанным page, per_page получаем нужные данные из users_data.
    """
    start_index: int = (page - 1) * per_page
    end_index: int = start_index + per_page
    return start_index, end_index


def _get_users_on_page(
    page: int,  per_page: int, total_pages: int, users_data: list[dict],
) -> list | list[dict]:
    """Получаем данные сущностей на странице по нашим page, и total_pages.

    Если page > общего количества страниц, то возвращаем [], если указанная страница входит в общее
    количество страниц, то выдаем данные по этой странице.
    """
    if page > total_pages:
        return []
    else:
        # Вычисляем индекс начала и конца для текущей страницы
        start_index, end_index = _get_start_and_end_index(page, per_page)
        return users_data[start_index:end_index]


@app.get("/api/users", response_model=UserResponse)
def get_users(
    page: Optional[int] = Query(None, ge=1, description="Page number"),
    per_page: Optional[int] = Query(None, ge=1, description="number of entities per page")
):
    """Ендпоинт для получения данных о юзерах.

    Есть вовзможность получения среза данных через page, per_page параметров в url-е.
    """
    users_data: list[dict] = _get_json('users_data.json')
    default_per_page = 6
    default_number_page = 1
    total_users = len(users_data)
    per_page: int = per_page if per_page else default_per_page
    page: int = page if page else default_number_page
    total_pages: int = _calculate_total_pages(total_users, per_page)
    users_on_page = _get_users_on_page(page, per_page, total_pages, users_data)
    support_data: dict = _get_json('support_data.json')

    return UserResponse(
        page=page,
        per_page=per_page,
        total=total_users,
        total_pages=total_pages,
        data=users_on_page,
        support=support_data
    )


@app.post("/api/users", response_model=UserCreateResponse, status_code=201)
async def post_create_users(request_payload: User):
    """Ендпоинт для создания данных о юзере.

    В теле запроса указываем name, job и юзер создается(точнее он дополняется к уже созданным
    юзерам) в данных user_data.json.
    """
    return UserCreateResponse(
        name=request_payload.name,
        job=request_payload.job,
        id=str(random.randint(100, 999)),
        createdAt=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)
