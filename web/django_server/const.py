import enum


class BaseEnum(enum.Enum):
    @classmethod
    def to_choice(cls):
        return [(tag.value, tag) for tag in cls]

    @classmethod
    def values(cls, excepts=[]):
        return [tag.value for tag in cls if tag not in excepts]

    @classmethod
    def of(cls, value):
        if value is None:
            return None

        for tag in cls:
            if tag.value == value:
                return tag
        return None


class SexEnum(BaseEnum):
    MALE = 'm'
    FEMALE = 'f'
