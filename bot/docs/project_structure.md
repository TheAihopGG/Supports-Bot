# Project Structure

## Bot structure

### 1. Cogs

The `./bot/cogs` contains special directories, cogs. About [cogs' structure](#cog-structure)

### 2. Services

The `./bot/services` contains special directories, services. In them, the bot handles disnake events. About [services' structure](#service-structure)

### 3. Core

The `./bot/core` contains special modules, which is required for cogs and services.

#### 3.1. `base_embeds.py`

Module contains some classes inherited from `disnake.Embed`. You can use them to your code shorter.

There are classes:

- `TimestampEmbed`
- `ErrorEmbed`
- `CriticalErrorEmbed`
- `SuccessEmbed`
- `WarningEmbed`
- `InfoEmbed`

#### 3.2. `configuration.py`

There are the project configuration. See [project configuration](./project_configuration.md) for more information.

#### 3.3. `database.py`

This module is designed to create a database connection.

To create a async connection, execute:

```python
async with session_factory() as session:
  ...
```

#### 3.4. `logger.py`

This module is designed to interact with logging system. Use `logger` to interact with logging system.

#### 3.5. `utils.py`

The module contains some useful functions.

#### 3.6. `embeds.py`, `enums.py`

These modules are *global* modules. For comparison, `./bot/cogs/*example_cog*/embeds.py` contains embeds for *example_cog*, it means that embeds in the module can be used only in *example_cog*, but the *global* embed means that embeds in the module can be used in every cog.

#### 3.7. `template_configuration.py`

There is a template for `configuration.py`.

## Cog structure

The cog consists from the next files:

- `views.py` (if necessary)
- `modals.py` (if necessary)
- `embeds.py` (if necessary)
- `enums.py` (if necessary)
- `cog.py`
- `__init__.py`

## Service structure

The service consists from the next files:

- `service.py`
- `__init__.py`
