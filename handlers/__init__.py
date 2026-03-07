from aiogram import Router
from handlers.commands_handler import router as commands_router
from  handlers.random_fact import router as random_facts_router
from handlers.gpt_chat import router as gpt_chats_router
router = Router()

router.include_routers(random_facts_router,gpt_chats_router,commands_router)