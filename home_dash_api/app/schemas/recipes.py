import datetime as dt
from uuid import UUID

from app.models.recipes.category import CategorySchema
from app.models.user import UserRecipeSchema
from pydantic import BaseModel


class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


# class CategorySchema(CategoryBase):
#     id: UUID
#     created_at: dt.datetime
#     updated_at: dt.datetime
#
#     class Config:
#         orm_mode = True


class IngredientBase(BaseModel):
    ingredient_name: str


class IngredientCreate(IngredientBase):
    measurement: str
    measurement_qty: str


class IngredientSchema(IngredientBase):
    id: UUID
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        orm_mode = True


class MeasurementBase(BaseModel):
    measurement_name: str


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementSchema(MeasurementBase):
    id: UUID
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        orm_mode = True


class MeasurementQtyBase(BaseModel):
    measurement_qty_name: str


class MeasurementQtyCreate(MeasurementBase):
    pass


class MeasurementQtySchema(MeasurementBase):
    id: UUID
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        orm_mode = True

    class PydanticMeta:
        exclude = ("created_at", "updated_at")


class RecipeBase(BaseModel):
    name: str
    description: str
    image: str
    cooking_time: int
    prep_time: int
    servings: int
    notes: str


class CreateRecipe(RecipeBase):
    ingredients: list[IngredientCreate]
    categories: list[CategoryCreate]


class RecipeSchema(RecipeBase):
    id: UUID
    creator: UserRecipeSchema
    categories: list[CategorySchema]
    created_at: dt.datetime
    updated_at: dt.datetime

    class Config:
        orm_mode = True

    class PydanticMeta:
        exclude = ("created_at", "updated_at")


class RecipeIngredientBase(BaseModel):
    recipe: RecipeSchema
    ingredient: IngredientBase
    measurement: MeasurementBase
    measurement_qty: MeasurementQtyBase


class RecipeIngredientCreate(MeasurementBase):
    pass
