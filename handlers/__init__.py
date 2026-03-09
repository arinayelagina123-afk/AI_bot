from aiogram import Router
from handlers.commands_handler import router as commands_router
from handlers.random_fact import router as random_facts_router
from handlers.gpt_chat import router as gpt_chats_router
from handlers.talk import router as talk_router
from handlers.quiz import router as quiz_router
from handlers.translate import router as translate_router
from handlers.Recommendation import router as recommendation_router

router = Router()

router.include_routers(recommendation_router, translate_router
                       , quiz_router, talk_router, random_facts_router,
                       gpt_chats_router, commands_router)
