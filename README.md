# Pi Discord Bot
## How to create a simple Discord Bot on a Raspberry Pi using Python

---

## 1.Create the bot
Go to <a href="https://discord.com/developers/applications">discord.com/developers/applications</a> and create the bot. After that, invite your bot to your server.

## 2.Update your pi
In the terminal, type:
```bash
sudo apt update
sudo apt upgrade
```

## 3.Make sure you have the following packages installed
In the terminal, type:
```bash
sudo apt install python3-pip python3-cffi git
```

## 4.Install discord.py
In the terminal, type:
```bash
sudo pip3 install discord.py
```

## 5.Get the bot code
In the terminal, type:
```bash
git clone https://github.com/GamerCristi11/Pi-Discord-Bot.git
```

## 6.Modify the code
In the terminal, type:
```bash
cd Pi-Discord-Bot
nano discordbot.py
```
After that, in the code, replace "bot_token" with your actual bot token from the discord developer protal. After that, save the code.

## 7.Run the code
In the terminal, type:
```bash
python3 discordbot.py
```

## 8.Test the bot
On discord, in the server with the bot, type:
```bash
!Hello
```
