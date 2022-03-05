# nullnyat Twitter Proxy for Misskey

## 仕様

TwitterAPI を叩いて、そのアカウントのツイートを 5 分おきに取得して、それを Misskey に投稿します。

## 使い方

main.py を実行してください。  
systemd などでサービス化すると便利です

次のパッケージが必要です

```
tweepy
requests
misskey.py
```

config.py

isDiscord が True の場合、Discord に投稿します。  
False の場合、Misskey に投稿します。

```
CONFIG = {
   "CONSUMER_KEY": "jiohfsaohinaffwaiohafw",
   "CONSUMER_SECRET": "faafsfwafafw",
   "ACCESS_TOKEN": "faaflwaffwaawf",
   "ACCESS_SECRET": "afmjsaflkfaawf",
   "MISSKEY_ADDRESS": "https://simkey.net",
   "MISSKEY_API": "afwjwafwafkawf",
   "isDiscord": False,
   "DiscordWebhook": "https://discordapp.com/api/webhooks/9999999999999999",
}
```

## 投稿形式

```
ID: 1500174602689220608
Name: こけっちさぶ
Time: 2022-03-05 18:21:11+00:00

あfwのfわjfわbjかwfjくぁfbfうぇあわふぇbklはfうぇbjぁふぁw
https://twitter.com/_kobh/status/1500174602689220608
```
