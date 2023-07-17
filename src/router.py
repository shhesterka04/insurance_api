from fastapi import APIRouter
from starlette import status

insurance_router = APIRouter(
    prefix="",
    tags=["Insurance"]
)


# post запрос тарифов в БД
# get запрос из бд актуального тарифа и стоимости страховки

@insurance_router.get(
    "/test",
    name="wtf",
    status_code=status.HTTP_200_OK
)
def hello():
    return "Hello!"


@insurance_router.post(
    "/update_tariff",
    name="Update tariff",
    status_code=status.HTTP_200_OK
)
def update_rates():
    # получаем через пост запрос json и загружаем его в БД
    pass


@insurance_router.get(
    "/get_tariff",
    name="Tariff calculation",
    status_code=status.HTTP_200_OK
)
def get_tariff(cargo_type: str, date: str, price: str) -> str:
    # делаем селет по дате и типу, получаем ставку, перемножаем с price и возвращаем
    pass

