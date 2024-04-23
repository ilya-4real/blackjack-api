from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

VT = TypeVar("VT", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError

    def __post_init__(self) -> None:
        self.validate()

    def as_value_type(self) -> VT:
        return self.value
