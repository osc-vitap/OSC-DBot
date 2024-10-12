import { PrismaClient, department as DepartmentEnum } from '@prisma/client';
import { type ChatInputCommandInteraction, SlashCommandBuilder, GuildMemberRoleManager } from 'discord.js';
import { type CustomClient } from '../../typings';

const prisma = new PrismaClient();

export const data = new SlashCommandBuilder()
  .setName('add')
  .setDescription('Adds a user to the club')
  .addStringOption(option =>
    option.setName('name')
      .setDescription('The full name of the user')
      .setRequired(true))
  .addIntegerOption(option =>
    option.setName('year')
      .setDescription('Year of joining')
      .setRequired(true))
  .addStringOption(option =>
    option.setName('department')
      .setDescription('The department of the user')
      .setRequired(true)
      .addChoices(
        { name: 'ADMIN', value: 'ADMIN' },
        { name: 'TECHNICAL', value: 'TECHNICAL' },
        { name: 'EVENT', value: 'EVENT' },
        { name: 'CREATIVE', value: 'CREATIVE' },
        { name: 'EDITORIAL', value: 'EDITORIAL' },
        { name: 'DESIGN', value: 'DESIGN' },
        { name: 'HR', value: 'HR' }
      ))
  .addStringOption(option =>
    option.setName('role')
      .setDescription('Their role in the club')
      .setRequired(true));

export async function execute(
  client: CustomClient,
  interaction: ChatInputCommandInteraction
): Promise<void> {
  const allowedRoleId = '994910850009800734';
  const allowedUserId = '575955328496173056';

  const userId = interaction.user.id;

  const hasPermission = interaction.member?.roles instanceof GuildMemberRoleManager
    ? (await interaction.member.roles.cache.has(allowedRoleId)) || (userId === allowedUserId)
    : false;

  if (!hasPermission) {
    await interaction.reply({ content: 'You do not have permission to use this command.', ephemeral: false });
    return;
  }

  const fullName = interaction.options.getString('name')!;
  const yearOfJoining = interaction.options.getInteger('year')!;
  const department = interaction.options.getString('department')! as DepartmentEnum;
  const role = interaction.options.getString('role')!;
  const guild = interaction.guild!;

  try {
    await interaction.deferReply();

    let user = await prisma.users.findUnique({
      where: { name: fullName }
    });

    if (!user) {
      user = await prisma.users.create({
        data: { name: fullName }
      });
    }

    await prisma.membership.create({
      data: {
        name: fullName,
        year: yearOfJoining,
        department,
        role,
      },
    });

    const departmentRole = guild.roles.cache.find(r => r.name === department);
    const ebRole = guild.roles.cache.find(r => r.name === role);

    if (departmentRole && interaction.member?.roles instanceof GuildMemberRoleManager) {
      await (interaction.member.roles as GuildMemberRoleManager).add(departmentRole);
    }

    if (ebRole && interaction.member?.roles instanceof GuildMemberRoleManager) {
      await (interaction.member.roles as GuildMemberRoleManager).add(ebRole);
    }

    await interaction.editReply(`User ${fullName} has been added to the club with the role ${role} in the ${department} department.`);
  } catch (error) {
    console.error(error);
    await interaction.editReply('There was an error while executing this command!');
  }
}
