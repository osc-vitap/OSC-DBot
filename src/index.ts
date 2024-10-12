import { ActivityType, Client, Collection, GatewayIntentBits } from 'discord.js'
import * as dotenv from 'dotenv'
import { loadEvents } from './events/index'
import type { CustomClient } from './typings'
import { handleSubCommands } from './utils/handleSubcommands'

async function main (): Promise<void> {
  dotenv.config()
  const client = new Client({
    intents: [
      GatewayIntentBits.Guilds,
      GatewayIntentBits.GuildMessages,
      GatewayIntentBits.MessageContent
    ]
  }) as CustomClient

  client.commands = new Collection()
  client.handleSubcommands = handleSubCommands

  const { DISCORD_TOKEN } = process.env

  await loadEvents(client)
  await client.login(DISCORD_TOKEN)
}

main().catch((err) => {
  console.error(err)
})