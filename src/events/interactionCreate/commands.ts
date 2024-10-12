import { type Interaction } from 'discord.js'
import type { CustomClient } from '../../typings'

export const execute = async (client: CustomClient, interaction: Interaction): Promise<void> => {
  if (!interaction.isCommand()) return

  const command = client.commands?.get(interaction.commandName)
  if (command === undefined) return

  try {
    await command(client, interaction)
  } catch (error) {
    console.error(error)
    await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true })
  }
}
