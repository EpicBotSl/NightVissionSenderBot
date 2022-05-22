# Channel Auto-Post Bot

<img src=https://te.legra.ph/file/4639ebcdc06761d31c9be.jpg>
This bot can send all new messages from one channel, directly to another channel (or group, just in case), without the forwarded tag!

## Setting up 
* First:
> `APP_ID` and `API_HASH` - Get it from my.telegram.org   
> `BOT_TOKEN` - Get it from [@BotFather](https://t.me/BotFather)   
> `OWNER_ID` - Telegram User id Of OWNER.
> `REDIS_URI` - Get This Value from [RedisLabs.](https://redislabs.com)
> `REDIS_PASS` - Redis Password.
> `START_MESSAGE (optional)` - If want to Change The Start Message.
> `FROM_CHANNEL` - The ID of the main channel from where posts have to be copied. 
> `TO_CHANNEL` - The ID of the channel to which the posts are to be sent. 
   
* Chose a platform to deploy on:
<details>
<summary>Heroku/Kintohub/Zeet</summary>
<br>
Add the above values to the environment vars and deploy the bot.
</details>
<details>
<summary>Local Deploys</summary>
<br>
- Clone the repo:   <code>git clone https://github.com/Captainamarica/NightVissionSenderBot</code></br>
- Make a <code>.env</code> file in the root of the repo, like <a href="https://github.com/Captainamarica/NightVissionSenderBot/blob/main/.env.sample">.env.sample</a> and fill in the values.</br>
- Use <code>python3 bot.py</code> to start the bot.</br>  
</details>

## Usage
Add the bot to both channels with admin permission, and thats it!
All new messages will be auto-posted!!

Visit [@NIGHT VISSION BOTS 🇱🇰](https://t.me/NightVission) for help.
## Credits
> [Lonami](https://github.com/LonamiWebs), for [Telethon](https://github.com/LonamiWebs/Telethon).   
> [NAVANJANA](https://github.com/Captainamarica), me.   
> [CONTACT](https://t.me/NA_VA_N_JA_NA1)   

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Captainamarica/NightVissionSenderBot)

