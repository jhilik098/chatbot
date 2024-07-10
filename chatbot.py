{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "20cec14e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name '_name_' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 35\u001b[0m\n\u001b[0;32m     32\u001b[0m             \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m     33\u001b[0m                 \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mChatBot: I\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mm sorry, I didn\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt understand that.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 35\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[43m_name_\u001b[49m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m_main_\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m     36\u001b[0m     bot \u001b[38;5;241m=\u001b[39m SimpleChatBot()\n\u001b[0;32m     37\u001b[0m     bot\u001b[38;5;241m.\u001b[39mstart_chat()\n",
      "\u001b[1;31mNameError\u001b[0m: name '_name_' is not defined"
     ]
    }
   ],
   "source": [
    "import re\n",
    "import random\n",
    "import nltk\n",
    "from nltk.chat.util import Chat, reflections\n",
    "\n",
    "class SimpleChatBot:\n",
    "    def _init_(self):\n",
    "        self.pairs = [\n",
    "            (r\"hi|hello|hey\", [\"Hello!\", \"Hi there!\", \"Hey!\"]),\n",
    "            (r\"how are you?\", [\"I'm a bot, I'm always good.\", \"Doing great!\"]),\n",
    "            (r\"what is your name?\", [\"I am a chatbot created by you.\", \"You can call me ChatBot.\"]),\n",
    "            (r\"bye|goodbye|see you\", [\"Goodbye!\", \"See you later!\", \"Bye!\"]),\n",
    "            (r\"what can you do?\", [\"I can chat with you.\", \"I can respond to your queries.\", \"I am here to keep you company.\"]),\n",
    "            (r\"how old are you?\", [\"I am ageless.\", \"I exist beyond the realm of time.\"]),\n",
    "            (r\"who created you?\", [\"I was created by a programmer.\", \"A human like you made me.\"]),\n",
    "            (r\"i need (.*)\", [\"Why do you need %1?\", \"Are you sure you need %1?\", \"It might be good to have %1.\"]),\n",
    "            (r\"i want (.*)\", [\"Why do you want %1?\", \"What would you do with %1?\", \"Are you sure you want %1?\"]),\n",
    "            (r\"quit\", [\"Bye-bye, take care!\", \"It was nice talking to you. Goodbye!\"]),\n",
    "        ]\n",
    "        self.chatbot = Chat(self.pairs, reflections)\n",
    "\n",
    "    def start_chat(self):\n",
    "        print(\"Hi, I'm a simple chatbot. Type 'quit' to exit.\")\n",
    "        while True:\n",
    "            user_input = input(\"You: \")\n",
    "            if user_input.lower() == 'quit':\n",
    "                print(\"ChatBot: Goodbye!\")\n",
    "                break\n",
    "            response = self.chatbot.respond(user_input)\n",
    "            if response:\n",
    "                print(f\"ChatBot: {response}\")\n",
    "            else:\n",
    "                print(\"ChatBot: I'm sorry, I didn't understand that.\")\n",
    "\n",
    "if _name_ == \"_main_\":\n",
    "    bot = SimpleChatBot()\n",
    "    bot.start_chat()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b62e922",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
