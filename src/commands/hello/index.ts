import { type ChatInputCommandInteraction, SlashCommandBuilder, type HexColorString } from 'discord.js'
import { type CustomClient } from '../../typings'
import { EmbedBuilder } from 'discord.js'

export const data = new SlashCommandBuilder()
	.setName('hello')
	.setDescription('Replies with Hello, world!')

export async function execute (
	client: CustomClient,
	interaction: ChatInputCommandInteraction
): Promise<void> {
	await client.handleSubcommands(client, interaction, __dirname)
}