from aiogram import types, Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart

from aiohttp import web


TOKEN_API = '6677077782:AAEEiomVJtt1JnNntOjTjhR4_0pyoB1kzM0'
bot = Bot(token=TOKEN_API)

router = Router()
dp = Dispatcher()
app = web.Application()
dp.include_router(router)

webhook_path = f'/{TOKEN_API}'


async def set_webhook():
    webhook_uri = f'https://4952-109-126-178-119.ngrok-free.app{webhook_path}'
    await bot.set_webhook(webhook_uri)


async def on_startup(_):
    await set_webhook()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Бот вышел на связь!')


async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[index+1:]

    if token == TOKEN_API:
        request_data = await request.json()
        update = types.Update(request_data)

        await dp._process_update(update)
        return web.Response()
    else:
        web.Response(status=403)


app.router.add_post(f'/{TOKEN_API}', handle_webhook)


if __name__ == '__main__':
    app.on_startup.append(on_startup)

    web.run_app(
        app,
        host='0.0.0.0',
        port=8080,
    )
