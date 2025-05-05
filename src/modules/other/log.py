from colorama import Fore, Back, Style

class log:
    @staticmethod
    def print(content: str) -> str:
        print(Fore.WHITE + f"[LOG] {content}")
        return content
        
    @staticmethod
    def warn(content: str) -> str:
        print(Fore.YELLOW + f"[WARN] {content}")
        return content
        
    @staticmethod
    def success(content: str) -> str:
        print(Fore.GREEN + f"[SUCCESS] {content}")
        return content
        
    @staticmethod
    def error(content: str) -> str:
        print(Fore.RED + f"[ERROR] {content}")
        return content

if __name__ == "__main__":
    exit()
