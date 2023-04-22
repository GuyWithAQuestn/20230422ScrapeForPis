def sendDiscordMessage(message_to_user):
    from discord import SyncWebhook
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/953440793761312808/RuLeQ4PUm3jaeMBfjDHgWl2VnZNxQ7kMNgqZN68KVum4A4dFFUooB1sOPDK7jD9D2qmH")
    webhook.send("Pi Scrape Bot: " + message_to_user)

    return 0