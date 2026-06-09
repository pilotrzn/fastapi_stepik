from pydantic import BaseModel, Field, EmailStr, PositiveInt, NonNegativeInt, SecretStr
from typing import Annotated
from decimal import Decimal
from datetime import datetime


class User(BaseModel):
    username: Annotated[
        str,
        Field(
            ...,
            min_length=5,
            max_length=20,
            description="Пользовательское имя, от 5 до 20 символов",
        ),
    ]
    password: Annotated[
        SecretStr,
        Field(
            ..., min_length=8, max_length=50, description="Пароль, от 8 до 50 символов"
        ),
    ]
    email: Annotated[EmailStr, Field(..., description="Электронная почта")]
    first_name: Annotated[
        str | None,
        Field(
            min_length=2,
            max_length=30,
            default=None,
            description="Имя, от 2 до 30 символов",
        ),
    ]
    last_name: Annotated[
        str | None,
        Field(
            min_length=2,
            max_length=30,
            default=None,
            description="Фамилия, от 2 до 30 символов",
        ),
    ]
    is_active: Annotated[
        bool, Field(default=True, description="Статус активности пользователя")
    ]
    is_staff: Annotated[
        bool, Field(default=False, description="Является служебным пользователем")
    ]
    is_superuser: Annotated[
        bool, Field(default=False, description="Является суперпользователем")
    ]
    date_joined: Annotated[
        datetime, Field(default_factory=datetime.now, description="Зарегистрирован")
    ]
    last_login: Annotated[
        datetime | None, Field(default=None, description="Последнее посещение")
    ]


class Post(BaseModel):
    author_id: Annotated[PositiveInt, Field(..., description="Идентификатор автора")]
    title: Annotated[
        str,
        Field(
            ..., max_length=100, description="Заголовок записи, не более 100 символов"
        ),
    ]
    description: Annotated[
        str | None,
        Field(
            max_length=250,
            default=None,
            description="Описание записи, не более 250 символов",
        ),
    ]
    content: Annotated[str, Field(..., description="Контент записи")]
    created_at: Annotated[
        datetime, Field(default_factory=datetime.now, description="Запись создана")
    ]
    updated_at: Annotated[
        datetime | None, Field(default=None, description="Запись обновлена")
    ]
    is_published: Annotated[
        bool, Field(default=False, description="Запись опубликована")
    ]
    tags: Annotated[list[str], Field(default=[], description="Теги записи")]


class Product(BaseModel):
    product_slug: Annotated[
        str,
        Field(
            ...,
            min_length=3,
            max_length=120,
            pattern=r"^[A-Za-z0-9_-]+$",
            description="Слаг продукта",
        ),
    ]
    name: Annotated[
        str, Field(..., min_length=3, max_length=100, description="Название продукта")
    ]
    price: Annotated[Decimal, Field(..., ge=0, description="Цена продукта")]
    stock: Annotated[
        NonNegativeInt, Field(default=0, description="Количество продукта на складе")
    ]


class Address(BaseModel):
    user_id: Annotated[
        PositiveInt, Field(..., description="Идентификатор пользователя")
    ]
    city: Annotated[str, Field(..., min_length=2, max_length=100, description="Город")]
    street: Annotated[
        str, Field(..., min_length=2, max_length=200, description="Улица")
    ]
    postal_code: Annotated[
        PositiveInt, Field(..., ge=101000, le=999999, description="Почтовый индекс")
    ]


class Order(BaseModel):
    order_id: Annotated[
        PositiveInt, Field(..., gt=0, description="Уникальный идентификатор заказа")
    ]
    user_id: Annotated[
        PositiveInt,
        Field(..., gt=0, description="Идентификатор пользователя, сделавшего заказ"),
    ]
    total_amount: Annotated[Decimal, Field(..., ge=0, description="Общая сумма заказа")]
    created_at: Annotated[
        datetime, Field(..., description="Дата и время создания заказа")
    ]


class Task(BaseModel):
    title: Annotated[
        str, Field(min_length=1, max_length=100, description="Название задачи")
    ]
    description: Annotated[
        str | None, Field(max_length=500, default=None, description="Описание задачи")
    ]
    is_completed: Annotated[
        bool | None, Field(default=False, description="Статус завершения задачи")
    ]
