from typing import List, Literal, Any

from .base_types import Subsystem


class UserRole:
    """User's role"""
    id: int
    "Role ID"

    title: str
    "Display title"

    subsystems: List[Subsystem]
    "Available for using subsystems"


class UserInfo:
    """Base class for user personal data
    """
    birthday: str # reformat to datetime.datetime
    "user's birthday"

    mail: str = None
    "user's email"

    gender: Literal["M", "F"]
    "user's gender"

    trusted: bool = True
    "idk"

    FirstName: str
    "user's first name"

    mobile: str = None
    "user's mobile phone"

    guid: int = None # may be None because user can sign in with login-password
    "user's Gosuslugi ID"

    failed: bool = False
    "idk"

    LastName: str
    "User's last name"

    error: Any = None # idk what error can be happen
    "idk"

    MiddleName: str
    "User's middle name"

    snils: str
    "User's snils"

    # for pep8 and good development expirence
    # first_name = FirstName
    # middle_name = MiddleName
    # LastName = LastName

    def __init__(
            self,
            birthday: str,
            gender: Literal["M", "F"],
            trusted: bool,
            FirstName: str,
            LastName: str,
            MiddleName: str,
            snils: str,
            mobile: str = None,
            guid: bool = None,
            failed: bool = False,
            error: Any = None
    ) -> None:
        super().__init__(
            birthday=birthday,
            gender=gender,
            trusted=trusted,
            FirstName=FirstName,
            LastName=LastName,
            MiddleName=MiddleName,
            snils=snils,
            mobile=mobile,
            guid=guid,
            failed=failed,
            error=error
        )


class UserV3:
    """Class for /v3/userinfo typing
    """
    userId: int
    "User ID"

    isAdActivated: bool = False
    "idk"

    info: UserInfo
    "User information. Personal data, be accurate"

    roles: List[UserRole]
    "User roles"

    savedChoise: bool = None
    notification: bool = True
    login: str = None
