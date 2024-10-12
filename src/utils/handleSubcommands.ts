import { ChatInputCommandInteraction, Interaction, SlashCommandBuilder } from "discord.js";
import { CustomClient } from "../typings";
import * as fs from 'fs/promises'
import * as path from 'path'

interface Command {
	data: SlashCommandBuilder
	execute: (client: CustomClient, interaction: Interaction) => Promise<void>
}
const cache = new Map<string, Command>()

export async function handleSubCommands(
	client: CustomClient,
	interaction: ChatInputCommandInteraction,
	commandPath: string
): Promise<void> {
	const subcommandsDirs = await fs.readdir(commandPath);
	if (cache.has(interaction.options.getSubcommand())) {
		const command = cache.get(interaction.options.getSubcommand()) as Command
		command.execute(client, interaction)
		return
	}

	for (const dir of subcommandsDirs) {
		if (!(await fs.stat(path.join(commandPath, dir))).isDirectory()) continue
		
		const commandFile = path.join(commandPath, dir, 'index');
		
		let command: Command;
		try {
			command = await import(commandFile);
		} catch (e) {
			console.warn(`Command ${dir} doesnt have data or execute`)
			continue
		}

		if (command.data === undefined || command.execute === undefined) {
			console.warn(`Command ${dir} doesnt have data or execute`)
			return
		}

		cache.set(command.data.name, command);
		if (interaction.options.getSubcommand() === command.data.name) {
			command.execute(client, interaction)
		}
	}
}