from typing import final

from project.libs.user.domain.properties import UserId
from project.libs.user.domain.repositories import UserRepository


@final
class UserDeleterService:
    __slots__ = '_repository'

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    async def __call__(self, user_id: UserId) -> None:
        user = await self._repository.find(user_id)
        user.delete()
        await self._repository.delete_and_publish(user)
