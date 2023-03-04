class Solution:
    def interpret(self, command: str) -> str:
        map_ = {"()":"o", "(al)":"al"}
        for k, v in map_.items():
            command = command.replace(k, v)
        return command