from aiogram import Bot, Dispatcher, types, executor
from buttons import button
from apiii import create_user, create_feedback
from states import FeedbackState
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from environs import Env

env = Env()
env.read_env()
TOKEN = env("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def send_welcome(msg: types.Message):
    print(msg.from_user.id)
    await msg.reply(
        "Assalomu aleykum .\nmuloqot botiga xush kelibsiz !.",
        reply_markup=button,
    )
    create_user(msg.from_user.username, msg.from_user.full_name, msg.from_user.id)
    await bot.send_message(
        chat_id="-1001946414925",
        text=f"Username: @{msg.from_user.username}\nFull name: {msg.from_user.full_name}\nUser id: {msg.from_user.id}",
    )


@dp.message_handler(Text(startswith="Xabar qodirish ✍️"))
async def feedback_1(message: types.Message):
    await message.answer("Xabar matnini yuboring")
    await FeedbackState.body.set()


@dp.message_handler(state=FeedbackState.body)
async def feedback_2(message: types.Message, state: FSMContext):
    await message.answer(create_feedback(message.from_user.id, message.text))
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
