from asyncio import run
from typing import Optional

from aiohttp import ClientSession

from exception import InputSessionException
from mesh_types import UserV3, UserInfo, UserRole, Subsystem


class MeshClient:
    async def __init__(
            self,
            token: str,
            session: Optional[ClientSession] = None,
    ):
        """Base class for mesh library

        Args:
            token (str): user token
            session (Optional[ClientSession]): Session with your token. If not, creates automaticly
        """
        if not session:
            self._session = ClientSession(
                headers={
                    "Authorization": f"Bearer {token}",
                    "Auth-token": token,
                    "X-mes-subsystem": "familyweb",
                    "X-Mes-Role": "student" # now only students support
                }
            )
        else:
            if not session.headers.get("Authorization") or not session.headers.get("Auth-token") \
                or not session.headers.get("X-mes-subsystem") or session.headers.get("X-mes-role"):
                raise InputSessionException("Not enought headers for mesh work")
            self._session = session
        self._token = token
        self._baseurl = "https://ms-edu.tatar.ru"

    async def get_me(self) -> UserV3:
        """Get your profile by v3 version endpoints"""
        response = await self._session.get(self._baseurl + "/v3/userinfo")
        data = await response.data()
        data['info'] = UserInfo(**data['info'])
        data['roles'] = []
        for role in data['roles']:
            role['subsystems'] = [Subsystem(**ss) for ss in role['symsystems']]
            data['roles'].append(UserRole(**role))
        return UserV3(**data)
