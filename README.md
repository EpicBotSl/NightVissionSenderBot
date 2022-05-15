# Channel Auto-Post Bot

<img src=https://telegra.ph/file/0e41c9763a65e874e39a5.jpg>
This bot can send all new messages from one channel, directly to another channel (or group, just in case), without the forwarded tag!

## Setting up 
* First:
> `APP_ID` and `API_HASH` - Get it from my.telegram.org   
> `BOT_TOKEN` - Get it from [@BotFather](https://t.me/BotFather)   
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
- Clone the repo:   <code>git clone https://github.com/DARKEMPIRESL/ChannelAutoForwarder</code></br>
- Make a <code>.env</code> file in the root of the repo, like <a href="https://github.com/DARKEMPIRESL/ChannelAutoForwarder/blob/main/.env.sample">.env.sample</a> and fill in the values.</br>
- Use <code>python3 bot.py</code> to start the bot.</br>  
</details>

## Usage
Add the bot to both channels with admin permission, and thats it!
All new messages will be auto-posted!!

Visit [@Team SL Bots🇱🇰](https://t.me/SLBotOfficial) for help.
## Credits
> [Lonami](https://github.com/LonamiWebs), for [Telethon](https://github.com/LonamiWebs/Telethon).   
> [𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊](https://github.com/DARKEMPIRESL), me.   
> [@ettan_fan](https://t.me/ettan_fan)   

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

