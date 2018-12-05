from enum import Enum


# pseudo-enum for the asset, shot, and whatever gets added
class BODY_TYPE(Enum):
    ASSET = "asset"
    SHOT = "shot"


class HISTORY_TYPES(Enum):
    CHECKOUT: "checkout"
    CREATE = "create"
    RENAME = "rename"
    REVERT = "revert"
    DELETE = "delete"
    RESTORE = "restore"
