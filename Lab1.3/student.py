from dataclasses import asdict, dataclass, field
from enum import Enum
from hashlib import sha256
from typing import Any


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


@dataclass
class Student:
    name: str
    surname: str
    course: int
    residence: str
    gender: Gender = field(compare=True)
    student_id: int = field(default=0, repr=False)

    def _attributes_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d.pop("student_id", None)
        return d

    def compute_hash(self) -> int:
        attrs = self._attributes_dict()
        sha_code = sha256(str(attrs).encode("utf-8")).hexdigest()
        digest_int = int(sha_code, 16)
        return digest_int

    def __post_init__(self) -> None:
        if isinstance(self.gender, str):
            self.gender = Gender(self.gender.lower())

        if not self.student_id:
            self.student_id = self.compute_hash()
