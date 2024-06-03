from collections.abc import Generator


class Transition:
    """
    Transition class to represent the transition from one state (one type of string) to another

    Args:
        initial (str): The initial string
        final (str): The final string

    Returns:
        None
    """

    def __init__(self, initial: str, final: str) -> None:
        self.initial: str = initial
        self.final: str = final
        return


class Language:
    """
    Language class to represent the language

    Args:
        init_stat (str): The initial state (string) of the language
        transitions (list[Transition]): The list of transitions

    Returns:
        None
    """

    def __init__(self, init_stat: str, transitions: list[Transition]) -> None:
        self.init_stat: str = init_stat
        self.transitions: list[Transition] = transitions
        return

    def gen_next_str(self, now_stat: str = None) -> Generator[str, None, None]:
        """
        Generate the next string based on the current string

        Args:
            now_stat (str): The current string, if not provided, the initial state of the language will be used

        Returns:
            Generator[str, None, None]: The generator of the next string
        """

        if now_stat is None:
            now_stat = self.init_stat

        for transition in self.transitions:
            # If the initial string is found in the current string, then replace it with the final string
            if now_stat.find(transition.initial) != -1:
                new_stat = now_stat.replace(
                    transition.initial, transition.final, 1)
                yield from self.gen_next_str(new_stat)
        else:
            # If no transition is found, then the current string is the final string

            # Note that this implementation do not check all alphabet in the final string is valid or not
            # i.e. the final string may contain alphabet that is not in the terminal alphabet
            yield now_stat


if __name__ == "__main__":
    # Transitions for L1 = {a^n b^n c^n | n >= 1} which is context-sensitive
    # transitions = [
    #     Transition("S", "abc"),
    #     Transition("S", "aAbc"),
    #     Transition("Ab", "bA"),
    #     Transition("Ac", "Bbcc"),
    #     Transition("bB", "Bb"),
    #     Transition("aB", "aa"),
    #     Transition("aB", "aaA"),
    # ]

    # Transitions for L2 = {a^n b^n c^n d^n | n >= 1} which is context-sensitive
    transitions = [
        Transition("S", "abcd"),
        Transition("S", "aAbcd"),
        Transition("Ab", "bA"),
        Transition("Ac", "cA"),
        Transition("Ad", "Bcdd"),
        Transition("cB", "Bc"),
        Transition("bB", "Cbb"),
        Transition("aC", "aa"),
        Transition("aC", "aaA"),
        Transition("bC", "Cb"),
    ]

    lang = Language("S", transitions)

    for _, i in enumerate(lang.gen_next_str()):
        if _ > 20:
            break

        print(_, i)
