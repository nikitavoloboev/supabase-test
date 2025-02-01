import asyncio
import uuid

from app.db import AsyncSessionLocal
from app.schema import User


async def create_user() -> User:
    async with AsyncSessionLocal() as session:
        new_user = User(
            id=str(uuid.uuid4()),
            name="nikiv",
            email="nikita@nikiv.dev",
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        print("Created user:", new_user)
        return new_user


async def main() -> None:
    await create_user()


if __name__ == "__main__":
    asyncio.run(main())
    print("done")
