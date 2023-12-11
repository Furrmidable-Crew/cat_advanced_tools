from cat.mad_hatter.decorators import tool


@tool(return_direct=True)
def show_working_memory(none, cat):
    """Useful to display the content of the working memory. Input is None."""

    # print(cat.working_memory)
    return f"{cat.working_memory.keys()}"
