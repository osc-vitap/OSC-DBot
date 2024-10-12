import type { Client, Collection } from 'discord.js'

export interface CustomClient extends Client {
  commands: Collection<string, CallableFunction>
  handleSubcommands: CallableFunction
}