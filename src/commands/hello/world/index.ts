import { type ChatInputCommandInteraction, SlashCommandBuilder, type HexColorString, SlashCommandSubcommandBuilder } from 'discord.js'
import { type CustomClient } from '../../../typings'
import { EmbedBuilder } from 'discord.js'

export const data = new SlashCommandSubcommandBuilder()
	.setName('world')
	.setDescription('Hello World subcommand')

export async function execute (
	client: CustomClient,
	interaction: ChatInputCommandInteraction
): Promise<void> {
	interaction.reply('ZA WARUDO!!')
}
