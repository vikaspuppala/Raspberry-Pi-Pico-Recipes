# Macros plugin for MkDocs
# See https://mkdocs-macros-plugin.readthedocs.io/en/latest/#full-example

# Here you can define your own macros, which can be used in your markdown files.

def define_env(env):
    "Hook function"

    # Example
    # This macro will be available in your markdown files as {{ mymacro(" world") }}
    @env.macro
    def mymacro(s):
        return "hello" + s
