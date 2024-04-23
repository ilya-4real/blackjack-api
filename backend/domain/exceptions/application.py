from dataclasses import dataclass


@dataclass
class ApplicationException(Exception):
    msg: str

    @property
    def message(self) -> str:
        return self.msg
