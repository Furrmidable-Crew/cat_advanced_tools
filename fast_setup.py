import json
import os.path

from cat.mad_hatter.decorators import tool, hook


def get_settings():
    if os.path.isfile("cat/plugins/cat_advanced_tools/settings.json"):
        with open("cat/plugins/cat_advanced_tools/settings.json", "r") as json_file:
            settings = json.load(json_file)
    else:
        with open("cat/plugins/cat_advanced_tools_main/settings.json", "r") as json_file:
            settings = json.load(json_file)
    return settings


@hook
def agent_prompt_prefix(prefix, cat):
    settings = get_settings()
    prefix = settings["prompt_prefix"]

    return prefix


@hook
def before_cat_recalls_episodic_memories(default_episodic_recall_config, cat):
    settings = get_settings()
    default_episodic_recall_config["k"] = settings["episodic_memory_k"]
    default_episodic_recall_config["threshold"] = settings["episodic_memory_threshold"]

    return default_episodic_recall_config


@hook
def before_cat_recalls_declarative_memories(default_declarative_recall_config, cat):
    settings = get_settings()
    default_declarative_recall_config["k"] = settings["declarative_memory_k"]
    default_declarative_recall_config["threshold"] = settings["declarative_memory_threshold"]

    return default_declarative_recall_config


@hook
def before_cat_recalls_procedural_memories(default_procedural_recall_config, cat):
    settings = get_settings()
    default_procedural_recall_config["k"] = settings["procedural_memory_k"]
    default_procedural_recall_config["threshold"] = settings["procedural_memory_threshold"]

    return default_procedural_recall_config
