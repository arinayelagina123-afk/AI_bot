from aiogram import Router
from handlers.commands_handler import router as commands_router
from  handlers.random_fact import router as random_facts_router
router = Router()

router.include_routers(random_facts_router,commands_router)