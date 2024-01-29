from typing import Optional, Literal
from logging import debug

from aiohttp import ClientSession

from exception import InputSessionException


class MeshClient:
    def __init__(
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
                    "X-Mes-Role": "student"  # now only students support
                }
            )
        else:
            if not session.headers.get("Authorization") or not session.headers.get("Auth-token") \
                    or not session.headers.get("X-mes-subsystem") or session.headers.get("X-mes-role"):
                raise InputSessionException("Not enough headers for mesh work")
            self._session = session
        self._token = token
        self._baseurl = "https://ms-edu.tatar.ru"

    async def request(self, version: Literal["v3", "v1"], method: str, *args, **kwargs):
        ...
