import aiomysql

async def create_db_pool():
    return await aiomysql.create_pool(
        host="localhost",
        user="root",
        password="0000",
        port=3306,
        db="ssl",
        charset="utf8",
        minsize=1,
        maxsize=5,
    )

async def close_db_pool(pool):
    pool.close()
    await pool.wait_closed()

async def pool_query(pool, query, *args):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.cursors.DictCursor) as cursor:
            await cursor.execute(query, args)
            await conn.commit()
            return await cursor.fetchall()
