const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = '-';

const fs = require('fs');

client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command);
}

client.once('ready', () => {
    console.log('Testing123 is online yo!');
})

client.on('message', message => {
    message.member.roles.cache.has
    if (!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if (command === 'ping') {
        client.commands.get('ping').execute(message, args);
    } else if (command == 'mc3') {
        client.command.get('mc3').execute(message, args);
    }
})





client.login('Nzc0MzUzMjA2MTg0MjQ3MzI4.X6Winw.xSjVtM9rd38BbIj7705FXhNC7pM');