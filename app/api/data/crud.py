#from sqlalchemy import select
#from sqlalchemy.ext.asyncio import AsyncSession
#from app.api.data.models import Cocktail
#from models import Cocktail

#async def get_cocktail(session: AsyncSession, cocktail_id: int):
#    statement = select(Cocktail).where(Cocktail.id == cocktail_id)
#    result = await session.execute(statement)
#    return result.scalar_one_or_none()
