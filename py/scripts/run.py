import asyncio
import uuid

from app.db import AsyncSessionLocal
from app.models import User


async def create_user() -> User:
    async with AsyncSessionLocal() as session:
        # Create a new User instance.
        new_user = User(
            id=str(uuid.uuid4()),
            name="nikiv",  # Corresponds to the "username" in your TS snippet.
            email="nikita@nikiv.dev",
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)  # Refresh to load any DB-generated defaults.
        print("Created user:", new_user)
        return new_user


async def main() -> None:
    await create_user()


if __name__ == "__main__":
    asyncio.run(main())
    print("done")
