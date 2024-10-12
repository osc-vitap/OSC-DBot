import * as fs from 'fs/promises'
import * as path from 'path'
import type { Client } from 'discord.js'

export const loadEvents = async (client: Client): Promise<void> => {
  const eventDir = await fs.readdir(path.join(__dirname))
  for (const dir of eventDir) {
    if (dir.endsWith('.ts') || dir.endsWith('.js')) continue
    const eventFiles = await fs.readdir(path.join(__dirname, dir))
    for (const file of eventFiles) {
      const event = await import(path.join(__dirname, dir, file))
      client.on(dir, (...args) => event.execute(client, ...args))
    }
  }
}
