# Contributing

- **Formatter**: black
- **Code style**: snake_case
- **Commits lang**: russian
- **Comments lang**: russian
- **Docs lang**: english (temporary)

## About embeds

- Use base embeds from `./bot/core/base_embeds.py` to create embed, instead of `disnake.Embed`
- The title of the embed - is the embed status

## About tasks

We hosts our tasks in github projects. To complete the task, follow the following instructions:

- Make sure that the task's status is "Ready"
- Make sure that you are assigned to the task
- Set the task's status to "In process"
- Create a branch for the task
- Complete the task
- Create a pull request
- Set the task's status to "In review"
- Wait for the code review and fix a bugs
- After bugfix, reviewer will confirm the pull request
- Set the task's status to "Done"