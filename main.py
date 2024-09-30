# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 

# bot.py

import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatInviteLink
from config import api_id, api_hash, bot_token, channel_id  # Import credentials

app = Client("join_request_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_chat_join_request()
async def join_request_handler(client, message):
    user = message.from_user
    chat = message.chat

    # Ensure that the join request is from the correct channel
    if chat.id == channel_id:
        welcome_message = f"👋 Welcome, {user.first_name}! Your join request is noted. Please wait for admin approval."

        # Send the message to the user via a private message
        try:
            await client.send_message(chat_id=user.id, text=welcome_message)
        except:
            # Handle the case where the bot can't send messages to the user
            print(f"Could not send welcome message to {user.first_name} ({user.id})")

        # Log the event
        print(f"Join request from {user.first_name} ({user.id}) for channel {chat.title} was not approved.")

# Run the bot
app.run()

# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 
