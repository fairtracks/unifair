from typing import Any, List, Optional, Type

from pydantic import BaseModel, PrivateAttr, validate_model


class OnlyTypedMixin:
    _types_provided: bool = PrivateAttr(default=False)

    def __class_getitem__(cls, model: Type[Any]) -> Type[Any]:
        cls._types_provided = True
        return super().__class_getitem__(model)

    # def __init_subclass__(cls, req_field_names: List[str], **kwargs):  # noqa
    # def __init_subclass__(cls, **kwargs):  # noqa
    #     super().__init_subclass__(**kwargs)
    # cls.check_types_provided()

    # def __new__(cls, *args, req_field_names: List[str], **kwargs) -> Any:
    def __new__(cls, **kwargs) -> Any:
        cls.check_types_provided()
        cls._types_provided = False
        return super().__new__(cls, **kwargs)

    @classmethod
    # def check_required_fields_in_model(cls, req_field_names: List[str]):
    def check_types_provided(cls):
        print(cls.__fields__)
        print(cls.__annotations__)
        print(cls.__dict__.get('__root__'))
        print(cls.__dict__)
        # for req_field_name in req_field_names:
        #     if req_field_name not in cls.__annotations__:
        if not cls._types_provided:
            raise TypeError(
                'Subclasses of {} are required to specify the model in '.format(cls.__name__)
                + 'the class definition, e.g.: '
                '"class MyNumberList(DatasetModel[List[int]]): pass"')


def validate(model: BaseModel):
    *_, validation_error = validate_model(model.__class__, model.__dict__)
    if validation_error:
        raise validation_error
