import html
import random
import SaitamaRobot.modules.gbam_strings as gban_strings
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


@run_async
def gbam(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(gbam_strings.GBAM_REASON))
   


GBAM_REASON_HANDLER = DisableAbleCommandHandler("gbam", gbam)

dispatcher.add_handler(GBAM_HANDLER)
